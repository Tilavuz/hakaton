from django.db import models
from accounts.models import Tuman, Mahalla, Maktab

# UserInfo model represents detailed user information
class UserInfo(models.Model):
    name = models.CharField(max_length=500)  # User's first name
    lastname = models.CharField(max_length=500)  # User's last name
    fname = models.CharField(max_length=500)  # User's father's name
    image = models.ImageField(upload_to="images", blank=True)  # User's profile image
    school = models.ForeignKey(Maktab, on_delete=models.CASCADE)  # User's school
    neighborhood = models.ForeignKey(Mahalla, on_delete=models.CASCADE)  # User's neighborhood
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)  # User's district
    JSHSHIR = models.IntegerField()  # User's unique identification number
    phone_number = models.CharField(max_length=20)  # User's phone number
    userdate = models.DateField(auto_now_add=True)  # Date when the user information was added

    # Language choices for the user
    LANG_CHOICES = (
        ("english", "English"),
        ("others", "Others"),
        ("nemesis", "Nemesis"),
    )
    title = models.CharField(max_length=300, verbose_name="Language", choices=LANG_CHOICES)  # User's preferred language

    # Status choices for the user
    STATUS_CHOICES = (
        ("uqimoqda", "Uqimoqda"),
        ("tugatgan", "Tugatgan"),
    )
    status = models.CharField(max_length=300, choices=STATUS_CHOICES)  # User's status

    def __str__(self):
        return self.name  # String representation of the model

# Certificate model represents certificates owned by a user
class Certificate(models.Model):
    user_info = models.ForeignKey(
        UserInfo, on_delete=models.CASCADE, related_name="certificates"
    )  # Foreign key to UserInfo model

    # Language choices for the certificate
    LANG_CHOICES = (
        ("english", "English"),
        ("others", "Others"),
        ("nemesis", "Nemesis"),
    )
    title = models.CharField(max_length=300, verbose_name="Language", choices=LANG_CHOICES)  # Certificate language

    # Proficiency level choices for the certificate
    LEVEL_CHOICES = (
        ("B2", "B2"),
        ("C1", "C1"),
    )
    overel = models.CharField(max_length=2, verbose_name="Overel", choices=LEVEL_CHOICES)  # Proficiency level

    url = models.CharField(max_length=300, blank=True)  # URL of the certificate
    serticatedate = models.DateField(auto_now_add=True)  # Date when the certificate was added

    def __str__(self):
        return f"{self.user_info.name} - {self.title} - {self.overel}"  # String representation of the model
