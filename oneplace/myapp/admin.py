from django.contrib import admin
from myapp.models import SPD,USINF,PHTGO,CABO,PHTGOBooking,CABOBooking,CATS,CATSBooking,PHTGOimg
# Register your models here.

class spdadmin(admin.ModelAdmin):
    list_display = ('id','namecu',"rwork",'slink',"job","usernm","userpw","status")

admin.site.register(SPD,spdadmin)
admin.site.register(USINF)
admin.site.register(PHTGO)
admin.site.register(CABO)
admin.site.register(CATS)
admin.site.register(PHTGOBooking)
admin.site.register(CABOBooking)
admin.site.register(CATSBooking)
admin.site.register(PHTGOimg)