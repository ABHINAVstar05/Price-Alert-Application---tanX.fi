from django.db import models

# Create your models here.

# A user model to store user details.

class User(models.Model) :
    username = models.CharField(max_length = 100, unique = True, null = False, blank = False)
    password = models.TextField(null = False, blank = False)
    email = models.EmailField(unique = True, null = False, blank = False)

    def __str__(self):
        return f"{self.username} ({self.email})"
    

# An alert model to store details of alerts associated with different users. 
class Alert(models.Model) :
    
    STATUS = [
        ('CREATED', 'Created'),
        ('DELETED', 'Deleted'),
        ('TRIGGERED', 'Triggered'),
    ]

    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alert', null = False, blank = False)
    alert_purpose = models.CharField(max_length = 500, unique = True, null = False, blank = False)
    alert_price = models.DecimalField(max_digits=10, decimal_places=2, null = False, blank = False)
    alert_status = models.CharField(max_length = 20, choices = STATUS, default = 'CREATED')

    def __str__(self):
        return f"{self.username} ({self.alert_purpose})"
    