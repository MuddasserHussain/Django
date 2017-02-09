"""
Views for searchapp
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from searchapp.utils import (
    get_term_occurances,
    add_to_history,
    SEARCH_TEMPLATE,
    SEARCH_RESULTS_TEMPLATE,
)
from searchapp.forms import SearchForm


def search(request):
    """
    Displays a serach form.
    """
    search_form = SearchForm()
    return render(request, SEARCH_TEMPLATE, {'form': search_form})


def search_results(request):
    """
    Displays the results of a search term.
    """
    search_term_identifier = 'search_term'
    search_term = request.GET[search_term_identifier]

    form = SearchForm(request.GET)

    if not form.is_valid():
        return render(request, SEARCH_TEMPLATE, {'form': form})

    if search_term_identifier in request.GET:
        occurances = get_term_occurances(search_term)
        add_to_history(search_term)
        return render(
            request, SEARCH_RESULTS_TEMPLATE, {'result_list': occurances}
        )
