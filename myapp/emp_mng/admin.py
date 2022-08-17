from django.contrib import admin
from .models import Emp_mng,Testimonial
# Register your models here.

class Emp_mngAdmin(admin.ModelAdmin):
    list_display=('working','name','emp_id','phone')
    list_editable=('name',)
    search_fields=('name',)
    list_filter=('working',)




admin.site.register(Emp_mng,Emp_mngAdmin)
admin.site.register(Testimonial)