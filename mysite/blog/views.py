from django.shortcuts import render
from blog import models
# Create your views here.
info_list=[]

def userInfo(req):

    if req.method=="POST":
        username=req.POST.get("username",None)
        sex=req.POST.get("sex",None)
        email=req.POST.get("email",None)

        # info={"username":username,"sex":sex,"email":email}
        # info_list.append(info)

        models.UserInfo.objects.create(
            username=username,
            sex=sex,
            email=email
        )
    info_list = models.UserInfo.objects.all()
    return render(req,"userInfo.html",{"info_list":info_list})
