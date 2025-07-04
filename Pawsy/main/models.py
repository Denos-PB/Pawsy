from django.db import models
from django.db.models.fields import CharField


class AnimalGenderChoice(models.TextChoices):
    MALE = 'M','Male'
    FEMALE = 'F','Female'


class WoolChoice(models.TextChoices):
     SHORT = 'S', 'Short'
     LONG = 'L', 'Long'
     CURLY = 'C', 'Curly'
     HAIRLESS = 'H', 'Hairless'


class AnimalStatusChoice(models.TextChoices):
    LOOKING_FOR_HOME = 'L', 'Looking for home'
    NEED_SPECIAL_CARE = 'S', 'Need special care'
    FOUND_HOME = 'H', 'Found home'


class VolunteerStatusChoice(models.TextChoices):
    NEW = 'new', 'New'
    APPROVED = 'approved', 'Approved'
    REJECTED = 'rejected', 'Rejected'
    INACTIVE = 'inactive', 'Inactive'


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
    age = models.IntegerField()
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
    sterilized = models.BooleanField(default=False, verbose_name='sterilized')
    vaccinated = models.BooleanField(default=False,verbose_name='vaccinated')
    special_needs = models.TextField(blank=True,verbose_name='special needs')
    location = models.CharField(max_length=200,blank=True,verbose_name='location')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-data_arrived']
        verbose_name ='animal'
        indexes = [models.Index(fields = ['name'])]

class AdoptionRequest(models.Model):
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE,
                               related_name='adoption_request')
    name = models.CharField(max_length=100,verbose_name='name')
    phone = models.CharField(max_length=30,verbose_name='phone')
    email = models.EmailField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='new')

class Volunteer(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    phone = models.CharField(max_length=30, verbose_name='phone')
    email = models.EmailField()
    photo = models.ImageField(upload_to='volunteers/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=VolunteerStatusChoice.choices,
        default=VolunteerStatusChoice.NEW
    )
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']