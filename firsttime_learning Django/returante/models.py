from django.db import models


# ----------------------
# - Menu model
# ---------------------


class Menu(models.Model):
    SELECTION = [
        ("food", "Food"),
        ("drink", "Drink"),
        ("snack", "Snack"),
    ]

    sample = models.ImageField(upload_to="sample/", blank=True, null=True)
    title = models.CharField(max_length=20)
    discription = models.TextField(null=True, blank=True, max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    selection = models.CharField(max_length=10, choices=SELECTION, default="Foods")
    available = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " - " + str(self.price)


class Reservation(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    date = models.DateTimeField()
    meassage = models.TextField(max_length=500, null=True, blank=True)
    guest_phone_num = models.IntegerField()
    menu_items = models.ManyToManyField(Menu, blank=True)

    def __str__(self):
        return f"placed reservertion by {self.name} on {self.date}"


class GroupLink(models.Model):
    title = models.CharField(max_length=100, default="KFC Student Group")
    link = models.URLField(
        default="https://chat.whatsapp.com/XXXXXXXXXXXXXXX",
        help_text="WhatsApp group invite link for registered students.",
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registered_on = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(blank=True, null=True)
    whatsapp_joined = models.BooleanField(default=False)
    joined_group_name = models.ForeignKey(
        GroupLink,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students",
        help_text="The WhatsApp group this student joined.",
    )

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    desc = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class GalleryItem(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="gallery/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BlogDisplay(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="blogs/")
    description = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Auto-generate subtitle if none provided
        if not self.sub_title:
            self.sub_title = self.title[:20]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.sub_title}"
