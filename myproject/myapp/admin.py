from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib import messages
from .models import myproject,groupreq

# Register your models here.
def approve(modeladmin, request, queryset):
    print(queryset)
    for requests in queryset:
        user = User.objects.get(username=''+requests.name)
        group = Group.objects.get(name=''+requests.groupReq)
        group.user_set.add(user)
        print(requests.name)
        print(requests.groupReq)

        requests.delete()
    print(queryset)
    messages.add_message(request, messages.INFO, 'Requests have been approved successfully')

class groupRequest(admin.ModelAdmin):
    actions = [approve,]

admin.site.register(myproject)
admin.site.register(groupreq,groupRequest)

