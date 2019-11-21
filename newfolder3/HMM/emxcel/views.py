from django.shortcuts import render,redirect, get_object_or_404
from emxcel.forms import Userhome
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# from .forms import UploadFileForm
# from  import handle_uploaded_file

# Create your views here.

def home_view(request):
    msg=""
    if request.method=="POST":
        data=request.POST
        user=authenticate(username=request.POST["username"],
             password=request.POST["password"])
        if user:
            login(request,user)
            return redirect("/index/")
            msg="login successfully"
        else:
            msg="login failed"

    return render(request,'emxcel/home.html',{"msg":msg})

def register_view(request):
    msg=""
    if request.method=="POST":
        frm=Userhome(request.POST)
        if frm.is_valid():
           frm.save()
           user_instance=frm.instance
           user_instance.set_password(user_instance.password)
           user_instance.save()
        msg="registerd successfully"
    else:
        msg="registered not completed"
    frm=Userhome()
    return render(request,"emxcel/register.html",{'frm':frm,"msg":msg})
@login_required
def logout_view(request):
    logout(request)
    return redirect("/")



# def upload_file(request):
#     if request.method=="POST":
#         frm=UploadFileForm(request.POST, request.FILES)
#         if frm.is_valid():
#            handle_uploaded_file(request.FILES['file'])
#         return render('/success/url')
#     else:
#         frm=UploadFileForm()
#         return render(request,'emxcel/upload.html',{'frm':frm})


# def resview(request):
#     if request.method == "POST":
#         frm = resmodelForm(request.POST, request.FILES)
#         if frm.is_valid():
#             a=resmodel(resume_header=resume_header, upload_resume=request)

# def bankdetail_confirm_delete_view(request,id):
#     obj=get_object_or_404(bank,id=id)
#     if request.method =="POST":
#         obj.delete()
#         return redirect("../../")
#         context={
#              "object":obj
#         }

#         return render(request,"emxcel/bankdetail_confirm_delete.html",context)