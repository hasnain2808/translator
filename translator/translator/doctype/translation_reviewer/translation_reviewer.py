# Copyright (c) 2022, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class TranslationReviewer(Document):

	def validate(self):
		if self.status == "Review Pending":
			frappe.sendmail(
				subject = "Verify Translation Reviewer",
				message = self.get_message(),
				recipients = self.get_recipients(),
				reference_doctype = self.doctype,
				reference_name = self.name,
			)

	def get_recipients(self):
		return frappe.db.get_all("Translation Reviewer", filters = {
				"language": self.language,
				"status": "Approved"
			}, fields = "user", pluck = "user", limit = 3)

	def get_message(self):
		return f"Verify if {self._get_url()} can be a Translation Reviewer for {self.language}"

	def _get_url(self):
		return frappe.utils.get_url_to_form(self.doctype, self.name)

	@frappe.whitelist()
	def approve(self):
		if self.can_manage():
			self.status = "Approved"
			self.save()
		else:
			frappe.throw(_("You are not authorized to approve this Translation Reviewer"), frappe.PermissionError)

	@frappe.whitelist()
	def reject(self):
		if self.can_manage():
			self.status = "Rejected"
			self.save()
		else:
			frappe.throw(_("You are not authorized to reject this Translation Reviewer"), frappe.PermissionError)

	@frappe.whitelist()
	def can_manage(self):

		if frappe.session.user == "Administrator":
			return True

		users = frappe.get_value("Translation Reviewer", {
				"user": frappe.session.user,
				"language": self.language,
				"status": "Approved"
			}, "user")

		if users:
			return True

