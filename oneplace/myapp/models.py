from django.db import models
from myapp.proviers import *
from datetime import date
class SPD(models.Model): #service provider details

    namecu= models.CharField(unique=True,max_length=40,null=False)
    fname=models.CharField(null=False,max_length=40)
    lname = models.CharField(null=False,max_length=40)
    job=models.CharField(max_length=10,null=False)
    rwork=models.CharField(null=False,max_length=40)
    pnum=models.IntegerField(null=False)
    email=models.EmailField(null=False)
    Add=models.CharField(max_length=100,null=False)
    about=models.CharField(max_length=200,null=False)
    usernm=models.CharField(max_length=30,unique=True,null=False)
    userpw=models.CharField(null=False,max_length=40)
    slink=models.CharField(null=True,max_length=50)
    status=models.CharField(null=True,max_length=3,default="WL")

class USINF(models.Model):
    username=models.CharField(max_length=40,unique=True,null=False)
    pnum=models.CharField(null=False,max_length=30)
    email=models.CharField(null=False,max_length=40)
    usernm=models.CharField(null=False,unique=True,max_length=30)
    userpw=models.CharField(null=False,max_length=40)
    prv=models.CharField(null=False,max_length=3,default="USR")


class PHTGO(models.Model):
    picmg=models.ImageField(upload_to="PHTGO/",null=True)
    cicmg=models.ImageField(upload_to="PHTGO/",null=True ,default=None)
    slink=models.CharField(max_length=40)
    tpric=models.CharField(max_length=10)
    opric=models.CharField(max_length=10)
    about=models.CharField(max_length=30)
    pid=models.CharField(max_length=40)

class PHTGOimg(models.Model):
    uid=models.IntegerField()
    img=models.ImageField(upload_to="PHTGO/useraddimg/")




class CABO(models.Model):
    pid=models.CharField(max_length=40)
    bookingch=models.IntegerField(default=2000)
    cimg=models.ImageField(upload_to="CABO/")
    carnm=models.CharField(max_length=60,null=False)
    carmdl=models.CharField(max_length=60,null=False)
    stcp=models.CharField(max_length=60,null=False)
    tpric=models.CharField(max_length=60,null=False)



class PHTGOBooking(models.Model):
    bno=models.IntegerField(primary_key=True)
    bdate=models.DateField(default=date.today)
    custid=models.IntegerField()
    custname=models.CharField(max_length=40,null=False)
    srvid=models.IntegerField()
    sname=models.CharField(max_length=30)
    serv=models.CharField(max_length=40)
    rdate=models.DateField()
    rtime=models.CharField(max_length=30)
    amtpaid=models.IntegerField(default="0")
    rstat=models.CharField(max_length=20,default="NEW REQ")
    pstat=models.CharField(max_length=20,default="NOT PAID")
    cardno=models.CharField(default="0",max_length=15)
class CABOBooking(models.Model):
    bno=models.IntegerField(primary_key=True)
    bdate=models.DateField(default=date.today)
    custid=models.IntegerField()
    custname=models.CharField(max_length=40,null=False)
    srvid=models.IntegerField()
    sname=models.CharField(max_length=30)
    serv=models.CharField(max_length=40)
    carname=models.CharField(max_length=40)
    carmodel=models.CharField(max_length=40)
    packid=models.IntegerField()
    rdate=models.DateField()
    rtime = models.CharField(max_length=30,default="12:00AM")
    amtpaid=models.IntegerField(default="0")
    rstat=models.CharField(max_length=20,default="NEW REQ")
    pstat=models.CharField(max_length=20,default="NOT PAID")
    cardno=models.CharField(default="0",max_length=15)

class CATSBooking(models.Model):
    bno=models.IntegerField(primary_key=True)
    bdate=models.DateField(default=date.today)
    custid=models.IntegerField()
    custname=models.CharField(max_length=40,null=False)
    srvid=models.IntegerField()
    sname=models.CharField(max_length=30)
    serv=models.CharField(max_length=40 ,default="catering")
    pckname=models.CharField(max_length=40)
    packid=models.IntegerField()
    rdate=models.DateField()
    rtime = models.CharField(max_length=30,default="12:00AM")
    amtpaid=models.IntegerField(default="0")
    rstat=models.CharField(max_length=20,default="NEW REQ")
    pstat=models.CharField(max_length=20,default="NOT PAID")
    cardno=models.CharField(default="0",max_length=15)


class CATS(models.Model):
    pid=models.IntegerField()
    pckname=models.CharField(max_length=40)
    foodit=models.CharField(max_length=200)
    bkch=models.IntegerField()
    pech=models.IntegerField()
    cimg=models.ImageField(upload_to='CATS/images/')

