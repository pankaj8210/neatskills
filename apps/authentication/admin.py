# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from apps.authentication.models import *
from django.contrib import admin

# Register your models here.
admin.site.register(user)
admin.site.register(StudentInquiry)
admin.site.register(otpverifywithtimer)
admin.site.register(Courses)
admin.site.register(Chapter)
admin.site.register(Topics)
admin.site.register(Topics_screen)
admin.site.register(Batch_timing)
admin.site.register(Course_schedule)
admin.site.register(add_courses)
admin.site.register(Topic_course)
admin.site.register(Chapter_course)
admin.site.register(Screan_course)
admin.site.register(Addbatches)
admin.site.register(Courseschedule)
admin.site.register(Enrollmentlist)
