from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.views import View
from cart.cartmanager import *
# Create your views here.
#对购物进行各种操作
class AddCartView(View):
    def post(self,request):
        #获取当前操作类型
        flag = request.POST.get('flag','')
        #判断当前操作类型
        if flag == 'add':
            #创建cartManager对象
            carMangerObj = getCartManger(request)
            if carMangerObj == 'errorlogin':
                print("未登录")
                return HttpResponseRedirect('/user/login/')
            carMangerObj.add(**request.POST.dict())
        elif flag == 'plus':
            carMangerObj = getCartManger(request)
            carMangerObj.update(step=1,**request.POST.dict())
        elif flag == 'minus':
            carMangerObj = getCartManger(request)
            carMangerObj.update(step=-1, **request.POST.dict())
        elif flag == 'delete':
            carMangerObj = getCartManger(request)
            carMangerObj.delete(**request.POST.dict())
        return HttpResponseRedirect('/cart/queryAll/')

#显示购物车商品
class CartListView(View):
    def get(self,request):
        carMangerObj = getCartManger(request)
        #查询所有的购物车信息
        cartList = carMangerObj.queryAll()
        return render(request,'cart.html',{"cartList":cartList})