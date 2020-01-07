from django.contrib import admin

# Register your models here.

from .models import (BlogPost, CompanyEmail1, KnowledgeBase, Readings, ReadingsSonar, ReadingsSonarDist, ReadingsTemp, VideoStat,
VideoStatTableDf)

table_list = [BlogPost, CompanyEmail1, KnowledgeBase, Readings, ReadingsSonar, ReadingsSonarDist, ReadingsTemp, VideoStat,
VideoStatTableDf]

# Register the database in the admin
for i in table_list:
    admin.site.register(i)

