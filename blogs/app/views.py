from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .serializers import LoginSerializer,InforSerializer
from .models import Login,Information
from rest_framework import viewsets

from app.utils import getRecords
from app.models import Deal_img
# Create your views here.
import json
def index(request):
    all=Deal_img.objects.all()
    print(all,'=========')
    return render(request,"index.html")

class LoginViews(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    def get_queryset(self):
        return Login.objects.all()

class InforViews(viewsets.ModelViewSet):
    serializer_class = InforSerializer
    def get_queryset(self):
        return Information.objects.all()
#删除操作
# def remove(request):
#     id=(int)(request.GET['id'])
#     Blog.objects.get(bid=id).delete()
#     return HttpResponse(json.dumps({"code":200,"msg":"删除成功"}))
from app.models import Deal_img
from app.Gray import Gray
from app.HSV import HSV
from app.Canny import Canny
from app.Sobel import Sobel
from app.Guass import Guass
from app.XYZ import XYZ
from app.YCrCb import YCrCb
from app.HLS import HLS
from app.erode import Erode
from app.dilate import Dilate
from app.Scharr import Scharr
from app.Laplacian import Laplacian
from app.Blur import Blur
from app.median import Median
from app.bilater import Bilater
from app.Filter import Filter
from app.affine import affine
from app.Revole import Revole
from app.toushi import Toushi
from app.Little import Little
import time
# @require_http_methods(['POST'])
import os

global cur_login_user

def store(request):
    username = request.POST.get('name')
    neirong = request.POST.get('neirong')
    if username!="":
        Information.objects.create(name=username,infor=neirong)
    return HttpResponse(json.dumps
                        ({"code": 200, "mation": "存储成功"}))

def cur_login_insert(request):
    username = request.POST.get('cur_name')
    global cur_login_user
    cur_login_user = username
    return HttpResponse(json.dumps
                        ({"code": 200, "mation": "创建成功"}))
def set_condition(request):
    global cur_login_user
    cur_login_user = ""
    return HttpResponse(json.dumps
                        ({"code": 200, "temp": "设置成功"}))

def cur_login_get(request):
    global cur_login_user
    a = cur_login_user
    return HttpResponse(json.dumps
                        ({"code": 200, "cur": a}))

def update(request):
    infor = request.POST.get('infor')
    form = Login.objects.values()
    for i in range(len(form)):
        if form[i]['username'] == infor.split(',')[0]:
            return HttpResponse(json.dumps
                                ({"code": 200, "infor": "用户名已经存在"}))

    Login.objects.create(username=infor.split(',')[0], password=infor.split(',')[1])

    return HttpResponse(json.dumps
                        ({"code": 200, "infor": "创建成功"}))

def upload(request):
    basepath='/static/media/'
    status=request.POST.get("type")

    print("处理模式--",status)
    img=request.FILES.get("file")#上传的图片
    deal=Deal_img.objects.create(
        frame=img
    )

    deal.save()#保存到库里

    name=basepath+deal.frame.name #获取名字
    abspath=(os.path.dirname(os.path.abspath(__file__))+basepath).replace("\\","/").replace("/static/media",'')#上传后的图片路径
    abspath_old_file=(abspath+name).replace("//",'/') #绝对路径，之前的名字
    abspath_newFile=(abspath+name).replace("//",'/')#处理后的名字替换原来的图片文件
    #后续在这里换另一个算法
    if status=='0':
        print("灰度图")
        Gray(abspath_old_file, abspath_newFile)
    elif status=="1":
        print("XYZ")
        XYZ(abspath_old_file,abspath_newFile)
    elif status=="2":
        print("YCrCb")
        YCrCb(abspath_old_file,abspath_newFile)
    elif status=="3":
        print("HSV")
        HSV(abspath_old_file,abspath_newFile)
    elif status=="4":
        print("HLS")
        HLS(abspath_old_file,abspath_newFile)
    elif status=="5":
        print("腐蚀")
        Erode(abspath_old_file,abspath_newFile)
    elif status=="6":
        print("膨胀")
        Dilate(abspath_old_file,abspath_newFile)
    elif status=="7":
        print("缩放")
        beilv = request.POST.get('beilv')
        Little(abspath_old_file,abspath_newFile,beilv)

    elif status=="8":
        print("翻转")
        choice = request.POST.get("choice_revole")
        Revole(abspath_old_file,abspath_newFile,choice)

    elif status=="9":
        print("仿射")
        affine(abspath_old_file,abspath_newFile)

    elif status=="10":
        print("透视")
        zuobiao = request.POST.get("zuobiao")
        Toushi(abspath_old_file,abspath_newFile,zuobiao)

    elif status=="11":
        print("均值滤波")
        Blur(abspath_old_file, abspath_newFile)
    elif status=="12":
        print("方框滤波")
        Filter(abspath_old_file, abspath_newFile)
    elif status=="13":
        print("高斯滤波")
        Guass(abspath_old_file, abspath_newFile)
    elif status=="14":
        print("中值滤波")
        Median(abspath_old_file, abspath_newFile)
    elif status=="15":
        print("双边滤波")
        Bilater(abspath_old_file, abspath_newFile)
    elif status=="16":
        print("canny")
        Canny(abspath_old_file, abspath_newFile)
    elif status=="17":
        print("Sobel")
        Sobel(abspath_old_file, abspath_newFile)
    elif status=='18':
        print("Scharr")
        Scharr(abspath_old_file, abspath_newFile)
    elif status=='19':
        print("Laplacian")
        Laplacian(abspath_old_file, abspath_newFile)


    print("处理完成")


    return HttpResponse(json.dumps
                        ({"code":200,"url":name}))