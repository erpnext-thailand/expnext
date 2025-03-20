# Copyright (c) 2025, limweb@hotmail.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PurchaseOrder(Document):
	def validate(self):
		self.calculate_totals()
	
	def on_submit(self):
		if self.status == "Draft":
			self.status = "To Receive"
	
	def on_cancel(self):
		self.status = "Cancelled"
	
	def calculate_totals(self):
		total_qty = 0
		total_amount = 0
		
		for item in self.items:
			item.amount = item.qty * item.rate
			total_qty += item.qty
			total_amount += item.amount
		
		self.total_quantity = total_qty
		self.total_amount = total_amount
