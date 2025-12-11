from django.contrib import admin

# Register your models here.
class NearmeAdmin(admin.AdminSite):
    site_header = "Nearme Administration"
    site_title = "Nearme Admin Portal"
    index_title = "Welcome to Nearme Admin Portal"
admin_site = NearmeAdmin(name='nearme_admin')
  # Register your models here