"""
Form for searchapp
"""
from django import forms


class SearchForm(forms.Form):
    """
    A form which allows you to search a term.
    """
    search_term = forms.CharField(required=True, max_length=100)
