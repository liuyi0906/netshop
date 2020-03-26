# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#商品类别表
class Category(models.Model):
    cname = models.CharField(max_length=10)
    def __unicode__(self):
        return u'Category:%s'%self.cname

#商品详情
class Goods(models.Model):
    gname = models.CharField(max_length=100)   #商品的名称
    gdesc = models.CharField(max_length=100)    #商品的描述
    oldprice = models.DecimalField(max_digits=5,decimal_places=2)    #原价
    price = models.DecimalField(max_digits=5,decimal_places=2)       #现价
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __unicode__(self):
        return u'Goods:%s'%self.gname

    #获取商品的大图
    def getImage(self):
        return self.inventory_set.first().color.colorurl

    #获取商品所有颜色对象
    def getColors(self):
        colorlist=[]
        for inventory in self.inventory_set.all():
            color = inventory.color
            if color not in colorlist:
                colorlist.append(color)
        return colorlist

    def getSizeList(self):
        sizeList=[]
        for inventory in self.inventory_set.all():
            size = inventory.size
            if size not in sizeList:
                sizeList.append(size)
        return sizeList
    def getDetailList(self):
        import collections
        datas = collections.OrderedDict()
        for goodsdetail in self.goodsdetail_set.all():
            gdname = goodsdetail.name()
            if gdname not in datas.keys():
                datas[gdname] = [goodsdetail.gdurl]
            else:
                datas[gdname].append(goodsdetail.gdurl)
        return datas

#商品详情名称
class GoodsDetailName(models.Model):
    gdname = models.CharField(max_length=30)

    def __unicode__(self):
        return u'GoodsDetailName:%s'%self.gdname

#详情信息
class GoodsDetail(models.Model):
    gdurl = models.ImageField(upload_to='')
    gdname = models.ForeignKey(GoodsDetailName,on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)

    #获取详情名称
    def name(self):
        return self.gdname.gdname

#
class Size(models.Model):
    sname = models.CharField(max_length=10)

    def __unicode__(self):
        return u'Size:%s'%self.sname


class Color(models.Model):
    colorname = models.CharField(max_length=10)
    colorurl = models.ImageField(upload_to='color/')

    def __unicode__(self):
        return u'Color:%s'%self.colorname
#库存
class Inventory(models.Model):
    count = models.PositiveIntegerField()    #数量
    color = models.ForeignKey(Color,on_delete=models.CASCADE)          #颜色
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)



