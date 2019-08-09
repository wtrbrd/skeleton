from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language


# Register your models here.
admin.site.register(Genre)
#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
#admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
#admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Language)