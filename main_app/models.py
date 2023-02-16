from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

CATEGORIES = (
    ('animals', 'Animals'),
    ('business', 'Business'),
    ('community', 'Community'),
    ('competition', 'Competition'),
    ('creative', 'Creative'),
    ('education', 'Education'),
    ('environment', 'Environment'),
    ('event', 'Event'),
    ('faith', 'Faith'),
    ('family', 'Family'),
    ('financial-emergency', 'Financial Emergency'),
    ('medical', 'Medical'),
    ('memorial', 'Memorial'),
    ('nonprofit', 'Nonprofit'),
    ('sports', 'Sports'),
    ('travel', 'Travel'),
    ('volunteer', 'Volunteer'),
    ('wishes', 'Wishes')
)

class Campaign(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(
        max_length=100,
        choices=CATEGORIES
    )
    goal = models.IntegerField()
    about = models.TextField(max_length=1000)
    link = models.CharField(
        max_length=250,
        blank=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'campaign_id': self.id})
    
class Donation(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    message = models.TextField(max_length=300)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for campaign_id: {self.campaign_id} @{self.url}"

        