import frappe
import json
from frappe.utils import cint
from frappe.translate import load_lang, get_user_translations, get_messages_for_app

@frappe.whitelist(allow_guest=True)
def add_translations(translation_map, contributor_name, contributor_email, language):
	translation_map = json.loads(translation_map)
	name_map = frappe._dict({})
	for source_id, translation_dict in translation_map.items():
		translation_dict = frappe._dict(translation_dict)
		existing_doc = frappe.db.get_all('Translated Message', {
			'source': source_id,
			'translation_source': 'Community Contribution',
			'contributor_email': contributor_email
		})
		if existing_doc:
			existing_doc_name = existing_doc[0].name
			name_map[translation_dict.name] = existing_doc_name
			frappe.db.set_value('Translated Message', existing_doc_name, 'translated', translation_dict.translated_text)
		else:
			doc = frappe.get_doc({
				'doctype': 'Translated Message',
				'source': source_id,
				'translation_source': 'Community Contribution',
				'contribution_status': 'Pending',
				'translated': translation_dict.translated_text,
				'contributor_email': contributor_email,
				'contributor_name': contributor_name,
				'language': language
			})
			doc.insert(ignore_permissions=True)
			name_map[translation_dict.name] = doc.name

	frappe.db.commit()

	return name_map


@frappe.whitelist(allow_guest=True)
def get_strings_for_translation(language, start=0, page_length=100, search_text='', app_name='%'):
	return frappe.db.sql("""
		SELECT * FROM (
			SELECT
				DISTINCT source.name AS id,
				source.message AS source_text,
				source.context AS context,
				translated.translated AS translated_text,
				CASE WHEN translated.translated IS NOT NULL THEN 1 ELSE 0 END AS translated,
				CASE WHEN translated.translation_source = 'Google Translated' THEN 1 ELSE 0 END AS translated_by_google,
				translated.contributor_name,
				translated.contributor_email,
				translated.modified_by,
				source.creation
			FROM `tabSource Message` source
				LEFT JOIN `tabTranslated Message` AS translated
					ON (
						source.name=translated.source
						AND translated.language = %(language)s
						AND (translated.contribution_status='Verified' OR translated.translation_source != 'Community Contribution')
					)
				Inner join `tabSource Message Position` as smp
					on (
						source.name=smp.parent
					)
			WHERE
				source.disabled != 1 && ((source.message like %(search_text)s or translated.translated like %(search_text)s) and smp.app like %(app_name)s)
			ORDER BY
				translated_by_google
		) as res
		GROUP BY res.id
		ORDER BY  res.translated, res.translated_by_google, res.creation
		LIMIT %(page_length)s
		OFFSET %(start)s
	""", dict(language=language, search_text='%' + search_text + '%', page_length=cint(page_length), start=cint(start), app_name=app_name), as_dict=1 )

@frappe.whitelist(allow_guest=True)
def get_source_additional_info(source, language=''):
	data = {}
	data['contributions'] = frappe.get_all('Translated Message', filters={
		'translation_source': 'Community Contribution',
		'source': source,
		'language': language
	}, fields=['name', 'translated', 'contributor_email', 'contributor_name', 'creation', 'contribution_status', 'modified_by'])

	data['positions'] = frappe.get_all('Source Message Position', filters={
		'parent': source,
	}, fields=['position as path', 'line_no', 'app',
		'app_version', 'module', 'type', 'document_name'])

	return data

@frappe.whitelist(allow_guest=True)
def upvote_translation(translation_id, user_email, site):
	# translation votes
	pass

@frappe.whitelist(allow_guest=True)
def get_contribution_status(translation_id, user_email=None, site=None):
	return frappe.get_doc('Translated Message', translation_id)


@frappe.whitelist(allow_guest=True)
def get_apps():
	return frappe.get_all('Translator App', fields=['name', 'app_name', 'logo', 'description'])

@frappe.whitelist(allow_guest=True)
def get_app(name):
	return frappe.get_all('Translator App', fields=['name', 'app_name', 'logo', 'description'], filters={
		"name": name
	})[0]

@frappe.whitelist(allow_guest=True)
def get_reviewer_applications(start):

	if frappe.session.user == 'Administrator':
		return frappe.get_all("Translation Reviewer",
			filters={"status": "Review Pending"},
			fields=['language', 'user', 'name', 'creation'],
			start=start,
			limit=10
		)

	reviewer_for_languages = frappe.get_all("Translation Reviewer", filters= {
			"user": frappe.session.user,
			"status": "Approved"
		}, fields = ["language"], pluck=["language"])


	return frappe.get_all("Translation Reviewer",
			filters=[["status",'=', "Review Pending"]["language",'in', reviewer_for_languages ]],
			fields=['language', 'user', 'creation', 'name', "linkedin_url", 'reason',
				"github_url", "portfolio_url", "language_certification_url"],
			start=start,
			limit=10
		)

@frappe.whitelist(allow_guest=True)
def get_reviewer_application(name):
	if not name:
		frappe.get_last_doc("Translation Reviewer")
	return frappe.get_doc("Translation Reviewer", name)


def get_strings_count(app_name):
	SourceMessagePosition = frappe.qb.DocType('Source Message Position')
	SourceMessage = frappe.qb.DocType('Source Message')

	from frappe.query_builder.functions import Count
	count_names = Count(SourceMessage.name).as_("count_name")

	return (frappe.qb.from_(SourceMessage)
		.join(SourceMessagePosition)
		.on(SourceMessage.name == SourceMessagePosition.parent )
		.where(SourceMessagePosition.app == app_name)
		.select(count_names)
		.distinct()
	).run()

def get_translation_count(app_name, lang):
	return frappe.db.sql("""
			SELECT
				COUNT(DISTINCT source.name) AS source_name
			FROM `tabSource Message` source
				LEFT JOIN `tabTranslated Message` AS translated
					ON (
						source.name=translated.source
						AND translated.language = %(language)s
						AND (translated.contribution_status='Verified')
					)
				LEFT JOIN `tabSource Message Position` AS position
					ON (
						source.name=position.parent
					)
			WHERE
				source.disabled != 1
				AND position.app = %(app)s
				AND translated.translation_source != 'Google Translated'
	""".format(
		), dict(language=lang, app=app_name), as_dict=0)

def get_translation_percentage(app_name, lang):
	return (get_translation_count(app_name, lang)[0][0]/ get_strings_count(app_name)[0][0] ) * 100

@frappe.whitelist(allow_guest=True)
def get_application_stats(app_name, lang):
	return [
		frappe._dict({ 'name': 'Translation Completed', 'stat': f'{get_translation_percentage(app_name, lang)}%' }),
		frappe._dict({ 'name': 'Total Strings', 'stat': get_strings_count(app_name)[0][0] }),
		frappe._dict({ 'name': 'Translated Strings', 'stat': get_translation_count(app_name, lang)[0][0] }),
	]

@frappe.whitelist(allow_guest=True)
def get_top_contributors(lang):
	return frappe.db.get_all('Translated Message',
		fields=['count(name) as count', 'contributor_name'],
		filters={'contributor_name': ('is', 'set'), 'contributor_email': ('!=', 'Administrator'), 'language': lang},
		group_by='contributor_email',
		order_by='count desc',
		limit=10)

@frappe.whitelist(allow_guest=True)
def get_translated_messsages_for_verification(lang, start):
	if frappe.session.user == 'Administrator':
		return frappe.get_all("Translated Message",
			filters={"language": lang, "contribution_status": "Pending", 'translation_source': 'Community Contribution'},
			fields=['name', 'source_message', 'translated'],
			start=start,
			limit=10
		)

	return frappe.db.get_all('Translated Message',
		fields=['*'],
		filters={'contributor_name': ('is', 'set'), 'contributor_email': ('!=', 'Administrator'), 'language': lang},
		group_by='contributor_email',
		order_by='count desc',
		limit=10)


@frappe.whitelist(allow_guest=True)
def get_translated_messsage_details(translated_message_name):
	translated = frappe.get_doc('Translated Message', translated_message_name)
	source = frappe.get_doc('Source Message', translated.source)
	return {
		"source": source,
		"translated": translated
	}

@frappe.whitelist()
def verify_translated_messsage(translated_message_name):
	translated = frappe.get_doc('Translated Message', translated_message_name)
	translated.verify()

@frappe.whitelist()
def reject_translated_messsage(translated_message_name):
	translated = frappe.get_doc('Translated Message', translated_message_name)
	translated.reject()
