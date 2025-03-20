import frappe

def get_context(context):
    context.title = "ExpNext Accounting"
    
    # You can add dynamic content here
    # For example, fetching testimonials from the database
    # context.testimonials = frappe.get_all("Testimonial", fields=["name", "content", "author", "designation", "company"])
    
    # Or fetching features from the database
    # context.features = frappe.get_all("Feature", fields=["name", "title", "description", "icon"])
    
    return context
