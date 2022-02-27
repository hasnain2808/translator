# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import strip
from frappe.model.document import Document

import re

class TranslatedMessage(Document):
	@frappe.whitelist()
	def verify(self):
		if self.can_manage():
			self.contribution_status = "Verified"
			self.save()
		else:
			frappe.throw(_("You are not authorized to approve this Translated Message"), frappe.PermissionError)

	@frappe.whitelist()
	def reject(self):
		if self.can_manage():
			self.contribution_status = "Rejected"
			self.save()
		else:
			frappe.throw(_("You are not authorized to reject this Translated Message"), frappe.PermissionError)

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