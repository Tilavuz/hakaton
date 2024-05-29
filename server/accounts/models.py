from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Viloyat model represents a region
class Viloyat(models.Model):
    name = models.CharField(max_length=300)
    overall = models.SmallIntegerField(default=0)
    plan_en_b2 = models.SmallIntegerField(default=0)
    plan_en_c1 = models.SmallIntegerField(default=0)
    plan_en_c2 = models.SmallIntegerField(default=0)
    plan_deorother_b2 = models.SmallIntegerField(default=0)
    plan_deorother_c1 = models.SmallIntegerField(default=0)
    plan_deorother_c2 = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"
        ordering = ["name"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(plan_en_b2__lte=models.F("overall"))
                & models.Q(plan_en_c1__lte=models.F("overall"))
                & models.Q(plan_en_c2__lte=models.F("overall"))
                & models.Q(plan_deorother_b2__lte=models.F("overall"))
                & models.Q(plan_deorother_c1__lte=models.F("overall"))
                & models.Q(plan_deorother_c2__lte=models.F("overall")),
                name="viloyat_plan_constraint",
            )
        ]

    def __str__(self) -> str:
        return f"{self.name}"

    def clean(self):
        # Ensure that the sum of all plans does not exceed the overall value
        if (
            self.plan_en_b2
            + self.plan_en_c1
            + self.plan_en_c2
            + self.plan_deorother_b2
            + self.plan_deorother_c1
            + self.plan_deorother_c2
            > self.overall
        ):
            raise ValidationError(
                {"overall": "Sum of plans cannot exceed overall value"}
            )

    def save(self, *args, **kwargs):
        # Validate the data before saving
        self.clean()
        super().save(*args, **kwargs)

# Tuman model represents a district
class Tuman(models.Model):
    name = models.CharField(max_length=300)
    overall = models.SmallIntegerField(default=0)
    plan_en_b2 = models.SmallIntegerField(default=0)
    plan_en_c1 = models.SmallIntegerField(default=0)
    plan_en_c2 = models.SmallIntegerField(default=0)
    plan_deorother_b2 = models.SmallIntegerField(default=0)
    plan_deorother_c1 = models.SmallIntegerField(default=0)
    plan_deorother_c2 = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = "Tuman"
        verbose_name_plural = "Tumanlar"
        ordering = ["name"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(plan_en_b2__lte=models.F("overall"))
                & models.Q(plan_en_c1__lte=models.F("overall"))
                & models.Q(plan_en_c2__lte=models.F("overall"))
                & models.Q(plan_deorother_b2__lte=models.F("overall"))
                & models.Q(plan_deorother_c1__lte=models.F("overall"))
                & models.Q(plan_deorother_c2__lte=models.F("overall")),
                name="tuman_plan_constraint",
            )
        ]

    def __str__(self) -> str:
        return f"{self.name}"

    def clean(self):
        # Ensure that the sum of all plans does not exceed the overall value
        if (
            self.plan_en_b2
            + self.plan_en_c1
            + self.plan_en_c2
            + self.plan_deorother_b2
            + self.plan_deorother_c1
            + self.plan_deorother_c2
            > self.overall
        ):
            raise ValidationError(
                {"overall": "Sum of plans cannot exceed overall value"}
            )

    def save(self, *args, **kwargs):
        # Validate the data before saving
        self.clean()
        super().save(*args, **kwargs)

# Mahalla model represents a neighborhood
class Mahalla(models.Model):
    name = models.CharField(max_length=300)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    overall = models.SmallIntegerField(default=0)
    plan_en_b2 = models.SmallIntegerField(default=0)
    plan_en_c1 = models.SmallIntegerField(default=0)
    plan_en_c2 = models.SmallIntegerField(default=0)
    plan_deorother_b2 = models.SmallIntegerField(default=0)
    plan_deorother_c1 = models.SmallIntegerField(default=0)
    plan_deorother_c2 = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = "Mahalla"
        verbose_name_plural = "Mahallalar"
        ordering = ["name"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(plan_en_b2__lte=models.F("overall"))
                & models.Q(plan_en_c1__lte=models.F("overall"))
                & models.Q(plan_en_c2__lte=models.F("overall"))
                & models.Q(plan_deorother_b2__lte=models.F("overall"))
                & models.Q(plan_deorother_c1__lte=models.F("overall"))
                & models.Q(plan_deorother_c2__lte=models.F("overall")),
                name="mahalla_plan_constraint",
            )
        ]

    def __str__(self) -> str:
        return f"{self.name}"

    def clean(self):
        # Ensure that the sum of all plans does not exceed the overall value
        if (
            self.plan_en_b2
            + self.plan_en_c1
            + self.plan_en_c2
            + self.plan_deorother_b2
            + self.plan_deorother_c1
            + self.plan_deorother_c2
            > self.overall
        ):
            raise ValidationError(
                {"overall": "Sum of plans cannot exceed overall value"}
            )

    def save(self, *args, **kwargs):
        # Validate the data before saving
        self.clean()
        super().save(*args, **kwargs)

# Maktab model represents a school
class Maktab(models.Model):
    name = models.CharField(max_length=300)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE, default=1, related_name="maktablar")
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE, related_name="mahallalar")
    overall = models.SmallIntegerField(default=0)
    plan_en_b2 = models.SmallIntegerField(default=0)
    plan_en_c1 = models.SmallIntegerField(default=0)
    plan_en_c2 = models.SmallIntegerField(default=0)
    plan_deorother_b2 = models.SmallIntegerField(default=0)
    plan_deorother_c1 = models.SmallIntegerField(default=0)
    plan_deorother_c2 = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"
        ordering = ["name"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(plan_en_b2__lte=models.F("overall"))
                & models.Q(plan_en_c1__lte=models.F("overall"))
                & models.Q(plan_en_c2__lte=models.F("overall"))
                & models.Q(plan_deorother_b2__lte=models.F("overall"))
                & models.Q(plan_deorother_c1__lte=models.F("overall"))
                & models.Q(plan_deorother_c2__lte=models.F("overall")),
                name="maktab_plan_constraint",
            )
        ]

    def __str__(self) -> str:
        return f"{self.name}"

    def clean(self):
        # Ensure that the sum of all plans does not exceed the overall value
        if (
            self.plan_en_b2
            + self.plan_en_c1
            + self.plan_en_c2
            + self.plan_deorother_b2
            + self.plan_deorother_c1
            + self.plan_deorother_c2
            > self.overall
        ):
            raise ValidationError(
                {"overall": "Sum of plans cannot exceed overall value"}
            )

    def save(self, *args, **kwargs):
        # Validate the data before saving
        self.clean()
        super().save(*args, **kwargs)

# User model extending Django's AbstractUser
class User(AbstractUser):
    # Constants representing user roles
    ROLE_ADMIN = 7
    ROLE_HOKIM = 6
    ROLE_HOKIM_YORDAMCHISI = 5
    ROLE_TUMAN_MASUL = 4
    ROLE_TUMAN_YOSHLAR_ISHLARI = 3
    ROLE_MAHALLA_MASUL = 2
    ROLE_MAKTAB_MASUL = 1

    # Choices for user roles
    ROLE_CHOICES = [
        (ROLE_ADMIN, "Admin"),
        (ROLE_HOKIM, "Regional Governor"),
        (ROLE_HOKIM_YORDAMCHISI, "Regional Governor's Assistant"),
        (ROLE_TUMAN_MASUL, "District Governor"),
        (ROLE_TUMAN_YOSHLAR_ISHLARI, "District Youth Affairs Officer"),
        (ROLE_MAHALLA_MASUL, "Community Youth Affairs Officer"),
        (ROLE_MAKTAB_MASUL, "School Administrator"),
    ]

    # User model fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now=True)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE, null=True, blank=True, default=None)
    role = models.IntegerField(choices=ROLE_CHOICES, default=ROLE_MAHALLA_MASUL)
    rank = models.IntegerField(editable=False, null=True, blank=True)

    # Meta information
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["role", "username"]

    def __str__(self) -> str:
        return f"{self.username} - {self.role}"

    # User groups and permissions
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        related_name="custom_user_set",
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        related_name="custom_user_set",
        help_text="Specific permissions for this user.",
    )
