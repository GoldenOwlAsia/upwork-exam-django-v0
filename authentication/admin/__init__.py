from django.contrib import admin

from authentication.models import *

register_list = ((Customer,), (Profile,))

for register_item in register_list:
    admin.site.register(*register_item)
