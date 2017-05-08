from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile

# NOTE: make sure that if you're creating a model from a form, that the
# form will contain and pass on all the data required to populate the
# model correctly!

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.cat_max_length, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        # Meta class defines which model we're providing the form for!
        # This is crucial!
        model = Category
        # Meta also specifies which fields to include in form
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page.page_max_length, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        # if url is not empty and doesn't start with 'http:// then prepend http://

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data

    class Meta:
        model = Page
        # Need to either specify which fields are included on form OR specify excluded
        exclude = ('category',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

