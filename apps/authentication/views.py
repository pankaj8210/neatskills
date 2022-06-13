from datetime import date
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import messages
from apps.authentication.models import *
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
userr = get_user_model()
from apps.authentication.models import user
import razorpay
from .models import *
from django.contrib.auth.hashers import make_password
import uuid
import datetime
from threading import Timer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse
from datetime import date
from django.http import HttpResponseRedirect, JsonResponse

# Create your views here.


def index(request):
    return render(request, 'accounts/index.html')

def confirmation(request):
    return render(request, 'accounts/confirmation.html')

def course1(request):
    return render(request,'accounts/course-1.html')

def course2(request):
    return render(request,'accounts/course-2.html')

def course3(request):
    return render(request,'accounts/course-3.html')

def coursed(request):
    return render(request,'accounts/single-course.html')


def about(request):
    return render(request,'accounts/about-1.html')

def about2(request):
    return render(request,'accounts/about-2.html')

def instructor(request):
    return render(request,'accounts/instructor.html')

def instructorprofile(request):
    return render(request,'accounts/profile.html')

def blog(request):
    return render(request,'accounts/blog.html')

def blog2(request):
    return render(request,'accounts/single-post.html')


def stu_login(request):
    if request.method == 'POST':
        email = request.POST.get('emailstu')
        password = request.POST.get('passwordstu')
        print(email)
        print(email)

        if user.objects.filter(email=email).exists():
            user_obj = authenticate(request, email=email, password=password)
            if user_obj is not None:
                login(request, user_obj)
                otp = str(
                uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today()) + email).int)
                otp = otp[0:6]
                request.session['emailca11'] = email

                if not otpverifywithtimer.objects.filter(email=email).exists():
                    otpm = otpverifywithtimer.objects.create(otp=otp, email=email)
                    otpm.save()

                if otpverifywithtimer.objects.filter(email=email).exists():
                    otpm = otpverifywithtimer.objects.get(email=email)
                    otpm.otp = otp
                    otpm.save()


                def delunverifyotp():
                    if otpverifywithtimer.objects.filter(email=email).exists():
                        otpm = otpverifywithtimer.objects.get(email=email)
                        otpm.delete()
                t = Timer(60.0, delunverifyotp)
                t.start()

                sub = 'Welcome to NeatSkills'
                msg = '''Hi,
 Greetings!
 Thank you for the part of NeatSkills,

 We are sharing a verification code to access your account.
 The code is valid for 1 minutes and usable only once,

                        ''' + str(otp)
                EmailMessage(sub, msg, to=[email]).send()
                # messages.success(request,
                #              'NEATSKILLS !! Please verify your account with the OTP we have sent on your e-mail.OTP will be expired in 60 second')


                return redirect('/loginotp/')

            else:
                messages.error(request, 'You have entered incorrect password')
                return redirect('/login/')
        else:
            messages.error(request, 'This email is not exists')
            return redirect('/login/')

    return redirect('/pro')

def loginotp(request):
    return render(request,"accounts/otp.html")



# def adminlog(request):
#     return render(request,'accounts/login.html')

# def adminlogin(request):
#     print('ttttt')
#     if request.method == 'POST':
#         email = request.POST.get('emailad')
#         password = request.POST.get('passwordad')
#         print('rrrr')

#         if user.objects.filter(email=email).exists():
#             user_obj = authenticate(request, email=email, password=password)
#             if user_obj is not None:
#                 if user_obj.is_superuser == True and user_obj.is_staff == True:
#                     login(request, user_obj)
#                     return redirect('/adminhome')

#             else:
#                 messages.error(request, 'You have entered incorrect password')
#                 return redirect('/admin_login')
#         else:
#             messages.error(request, 'This email is not exists')
#             return redirect('/admin_login')

#     return redirect('/ooooooooo')


# @csrf_exempt
# def verify_loginotp(request):
# 	if request.method == 'POST':
# 		otp = request.POST.get('otp1')
# 		try:
# 		    otp_2 = request.session['otp1']
# 		except KeyError:
# 		    messages.info(request, 'Incorrect OTP Entered')
# 		    return redirect('/rotp')

# 		try:
# 			if otp == otp_2:
# 				return redirect('/student_login')
# 			else:
# 				messages.info(request, 'Incorrect OTP Entered')
# 				return redirect('/rotp')
# 		except KeyError:
# 			return redirect('/rotp')

@csrf_exempt
def verify_loginotp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp1')
        s = request.session['emailca11']

        if otpverifywithtimer.objects.filter(otp=otp,email=s).exists():
            if request.user.is_staff == True and request.user.is_superuser == True:
                return redirect('/admin_home/')
            if request.user.is_staff == False and request.user.is_superuser == False:
                return redirect('/myuserdash/')
            if request.user.is_staff == True and request.user.is_superuser == False:
                return redirect('/instructor_home/')

        else:
            messages.info(request, 'Incorrect OTP Entered')
            return redirect('/loginotp/')



def stulogin(request):
    return render(request, "accounts/login.html")


def myuserdash(request):
    c = Courses.objects.all()
    return render(request,'home/myuserdashboard.html',{'c':c})


def admin_home(request):
    return render(request, "home/index.html")

def co(request):
    return render(request,'home/co.html')


def course(request):
    return render(request, "home/course.html")




def login_view(request):
    print('yessss login coming ')
    return render(request, "accounts/login.html")
    # form = LoginForm(request.POST or None)

    # msg = None

    # if request.method == "POST":

    #     if form.is_valid():
    #         email = form.cleaned_data.get("email")
    #         password = form.cleaned_data.get("password")
    #         user = authenticate(email=email, password=password)
    #         if user is not None:
    #             if user.is_superuser == False and user.is_staff == False:
    #                 login(request, user)
    #                 return redirect("/")

    #             elif user.is_superuser == False and user.is_staff == True:
    #                 login(request, user)
    #                 return redirect("/ins")

    #             elif user.is_superuser == True and user.is_staff == True:
    #                 login(request, user)
    #                 return redirect('admin/dashboard.html')

    #             else:
    #                 msg = "invalid"
    #                 return redirect('login/')


    #         else:
    #             msg = 'Invalid credentials'
    #     else:
    #         msg = 'Error validating the form'




def registration(request):
    return render(request,'accounts/registration.html')

def Register_student(request):
    if request.method == "POST":
        name = request.POST.get("flname")
        contact = request.POST.get("fcontact")
        email = request.POST.get("femail")
        if user.objects.filter(email=email).exists():
            messages.info(request, 'Email is already exists')
            return redirect('/registration/')
        password = request.POST.get("fpwd")
        u = user(fullname=name,mobile=contact,email=email,password=make_password(password))
        u.save()
        otp = str(
                uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today()) + email).int)
        otp = otp[0:6]
        sub = 'Welcome to Placement Portal'
        msg = '''Hi there!
                        You have successfully registered at NEATSKILLS as Student. Please confirm your account with below OTP,
                        ''' + str(otp)
        EmailMessage(sub, msg, to=[email]).send()
        messages.success(request,'you are successfully Registered')

        return redirect('/stulogin/')

def Register_instructor(request):
    if request.method == "POST":
        name = request.POST.get("ifname")
        contact = request.POST.get("icontact")
        email = request.POST.get("iemail")
        if user.objects.filter(email=email).exists():
            messages.info(request, 'Email is already exists')
            return redirect('/registration/')
        password = request.POST.get("ipwd")
        u = user(fullname=name,mobile=contact,email=email,password=make_password(password),is_staff=True)
        u.save()
        otp = str(
                uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.today()) + email).int)
        otp = otp[0:6]
        sub = 'Welcome to Placement Portal'
        msg = '''Hi there!
                        You have successfully registered at NEATSKILLS as Instructor. Please confirm your account with below OTP,
                        ''' + str(otp)
        EmailMessage(sub, msg, to=[email]).send()
        messages.success(request,'you are successfully Registered')

        return redirect('/stulogin/')



def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = StudentInquiry()

    return render(request, "accounts/contact.html", {"form": form, "msg": msg, "success": success})


def stuinquiry(request):
    if request.method == "POST":
        name = request.POST.get('inqname')
        email = request.POST.get('inqemail')
        if StudentInquiry.objects.filter(email=email).exists():
            messages.info(request,'Email is already exists')
            return redirect('/inquiry/')
        number = request.POST.get('inqnumber')
        mod = request.POST.get('inqmod')
        msg = request.POST.get('message')
        si = StudentInquiry(name=name,email=email,number=number,selectmodel=mod,message=msg)
        si.save()
        sub = 'Welcome to Student Course Portal'
        msg = '''Hi there!
                You have successfully submitted your enquiry please
                 complete your registration through given link ,
                 '''+ "\nRegistrationlink:"+ "http://127.0.0.1:8000//registartion/"
        EmailMessage(sub, msg, to=[email]).send()
        u = user.objects.filter(is_superuser=True)
        for i in u:
            sub = 'Welcome to Student Course Portal'
            msg = '''Hi there!
                                    New user Requested to you ,
                                    '''+ "\nName:" + " " + name + "\nEmail:" + " " + email + "\nNumber:" + " " + number + " " + "Select-Mod:" +  " " + mod
            EmailMessage(sub, msg, to=[i.email]).send()
        return redirect('/confirmation/')

    return redirect('/login/')





def reg11(request):
    return render(request,'accounts/registration.html')

def Registerfill(request):
    if request.method == 'POST':
        fullname = request.POST.get('flname')
        fn = request.POST.get('rfname')
        ln = request.POST.get('lfname')
        p = request.POST.get('pwd')
        birthday = request.POST.get('rbname')
        gender = request.POST.get('rradio')
        email = request.POST.get('email')
        phone = request.POST.get('contact')
        password = request.POST.get('pwd')
        # aphone = request.POST.get('rphone')
        address = request.POST.get('address')
        state = request.POST.get('state')
        village = request.POST.get('rvillage')
        dist = request.POST.get('rdistrict')
        pin = request.POST.get('pincode')
        city = request.POST.get('rcity')
        aadhar = request.POST.get('raadhar')
        active = request.POST.get('acradio')
        qualification = request.POST.get('rqalification')
        sscs = request.POST.get('sscs')
        sscpy = request.POST.get('sscpy')
        sscom = request.POST.get('sscom')
        sscg = request.POST.get('sscg')
        # rupdated = request.POST.get('rupdated')
        # rlstupon = request.POST.get('rlstupon')
        # rfee = request.POST.get('rfee')
        # rfeepaiddate = request.POST.get('rfeepaiddate')
        # rfeepaidamount = request.POST.get('rfeepaidamount')

        pp = user(fullname=fullname, password= password, fname=fn, laname=ln, birthday=birthday, gender=gender, email=email, mobile=phone,
                  address1=address, state=state, village=village, district=dist,
                  pin=pin,
                  city=city, Aadhar=aadhar, qualification=qualification, school=sscs, passingyear=sscom,
                  marks=sscpy, grade=sscg,Active=active)
        pp.save()
        messages.success(request,'you are successfully Registered')
    return redirect('accounts/login.html')



def rrhomee(request):

    amount = 500*100

    order_currency = 'INR'
    client = razorpay.Client(auth=('rzp_test_PgHNzZxAI49468','IU8ChpBVTn3Yf4k9dnHa6Elm'))
    payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'0'})
    return render(request,'accounts/payment.html',{'payment':payment})


def successs(request):
    return redirect('/regg11/')

def Logout(request):
    # logout(request)
    return redirect('index')


def add_course(request):
    if request.method == 'POST':
        print('yesssss')
        ct = request.POST.get('coursetitle')
        # ci = request.POST.get('courseid=courseid')
        act = request.POST.get('Active')
        utb = request.POST.get('updatedby')
        lstutb = request.POST.get('lastupdated')
        cd = request.POST.get('cduration')
        cl = request.FILES.get('clogo')
        cchp = request.POST.getlist('cchapters')
        print('cchpttt',cchp)
        des = request.POST.getlist('ctopics')
        cpr = request.POST.get('cprice')
        cdes = request.POST.get('cdescription')
        cts = request.FILES.getlist('ctscreens')
        print('cchp',cchp)

        c = Courses(user=request.user,coursename=ct,courseduration=cd,logo=cl,courseprice=cpr,coursedescription=cdes,active=act,updatedby=utb,lastupdatedon=lstutb)
        c.save()

        cid = c.id
        print('cid',cid)

        for i in des:
            course = Topic_course(tpicid=cid,topic=i)
            course.save()

        for j in cchp:
            course = Chapter_course(chapterid=cid,chapter=j)
            course.save()

        for v in cts:
            course = Screan_course(screanid=cid,screan=v)
            course.save()


    return redirect('home/course.html')

def batches(request):
    return render(request,'home/batch.html')

def allusers(request):
    alluser = user.objects.filter(is_superuser=False).filter(is_staff=False)
    print('alluser',alluser)
    return render(request,'home/allusers.html',{'alluser':alluser})


def allinstructors(request):
    alluser = user.objects.filter(is_superuser=False).filter(is_staff=True)
    print('alluser',alluser)
    return render(request,'home/allinstructors.html',{'alluser':alluser})


def userviewdetail(request,id):
    userrr = user.objects.get(id=id)
    return render(request,'home/userviewdetail.html',{'user':userrr})

def instructorviewdetail(request,id):
    userrr = user.objects.get(id=id)
    return render(request,'home/instructordetail.html',{'user':userrr})

def instructordetail(request):
    return render(request,'home')



def updateuserrecord(request,id):
    u = userr.objects.get(id=id)
    u.fullname = request.POST.get('uufullname')
    u.Active = request.POST.get('uuActive')
    u.updated_by = request.POST.get('uuupdatedby')
    u.fname = request.POST.get('uufname')
    u.laname = request.POST.get('uulname')
    u.birthday = request.POST.get('uudob')
    u.email = request.POST.get('uuemail')
    u.mobile = request.POST.get('uumno')
    u.gender = request.POST.get('uugender')
    u.address1 = request.POST.get('uusddders')
    u.district = request.POST.get('uudistrict')
    u.state = request.POST.get('uucity')
    u.pin = request.POST.get('uupin')
    u.Aadhar = request.POST.get('uuaadhar')
    u.save()
    return redirect('/allusers')

def updateinstructrecord(request,id):
    u = userr.objects.get(id=id)
    u.fullname = request.POST.get('insfullname')
    u.Active = request.POST.get('insActive')
    u.updated_by = request.POST.get('insupdatedby')
    u.lastupdateon = request.POST.get('inslastupdated')
    u.totalexp = request.POST.get('insexp')
    u.subjectexp = request.POST.get('inssubexp')
    u.mobile = request.POST.get('insmob')
    u.gender = request.POST.get('insgen')
    u.address1 = request.POST.get('insaddress')
    u.district = request.POST.get('insdict')
    u.state = request.POST.get('insstate')
    u.pin = request.POST.get('inspin')
    u.coursemodule = request.POST.get('inscoursemodul')
    u.save()
    return redirect('/allusers')


def addbatch(request):
    if request.method == 'POST':
        name = request.POST.get('batchname')
        active = request.POST.get('bActive')
        bupdatedby = request.POST.get('bupdatedby')
        blastupdated = request.POST.get('blastupdated')
        bstart = request.POST.get('bstart')
        bend = request.POST.get('bend')
        bduration = request.POST.get('bduration')

        b = Addbatches(name=name,active=active,updatedby=bupdatedby,lastupdateon=blastupdated,starttime=bstart,enddatetime=bend,duration=bduration)
        b.save()
        messages.info(request,'Added Batch!!')
        return redirect('/batches')

def schedulecourse(request):
    if request.method == 'POST':
        name = request.POST.get('namechedule')
        active = request.POST.get('activechedule')
        bupdatedby = request.POST.get('updatechedule')
        blastupdated = request.POST.get('updateonchedule')
        btime = request.POST.get('bathtimechedule')
        studentchedule = request.POST.get('studentchedule')
        durationchedule = request.POST.get('durationchedule')

        b = Courseschedule(name=name,active=active,updatedby=bupdatedby,lastupdatedon=blastupdated,batchtime=btime,studentattemt=studentchedule,duration=durationchedule)
        b.save()
        messages.info(request,'Course Scheduled!!')
        return redirect('/courseschedule')



def edit_batches(request,id):
    ecourse = Addbatches.objects.get(id=id)
    return render(request,'home/editbatch.html',{'ebatch':ecourse})


def Edit_schedulecourse(request,id):
    ecourse = Courseschedule.objects.get(id=id)
    return render(request,'home/editscheduledcourse.html',{'ebatch':ecourse})


def updatebatchdetail(request,id):
    u = Addbatches.objects.get(id=id)
    u.name = request.POST.get('eebatchname')
    u.active = request.POST.get('eebActive')
    u.updatedby = request.POST.get('eebupdatedby')
    u.lastupdateon = request.POST.get('eeblastupdated')
    u.starttime = request.POST.get('eebstart')
    u.enddatetime = request.POST.get('eebend')
    u.duration = request.POST.get('eebduration')

    u.save()
    return redirect('/all_batches')

def updatecouurscheduledetail(request,id):
    u = Courseschedule.objects.get(id=id)
    u.name = request.POST.get('batchnameche')
    u.active = request.POST.get('bActiveche')
    u.updatedby = request.POST.get('bupdatedbyche')
    u.lastupdateon = request.POST.get('blastupdatedche')
    u.starttime = request.POST.get('bstartche')
    u.enddatetime = request.POST.get('bendche')
    u.duration = request.POST.get('bdurationche')

    u.save()
    return redirect('/all_schedulecourse')


def all_batches(request):
    b = Addbatches.objects.all()
    return render(request,'home/allbatch.html',{'allbatchs':b})

def all_schedulecourse(request):
    b = Courseschedule.objects.all()
    return render(request,'home/allschedule.html',{'allbatchs':b})


def courselist(request):
    allcourse = Courses.objects.all().order_by('-id')
    return render(request,'home/allcourse.html',{'allcourse':allcourse})


def editcourse(request,id):
    ecourse = Courses.objects.get(id=id)
    Topic = Topic_course.objects.filter(tpicid=id)
    Chapter = Chapter_course.objects.filter(chapterid=id)
    Screan = Screan_course.objects.filter(screanid=id)
    print('courseid')
    return render(request,'home/editcourse.html',{'ecourse':ecourse,'topic':Topic,"chapter":Chapter,'screan':Screan})


def updateprofile(request):
    user = request.user
    print('uuser',user)
    u = user.objects.get(email='abhi@gmail.com')
    print('obj',u)
    u.fullname = request.POST.get('uuname')
    u.fname = request.POST.get('uufname')
    u.email = request.POST.get('uuemail')
    u.laname = request.POST.get('uulname')
    u.address1 = request.POST.get('uuaddress')
    u.city = request.POST.get('uucity')
    u.country = request.POST.get('uucountry')
    u.pin = request.POST.get('uupostel')
    u.aboutme = request.POST.get('uuaboutme')
    u.save()
    return redirect('profile.html')



def updatecoursedetail(request,id):
    u = Courses.objects.get(id=id)
    Topic = Topic_course.objects.filter(tpicid=id)
    Chapter = Chapter_course.objects.filter(chapterid=id)
    Screan = Screan_course.objects.filter(screanid=id)
    u.coursename = request.POST.get('ecoursetitle')
    u.active = request.POST.get('eactive')
    u.updatedby = request.POST.get('eupdatedby')
    u.lastupdatedon = request.POST.get('elastupdated')
    u.courseduration = request.POST.get('ecduration')
    u.courselogo = request.FILES.get('eclogo')
    coursechapter = request.POST.get('ecchapters')
    for i in coursechapter:
        u.coursechapter = i

    u.courseprice = request.POST.get('ecprice')
    u.coursedescription = request.POST.get('ecdescription')
    u.save()
    return redirect('/courselist')

def deletecourse(request):
    dd = request.GET.get('id')
    d = Courses.objects.get(id=dd)
    d.delete()
    return JsonResponse({'true':True})

def userdelete(request):
    dd = request.GET.get('id')
    d = userr.objects.get(id=dd)
    d.delete()
    return JsonResponse({'true':True})

def instdelete(request):
    dd = request.GET.get('id')
    d = userr.objects.get(id=dd)
    d.delete()
    return JsonResponse({'true':True})

def deletebatch(request):
    dd = request.GET.get('id')
    d = Addbatches.objects.get(id=dd)
    d.delete()
    return JsonResponse({'true':True})

def deleteschedulecourse(request):
    dd = request.GET.get('id')
    d = Courseschedule.objects.get(id=dd)
    d.delete()
    return JsonResponse({'true':True})

def courseschedule(request):
    return render(request,'home/course_schedule.html')

def courseaply(request,id):
    request.session['payid'] = id
    return redirect('/payment')

def payforcourse(request,id):
    request.session['courseid'] = id
    corse = Courses.objects.get(id=id)

    coprize = corse.courseprice

    amount = int(coprize)*100
    order_currency = 'INR'
    client = razorpay.Client(auth=('rzp_test_PgHNzZxAI49468','IU8ChpBVTn3Yf4k9dnHa6Elm'))
    payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'0'})
    return render(request,'home/payment.html',{'payment':payment})


def successpayment(request):
    response = request.POST
    param_dict = {
        "razorpay_payment_id":response['razorpay_payment_id'],
        "razorpay_order_id":response['razorpay_order_id'],
        "razorpay_signature":response['razorpay_signature'],
    }
    print(param_dict)

    try:
        if response['razorpay_signature']:
            cid = request.session['courseid']
            corse = Courses.objects.get(id=cid)
            e = Enrollmentlist(name=corse.coursename,price=corse.courseprice,courseduration=corse.courseduration)
            e.save()

            return redirect('/myuserdash')
    except:
        return redirect('/oyiuy/')


def Allenrolledusers(request):
    a = Enrollmentlist.objects.all()
    return render(request,'home/enrollment.html',{'a':a})
