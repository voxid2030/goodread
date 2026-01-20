from django.contrib import admin
from .models import Book, Author, BookAuthor, BookReview


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')
    list_filter = ('title',)
    list_display = ('title', 'isbn', 'description')

class AuthorAdmin(admin.ModelAdmin):
        search_fields = ('first_name','last_name','email',)
        list_filter = ('first_name','last_name','email',)
        list_display = ('first_name','last_name','email',)


admin.site.register(Book, BookAdmin)

admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor)
admin.site.register(BookReview)



