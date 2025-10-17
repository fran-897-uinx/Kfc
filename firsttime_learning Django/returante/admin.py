from django.contrib import admin
from .models import Menu, Reservation, Student, GroupLink

# ----------------------------
#  MENU ADMIN
# ----------------------------
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("title", "selection", "price", "available", "date_added")
    list_filter = ("selection", "available")
    search_fields = ("title",)
    list_editable = ("available",)
    ordering = ("-date_added",)

# ----------------------------
#  RESERVATION ADMIN
# ----------------------------
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "guest_phone_num", "date")
    search_fields = ("name", "email")
    ordering = ("-date",)
    readonly_fields = ("date",)

# ----------------------------
#  STUDENT ADMIN
# ----------------------------
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone_number", "registered_on")
    search_fields = ("name", "email", "phone_number")
    list_filter = ("registered_on",)
    readonly_fields = ("registered_on",)
    ordering = ("-registered_on",)

# ----------------------------
#  GROUP LINK ADMIN
# ----------------------------
@admin.register(GroupLink)
class GroupLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "link", "active")
    list_editable = ("active",)
    search_fields = ("title",)

    def save_model(self, request, obj, form, change):
        """
        Ensure only one WhatsApp group is active at a time.
        """
        if obj.active:
            # Deactivate all other active groups before saving this one
            GroupLink.objects.exclude(id=obj.id).update(active=False)
        super().save_model(request, obj, form, change)
