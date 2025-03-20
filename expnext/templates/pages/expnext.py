import frappe

def get_context(context):
    context.title = "ExpNext - Accounting Solution"
    
    # You can add dynamic content here if needed
    # For example, fetching testimonials from the database
    # context.testimonials = frappe.get_all("Testimonial", fields=["name", "content", "author", "designation", "company"])
    
    # Or fetching modules from the database
    # context.modules = frappe.get_all("Module", fields=["name", "title", "description", "icon"])
    
    return context
