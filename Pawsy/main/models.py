from django.db import models
from django.db.models.fields import CharField


class AnimalGender(models.TextChoices):
    MALE = 'M','Male'
    FEMALE = 'F','Female'
class Gender(models.Model):
    name = models.CharField(max_length=1,choices=AnimalGender.choices,
                            default=AnimalGender.MALE)

    def __str__(self):
        return self.name


class Wool(models.Model):



class Size(models.Model):
    name = models.IntegerField(max_length=25)

    def __str__(self):
        return self.name


class AnimalBreed(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields='name')]
        verbose_name = 'animal_breed'
        verbose_name_plural = 'animal_breeds'


class Animal(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    age = models.IntegerField(max_length=30)
    size = models.ManyToManyField(Size,verbose_name='animal-size',
                                  related_name='animal_size')
    gender = models.ManyToManyField(Gender,through='animal-gender',
                                    related_name='animal_gender')
    breed = models.ForeignKey(AnimalBreed,on_delete=models.CASCADE,
                              verbose_name='animal-breed',related_name='animal_breed')