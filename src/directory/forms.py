from django import forms
from . import models

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
            "Genre", "name"
        ]