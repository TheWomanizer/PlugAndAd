from django.db import models

# Create your models here.
class Saving (models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"${self.amount}-{self.date.strftime('%Y-%m-%d')}"