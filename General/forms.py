from django import forms
from .models import Author

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Nombre', help_text='Ingrese su nombre completo.',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'autor@email.com'}))
    born_date = forms.DateField(required=True,label='Fecha de Nacimiento', help_text='Ingrese la fecha de nacimiento del Autor' ,widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    died_date = forms.DateField(required=False,label='Fecha de Muerte', help_text='Ingrese la fecha de muerte del Autor (Opcional)' ,widget=forms.DateInput(attrs={'class': 'form-control',  'type':  'date'}))
    country = forms.CharField(max_length=100, required=True,label='Pais', help_text='Ingrese el pais de origen del Autor' ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    
    
class BookForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    release_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class':'form-control', 'type': 'date'}))
    isbn = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    author =forms.ModelChoiceField(Author.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))