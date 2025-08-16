from django.db import models

class Teacher(models.Model):
    full_name   = models.CharField(max_length=150)
    email       = models.EmailField(unique=True)
    phone       = models.CharField(max_length=20, blank=True)
    department  = models.CharField(max_length=100)
    hire_date   = models.DateField()
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name
