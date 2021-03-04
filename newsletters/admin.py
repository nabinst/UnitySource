from django.contrib import admin
from .models import NewsletterUser, NewsLetter
# Register your models here.
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed',)

admin.site.register(NewsletterUser,NewsLetterAdmin)
admin.site.register(NewsLetter)