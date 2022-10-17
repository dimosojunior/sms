from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from DimosoApp.models import *

# Register your models here.

class MyUserAdmin(BaseUserAdmin):
    list_display=('username', 'email', 'company_name', 'profile_image', 'date_joined', 'last_login', 'is_admin', 'is_active')
    search_fields=('email', 'first_name', 'last_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'username','role', 'first_name', 'middle_name', 'last_name', 'company_name', 'phone', 'profile_image', 'password1', 'password2'),
        }),
    )

    ordering=('email',)
class ActivitiesAdmin(admin.ModelAdmin):
	list_display =["activity_name", "link","recorded_at","updated_at"]
	list_filter = ["recorded_at", "updated_at"]
	search_fields = ["activity_name","link"]

class RegisterStudentsAdmin(admin.ModelAdmin):
	list_display =["first_name","middle_name", "last_name", "regno", "phone", "email", "recorded_at","updated_at"]
	list_filter = ["recorded_at", "updated_at"]
	search_fields = ["first_name","middle_name", "last_name", "regno", "phone", "email"]
class SubjectsAdmin(admin.ModelAdmin):
	list_display =["subject_name", "subject_no","recorded_at","updated_at"]
	list_filter = ["recorded_at", "updated_at"]
	search_fields = ["subject_name","subject_no"]

class MarksAdmin(admin.ModelAdmin):
	list_display =["registerstudents","subjects", "Test1", "Test2", "Test3", "Test4","Test5","MidTerm","Term","total_marks","Average"]
	list_filter = ["Average", "subjects"]
	search_fields = ["registerstudents","subjects"]

class GeneralResultsAdmin(admin.ModelAdmin):
	list_display =["students","student_total", "student_average", "student_point", "student_grade"]
	list_filter = ["student_average", "student_point", "student_grade"]
	search_fields = ["students"]

class ImportantInformationsAdmin(admin.ModelAdmin):
	list_display =["students", "habit","debt"]
	list_filter = ["habit", "debt"]
	search_fields = ["students"]

class SendSmsEmailAdmin(admin.ModelAdmin):
	list_display =["students", "email","phone","post_date"]
	list_filter = ["post_date"]
	search_fields = ["students","email","phone"]
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Activities, ActivitiesAdmin)
admin.site.register(RegisterStudents, RegisterStudentsAdmin)
admin.site.register(Subjects, SubjectsAdmin)

admin.site.register(Marks, MarksAdmin)
admin.site.register(GeneralResults, GeneralResultsAdmin)
admin.site.register(ImportantInformations, ImportantInformationsAdmin)
admin.site.register(SendSmsEmail, SendSmsEmailAdmin)
admin.site.register(PangiliaAlama)
admin.site.register(IndividualResults)