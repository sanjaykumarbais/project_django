from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("home/",emp_mng_home),
    path("add_emp_mng/",add_emp_mng),
    path("delete_emp_mng/<int:emp_id>",delete_emp_mng),
    path("update_emp_mng/<int:emp_id>",update_emp_mng),
    path("do_update_emp_mng/<int:emp_id>",do_update_emp_mng),
    path("testimonials/",testimonials),
    path("feedback/",feedback),

]
