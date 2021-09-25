from django.db import models


class Subdivision(models.Model):
    """ Subdivision model """
    name = models.CharField(max_length=100, verbose_name='Name')
    slug = models.SlugField(max_length=100, verbose_name='Slug')
    order = models.IntegerField(default=0, verbose_name='Order')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    parent = models.ForeignKey("self", null=True, blank=True,
                               on_delete=models.SET_NULL,
                               verbose_name='Parent Item')

    class Meta:
        verbose_name = 'Subdivision item'
        verbose_name_plural = 'Subdivision items'
        ordering = ("order",)

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    """ Employee model """
    full_name = models.CharField(max_length=250, verbose_name='Full name')
    position = models.CharField(max_length=250)
    salary = models.DecimalField(max_digits=20, decimal_places=2)
    hiring = models.DateField(verbose_name='Hiring date')
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE,
                                    verbose_name='Subdivision')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Workers'

    def __str__(self):
        return f'{self.full_name}'
