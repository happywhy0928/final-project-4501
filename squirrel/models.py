from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    
    latitude = models.FloatField(
            help_text=_('Latitude of Squirrel sighting'),
            blank = True,
    )

    longitude = models.FloatField(
            help_text=_('Longitude of Squirrel sighting'),
            blank = True,
    )

    unique_id = models.CharField(
            max_length = 100,
            help_text=_('Unique ID of Squirrel'),
    )

    AM = 'AM'
    PM = 'PM'
    
    SHIFT_CHOICES = [
            (AM, _('AM')),
            (PM, _('PM')),
    ]

    shift = models.CharField(
            max_length = 2,
            help_text=_('Shift of Squirrel'),
            choices=SHIFT_CHOICES,
            blank=True,
    )

    date = models.DateField(
            help_text = ('Date of record'),
            blank = True,
    )
    
    JUVENILE = 'Juvenile'
    ADULT = 'Adult'

    AGE_CHOICES = [
            (JUVENILE, _('Juvenile')),
            (ADULT, _('Adult')),
    ]

    age = models.CharField(
            max_length = 8,
            help_text=_('Age of Squirrel'),
            choices = AGE_CHOICES,
            blank=True,
    )
    
    BLACK = 'Black'
    CINNAMON = 'Cinnamon'
    GRAY = 'Gray'

    COLOR_CHOICE = (
            (BLACK,_('Black')),
            (CINNAMON,_('Cinnamon')),
            (GRAY,_('Gray')),
            )

    furColor = models.CharField(
            max_length=20,
            choices = COLOR_CHOICE,
            blank = True,
    )

    running = models.BooleanField(
            blank = True,
    )

    eating = models.BooleanField(
            blank = True,
    )

    climbing = models.BooleanField(
            blank = True,
    )
    
    def __str__(self):
        return self.unique_id
