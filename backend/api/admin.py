"""Модуль настройки административной панели приложения api."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Класс настройки отображения модели Task в админке."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
