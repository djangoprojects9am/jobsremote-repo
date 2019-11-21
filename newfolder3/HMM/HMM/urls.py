
"""HMM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from emxcel.views import home_view,register_view,logout_view
from django.views.generic import TemplateView,ListView,UpdateView,DeleteView,CreateView
from emxcel.models import EmployeeDetail,BankDetail,EmpBankdetails
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('register/', register_view),
    path('index/',login_required(TemplateView.as_view(template_name="emxcel/index.html"))),
    path('employee/',login_required(ListView.as_view(model=EmployeeDetail))),
    path('create_employee/',CreateView.as_view(
    	model=EmployeeDetail,
    	fields="__all__",
    	success_url="/employee")),
    re_path("empdetail_update/(?P<pk>[0-9]+)",UpdateView.as_view(
    	model=EmployeeDetail,
    	fields="__all__",
    	success_url="/employee")),
    re_path("empdetail_delete/(?P<pk>[0-9]+)",DeleteView.as_view(
    	model=EmployeeDetail,
    	success_url="/employee")),
    path('bank/',login_required(ListView.as_view(model=BankDetail))),
    path('create_bank/',CreateView.as_view(
    	model=BankDetail,
    	fields="__all__",
    	success_url="/bank")),
    re_path("bankdetail_update/(?P<pk>[0-9]+)",UpdateView.as_view(
    	model=BankDetail,
    	fields="__all__",
    	success_url="/bank")),
    re_path("bankdetail_delete/(?P<pk>[0-9]+)",DeleteView.as_view(
    	model=BankDetail,
    	success_url="/bank")),
    path("bankdetail_delete", DeleteView.as_view(
    	model=BankDetail,
    	success_url="/bank")),
    path("empbank/",login_required(ListView.as_view(model=EmpBankdetails))),
    path('create_empbank/',CreateView.as_view(
    	model=EmpBankdetails,
    	fields="__all__",
    	success_url="/empbank")),
    re_path("empbank_update/(?P<pk>[0-9]+)",UpdateView.as_view(
    	model=EmpBankdetails,
    	fields="__all__",
    	success_url="/empbank")),
    re_path("empbank_delete/(?P<pk>[0-9]+)",DeleteView.as_view(
    	model=EmpBankdetails,
    	success_url="/empbank")),
    path("logout/",logout_view),
    # path('emxcel/<int:id>/delete/',bankdetail_delete_view, name='bankdetail_delete')
    
]
