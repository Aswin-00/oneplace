from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.index),
    path("home/",views.index),
    path("reg/",views.phreg),
    path("login/",views.lgin),
    path("sing/",views.usrsing),
    path("wadmin/",views.wadmin),
    path("photographer/",views.phtogh),
    path("aduitorium/",views.adtorium),
    path("cabowners/",views.cabdriver),
    path("catering/",views.catring),
    path("emangemant/",views.magment),
    path("blocked/",views.blocked),
    path("rej/<int:id>/",views.reject),
    path("acc/<int:id>/",views.accpt),
    path("pht/",views.PHTGO),
    path("photografer/",views.PHTGO),
    path("pht/<int:id>/",views.PHTGOusrvw),
    path("phtimg/",views.PHTGOimageupload),

    path("noneloginuserphto/<int:id>/",views.noneloginuserphto),
    path("noneloginusercabo/<int:id>/",views.noneloginusercabo),
    path("noneloginusercats/<int:id>/",views.noneloginusercats),

    path("info/<int:id>",views.PHTGOreq),

    path("sch/<int:id>",views.PHTGOsch),

    path("fedit/<int:id>",views.PHTGOfirst),

    # path("uld/",views.PHTGOup),

    # path("uld/<int:id>",views.PHTGOup),

    path("edit/<int:id>",views.PHTGOed),
    path("fedit/<int:id>",views.PHTGOdetailupload),
    path("caradd/",views.caradd),
    path("car/",views.CABO),
    path("carurinfo/",views.carusrinfo),
    path("carusr/<int:id>/",views.CABOusrc),
    path("user/",views.userpage),
    path("usrbk/",views.usrphotobooking),
    path("cancel/<int:bid>/<str:job>",views.cancel),
    path("payadvance/<int:bid>/<str:job>",views.payadvance),
    path("userbookingpage/",views.userbookingpage),
    path("payment/<int:bno>/<str:job>",views.payment),
    path("cardetailedit/",views.caredit),
    path("carupdate/<int:id>",views.updatecar),
    path("carreq/",views.careq),
    path("carbk/<int:id>",views.carbooking),
    path("cataddmenu/",views.catsaddmenu),
    path("cats/",views.cateringservice),
    path("catbk/<int:id>/",views.catbooking),
    path("catreq/",views.catreq),
    path("CATSusrvw/<int:id>/",views.CATSERV),
    path("changepasss/",views.changepwd),


]
