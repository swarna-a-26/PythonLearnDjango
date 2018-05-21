from django.db import models
import uuid
from restapi.models import Story

# Create your models here.
class Circle(models.Model):
    circle_id = models.AutoField(primary_key=True)
    story = models.ForeignKey(Story)
    duration = models.IntegerField(blank=True)
    is_active = models.BooleanField(default=False)
    album_image = models.TextField()
    teller_image = models.TextField()
    teller_name = models.TextField(blank=True)
    scheduled_time = models.DateTimeField(blank=True)
    created_date = models.DateTimeField(blank=True)
    updated_date = models.DateTimeField()
    live_stream_url = models.TextField()
    last_index = models.IntegerField()
    group_access = models.TextField(blank=True)
    vod_stream_url = models.TextField(blank=True)
    on_demand_id  = models.UUIDField(default=uuid.uuid1,unique=True)
    status = models.TextField(default="NOT_STARTED")
    on_demand_status = models.TextField(default="NOT_AVAILABLE")

    class Meta:
        db_table = 'circle'