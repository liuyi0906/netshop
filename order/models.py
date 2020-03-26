# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from userapp.models import Address, UserInfo


class Order(models.Model):
    out_trade_num = models.UUIDField()         #uuid唯一字符串编码
    order_num = models.CharField(max_length=50)    #订单编号
    trade_no = models.CharField(max_length=120)    #支付完成生成的编号
    status = models.CharField(max_length=20)         #订单状态
    payway = models.CharField(max_length=20,default='alipay')    #支付方式
    address = models.ForeignKey(Address,on_delete=models.CASCADE)    #
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)



class OrderItem(models.Model):
    goodsid = models.PositiveIntegerField()
    colorid = models.PositiveIntegerField()
    sizeid = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    order = models.ForeignKey(Order,on_delete=models.CASCADE)

