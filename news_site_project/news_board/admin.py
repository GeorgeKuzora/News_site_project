from django.contrib import admin
from news_board.models import News, Commentaries


class CommentariesInLine(admin.TabularInline):
    model = Commentaries


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'creation_at', 'updated_at', 'is_active']
    list_filter = ['is_active']
    inlines = [CommentariesInLine]
    actions = ['mark_is_active', 'mark_not_active']

    def mark_is_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_not_active(self, request, queryset):
        queryset.update(is_active=False)

    mark_is_active.short_description = 'Перевести в статус активно'
    mark_not_active.short_description = 'Перевести в статус неактивно'

    def __str__(self):
        return self.title


@admin.register(Commentaries)
class CommentariesAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'short_commentary', 'connected_news']
    list_filter = ['user_name']
    actions = ['replace_comment_text_with_delete']

    @admin.display(description='commentary')
    def short_commentary(self, obj):
        return ("%s..." % obj.commentary[:15])

    def replace_comment_text_with_delete(self, request, queryset):
        queryset.update(commentary='Удалено андминистратором')

    replace_comment_text_with_delete.short_description = 'Заменить текст комментария на "Удалено администратором"'

    def __str__(self):
        return self.commentary

