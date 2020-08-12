from django.contrib import admin

from document.models import Document, DocumentStatus, Contract, Letter, DocumentComment

admin.site.register(Document)
admin.site.register(DocumentComment)
admin.site.register(DocumentStatus)
admin.site.register(Contract)
admin.site.register(Letter)
