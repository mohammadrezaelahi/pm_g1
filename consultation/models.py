from django.db import models


class ConsultationRequest(models.Model):
    subject = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} requested a consultation about {self.subject} | {self.phone}"
