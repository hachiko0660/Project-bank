from django.urls import path
from .views import *

urlpatterns=[
    path('bnklog/',banknew),
    path('bnk2/',bnkfun),
    path('index/',index),
    path('profile/',profile),
    path('edit/<int:id>',edit1),
    path('fileedit/<int:id>',fileedit),
    path('tickmrk/',tickmrk),
    path('amountadd/<int:id>',amountadd),
    path('wdrawamount/<int:id>',wdrawamount),
    path('tickmar/',tickmar),
    path('check/<int:id>',check),
    path('success/',success),
    path('depo/',depo),
    path('wdrw/',wdraw),
    path('ministate/<int:id>',ministate),
    path('news/',newss),
    path('dis/',dis),
    path('adminlog/',adminlog),
    path('adminpro/',adminpro),
    path('admnds/',admnds),
    path('editadmn/<int:id>',editadmn),
    path('deladmin/<int:id>',deladmn),
    path('wishlist/<int:id>',wish),
    path('wishl/',wishl),
    path('logout/',logout_view),
    path('forgotpassword/',forgot_password),
    path('change/<int:id>',change_password)




]
