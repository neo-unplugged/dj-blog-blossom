from django.db import models

class Content(models.Model):
    TYPE_CHOICES = [
        ('poem', 'Poem'),
        ('story', 'Story'),
        ('article', 'Article'),
    ]
    
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    content = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-upload_time']  # Orders by newest content first
