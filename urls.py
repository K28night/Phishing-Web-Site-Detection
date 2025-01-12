"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from.import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login/',LoginView.as_view(template_name="login.html"),name="login"),
    path('home/',views.home,name="home"),
    path('about1/',views.about1,name="about1"),
    path('logout/',views.logout_request,name="logout"),
    path('feedback/',views.feedback,name="feedback"),
    path('test/',views.test,name="test"), 
    path('predict/',views.predict,name="predict"),
    path('afterlogin_view',views.afterlogin_view,name="afterlogin"),
    path('profile_edit/',views.profile_edit,name="profile_edit"),
    path('contact/',views.contact,name="contact"),
    path('report/',views.report,name="report"),
    path('admindash/',views.admindash,name="admindash"),
    path('adminregister/',views.adminregister,name="adminregister"),

    path('userdetailsview/',views.userdetailsview,name="userdetailsview"),
    path('feedbackview/',views.feedbackview,name="feedbackview"),
    path('reportsview/',views.reportsview,name="reportsview"),
    path('sitesinformation/',views.sitesinformation,name="sitesinformation"),
    path('usersiteview/',views.usersiteview,name="usersiteview"),

    path('delete1/<str:pk>',views.delete1,name="delete1"),
    path('delete2/<str:pk>',views.delete2,name="delete2"),
    path('delete3/<str:pk>',views.delete3,name="delete3"),
    path('delete4/<str:pk>',views.delete4,name="delete4"),












    

]
