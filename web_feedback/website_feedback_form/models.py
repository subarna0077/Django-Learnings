from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator, MaxLengthValidator, MinLengthValidator

# Create your models here.
class WebsiteFormModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Enter full name", validators=[MinLengthValidator(10), MaxLengthValidator(50)])
    email_address = models.EmailField(validators=[EmailValidator()])

    yes_no_choices = [
        ("yes", "Yes"),
        ("no", "No")
    ]
    first_time_visit = models.CharField('Is this the first time you have visited the site?',max_length=3, choices= yes_no_choices, blank=False,)
    reason_to_visit = models.TextField('What is your reason of visiting this site?')
    user_friendlyness = models.IntegerField('How user friendly is this website?', validators=[MinValueValidator(1), MaxValueValidator(5)])

    FIND_CHOICES = [
        ("all", "Yes, all of it"),
        ("some", "Yes, some of it"),
        ("none", "No, none of it"),
    ]
    found_what_needed = models.CharField(
        max_length=10,
        choices=FIND_CHOICES,
        blank=False
    )


    

    def __str__(self):
        return f" {self.name} - {self.email_address}"
    