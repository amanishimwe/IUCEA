from django.db import models
from django.shortcuts import render


# choices for type of establishment
countries = [('Burundi','Burundi'),('Kenya','Kenya'),('Rwanda','Rwanda'),('South Sudan','South Sudan'),('Tanzania','Tanzania'),('Uganda','Uganda')]
establishment_choices = [('private', 'private'),('public','public')]
membership = [('full member', 'full member'),('associate','associate'),('not member','not member')]
progression = [('chartered','chartered'), ('provisional', 'provisional'),('letter_of_intent','letter_of_intent')]
levels = [('Bachelors','Bachelors'),('Masters','Masters'),('Post Graduate Diploma','Post Graduate Diploma'),('Doctorate','Doctorate')]
offering =[('Full Time','Full Time'),('Part Time','Part Time'),('Weekend','Weekend'),('Online','Online')]
thematic =[('Science','Science'),('Engineering','Engineering'),('Business','Business')]
# Create your models here.
class Country(models.Model):
    class Meta:
        verbose_name_plural = 'countries'
    country_name = models.CharField(max_length = 100, choices = countries, default ='Burundi')

    def __str__(self):
        return self.country_name

class University(models.Model):
    class Meta:
        verbose_name_plural ='universities'
    country = models.ForeignKey('Country', on_delete = models.CASCADE,)
    university_name = models.CharField(max_length = 100)
    iucea_membership = models.CharField(max_length = 100,choices = membership, default = 'full member')
    type_of_establishment = models.CharField(max_length = 100, choices = establishment_choices, default = 'public')
    level_of_progression = models.CharField(max_length = 100, choices= progression, default = 'chartered')
    website = models.URLField(max_length = 140, default ="")

    def __str__(self):
        return self.university_name

class Program(models.Model):
    university = models.ForeignKey('University', on_delete = models.CASCADE,)
    program_name = models.CharField(max_length = 100)
    program_level = models.CharField(max_length = 100, choices = levels, default = 'Bachelors')
    program_offering = models.CharField(max_length = 100, choices = offering , default = 'Full Time')
    thematic_area = models.CharField(max_length = 100, choices = thematic , default = 'Science')

    def __str__(self):
        return self.program_name