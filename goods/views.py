import math
from django.shortcuts import render

from goods.models import *
# Create your views here.
from django.views import View
from django.core.paginator import Paginator
class IndexView(View):
    def get(self,request,cid=1,num=1):
        cid = int(cid)
        num = int(num)
        #查询所有的类别信息
        category=Category.objects.all().order_by('id')

        #查询当前类型下的商品信息
        goodslists=Goods.objects.filter(category_id=cid).order_by('id')

        #分页（每页显示8条）
        pager = Paginator(goodslists,8)

        #获取当前页的数据
        page_goodsList = pager.page(num)

        begin = (num-int(math.ceil(10.0/2)))
        if begin < 1:
            begin = 1
        end = begin+9
        if end > pager.num_pages:
            end = pager.num_pages
        if begin <= 10:
            begin = 1
        else:
            begin = end - 9
        pagelist = range(begin,end+1)

        return render(request,'index.html',
                      {'categorys':category,'goodsList':page_goodsList,'CurrentCid':cid,'pagelist':pagelist,'num':num})

#商品详情装饰器实现推荐商品
def recommend_view(func):
    def wrapper(detailView,request,goodsid,*args,**kwargs):
        #将存放在cookie中的goodsid获取
        cookie_str = request.COOKIES.get("recommend",'')

        #存放goodsid的列表
        goodsidList = [gid for gid in cookie_str.split() if gid.strip()]

        #最终获取需要的推荐商品
        goodsList = [Goods.objects.get(id=gsid) for gsid in goodsidList if gsid!=goodsid and Goods.objects.get(id=gsid).category_id==Goods.objects.get(id=goodsid).category_id][:4]

        #将goodsList传递给get方法
        response = func(detailView,request,goodsid,goodsList,*args,**kwargs)

        #判断goodsid是否存在goodsidList
        if goodsid in goodsidList:
            goodsidList.remove(goodsid)
            goodsidList.insert(0,goodsid)
        else:
            goodsidList.insert(0,goodsid)
        #将goodsidList中的数据保存到cookie中
        response.set_cookie("recommend",' '.join(goodsidList),max_age=3*24*60*60)
        return response
    return wrapper
class DetailView(View):
    @recommend_view
    def get(self,requst,goodsid,recommendList=[]):
        goodsid = int(goodsid)
        #根据goodsid查询商品的详情信息
        goods = Goods.objects.get(id=goodsid)
        print(recommendList)
        return render(requst,'detail.html',{'goods':goods,'recommentlist':recommendList})


