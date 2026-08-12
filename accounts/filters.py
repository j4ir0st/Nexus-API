from rest_framework import permissions, viewsets, filters
from django_filters import rest_framework as filter
import django_filters.rest_framework as df
from django.shortcuts import render
from django.contrib import admin
from django.db.models import Q
from .serializers import *
from .models import *


class CharInFilter(filter.BaseInFilter, filter.CharFilter):
    pass

class ExtendedUsersFilter(df.FilterSet):
    class Meta:
        model = ExtendedUsers
        fields = {
            'username': ['exact'], 
            'first_name': ['exact'], 
            'last_name': ['exact'], 
            'email': ['exact'],
            'is_active': ['exact'],
        }