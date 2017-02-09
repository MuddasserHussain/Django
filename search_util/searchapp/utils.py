"""
Utility functions and constants
"""
import os
import datetime

from searchapp.models import History

BASE_URL = os.path.dirname(os.path.abspath(__file__))
DATA_DIRECTORY = os.path.join(BASE_URL, 'data')
DATA_FILE_NAME = 'data_file.txt'

DATA_FILE_PATH = os.path.join(DATA_DIRECTORY, DATA_FILE_NAME)

SEARCH_TEMPLATE = 'search.html'
SEARCH_RESULTS_TEMPLATE = 'search_results.html'


def get_term_occurances(term):
    """
    Returns the occurances of a term in our
    data file. Returs a dictionary which
    consists of line numbe (as key) and text
    (as value) of actual line.

    Arguments:
        term(str): The term to be found.

    Returs:
        dict: A dictionary of found occurances.
    """
    line_to_return = None
    line_number_iterator = 1
    matching_lines = []
    matching_line_numbers = []

    with open(DATA_FILE_PATH, 'r', encoding='utf-8') as data_file:
        for line in data_file:
            if term in line:
                matching_line_numbers.append(line_number_iterator)
                matching_lines.append(line)
            line_number_iterator += 1

    return dict(zip(matching_line_numbers, matching_lines))


def add_to_history(term):
    """
    Adds the term into history table.
    """
    history = History(search_term=term, time_stamp=datetime.datetime.now())
    history.save()
