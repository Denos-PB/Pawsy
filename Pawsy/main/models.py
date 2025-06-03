from django.db import models
from django.db.models.fields import CharField


class AnimalGenderChoice(models.TextChoices):
    MALE = 'M','Male'
    FEMALE = 'F','Female'

class WoolChoice(models.TextChoices):
     SHORT = 'S' 'Short'
     LONG = 'L' 'Long'
     CURLY = 'C' 'Curly'
     HAIRLESS = 'H' 'Hairless'

class AnimalStatusChoice(models.TextChoices):
    LOOKING_FOR_HOME = 'L' 'Looking for home'
    NEED_SPECIAL_CARE = 'S' 'Need special care'
    FOUND_HOME = 'H' 'Found home'


class Gender(models.Model):
    name = models.CharField(max_length=1, choices=AnimalGenderChoice.choices,
                            default=AnimalGenderChoice.MALE)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100,)

    def __str__(self):
        return self.name

class Wool(models.Model):
    name = models.CharField(max_length=9, choices=WoolChoice.choices,
                            default=WoolChoice.SHORT)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=18,choices=AnimalStatusChoice.choices,
                            default=AnimalStatusChoice.LOOKING_FOR_HOME)

    def __str__(self):
        return self.name


class AnimalBreed(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'animal_breed'
        verbose_name_plural = 'animal_breeds'


class Animal(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    age = models.IntegerField(max_length=30)
    size = models.ForeignKey(Size,on_delete=models.SET_NULL,verbose_name='animal size',
                                  related_name='animal_size',null=True)
    gender = models.ForeignKey(Gender,on_delete=models.SET_NULL, verbose_name='animal gender',
                                    related_name='animal_gender',null=True)
    breed = models.ForeignKey(AnimalBreed,on_delete=models.SET_NULL,
                              verbose_name='animal breed',related_name='animal_breed',null=True)
    wool = models.ForeignKey(Wool,on_delete=models.SET_NULL,verbose_name='animal wool',
                                  related_name='animal_wool',null=True)
    color = models.ManyToManyField(Color,verbose_name='animal color',
                                   related_name='animal_color')
    status = models.ForeignKey(Status,on_delete=models.SET_NULL, verbose_name='animal status',
                                    related_name='animal_status', null=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='animals/',blank=True,null=True)
    data_arrived = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-data_arrived']
        verbose_name ='animal'
        indexes = [models.Index(fields = ['name'])]