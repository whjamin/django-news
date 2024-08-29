from django import forms

class CrawlForm(forms.Form):
    keyword = forms.CharField(label='Keyword', max_length=100)
    page_number = forms.IntegerField(label='Page Number', min_value=1)