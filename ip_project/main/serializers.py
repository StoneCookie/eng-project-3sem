from rest_framework import serializers
from .models import Role, Users, Work, Company, Category, Course, Vacancy, Event, Note, News

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'fio',
                  'mail', 'phone', 'id_role')


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'fio', 'id_role')
