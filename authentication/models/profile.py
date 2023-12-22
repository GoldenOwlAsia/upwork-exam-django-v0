from django.db import models
from .customer import Customer
from django_core.models import BaseModel


class Profile(BaseModel):
    name = models.CharField(verbose_name="Name", max_length=30, blank=True)
    description = models.TextField(
        verbose_name="Description", max_length=500, blank=True
    )
    user = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="profile_list"
    )
    is_liked_by = models.ManyToManyField(
        Customer, related_name="favorite_profiles", null=True
    )

    class Meta:
        db_table = "profile"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
