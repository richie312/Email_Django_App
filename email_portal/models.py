# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import Model 

# Create your models here.
class BlogPost(models.Model):
	title = models.TextField()
	content = models.CharField(max_length = 100, null = True,blank = True) 



class CompanyEmail1(models.Model):
    company_name = models.CharField(db_column='Company_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=35, blank=True, null=True)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=50, blank=True,primary_key = True)  # Field name made lowercase.
    application_date = models.DateTimeField(db_column='Application_Date', blank=True, null=True)  # Field name made lowercase.
    #id = models.IntegerField(blank=True, primary_key = True)
    class Meta:
        managed = False
        db_table = 'company_email1'


class KnowledgeBase(models.Model):
    id = models.IntegerField(blank=True, primary_key = True)
    dateofreading = models.DateTimeField(blank=True, null=True)
    title = models.CharField(db_column='Title', max_length=30, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=30, blank=True, null=True)  # Field name made lowercase.
    resource = models.TextField(db_column='Resource', blank=True, null=True)  # Field name made lowercase.
    online_resource = models.CharField(db_column='Online_Resource', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'knowledge_base'


class Readings(models.Model):
    id = models.IntegerField(primary_key=True)
    dateofreading = models.DateTimeField()
    temperature = models.CharField(max_length=10, blank=True, null=True)
    humidity = models.DecimalField(db_column='Humidity', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'readings'
        unique_together = (('id', 'dateofreading'),)


class ReadingsSonar(models.Model):
    id = models.IntegerField(primary_key=True)
    dateofreading = models.DateTimeField()
    distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'readings_sonar'
        unique_together = (('id', 'dateofreading'),)


class ReadingsSonarDist(models.Model):
    dateofreading = models.DateTimeField(primary_key=True)
    distance = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'readings_sonar_dist'


class ReadingsTemp(models.Model):
    id = models.IntegerField(primary_key=True)
    dateofreading = models.DateTimeField()
    temperature = models.CharField(max_length=10, blank=True, null=True)
    humidity = models.CharField(db_column='Humidity', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'readings_temp'
        unique_together = (('id', 'dateofreading'),)


class VideoStat(models.Model):
    id = models.CharField(db_column='ID', max_length=50, blank=True, primary_key = True)  # Field name made lowercase.
    viewcount = models.CharField(db_column='viewCount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    likecount = models.CharField(db_column='likeCount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    favoritecount = models.CharField(db_column='favoriteCount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    commentcount = models.CharField(db_column='commentCount', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dislikecount = models.CharField(db_column='dislikeCount', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'video_stat'


class VideoStatTableDf(models.Model):
    id = models.CharField(max_length=11, blank=True, primary_key = True)
    view_count = models.CharField(db_column='view_Count', max_length=10, blank=True, null=True)  # Field name made lowercase.
    like_count = models.CharField(db_column='like_Count', max_length=7, blank=True, null=True)  # Field name made lowercase.
    favorite_count = models.CharField(db_column='favorite_Count', max_length=4, blank=True, null=True)  # Field name made lowercase.
    comment_count = models.CharField(db_column='comment_Count', max_length=6, blank=True, null=True)  # Field name made lowercase.
    dislike_count = models.CharField(db_column='dislike_Count', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'video_stat_table_df'