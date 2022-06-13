import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.urls import reverse



# Create your models here.

class Usermanager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('email must be required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be is_superuser=True')

        return self._create_user(email, password, **extra_fields)

class user(AbstractBaseUser,PermissionsMixin):
    fullname = models.CharField(max_length=255, null=True,blank=True)
    email = models.CharField(max_length=255, null=True,blank=True , unique=True)
    mobile = models.CharField(max_length=12, null=True,blank=True)
    alternate_mobile = models.CharField(max_length=12, null=True,blank=True)
    fname = models.CharField(max_length=255, null=True,blank=True)
    birthday = models.CharField(max_length=255, null=True,blank=True)
    laname = models.CharField(max_length=255, null=True,blank=True)
    age = models.CharField(max_length=10, null=True,blank=True)
    gender = models.CharField(max_length=20, null=True,blank=True)
    village = models.CharField(max_length=20, null=True,blank=True)
    district = models.CharField(max_length=20, null=True,blank=True)
    country = models.CharField(max_length=20, null=True,blank=True)
    city = models.CharField(max_length=20, null=True,blank=True)
    totalexp = models.CharField(max_length=20, null=True,blank=True)
    lastupdateon = models.CharField(max_length=20, null=True,blank=True)
    subjectexp = models.CharField(max_length=20, null=True,blank=True)
    coursemodule = models.CharField(max_length=20, null=True,blank=True)
    password = models.CharField(max_length=255, null=True,blank=True)
    cpassword = models.CharField(max_length=255, null=True,blank=True)
    address1 = models.CharField(max_length=100, null=True,blank=True)
    permanent_address = models.CharField(max_length=100, null=True,blank=True)
    pin = models.CharField(max_length=100, null=True,blank=True)
    Aadhar = models.CharField(max_length=100, null=True,blank=True)
    Active = models.BooleanField(default=False, null=True,blank=True)
    qualification = models.CharField(max_length=100, null=True,blank=True)
    school = models.CharField(max_length=100, null=True,blank=True)
    passingyear = models.CharField(max_length=100, null=True,blank=True)
    marks = models.CharField(max_length=100, null=True,blank=True)
    grade = models.CharField(max_length=100, null=True,blank=True)
    course_detail = models.CharField(max_length=100, null=True,blank=True)
    updated_by = models.CharField(max_length=100, null=True,blank=True)
    Fees = models.CharField(max_length=100, null=True,blank=True)
    Fees_date = models.CharField(max_length=100, null=True,blank=True)
    Fees_amount = models.CharField(max_length=100, null=True,blank=True)
    aboutme = models.CharField(max_length=100, null=True,blank=True)
    state = models.CharField(max_length=100, null=True,blank=True)
    is_staff = models.BooleanField(default=False, )
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = Usermanager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser




class StudentInquiry(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    selectmodel = models.CharField(max_length=500,blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)


class otpverifywithtimer(models.Model):
    email = models.EmailField(null=True, blank=True)
    otp = models.EmailField(null=True, blank=True)
    verify = models.BooleanField(default=False)




# class Instructor(models.Model):
#     instructorid =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     email = models.CharField(max_length=255, null=True,blank=True , unique=True)
#     fullname = models.CharField(max_length=255, null=True,blank=True)
#     mobile=models.CharField(max_length=15,null=True)
#     qualification=models.CharField(max_length=15,null=True)
#     experience = models.CharField(max_length=15,null=True)
#     subjectexperience  = models.CharField(max_length=15,null=True)
#     address =  models.CharField(max_length=50,null=True)
#     gender=models.CharField(max_length=10,null=True)
#     active = models.CharField(max_length=10,null=True)
#     type=models.CharField(max_length=15,null=True)
#     status=models.CharField(max_length=20,null=True)
#     def _str_(self):
#         return self.user.username

class Courses(models.Model):
    # courseid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(user,blank=True,null=True ,on_delete=models.CASCADE)
    coursename = models.CharField(max_length=200,null=True,blank=True, default="")
    courseduration = models.CharField(max_length=200,null=True,blank=True)
    logo = models.ImageField(upload_to='courselogos', null=True, blank=True)
    coursechapter = models.CharField(max_length=200,null=True,blank=True)
    coursetopic = models.CharField(max_length=200,null=True,blank=True)
    coursetopicscreen = models.FileField(null=True, blank=True)
    courseprice = models.CharField(max_length=200,null=True,blank=True)
    coursedescription = models.CharField(max_length=200,null=True,blank=True)
    active = models.CharField(max_length=10,null=True,blank=True)
    updatedby  = models.CharField(max_length=20,null=True,blank=True)
    lastupdatedon = models.CharField(max_length=20,null=True,blank=True)
    # def __str__(self):
    #     return self.coursename


class Chapter(models.Model):
    course = models.ForeignKey(Courses,null=True,blank=True,on_delete=models.CASCADE)
    # chapterid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chaptername = models.CharField(max_length=200,null=True,blank=True)
    active = models.CharField(max_length=10,null=True)
    updatedby  = models.CharField(max_length=20,null=True)
    lastupdatedon = models.CharField(max_length=20,null=True)
    # def __str__(self):
    #     return self.chaptername


class Topics(models.Model):
    courses = models.ForeignKey(Courses,null=True,blank=True,on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter,null=True,blank=True,on_delete=models.CASCADE)
    # topicsid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topicname = models.CharField(max_length=200,null=True,blank=True)
    active = models.CharField(max_length=10,null=True)
    updatedby  = models.CharField(max_length=20,null=True)
    lastupdatedon = models.CharField(max_length=20,null=True)
    # def __str__(self):
    #     return self.topicname

class Topics_screen(models.Model):
    courseid = models.ForeignKey(Courses,null=True,blank=True,on_delete=models.CASCADE)
    chapterid = models.ForeignKey(Chapter,null=True,blank=True,on_delete=models.CASCADE)
    topicsid = models.ForeignKey(Topics,null=True,blank=True,on_delete=models.CASCADE)
    # screenid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    screenname = models.CharField(max_length=200,null=True,blank=True)
    active = models.CharField(max_length=10,null=True)
    updatedby  = models.CharField(max_length=20,null=True)
    lastupdatedon = models.CharField(max_length=20,null=True)
    # def __str__(self):
    #     return self.screenname


class Batch_timing(models.Model):
    batchname = models.CharField(max_length=200,null=True,blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    timings =  models.TimeField(auto_now_add=True)
    duration = models.CharField(max_length=255, null=True,blank=True)
    active = models.CharField(max_length=10,null=True,blank=True)
    updatedby  = models.CharField(max_length=20,null=True,blank=True)
    lastupdatedon = models.CharField(max_length=20,null=True,blank=True)

class Course_schedule(models.Model):
    scourse = models.ForeignKey(Courses,on_delete=models.CASCADE,null=True,blank=True)
    student = models.ForeignKey(user,on_delete=models.CASCADE,null=True,blank=True)
    # instructorid = models.ForeignKey(Instructor,on_delete=models.CASCADE,null=True,blank=True)
    batch = models.ForeignKey(Batch_timing,on_delete=models.CASCADE,null=True,blank=True)
    course_schedulename = models.CharField(max_length=200,null=True,blank=True)
    duration = models.CharField(max_length=255, null=True,blank=True)
    active = models.CharField(max_length=10,null=True,blank=True)
    updatedby  = models.CharField(max_length=20,null=True,blank=True)
    lastupdatedon = models.CharField(max_length=20,null=True,blank=True)


class add_courses(models.Model):
    title = models.CharField(max_length=255, null=True,blank=True)
    active = models.CharField(max_length=255, null=True,blank=True)
    updated_by = models.CharField(max_length=255, null=True,blank=True)
    lastupdate = models.CharField(max_length=255, null=True,blank=True)
    courseduration = models.CharField(max_length=255, null=True,blank=True)
    logo = models.ImageField(upload_to='courselogo',null=True,blank=True)
    chapter = models.CharField(max_length=255, null=True,blank=True)
    topic = models.CharField(max_length=255, null=True,blank=True)
    screan = models.ImageField(upload_to='coursescrean', null=True, blank=True)
    desc = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)


class Topic_course(models.Model):
    tpicid = models.CharField(max_length=255, null=True,blank=True)
    topic = models.CharField(max_length=255, null=True, blank=True)

class Chapter_course(models.Model):
    chapterid = models.CharField(max_length=255, null=True,blank=True)
    chapter = models.CharField(max_length=255, null=True, blank=True)

class Screan_course(models.Model):
    screanid = models.CharField(max_length=255, null=True,blank=True)
    screan = models.ImageField(upload_to='screan_course', null=True, blank=True)


class Addbatches(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    active = models.CharField(max_length=255, null=True, blank=True)
    updatedby = models.CharField(max_length=255, null=True, blank=True)
    lastupdateon = models.CharField(max_length=255, null=True, blank=True)
    starttime = models.CharField(max_length=255, null=True, blank=True)
    enddatetime = models.CharField(max_length=255, null=True, blank=True)
    duration = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)


class Courseschedule(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True)
    active = models.CharField(max_length=10, null=True, blank=True)
    duration = models.CharField(max_length=255, null=True,blank=True)
    batchtime = models.CharField(max_length=255, null=True,blank=True)
    studentattemt = models.CharField(max_length=255, null=True,blank=True)
    updatedby  = models.CharField(max_length=20,null=True,blank=True)
    lastupdatedon = models.CharField(max_length=20,null=True,blank=True)

class Enrollmentlist(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True)
    price = models.CharField(max_length=10, null=True, blank=True)
    courseduration = models.CharField(max_length=255, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
