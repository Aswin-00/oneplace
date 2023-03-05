from django.shortcuts import render,redirect
from myapp.models import SPD,USINF,PHTGOBooking,CABOBooking,CATSBooking,PHTGOimg
from myapp.models import PHTGO as phg
from myapp.models import CATS as catering
from myapp.models import CABO as car
from django.utils.datastructures import MultiValueDictKeyError

# from django.shortcuts import render_to_response
# Create your views here.

def index(request):
    PH=phg.objects.all()
    CA=car.objects.all()
    CT=catering.objects.all()
    try:
        for key in request.session.keys():
            del request.session[key]
    except RuntimeError:
        pass
    return render(request,"index.html",{"PH":PH,"CA":CA,"CT":CT})


def phreg(request): ##photografer registraion
    if request.method =="POST":
        jb=request.POST.get('job')
        Fnam = request.POST.get('first_name')
        Lnam = request.POST.get('last_name')
        Rig = request.POST.get('region')
        cnam = request.POST.get('company')
        add = request.POST.get('Add')
        pin = request.POST.get('zip')
        Pnum = request.POST.get('phone')
        Cntry=request.POST.get('country')
        About = request.POST.get('about')
        Eid=request.POST.get('EID') #emaid id
        userid=request.POST.get('usnam') #instagram id
        passw=request.POST.get('psnam') # facebook id
        Sid=request.POST.get('SID') # website id
        ds=SPD(namecu=cnam,fname=Fnam,lname=Lnam,Add=add+" "+Cntry+" "+pin,
               email=Eid,usernm=userid,userpw=passw,job=jb,
               pnum=Pnum,about=About,rwork=Rig,slink=Sid)
        ds.save()
        return redirect("/home/")

    return render(request,"registration.html")


def lgin(request):
    msg="0"
    if request.method=="POST":
        usn= request.POST.get("usernm")
        upw= request.POST.get("userpw")

        request.session['username'] = usn
        request.session['userpssword'] = upw

        found=0
        de=SPD.objects.filter(usernm=usn,userpw=upw)
        if de.filter(usernm=usn,userpw=upw).exists():
            print("loop1")
            found=1
            for i in de:
                request.session['fname']=i.fname
                request.session['lname'] =i.lname
                id=i.id
                request.session['id']=id
                job=i.job
                st=i.status
                request.session["web"]=i.slink
                request.session['st']=st
                request.session["about"]=i.about
                request.session["email"]=i.email
                request.session["address"]=i.Add
                request.session["company"]=i.namecu
                request.session["region"]=i.rwork
                request.session["phoneno"]=i.pnum

            print(job)
            if st=="CR":
                print("loop2", job)
                if job=="PHTOG":
                    request.session['job'] = "phtografer"
                    pr = phg.objects.filter(pid=id)
                    if pr.exists():
                        for i in pr:
                            cimg=i.cicmg
                            img = i.picmg
                            tpric = i.tpric
                            opric = i.opric

                            # request.session['cimg'] = cimg
                            # request.session['img'] = img

                            request.session['opric'] = opric
                            request.session['tpric'] = tpric
                            return redirect("/pht/")
                    else:
                        return redirect(f"/fedit/{id}")
                elif job == "CATS": #catering service
                    request.session['job'] = "catering service"
                    de=catering.objects.filter(pid=id)
                    if de.exists():
                        return redirect("/cats/")
                    else:
                        return redirect("/cataddmenu/")



                elif job == "CABO":  #car onwers login
                    de = car.objects.filter(pid=id).all()
                    if de.exists():
                        request.session['job'] = "CAR OWNERS"
                        return render(request,"CABO.html",{"de":de})
                    else:
                        return redirect("/caradd/")

            elif st=="WL":
                msg='registration under process'
                return render(request,'login.html', {"msg":msg})
                     #under prox\c
            else:
                msg='registration under process'
                return render(request, 'login.html', {"msg":msg})
        if found==0:
            de=USINF.objects.filter(usernm=usn,userpw=upw)
            if de.exists():
                found=1
                for i in de:
                    username=i.username
                    email=i.email
                    phone=i.pnum
                    id=i.id
                request.session['id'] = id
                request.session['fname'] = username
                request.session['lname'] =phone
                request.session['job'] = "user"
                request.session['st'] = "CR"
                request.session['about'] = email

                if de.filter(prv="ADM"):
                    return redirect('/wadmin/')
                else:
                    return redirect("/user/")
        if found==0:
            msg="user not found"
            return render(request, "login.html", {"msg": msg});
            #sesstion set as user
    return render(request,"login.html",{"msg":msg});



def usrsing(request):
    if request.method=="POST":
        passw = request.POST.get('passw')
        usern= request.POST.get('usernam')  # facebook id
        email= request.POST.get('email')  # facebook id
        pnum= request.POST.get('pnum')  # facebook id
        usnm= request.POST.get('lgnm')  # facebook id
        st=USINF(username=usern,email=email,pnum=pnum,usernm=usnm,userpw=passw)
        st.save()
        return redirect("/home/")
    return render(request,"usersinup.html");


def wadmin(request):
    de=SPD.objects.filter(status="CR")
    ph=len(de.filter(job="PHTOG"))
    cat=len(de.filter(job="CATS"))
    car=len(de.filter(job="CABO"))
    evm=len(de.filter(job="EVMA"))
    audo=len(de.filter(job="AUDO"))
    return render(request,"wadmin.html",{"ph":ph,"car":car,"cat":cat,'evm':evm,"audo":audo,"de":de})

def phtogh(request):
    de=SPD.objects.filter(job="PHTOG",status="WL")
    x="PHOTOGRAPHER"
    return render(request, "AdminEM.html", {"de": de, "name": x, "len": len(de)})


def adtorium(request):
    de=SPD.objects.filter(job="AUDO",status="WL")
    x ="AUDITORIUM OWNERS"
    return render(request, "AdminEM.html", {"de": de, "name": x, "len": len(de)})


def cabdriver(request):
    de=SPD.objects.filter(job="CABO",status="WL")
    x ="CAB OWNERS"
    return render(request, "AdminEM.html", {"de": de, "name": x,"len":len(de)})


def catring(request):
    de=SPD.objects.filter( job="CATS",status="WL")
    x="CATERING SERVICE"
    return render(request, "AdminEM.html", {"de": de, "name": x, "len": len(de)})


def magment(request):
    de=SPD.objects.filter(job="EVMA",status="WL")
    x="EVENT MANAGEMENT"
    return render(request, "AdminEM.html", {"de": de, "name": x, "len": len(de)})



def blocked(request):
    de=SPD.objects.filter(status="R")
    x = "BLOCKED USERS"
    return render(request, "AdminEM.html", {"de": de, "name": x,"len":len(de)})


def reject(request,id):
    SPD.objects.filter(id=id).update(status="R")
    return redirect("/wadmin/")


def accpt(request,id):
    SPD.objects.filter(id=id).update(status="CR")
    return redirect("/wadmin/")

def PHTGOreq(request,id):
    dt = SPD.objects.filter(id=id)
    for j in dt:
        fname = j.fname
        lname = j.lname
        pnum = j.pnum
        adress = j.Add
        company = j.namecu
        socialmedia = j.slink
        job = "PHTOGRAFER"
        email = j.email
        about = j.about
    pr = phg.objects.filter(pid=id)
    for i in pr:
        img = i.picmg
        cmg = i.cicmg
        tpric = i.tpric
        opric = i.opric
    booking=PHTGOBooking.objects.filter(srvid=id,rstat="NEW REQ")

    return render(request, "PHTGOreq.html", {"fname": fname, "lname": lname, "job": job,
                                                     "phone": pnum,
                                                     "com": company,
                                                     "adress": adress,
                                                     "cimg": cmg,
                                                     "email": email,
                                                     "about": about,
                                                     "img": img,
                                                     "tpric": tpric,
                                                     "opric": opric,
                                                     "booking":booking
                                                     })
def PHTGOsch(request,id):
    dt = SPD.objects.filter(id=id)
    for j in dt:
        fname = j.fname
        lname = j.lname
        pnum = j.pnum
        adress = j.Add
        company = j.namecu
        socialmedia = j.slink
        job = "PHTOGRAFER"
        email = j.email
        about = j.about
    pr = phg.objects.filter(pid=id)
    for i in pr:
        img = i.picmg
        cmg = i.cicmg
        tpric = i.tpric
        opric = i.opric
    booking=PHTGOBooking.objects.filter(srvid=id,pstat="PAID")
    return render(request, "PHTGOsch.html", {"fname": fname, "lname": lname, "job": job,
                                                     "phone": pnum,
                                                     "com": company,
                                                     "adress": adress,
                                                     "cimg": cmg,
                                                     "email": email,
                                                     "about": about,
                                                     "img": img,
                                                     "tpric": tpric,
                                                     "opric": opric,
                                                     "booking":booking
                                                     })

def PHTGOfirst(request,id):
    if request.method=="POST":
        pimg=request.FILES["picmg"]
        cimg=request.FILES["cimg"]
        about=request.POST.get("about")
        slink=request.POST.get("wid")
        tpric=request.POST.get("tpric")
        opric=request.POST.get("opric")

        dt=phg(pid=id,tpric=tpric,opric=opric,picmg=pimg,cicmg=cimg,about=about,slink=slink)
        dt.save()
        return redirect("/pht/")

    sd=SPD.objects.filter(id=id)
    for i in sd:
        fname=i.fname
        lname=i.lname
        email=i.email
        slink=i.slink
        about=i.about
    return render(request ,"PHTGOedit.html",{"fname":fname,"lname":lname,"email":email,"slink":slink,
                                             "about":about})


def PHTGOed(request,id):
    if request.method=="POST":
        tpric=request.POST.get("tpric")
        opric=request.POST.get("opric")
        request.session["tpric"]=tpric
        request.session["opric"]=opric

        phg.objects.filter(pid=id).update(tpric=tpric,opric=opric)
        pr = phg.objects.filter(pid=id)
        for i in pr:
            cimg = i.cicmg
            img = i.picmg
        return render(request, "PHTGOpage.html", {"img": img, "cimg": cimg})

    else:
        sd=SPD.objects.filter(id=id)
        for i in sd:
            fname=i.fname
            lname=i.lname
            email=i.email
            slink=i.slink
            about=i.about
        hu= phg.objects.filter(pid=id)
        for j in hu:
            picmg=j.picmg
            cicmg=j.cicmg
            tpric=j.tpric
            opric=j.opric
        return render(request ,"PHTGOedit.html",{"fname":fname,"lname":lname,"email":email,"slink":slink,
                                             "about":about,"picmg":picmg,"cicmg":cicmg,"tpric":tpric,"opric":opric})

def PHTGO(request):
    de=phg.objects.filter(pid=request.session["id"])
    imgus=PHTGOimg.objects.filter(uid=request.session["id"])
    print(len(imgus))
    print(request.session["id"])
    for i in de:
        img=i.picmg
        cimg=i.cicmg
    return render(request,"PHTGOpage.html",{'img':img,"cimg":cimg,"imgus":imgus})

def PHTGOusrvw(request,id):
    request.session["phtid"]=id
    dt=SPD.objects.filter(id=id)
    imgus=PHTGOimg.objects.filter(uid=id)
    for j in dt:
        fname=j.fname
        lname=j.lname
        pnum=j.pnum
        adress=j.Add
        company= j.namecu
        socialmedia=j.slink
        job="PHTOGRAFER"
        email=j.email
        about=j.about
    pr =phg.objects.filter(pid=id)
    for i in pr:
        img=i.picmg
        cmg=i.cicmg
        tpric=i.tpric
        opric=i.opric

    return render(request,"PHTGOusrview.html",{"imgus":imgus,"fname":fname,"lname":lname,"job":job,
                                               "phone":pnum,
                                               "com":company,
                                               "adress":adress,
                                                "cimg":cmg,
                                               "email":email,
                                               "about": about,
                                               "img": img,
                                               "tpric":tpric,
                                               "opric":opric,
                                               })
def noneloginuserphto(request,id):
    request.session["phtid"]=id
    dt=SPD.objects.filter(id=id)
    imgus=PHTGOimg.objects.filter(uid=id)
    print(len(imgus))
    for j in dt:
        fname=j.fname
        lname=j.lname
        pnum=j.pnum
        adress=j.Add
        company= j.namecu
        socialmedia=j.slink
        job="PHTOGRAFER"
        email=j.email
        about=j.about
    pr =phg.objects.filter(pid=id)
    for i in pr:
        img=i.picmg
        cmg=i.cicmg
        tpric=i.tpric
        opric=i.opric

    return render(request,"PHTGOnonloginusrview.html",{"imgus":imgus,"fname":fname,"lname":lname,"job":job,
                                               "phone":pnum,
                                               "com":company,
                                               "adress":adress,
                                                "cimg":cmg,
                                               "email":email,
                                               "about": about,
                                               "img": img,
                                               "tpric":tpric,
                                               "opric":opric,
                                               })


def PHTGOdetailupload(request):
    if request.method=="POST":
        pimg=request.FILES["picmg"]
        print(pimg)
        cimg=request.FILES["cimg"]
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        website=request.POST.get("wid")
        tpric=request.POST.get("tpric")
        opric=request.POST.get("opric")
        tw=request.POST.get("tw")
        fb=request.POST.get("fb")
        pn=request.POST.get("pn")
        id=9
        print(id)
        inst=request.POST.get("inst")
        abt=request.POST.get("about")
        slink=[tw,fb,pn,inst,website]
        phd=phg(slink=slink,picmg=pimg,tpric=tpric,opric=opric,about=abt,pid=id)
        phd.save()
        return redirect('/pht/')
    return render(request,"PHTGOedit.html")

def PHTGOimageupload(request):
    id=request.session["id"]
    if request.method=="POST":
        img = request.FILES["image"]
        de=PHTGOimg(uid=id,img=img)
        de.save()

    return redirect("/pht/")



def CABO(request):
    de = car.objects.filter(pid=request.session["id"]).all()
    request.session['job'] = "CAR OWNERS"
    return render(request, "CABO.html", {"de": de})


def CABOusrc(request,id):
    packageid=id
    package = car.objects.filter(id=id).all()
    for i in package:
        pid = i.pid
        carname = i.carnm
        carmd = i.carmdl
        seat = i.stcp
        carbooking = i.bookingch
        carimg = i.cimg
        tpric = i.tpric
    request.session["carowner"] = pid
    provider = SPD.objects.filter(id=pid).all()
    job = "CAR OWNERS"
    return render(request, "CABOusrvw.html", {"provider": provider, "job": job,
                                              "packageid":packageid,
                                                       "carname": carname, "carmd": carmd, "tpric": tpric, "seat": seat,
                                                       "carbooking": carbooking,
                                                       "carimg": carimg})

def noneloginusercabo(request,id):
    package= car.objects.filter(id=id).all()
    for i in package:
        pid=i.pid
        carname=i.carnm
        carmd=i.carmdl
        seat=i.stcp
        carbooking=i.bookingch
        carimg=i.cimg
        tpric=i.tpric
    provider=SPD.objects.filter(id=pid).all()
    job = "CAR OWNERS"
    return render(request, "CABOnoneloginusrvw.html", {"provider":provider ,"job":job,
                                                       "carname":carname,"carmd":carmd,"tpric":tpric,"seat":seat,"carbooking":carbooking,
                                                       "carimg":carimg})

def carbooking(request,id):
    username=request.session["fname"]
    userid=request.session["id"]
    providerid=request.session["carowner"]

    for i in SPD.objects.filter(id=providerid):
        providername=i.fname

    if request.method == "POST":
        evtdata=request.POST.get("Evdate")
        evtime=request.POST.get("Evtime")
        for i in car.objects.filter(pid=providerid, id=userid):
            carname = i.carnm
            carmodel=i.carmdl
            packid=i.id
        bk=CABOBooking(custid=userid,custname=username,srvid=providerid,sname=providername,serv="CARBO",carname=carname,carmodel=carmodel,packid=packid,rdate=evtdata,rtime=evtime)
        bk.save()
        return redirect("/user/")

    return render(request,"carbooking.html",{"username":username,"providername":providername})




def caradd(request):
    id=request.session["id"]
    if request.method=="POST":
        pid=id
        bookingch=request.POST.get("bookingch")
        cimg=request.FILES["image"]
        carnm=request.POST.get("carnm")
        carmdl=request.POST.get("carmdl")
        stcp=request.POST.get("stcp")
        tpric=request.POST.get("tpric")
        de=car(pid=pid,cimg=cimg,carnm=carnm,carmdl=carmdl,stcp=stcp,tpric=tpric,bookingch=bookingch)
        de.save()
        return  redirect("/car/")



    return render(request,"caradd.html")



def userpage(request):
    PH = phg.objects.all()
    CA = car.objects.all()
    CT = catering.objects.all()
    return render(request, "userprofile.html", {"PH": PH, "CA": CA, "CT": CT})



def usrphotobooking(request):
    de=SPD.objects.filter(id=request.session['phtid'])
    for i in de:
        fname=i.fname
    cname=request.session["fname"]
    if request.method == "POST":
        Evdate = request.POST.get("Evdate")
        Evtime = request.POST.get("Evtime")
        photogfid=request.session["phtid"]
        userid=request.session["id"]
        df=PHTGOBooking(custid=userid,custname=cname,srvid=photogfid,sname=fname,serv="photographer",rdate=Evdate,rtime=Evtime)
        df.save()
        return redirect("/user/")



    return  render(request,"booking.html",{"fname":fname,"cname":cname})

def payadvance(request,bid,job):
    if job=="PH":
        PHTGOBooking.objects.filter(bno=bid).update(rstat="Conform request",pstat="PAY NOW")
        return  redirect("/pht/")
    elif job=="CR":
        CABOBooking.objects.filter(bno=bid).update(rstat="Conform request", pstat="PAY NOW")
        return redirect("/car/")
    elif job=="CT":
        CATSBooking.objects.filter(bno=bid).update(rstat="Conform request", pstat="PAY NOW")
        return redirect("/cats/")

def cancel(request,bid,job):
    if job=="PH":
        PHTGOBooking.objects.filter(bno=bid).update(rstat="Rejected",pstat="Rejected")
        return redirect("/pht/")
    elif job=="CR":
        CABOBooking.objects.filter(bno=bid).update(rstat="Rejected", pstat="Rejected")
        return redirect("/car/")
    elif job=="CT":
        CATSBooking.objects.filter(bno=bid).update(rstat="Rejected", pstat="Rejected")
        return redirect("/cats/")

def userbookingpage(request):
    uid=request.session["id"]
    phbooking=PHTGOBooking.objects.filter(custid=uid,rstat="Conform request",pstat="PAY NOW")
    crbooking=CABOBooking.objects.filter(custid=uid,rstat="Conform request",pstat="PAY NOW")
    ctbooking=CATSBooking.objects.filter(custid=uid,rstat="Conform request",pstat="PAY NOW")

    return  render(request,"userbookingpage.html",{"phbooking":phbooking,"crbooking":crbooking,"ctbooking":ctbooking})


def payment(request,bno,job):
    if job=="PH":
        de=PHTGOBooking.objects.filter(bno=bno)
        for i in de:
                providerid = i.srvid
                name = i.custname
        for i in phg.objects.filter(pid=providerid):
            pay = i.tpric
    elif job=="CR":
        de=CABOBooking.objects.filter(bno=bno)
        for i in de:
            pckid=i.packid
            providerid = i.srvid
            name = i.custname
        for i in car.objects.filter(pid=providerid,id=pckid):
            pay = i.bookingch
    elif job=="CT":
        de=CATSBooking.objects.filter(bno=bno)
        for i in de:
            pckid = i.packid
            providerid = i.srvid
            name = i.custname
        for i in catering.objects.filter(pid=providerid,id=pckid):
            pay=i.bkch



    if request.method=="POST":
        re=request.POST.get("cardnumber")
        if job=="PH":
            PHTGOBooking.objects.filter(bno=bno).update( pstat="PAID",cardno=re,amtpaid=pay)
        elif job=="CR":
            CABOBooking.objects.filter(bno=bno).update(pstat="PAID", cardno=re, amtpaid=pay)
        elif job=="CT":
            CATSBooking.objects.filter(bno=bno).update(pstat="PAID", cardno=re, amtpaid=pay)
        return redirect("/user/")


    return render(request,"payment.html",{"name":name,"pay":pay})


def carusrinfo(request):
    for i in SPD.objects.filter(id=request.session["id"]):
        fname=i.fname
        lname=i.lname
        email=i.email
        slink=i.slink
        phone=i.pnum
        address=i.Add
        about=i.about
    if request.method=="POST":
        Fnam = request.POST.get('fname')
        Lnam = request.POST.get('lname')
        add = request.POST.get('address')
        Pnum = request.POST.get('phone')
        email = request.POST.get("email")
        About = request.POST.get('about')
        print("value",Fnam,Lnam,add,Pnum,email,about)
        ds = SPD.objects.filter(id=request.session["id"]).update(fname=Fnam, lname=Lnam, Add=add,email=email,pnum=Pnum, about=About)
        return redirect("/car/")

    return render(request,"carbasicinfo.html",{"fname": fname,
                                              "lname": lname,
                                                "phone": phone,
                                            "address": address,
                                              "email": email,
                                              "about": about,
                                              "slink":slink
                                                     })


def caredit(request):
    de =car.objects.filter(pid=request.session["id"])
    return render(request,"cardetailedit.html",{"de":de})


def updatecar(request,id):
    if request.method=="POST":
        carid = id
        carname = request.POST.get("carname")
        carmodel = request.POST.get("carmodel")
        seatingcp = request.POST.get("stcp")
        price = request.POST.get("tpric")
        try:
            img = request.FILES["carimage"]
            car.objects.filter(id=id).update(cimg=img,carnm=carname,carmdl=carmodel,stcp=seatingcp,tpric=price)
        except MultiValueDictKeyError:
            car.objects.filter(id=id).update(carnm=carname, carmdl=carmodel, stcp=seatingcp, tpric=price)
    return redirect("/car/")


def careq(request):
    booking=CABOBooking.objects.filter(srvid=request.session["id"],rstat="NEW REQ")
    return render(request,"carrequest.html",{"booking":booking})


def catsaddmenu(request):
    if request.method=="POST":
        id=request.session["id"]
        pckanm=request.POST.get("pckname")
        pckpric=request.POST.get("tpric")
        bookingpr=request.POST.get("bookingpr")
        foodname=request.POST.getlist("foodname")

        coverimage=request.FILES["cimage"]
        sv=catering(pid=id,pckname=pckanm,foodit=foodname,bkch=bookingpr,cimg=coverimage,pech=pckpric)
        sv.save()
        return redirect("/cats/")


    return  render(request,"CATSaddmnu.html")

def cateringservice(request):
    data=catering.objects.filter(pid=request.session["id"])
    # for i in data:
    #     food=i.foodit

    return render(request,"CATS.html",{'data':data})


def noneloginusercats(request,id):
    data= catering.objects.filter(id=id).all()
    for i in data:
        pid=i.pid
    provider=SPD.objects.filter(id=pid).all()
    job = "CATERING SERVICE"
    return render(request, "CATSnonloginusrvw.html", {"provider":provider ,"data":data,"job":job})



def CATSERV(request,id):
    data = catering.objects.filter(id=id).all()
    for i in data:
        pid = i.pid
    provider = SPD.objects.filter(id=pid).all()
    job = "CATERING SERVICE"
    return render(request, "CATSusrvw.html", {"provider": provider, "data": data, "job": job})


def catbooking(request,id):
    username = request.session["fname"]
    userid = request.session["id"]
    packageid=id
    for i in catering.objects.filter(id=id):
        providerid = i.pid
        packagename=i.pckname

    for i in SPD.objects.filter(id=providerid):
        providername=i.fname

    if request.method == "POST":
        evtdata = request.POST.get("Evdate")
        evtime = request.POST.get("Evtime")

        bk = CATSBooking(custid=userid, custname=username, srvid=providerid, sname=providername,
                         pckname=packagename, packid=packageid, rdate=evtdata, rtime=evtime)
        bk.save()
        return redirect("/user/")
    return render(request, "foodbooking.html", {"username": username, "providername": providername})


def catreq(request):
    booking = CATSBooking.objects.filter(srvid=request.session["id"], rstat="NEW REQ")
    return render(request, "catrequest.html", {"booking": booking})


def changepwd(request):
    usid=request.session["id"]
    usernm=request.session["username"]
    uerpwd=request.session['userpssword']
    if request.method=="POST":
        enterpssw=request.POST.get("currentpassword")
        newpssw=request.POST.get("password")
        cpssw=request.POST.get("cpassword")
        if uerpwd==enterpssw:
            if newpssw==cpssw:
                de=SPD.objects.filter(id=usid,usernm=usernm)
                pe=USINF.objects.filter(id=usid,usernm=usernm)
                if de.exists():
                    de.update(userpw=newpssw)
                    return redirect("/")
                elif pe.exists():
                    pe.update(userpw=newpssw)
                    return redirect("/")
            else:
                msg="password doest't match"
                return render(request, "changepass.html",{"msg":msg})
        else:
            msg="invalid password"
            return render(request, "changepass.html",{"msg":msg})
    return  render(request,"changepass.html")
