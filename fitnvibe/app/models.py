from django.db import models

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    features = models.TextField()
    icon_class = models.CharField(max_length=50)
    icon_color = models.CharField(max_length=20, default="#000", help_text="Enter a valid color (e.g., '#FF0000' or 'red')")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name