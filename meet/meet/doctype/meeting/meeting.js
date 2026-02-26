// Copyright (c) 2026, emm and contributors
// For license information, please see license.txt

// frappe.ui.form.on("meeting", {
// 	refresh(frm) {

// 	},
// }); 
frappe.ui.form.on("Meeting", {
    attendee: function(frm, cdt, cdn) {
        var attendee = frappe.model.get_doc(cdt, cdn);
        if (attendee.attendee) {
            //if attendee is selected, fetch the full name and set it in the full name field
            frm.call({
                method: "meet.meet.doctype.meeting.meeting.get_full_name",
                args: {
                    attendee: attendee.attendee
                },
                callback: function(r) {
                    frappe.model.set_value(cdt, cdn, "full_name", r.message);
                }
            });
        } else {
            //if no attendee is selected, clear the full name field
            frappe.model.set_value(cdt, cdn, "full_name", null);
        }
    }})
