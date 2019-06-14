from django.shortcuts import render,loader,HttpResponse
from . import models
import datetime

now = datetime.date.today()

# Create your views here.

def homeview(request):
    template=loader.get_template('Home.html')
    return HttpResponse(template.render({},request))

def addstudent(request):
    template=loader.get_template('Students/addstudent.html')
    msg=''
    color=''
    if request.method=='POST':
        try:
            models.Student.objects.get(sid=request.POST.get('sid'))
            color='red'
            msg = 'Student ID is already exist'
        except models.Student.DoesNotExist:
            std=models.Student()
            std.sid=request.POST.get('sid')
            std.sname=request.POST.get('sname')
            std.scourse=request.POST.get('scourse')
            std.ssem=request.POST.get('ssem')
            std.sphn=request.POST.get('sphn')
            std.save()
            color='green'
            msg='Student Added Successfully'
    return HttpResponse(template.render({'msg':msg,'color': color},request))

def viewstudent(request):
    template=loader.get_template('Students/viewstudent.html')
    titles = ''
    std=''
    msg=''
    dd=''
    dd2=''
    dd3=''
    if request.method=='POST':
        try:
            std=models.Student.objects.get(sid=request.POST.get('sid'))
            titles = ['Student ID', 'Name', 'Course', 'Sem', 'Phone Number','Fine']
            dd = '#dddddd'
            dd2 = 'border: 1px solid #dddddd;'
            dd3= 'Student Details'
        except models.Student.DoesNotExist:
            msg='Student not Found'
    return HttpResponse(template.render({'student':std,'titles': titles,'msg':msg,'dd':dd,'dd2':dd2, 'dd3':dd3},request))

def deletestudent(request):
    template=loader.get_template('Students/deletestudent.html')
    msg=''
    m1=''
    m2=''
    m3=''
    name=''
    id=''
    if request.method=='POST':
        try:
            std=models.Student.objects.get(sid=request.POST.get('sid'))
            name=str(std.sname)
            id=str(std.sid)
            std.delete()
            m1 = 'Student '
            m2 = ' with Student_ID '
            m3 = ' Deleted Successfully'
        except models.Student.DoesNotExist:
            msg='Invalid Student ID'
    return HttpResponse(template.render({'msg': msg,'m1':m1,'m2':m2,'m3':m3,'name':name,'id': id},request))

def addbook(request):
    template=loader.get_template('Books/addbook.html')
    msg=''
    color=''
    if request.method=='POST':
        try:
            models.Book.objects.get(bid=request.POST.get('bid'))
            color='red'
            msg = 'Book ID already exist'
        except models.Book.DoesNotExist:
            bk=models.Book()
            bk.bid=request.POST.get('bid')
            bk.bname=request.POST.get('bname')
            bk.bcontent=request.POST.get('bcontent')
            bk.bauthor=request.POST.get('bauthor')
            bk.brackno=request.POST.get('brackno')
            bk.save()
            color='green'
            msg='Book Added Successfully'
    return HttpResponse(template.render({'msg':msg,'color': color},request))

def deletebook(request):
    template=loader.get_template('Books/deletebook.html')
    msg=''
    m1=''
    m2=''
    m3=''
    name=''
    id=''
    if request.method=='POST':
        try:
            bk=models.Book.objects.get(bid=request.POST.get('bid'))
            name=str(bk.bname)
            id=str(bk.bid)
            bk.delete()
            m1 = 'Book '
            m2 = ' with Book_ID '
            m3 = ' Deleted Successfully'
        except models.Book.DoesNotExist:
            msg='Invalid Book ID'
    return HttpResponse(template.render({'msg': msg,'m1':m1,'m2':m2,'m3':m3,'name':name,'id': id},request))

def searchbyid(request):
    template=loader.get_template('Books/searchbyid.html')
    titles = ''
    bk=''
    msg=''
    dd=''
    dd2=''
    dd3=''
    if request.method=='POST':
        try:
            bk=models.Book.objects.get(bid=request.POST.get('bid'))
            titles = ['Book ID', 'Name', 'Content', 'Author', 'Rack Number']
            dd = '#dddddd'
            dd2 = 'border: 1px solid #dddddd;'
            dd3= 'Book Details'
        except models.Book.DoesNotExist:
            msg='Book not Found'
    return HttpResponse(template.render({'book':bk,'titles': titles,'msg':msg,'dd':dd,'dd2':dd2, 'dd3':dd3},request))

def searchbyname(request):
    template=loader.get_template('Books/searchbyname.html')
    titles = ''
    bk=''
    msg=''
    dd=''
    dd2=''
    dd3=''
    if request.method=='POST':
        bk = models.Book.objects.filter(bname=request.POST.get('bname'))
        if len(bk)!=0:
            titles = ['Book ID', 'Name', 'Content', 'Author', 'Rack Number']
            dd = '#dddddd'
            dd2 = 'border: 1px solid #dddddd;'
            dd3= 'Book Details'
        else:
            msg='Book not Found'
    return HttpResponse(template.render({'books':bk,'titles': titles,'msg':msg,'dd':dd,'dd2':dd2, 'dd3':dd3},request))


def searchbyauthor(request):
    template=loader.get_template('Books/searchbyauthor.html')
    titles = ''
    bk=''
    msg=''
    dd=''
    dd2=''
    dd3=''
    if request.method=='POST':
        bk=models.Book.objects.filter(bauthor=request.POST.get('bauthor'))
        if len(bk)!=0:
            print('ssssssssssssss',bk)
            titles = ['Book ID', 'Name', 'Content', 'Author', 'Rack Number']
            dd = '#dddddd'
            dd2 = 'border: 1px solid #dddddd;'
            dd3= 'Book Details'
        else:
            msg='Book not Found'
    return HttpResponse(template.render({'books':bk,'titles': titles,'msg':msg,'dd':dd,'dd2':dd2, 'dd3':dd3},request))

def issuebook(request):
    template=loader.get_template('Services/issue.html')
    print('\033[1m' + 'Hello')
    msg=''
    color = 'red'
    fontsize=''
    if request.method == 'POST':
        bcheck = models.Book.objects.filter(bid=request.POST.get('bid'))
        scheck = models.Student.objects.filter(sid=request.POST.get('sid'))
        bscheck = models.Services.objects.filter(bid=request.POST.get('bid'),rdate=None)
        sscheck = models.Services.objects.filter(sid=request.POST.get('sid'),rdate=None)
        if  len(bcheck)==0:
            msg = 'Invalid BooK ID'
        elif len(scheck)==0:
            msg = 'Invalid Student ID'
        elif len(sscheck)==2:
            msg = 'This Student Already Issued 2 Books'
        elif len(bscheck)==1:
            msg = 'This Book is Already Issued'
        else:
            ser = models.Services()
            sid = models.Student.objects.get(sid=request.POST.get('sid'))
            ser.sid = sid
            bid = models.Book.objects.get(bid=request.POST.get('bid'))
            ser.bid = bid
            now = datetime.date.today()  # datetime.datetime.now().date() - same function
            ser.bdate = now
            ser.bcdate = now
            ser.save()
            msg= str(sid.sname) + ' with Student_ID ' + str(sid.sid) + ' Issued Book ' + str(bid.bname) + ' of Book_ID ' + str(bid.bid) +' with date ' +str(now)
            color = 'green'
            fontsize = 'font-size:20px;'
    return HttpResponse(template.render({'msg':msg,'color': color,'fontsize':fontsize},request))

def renewbook(request):
    template=loader.get_template('Services/renew.html')
    msg=''
    cf='red'
    if request.method == 'POST':
        bcheck= models.Book.objects.filter(bid=request.POST.get('bid'))
        ser = models.Services.objects.filter(bid=request.POST.get('bid'))
        if len(bcheck)==0:
            msg = 'Invalid Book_ID'
        elif len(ser)==0:
            msg = 'This Book is not Issued'
        else:
            try:
                nullcheck = models.Services.objects.get(bid=request.POST.get('bid'),rdate=None)
                now = datetime.date.today()
                days=(now - nullcheck.bcdate).days
                print(days)
                if days>15:
                    fine=(days-15)*.5
                    ffine=(nullcheck.bfine + fine)
                    nullcheck.bfine = ffine
                nullcheck.bcdate = now
                nullcheck.save()
                cf = 'green; font-size:20px;'
                msg='Student Name : ' + str(nullcheck.sid.sname)+ '<br><br>Student ID : ' + str(nullcheck.sid.sid)+'<br><br>Book Name : '+ str(nullcheck.bid.bname) + '<br><br>Book ID : ' + str(nullcheck.bid.bid) + '<br><br>Fine : ' + str(nullcheck.bfine) +' Rs<br><br>Date : ' + str(nullcheck.bcdate) + '<br><br>Book Renewed Successfully'
            except models.Services.DoesNotExist:
                msg = 'This Book is not Issued'
    return HttpResponse(template.render({ 'msg': msg,'cf' : cf },request))

def returnbook(request):
    template=loader.get_template('Services/return.html')
    msg = ''
    cf = 'red;'
    if request.method == 'POST':
        bcheck = models.Book.objects.filter(bid=request.POST.get('bid'))
        ser = models.Services.objects.filter(bid=request.POST.get('bid'))

        if len(bcheck)==0:
            msg = 'Invalid Book_ID'
        elif len(ser)==0:
            msg = 'This Book is not Issued'
        else:
            try:
                nullcheck=models.Services.objects.get(bid=request.POST.get('bid'), rdate=None)
                now = datetime.date.today()
                nullcheck.rdate = now
                days = (now - nullcheck.bcdate).days
                if days > 15:
                    fine = (days - 15) * .5
                    ffine     = nullcheck.bfine + fine
                    nullcheck.bfine = ffine
                nullcheck.sid.sfine=nullcheck.sid.sfine + nullcheck.bfine
                nullcheck.sid.save()
                nullcheck.save()
                cf = 'green; font-size:20px;'
                msg='Student Name : ' + str(nullcheck.sid.sname)+ '<br><br>Student ID : ' + str(nullcheck.sid.sid)+'<br><br>Book Name : '+ str(nullcheck.bid.bname) + '<br><br>Book ID : ' + str(nullcheck.bid.bid) + '<br><br>Fine : ' + str(nullcheck.bfine) +' Rs<br><br>Date : ' + str(nullcheck.rdate) + '<br><br>Book Returned Successfully'
            except models.Services.DoesNotExist:
                msg = 'This Book is not Issued'

    return HttpResponse(template.render({'msg':msg,'cf':cf },request))