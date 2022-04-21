from django.db import models


# Dev
class Dev(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    active=models.BooleanField()
    language=models.CharField(max_length=30)
    def __str__(self):
        return self.first_name +' '+ self.last_name


#Project
class Project(models.Model):
    des=models.CharField(max_length=500)
    name=models.CharField(max_length=20)
    start_date=models.DateField()
    end_date=models.DateField()
    cost=models.DecimalField(max_digits=20, decimal_places=2)
    dev = models.ManyToManyField(Dev, related_name="project") 
    def dev_name(self):
        return ', '.join([a[0] + ' '+a[1] for a in self.dev.values_list('first_name','last_name')])
    dev_name.short_description = "Dev Name"
    def __str__(self):
        return self.name