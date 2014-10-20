from django.contrib import admin
from books.models import Publisher, Book, Author

# Register your models here.

#admin.site.register(Publisher, Books)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    filter_vertical = ('authors',)
    raw_id_fields = ('publisher',)
    #fields = ('title', 'authors', 'publisher', 'publication_date')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
