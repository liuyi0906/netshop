from django.shortcuts import render,HttpResponseRedirect,HttpResponse

from django.views import View
from cart.cartmanager import *
import json
# Create your views here.
class ToOrderView(View):
    def get(self,request):
        #获取请求参数
        cartitems = request.GET.get('cartitems','')

        return HttpResponseRedirect('/order/order.html?cartitems='+cartitems)

class OrderView(View):
    def get(self,request):
        # 获取请求参数
        cartitems = request.GET.get('cartitems', '')

        #反序列化----将json格式字符串装换成python对象列表
        cartitemList = json.loads("["+cartitems+"]")

        #将Python对象列表装换成cartItem对象列表
        cartemObject = [getCartManger(request).get_cartitems(**item) for item in cartitemList if item]

        #获取用户默认收货地址
        address = request.session.get('user').address_set.get(isdefault=True)

        #获取支付的总金额
        total = 0
        for cm in cartemObject:
            total += cm.getTotalPrice()

        return render(request,'order.html',{'cartemObject':cartemObject,'address':address,'total':total})