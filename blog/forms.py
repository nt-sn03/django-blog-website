from django import forms


class BlogCreateForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=127)
    reading_minute = forms.IntegerField(min_value=1, max_value=120)
    content = forms.CharField(min_length=1)
    tg_link = forms.URLField()
    is_published = forms.BooleanField(required=False)


class BlogSearchForm(forms.Form):
    search = forms.CharField(min_length=5, max_length=20)
