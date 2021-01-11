from django.db import models



# choices for type of establishment
establishment_choices = [('private', 'private'),('public','public')]
membership = [('full member', 'full member'),('associate','associate'),('not member','not member')]
progression = [('chartered','chartered'), ('provisional', 'provisional'),('letter_of_intent','letter_of_intent')]
# Create your models here.
class Country(models.Model):
    class Meta:
        verbose_name_plural = 'countries'
    country_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.country_name

class University(models.Model):
    class Meta:
        verbose_name_plural ='universities'
    country = models.ForeignKey(Country, default =1, on_delete=models.CASCADE)
    university_name = models.CharField(max_length = 100)
    iucea_membership = models.CharField(max_length = 100,choices = membership, default = 'full member')
    type_of_establishment = models.CharField(max_length = 100, choices = establishment_choices, default = 'public')
    level_of_progression = models.CharField(max_length = 100, choices= progression, default = 'chartered')

    def __str__(self):
        return self.university_name
