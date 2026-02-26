# Copyright (c) 2026, emm and contributors
# For license information, please see license.txt

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