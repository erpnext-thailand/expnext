import frappe

def get_context(context):
    context.title = "ExpNext1 - Custom Page"
    
    # You can add dynamic content here if needed
    # For example, fetching data from the database
    # context.items = frappe.get_all("Item", fields=["name", "description"])
    
    return context
