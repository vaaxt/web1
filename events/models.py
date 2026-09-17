from django.db import models

app_name = "events"

class Event (models.Model) :
        title = models.CharField(max_length =200)
        description = models.TextField()
        slug = models.SlugField(max_length=220, unique=True)
        summary = models.CharField(max_length=240)
        poster = models.ImageField(upload_to="events/posters/", blank=True)
        starts_at = models.DateTimeField()
        is_published = models.BooleanField(default=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
                return self.title
        



                        