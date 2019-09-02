from django.db import models

# About model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"

# Service model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service Name")
    description = models.TextField(verbose_name="About Service")

    def __str__(self):
        return self.name

# Recent Work model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work Title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title

# Client Model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client Name")
    description = models.TextField(verbose_name="Client Say")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return self.email