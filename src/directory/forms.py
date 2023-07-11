from django import forms
from . import models
from django.core.exceptions import ValidationError

GenreChoice = [(obj.pk, obj.name) for obj in models.Genre.objects.all()]

class AddCityForm(forms.Form):
    Genre = forms.ChoiceField(
        choices= GenreChoice,
        required = True,
        label = "Select a genre",
    )
    name = forms.CharField(
        max_length=10,
        required=True,
        label="Enter book name"
    )
    description = forms.CharField(
        max_length=1000,
        required=True,
        label="Enter book description"
    )
    price = forms.DecimalField(
        max_digits=5,
        decimal_places=2
    )
 #   picture = forms.ImageField()

    def save(self):
        Genre = models.Genre.objects.get(
            pk=self.cleaned_data["Genre"])
        return models.Books.objects.create(
            Genre=Genre,
            name=self.cleaned_data["name"]
        )
    
class BooksModelForm(forms.ModelForm):
    class Meta:
        model = models.Books
        fields = [
            "Genre", "name", "description", "price"
        ]

#def email(data):
#    if data[-10:] !="@gmail.com":
#        raise ValidationError("The adress must be like '@gmail.com'")

#class TextArea(forms.Textarea):
#    template_name= "my-template.html"

class ContactForm(forms.Form):
    contact_gmail = forms.EmailField(
        required=True,
        label="Enter your email"
        #validators=[email]
    )
    message = forms.CharField(
        required=True,
        label="Enter your message",
        widget=forms.Textarea()
    )

    def send_gmail(self):
        contact_gmail=self.cleaned_data["contact_gmail"]
        message = self.cleaned_data["message"]