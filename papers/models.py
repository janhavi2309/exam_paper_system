from django.db import models
from users.models import CustomUser

class Paper(models.Model):
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'Teacher'})
    file = models.FileField(upload_to='encrypted_papers/')
    encrypted_key = models.BinaryField()
    status = models.CharField(max_length=20, default='Pending')  # Pending / Approved / Rejected
    uploaded_at = models.DateTimeField(auto_now_add=True)

class DecryptionRequest(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    moderator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'Moderator'})
    status = models.CharField(max_length=20, default='Pending')  # Pending / Approved / Rejected
    requested_at = models.DateTimeField(auto_now_add=True)

class ModerationReview(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    moderator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    decision = models.CharField(max_length=20)  # Approved / Rejected
    reviewed_at = models.DateTimeField(auto_now_add=True)

class FinalSelection(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    selected_at = models.DateTimeField(auto_now_add=True)

