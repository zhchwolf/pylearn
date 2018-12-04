from django.shortcuts import render

# Create your views here.
info_list=[]

def userInfor(req):

    if req.method=="POST":
        username=req.POST.get("username",None)
        sex=req.POST.get("sex",None)
        email=req.POST.get("email",None)

        info={"username":username,"sex":sex,"email":email}
        info_list.append(info)

    return render(req,"userInfor.html",{"info_list":info_list})