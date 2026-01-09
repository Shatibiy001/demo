from django.contrib import admin

# Register your models here.
from .models import Project, Review, Tag, Message

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'vote_ratio', 'vote_total', 'created')
    list_filter = ('created', 'vote_ratio')
    search_fields = ('title', 'description', 'owner__user__username', 'owner__name')
    filter_horizontal = ('tags',)
    raw_id_fields = ('owner',)
    
    fieldsets = (
        ('Project Info', {
            'fields': ('title', 'description', 'featured_image')
        }),
        ('Owner & Links', {
            'fields': ('owner', 'demo_link', 'source_link')
        }),
        ('Tags & Reviews', {
            'fields': ('tags',)
        }),
        ('Voting', {
            'fields': ('vote_total', 'vote_ratio')
        }),
    )

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('project', 'value', 'created')
    list_filter = ('value', 'created')
    search_fields = ('project__title', 'body')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Message)