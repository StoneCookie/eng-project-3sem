from django.contrib import admin
from .models import Role, Users, Work, Company, Category, Course, Vacancy, Event, Note, News
from django import forms

from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class RoleResource(resources.ModelResource):

    class Meta:
        model = Role
        skip_unchanged = True
        report_skipped = False

@admin.register(Role)
class RoleAdmin(ImportExportModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name", )
    search_fields = ("name__startswith", )
    resource_class = RoleResource

class UsersResource(resources.ModelResource):

    class Meta:
        model = Users
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'fio', 'mail', 'id_role')

@admin.register(Users)
class UsersAdmin(ImportExportModelAdmin):
    list_display = ("id", "fio", "mail", "login", "password", "id_role")
    list_filter = ("id_role", )
    search_fields = ("fio", )
    resource_class = UsersResource

class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category
        skip_unchanged = True
        report_skipped = False

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name", )
    search_fields = ("name__startswith", )
    resource_class = CategoryResource

class WorkResource(resources.ModelResource):

    class Meta:
        model = Work
        skip_unchanged = True
        report_skipped = False

@admin.register(Work)
class WorkAdmin(ImportExportModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name", )
    search_fields = ("name__startswith", )
    resource_class = WorkResource

class VacancyResource(resources.ModelResource):

    class Meta:
        model = Vacancy
        skip_unchanged = True
        report_skipped = False

@admin.register(Vacancy)
class VacancyAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "description", "requirements", "conditions",
                    "responsibilities", "id_category", "id_work", "id_company")
    list_filter = ("name", "requirements", "conditions",
                   "responsibilities", "id_category", "id_work", "id_company")
    search_fields = ("name",)
    resource_class = VacancyResource

class CompanyResource(resources.ModelResource):

    class Meta:
        model = Company
        skip_unchanged = True
        report_skipped = False

@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "description", "mail", "phone",
                    "fio", "login", "password", "id_role")
    list_filter = ("name", )
    search_fields = ("name", )
    resource_class = CompanyResource
    fields = ('name', 'description', 'fio', 'mail', 'phone', 'id_role',)

class EventResource(resources.ModelResource):

    class Meta:
        model = Event
        skip_unchanged = True
        report_skipped = False

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "date", "id_company")
    list_filter = ("name", "date", "id_company")
    search_fields = ("name", )
    date_hierarchy = ("date")
    resource_class = EventResource

class CourseResource(resources.ModelResource):

    class Meta:
        model = Course
        skip_unchanged = True
        report_skipped = False


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "description", "duration",
                    "id_category", "id_company", )
    list_filter = ("name", "duration",
                   "id_category", "id_company")
    search_fields = ("name", )
    resource_class = CourseResource

def make_published(modeladmin, request, queryset):
    queryset.update(status='о')


make_published.short_description = "Изменить статус на Опубликовано"


class NewsResource(resources.ModelResource):

    class Meta:
        model = News
        skip_unchanged = True
        report_skipped = False

@admin.register(News)
class NewsAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "description", "date",
                    "id_category", "id_company", "status")
    list_filter = ("id", "name", "id_company", "id_category", "date",)
    search_fields = ("name",)
    date_hierarchy = ("date")
    resource_class = NewsResource
    actions = [make_published]

class NoteResource(resources.ModelResource):

    class Meta:
        model = Note
        skip_unchanged = True
        report_skipped = False

@admin.register(Note)
class NoteAdmin(ImportExportModelAdmin):
    list_display = ("id", "id_user", "id_course")
    list_filter = ("id_course", )
    resource_class = NoteResource
