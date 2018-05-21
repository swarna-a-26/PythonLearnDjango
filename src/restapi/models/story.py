from django.db import models

# Create your models here.
class Story(models.Model):
    story_id = models.AutoField(primary_key=True)
    story_title = models.CharField(max_length=100, unique=True)
    age_group = models.CharField(max_length=100,default='3-8')
    is_active = models.BooleanField(default=False)
    album_image = models.TextField()

    class Meta:
        db_table = 'story'