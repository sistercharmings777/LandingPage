from django.contrib import admin
from . models import Contact, ContactAdmin, Subscription

admin.site.register([Contact, ContactAdmin, Subscription])