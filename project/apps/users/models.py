from __future__ import unicode_literals

import datetime

from dateutil import relativedelta

from django.db import models
from django.contrib.auth.models import AbstractUser

from project.apps.users.utils import get_random_number


class User(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    number = models.IntegerField(default=get_random_number)

    @property
    def allowed(self):
        today = datetime.datetime.now().today()
        rd = relativedelta.relativedelta(today, self.birthday)
        return rd.years > 13

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in User._meta.fields]

