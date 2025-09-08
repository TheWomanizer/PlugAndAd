from django.db import models
from django.contrib.auth.models import User


class AdAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)  # 'google', 'meta', 'tiktok'
    account_id = models.CharField(max_length=100)
    account_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'platform', 'account_id']

    def __str__(self):
        return f"{self.platform} - {self.account_name}"


class Campaign(models.Model):
    ad_account = models.ForeignKey(AdAccount, on_delete=models.CASCADE)
    campaign_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ad_account.platform} - {self.name}"
