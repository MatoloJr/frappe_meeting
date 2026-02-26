# Copyright (c) 2026, emm and contributors
# For license information, please see license.txt

#other imports
from __future__ import unicode_literals
import frappe
from frappe import _

# import frappe
from frappe.model.document import Document


class meeting(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from meet.meet.doctype.agenda.agenda import agenda
		from meet.meet.doctype.attendees.attendees import attendees
		from meet.meet.doctype.minutes.minutes import minutes

		agenda: DF.Table[agenda]
		amended_from: DF.Link | None
		attendee: DF.Table[attendees]
		date: DF.Date
		from_time: DF.Time
		minutes: DF.Table[minutes]
		status: DF.Literal["", "Planned", "In Progress", "Completed", "Cancelled"]
		title: DF.Data
		to_time: DF.Time
	# end: auto-generated types

	pass

#frappe methods and other custom methods
def validate(self):
	"""set missing name and warn if duplicate"""
	found = []
	for attendee in self.attendee:
		if not attendee.full_name:
			attendee.full_name = get_full_name(attendee.attendee)

		if attendee.attendee in found:
			frappe.throw(_("Attendee {0} entered twice").format(attendee.attendee))

		found.append(attendee.attendee)

#marked this function as a whitelist to be used in client side
@frappe.whitelist()
def get_full_name(attendee):
	user = frappe.get_doc("User", attendee)
	#concatenates by space if it has value
	return " ".join(filter(None, [user.first_name, user.middle_name, user.last_name]))
