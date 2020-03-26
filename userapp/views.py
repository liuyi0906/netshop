from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from userapp.models import *
from django.views import View
from utils.code import *
from django.core.serializers import serialize
# Create your views here.

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')

        user = UserInfo.objects.create(uname=uname,pwd=pwd)
        if user:
            #将用户存储到session对象中
            request.session['user'] = user
            return HttpResponseRedirect('/user/center/')
        return HttpResponseRedirect('/user/register/')


class CheckUnameView(View):
    def get(self,request):
        uname = request.GET.get('uname','')

        #从数据库中查询是否有这个用户
        userlist = UserInfo.objects.filter(uname=uname)

        flag = False
        if userlist:
            flag = True
        return JsonResponse({'flag':flag})


class CenterView(View):
    def get(self,request):
        return render(request,'center.html')


#退出登录
class LogoutView(View):
    def post(self,request):
        #删除session中登陆用户信息
        if 'user' in request.session:
            del request.session['user']
        return JsonResponse({'delflag':True})


#登录
class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        #获取请求参数
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')

        #查询数据库是否存在
        userList = UserInfo.objects.filter(uname=uname,pwd=pwd)
        print(userList)
        if userList:
            request.session['user'] = userList[0]
            return HttpResponseRedirect('/user/center/')
        return HttpResponseRedirect('/user/login/')

#存放验证码到session中和返回验证码
class LoadCodeView(View):
    def get(self,request):
        img,str = gene_code()
        #将生成的验证码放到session中
        request.session['sessioncode'] = str
        return HttpResponse(img,content_type='image/png')

#验证码验证
class CheckcodeView(View):
    def get(self,request):
        #获取输入框中的验证码
        code = request.GET.get('code','')

        #获取生产的验证码
        sessioncode = request.session.get('sessioncode',None)

        #比较是否相等
        flag = code == sessioncode

        return JsonResponse({"checkFlag":flag})


#地址管理界面
class AddressView(View):
    def get(self,request):
        user = request.session.get('user', '')
        addrList = user.address_set.all

        return render(request, 'address.html', {"addrList": addrList})

    #地址信息提交
    def post(self,request):
        aname = request.POST.get('aname','')
        aphone = request.POST.get('aphone','')
        addr = request.POST.get('addr','')
        user = request.session.get('user','')
        #将收货地址插入数据库
        address = Address.objects.create(aname=aname,aphone=aphone,addr=addr,userinfo=user,isdefault=(lambda count: True if count == 0 else False)(user.address_set.all().count()))
        #获取当前登录用户的所有的收货地址
        addrList = user.address_set.all

        return render(request,'address.html',{"addrList":addrList})

#地址三级联动
class LoadAreaView(View):
    def get(self,request):
        pid = request.GET.get('pid',-1)
        pid = int(pid)

        arealist = Area.objects.filter(parentid=pid)

        #将获取出来的对象转换成json格式的字符串
        jarelist = serialize('json',arealist)
        return JsonResponse({'jarelist':jarelist})