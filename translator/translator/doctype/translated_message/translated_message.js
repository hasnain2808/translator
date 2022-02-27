// Copyright (c) 2020, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Translated Message", {
  refresh: function (frm) {
	if (!frm.doc.__islocal && frm.doc.contribution_status == "Pending") {
		frm.trigger("set_management_buttons");
	  }
  },

  set_management_buttons: function (frm) {
	frm.call("can_manage").then(function (r) {
	  if (r.message) {
		frm.add_custom_button(__("Verify"), function () {
		  frm.trigger("verify");
		});
		frm.add_custom_button(__("Reject"), function () {
		  frm.trigger("reject");
		});
	  }
	});
  },

  verify: function (frm) {
	frm.call("verify").then(() => frm.reload_doc());
  },

  reject: function (frm) {
	frm.call("reject").then(() => frm.reload_doc());
  },
});
