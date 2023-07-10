from django.db import models
from django.contrib.auth import get_user_model
from directory.models import Books

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        verbose_name="Customer",
        on_delete=models.PROTECT,
        related_name="carts",
        null=True,
        blank=True
    )

class GoodInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name="cart",
        on_delete=models.CASCADE,
        related_name="goods"
    )
    good = models.ForeignKey(
        Books,
        verbose_name="Books",
        on_delete=models.PROTECT
    )
    quantity = models.PositiveIntegerField(
        verbose_name="quantity",
        default=1
    )
    price = models.DecimalField(
        verbose_name="price",
        max_digits=5,
        decimal_places=2
    )
    created = models.DateTimeField(
        verbose_name="created",
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name="updated",
        auto_now_add=False,
        auto_now=True
    )

    def __str__(self) -> str:
        return f"{self.good.name} x {self.quantity}"


class Status(models.Model):
    name = models.CharField(
        verbose_name='Status',
        max_length=20
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    delivery_address = models.TextField(
        verbose_name="delivery_address"
    )
    status = models.ForeignKey(
        Status,
        verbose_name="order_status",
        on_delete=models.PROTECT
    )
    cart = models.OneToOneField(
        Cart,
        verbose_name="cart",
        on_delete=models.PROTECT
    )
    created = models.DateTimeField(
        verbose_name="created",
        auto_now_add=True,
        auto_now=False
    )
    updated = models.DateTimeField(
        verbose_name="updated",
        auto_now_add=False,
        auto_now=True
    )