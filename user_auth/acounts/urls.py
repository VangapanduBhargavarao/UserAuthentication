from django.urls import path
from . views import signup,logout_view,login_view,patient_dashboard,doctor_dashboard
urlpatterns=[
    path('',signup,name='signup'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('dashboard/patient/',patient_dashboard,name='patient_dashboard'),
    path('dashboard/doctor/',doctor_dashboard,name='doctor_dashboard'),

]