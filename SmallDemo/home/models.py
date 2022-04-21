from django.db import models
from numpy import empty

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
    '''def save(self, *args, **kwargs):
        self.cost=round(float(self.cost),2)
        super(Project,self).save(*args,**kwargs)'''
    def __str__(self):
            return self.name

#Project Manager
class ProjectManager(models.Model):
    dev = models.ForeignKey(Dev, on_delete=models.CASCADE)
    project = models.ManyToManyField(Project, related_name="project_manager")  
    def project_name(self):
        return ', '.join([a.name for a in self.project.all()])
    project_name.short_description = "Project Name"
    
