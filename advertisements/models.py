from django.db import models


# Create your models here.
class AdvertisementBanner(models.Model):
    media = models.FileField(upload_to='advertisement-media/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class AdvertisementModel(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ManyToManyField(AdvertisementBanner, related_name="AdvertisementModel_banner", blank=True)
    redirected_link = models.URLField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
