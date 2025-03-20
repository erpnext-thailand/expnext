# -*- coding: utf-8 -*-
# Copyright (c) 2025, limweb@hotmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class CustomPage(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/custom_page.html",
		condition_field = "published",
		page_title_field = "title",
	)
	
	def get_context(self, context):
		context.parents = [{'name': 'Home', 'route': '/'}]
		return context
