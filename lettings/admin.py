from django.contrib import admin

<<<<<<<< HEAD:oc_lettings_site/admin.py
from .models import Letting as OldLetting
from .models import Address as OldAddress
from lettings.models import Letting
from lettings.models import Address
from .models import Profile as OldProfile
from profiles.models import Profile
========
from .models import Letting
from .models import Address
>>>>>>>> dev_architecture_modulaire:lettings/admin.py


admin.site.register(Letting)
admin.site.register(Address)
<<<<<<<< HEAD:oc_lettings_site/admin.py
admin.site.register(OldLetting)
admin.site.register(OldAddress)
admin.site.register(Profile)
admin.site.register(OldProfile)
========
>>>>>>>> dev_architecture_modulaire:lettings/admin.py
