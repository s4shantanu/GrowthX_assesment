from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.username

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tagged_assignments')
    task = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Assignment for {self.admin.username}"
