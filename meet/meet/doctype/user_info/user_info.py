# Copyright (c) 2026, emm and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class userinfo(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Data | None
		first_name: DF.Data | None
		language: DF.Data | None
		last_name: DF.Data | None
		middle_name: DF.Data | None
		time_zone: DF.Autocomplete | None
		user_image: DF.AttachImage | None
		username: DF.Data | None
	# end: auto-generated types

	pass
