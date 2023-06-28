from django.contrib import admin

from .models import Letting as OldLetting
from .models import Address as OldAddress
from lettings.models import Letting
from lettings.models import Address
from .models import Profile as OldProfile
from profiles.models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(OldLetting)
admin.site.register(OldAddress)
admin.site.register(Profile)
admin.site.register(OldProfile)
