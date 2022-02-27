// Copyright (c) 2022, Frappe Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on("Translation Reviewer", {
  refresh: function (frm) {
	if (!frm.doc.__islocal && frm.doc.status == "Review Pending") {
	  frm.trigger("set_management_buttons");
	}
  },

  approve: function (frm) {
	frm.call("approve").then( () => frm.reload_doc());
  },


  reject: function (frm) {
	frm.call("reject").then( () => frm.reload_doc());
  },

  set_management_buttons: function (frm) {
	frm.call("can_manage").then(function (r) {
	  if (r.message) {
	  frm.add_custom_button(__("Approve"), function () {
		frm.trigger("approve");
	  });
	  frm.add_custom_button(__("Reject"), function () {
		frm.trigger("reject");
	  });
	}
	});
  },
});
