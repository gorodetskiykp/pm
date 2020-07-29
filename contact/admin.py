from django.contrib import admin
from contact.models import Contact, Phone, Company, Email, Skype

admin.site.register(Contact)
admin.site.register(Phone)
admin.site.register(Company)
admin.site.register(Email)
admin.site.register(Skype)
