from django.contrib import admin

#if ENVIRONMENT == 'PROD':
#	from api.models import *
#else:
from api.models import *

# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(ApiKey, ApiKeyAdmin)
#admin.site.register(Dog, DogAdmin)
#admin.site.register(Breed, BreedAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Profile, ProfileAdmin)
#admin.site.register(User, UserAdmin)
