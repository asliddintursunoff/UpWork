from django.contrib import admin

from .models import Organization,Worker,Worker_about,User,Relationship
# from .forms import *
from django.contrib.auth.admin import UserAdmin



# class Worker_aboutAdmin(admin.ModelAdmin):
#     list_display=['FIO']
#     list_per_page=10
#     search_fields=["FIO"]#'tashkilot',"last_name","specialty"]



class WorkerAdmin(admin.ModelAdmin):
    list_display=["FIO","bulim","specialty"]
    list_per_page=10
    ordering=("FIO","bulim","specialty")
    search_fields=['FIO']#'tashkilot',"last_name","specialty"]


class OrganizationAdmin(admin.ModelAdmin):
    list_display=['name']
    list_per_page=10
    search_fields=['name']
admin.site.register(Organization,OrganizationAdmin)
# admin.site.register(Worker_about,Worker_aboutAdmin)
admin.site.register(Worker,WorkerAdmin)


class QarindoshInline(admin.TabularInline):

    model = Relationship

    fields = ["qarindoshligi","qarindosh_ismi","qarindosh_tug_yil",'yashash_joyi','ish_joyi']

@admin.register(Worker_about)




class Workers_aboutAdmin(admin.ModelAdmin):

    inlines = [QarindoshInline, ]

    search_fields = ['FIO']

    list_per_page = 10
# class CustomUserAdmin(UserAdmin):
#     add_form=CustomUserCreationForm
#     form =CustomUserChangeForm
#     model = CustomUser

# admin.site.register(User)