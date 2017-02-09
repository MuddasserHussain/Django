"""
Models for searchapp
"""
from django.db import models


class History(models.Model):
    """
    Model to store history of terms searached by user.
    """
    search_term = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of a single History object.
        """
        return "{}, {}".format(
            self.search_term,
            self.time_stamp.strftime("%Y-%m-%d %H:%M:%S")
        )
