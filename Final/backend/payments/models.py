from django.db import models
from django.conf import settings


class Payment(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="User",
        help_text="Select the user.",
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Amount",
        help_text="Enter the payment amount.",
    )
    payment_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Payment Date",
        help_text="The date and time this payment was made.",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
        verbose_name="Status",
        help_text="Select the payment status.",
    )
