from django.contrib import admin
from .models import Question, Choice

# Вариант 1: Простая регистрация (как было)
# admin.site.register(Question)
# admin.site.register(Choice)

# Вариант 2: Кастомизированная админка (рекомендуется)
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3  # Количество пустых полей для новых вариантов

class QuestionAdmin(admin.ModelAdmin):
    # Поля, которые отображаются в списке вопросов
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    
    # Фильтры справа
    list_filter = ['pub_date']
    
    # Поиск по полям
    search_fields = ['question_text']
    
    # Разбивка на страницы
    list_per_page = 20
    
    # Порядок полей в форме редактирования
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {
            'fields': ['pub_date'],
            'classes': ['collapse']  # Сворачиваемый раздел
        }),
    ]
    
    # Добавляем варианты ответов прямо в форму вопроса
    inlines = [ChoiceInline]

# Регистрируем с кастомизацией
admin.site.register(Question, QuestionAdmin)

# Если хочешь, чтобы Choice тоже был отдельно в админке
# (но они уже доступны через inline в Question)
admin.site.register(Choice)