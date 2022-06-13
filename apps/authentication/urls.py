# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, registration
from django.contrib.auth.views import LogoutView
from apps.authentication.views import *
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('login/',login_view, name="login"),
    path('course-1/', course1, name="course1"),
    path('course-2/', course2, name="course2"),
    path('course-3/', course3, name="course3"),
    path('single-course/', coursed, name="coursed"),
    path('about/', about, name="about"),
    path('about2/', about2, name="about2"),
    path('instructor/',instructor,name="instructor"),
    path('instructorprofile/',instructorprofile,name="instructorprofile"),
    path('blog/', blog, name="blog"),
    path('blog2/', blog2, name="blog2"),
    path('registration/',registration, name="registration"),
    path('confirmation/',confirmation, name="confirmation"),
    path('inquiry/', register_user, name="register"),
    # path("logout/", LogoutView.as_view(), name="logout"),
    path("inq/", stuinquiry, name="stuinquiry"),
    path("regg11/", reg11, name="reg11"),
    path("Registerfill/", Registerfill, name="Registerfill"),
    path("rrh/", rrhomee, name="rrhomee"),
    path("stu_login/", stu_login, name="stu_login"),
    path("stulogin/", stulogin, name="stulogin"),
    path("Register_student/", Register_student, name="Register_student"),
    path("admin_home/", admin_home, name="admin_home"),
    path("Register_instructor/", Register_instructor, name="Register_instructor"),
    path("loginotp/", loginotp, name="loginotp"),
    path("verify_loginotp/", verify_loginotp, name="verify_loginotp"),
    path("add_course/", add_course, name="add_course"),
    path('Logout' ,Logout,name="Logout"),
    path('courselist',courselist,name="courselist"),
    path('editcourse/<int:id>', editcourse, name="editcourse"),
    path('updatecourse/<int:id>', updatecoursedetail, name="updatecoursedetail"),
    path('deletecourse', deletecourse, name="deletecourse"),
    path('deletebatch', deletebatch, name="deletebatch"),
    path('batches', batches, name="batches"),
    path('edit_batches/<int:id>', edit_batches, name="edit_batches"),
    path('all_batches', all_batches, name="all_batches"),
    path('addbatch', addbatch, name="addbatch"),
    path('updatebatchdetail/<int:id>', updatebatchdetail, name="updatebatchdetail"),
    path('courseschedule', courseschedule, name="courseschedule"),
    path('schedulecourse', schedulecourse, name="schedulecourse"),
    path('Edit_schedulecourse/<int:id>', Edit_schedulecourse, name="Edit_schedulecourse"),
    path('all_schedulecourse', all_schedulecourse, name="all_schedulecourse"),
    path('updatecourseche11/<int:id>',updatecouurscheduledetail, name="updatecouurscheduledetail"),
    path('deleteschedulecourse',deleteschedulecourse, name="deleteschedulecourse"),
    path('updateprofile',updateprofile, name="updateprofile"),
    path('allusers',allusers, name="allusers"),
    path('userviewdetail/<int:id>',userviewdetail, name="userviewdetail"),
    path('updateuserrecord/<int:id>',updateuserrecord, name="updateuserrecord"),
    path('userdelete',userdelete, name="userdelete"),
    path('allinstructors',allinstructors, name="allinstructors"),
    path('instructorviewdetail/<int:id>',instructorviewdetail, name="instructorviewdetail"),
    path('updateinstructrecord/<int:id>',updateinstructrecord, name="updateinstructrecord"),
    path('instdelete',instdelete, name="instdelete"),
    path('myuserdash',myuserdash, name="myuserdash"),
    path('co',co, name="co"),
    path('payforcourse/<int:id>',payforcourse, name="payforcourse"),
    path('successspay',successpayment, name="successspay"),
    path('Allenrolledusers',Allenrolledusers, name="Allenrolledusers"),

    # path('change_status/<int:pid>',change_status,name="change_status")
]
