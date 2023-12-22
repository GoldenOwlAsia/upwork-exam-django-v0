from django.contrib.auth.models import User


# Create your models here.
class Customer(User):
    USERNAME_FIELD = "email"

    class Meta:
        db_table = "customer"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
