from rest_framework import generics
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage
from .serializers import ContactMessageSerializer


class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

    # Always send to admin
        send_mail(
            subject=f"New Contact from {instance.name}",
            message=f"Message from: {instance.email}\n\n{instance.message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["your_email@example.com"],
            fail_silently=False,
        )

    # Try sending confirmation (don’t break if it fails)
        try:
            send_mail(
                subject="We received your message",
                message=f"Hi {instance.name},\n\nThank you for reaching out! We'll get back to you soon.",
                from_email=settings.EMAIL_HOST_USER,   # use your sender
                recipient_list=[instance.email],
                fail_silently=False,
            )
        except Exception as e:
            # log but don’t crash API
            print(f"⚠️ Failed to send confirmation email: {e}")



# (Optional: for admin or dashboard API use)
class ContactMessageListView(generics.ListAPIView):
    queryset = ContactMessage.objects.all().order_by("-created_at")
    serializer_class = ContactMessageSerializer

