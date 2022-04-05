from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from Library.models import Book, Author, Publisher


class BookForms(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorForms(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class PublisherForms(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

