# Copyright (c) 2026, emm and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class minutes(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		action: DF.Data | None
		assigned_to: DF.Link | None
		completed_by: DF.Date | None
		description: DF.TextEditor
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		status: DF.Literal["", "OPEN", "CLOSED"]
	# end: auto-generated types

	pass
