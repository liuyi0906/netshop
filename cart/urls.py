
from django.conf.urls import url

from cart import views

urlpatterns=[
    url(r'^$',views.AddCartView.as_view()),      #对购物进行操作
    url(r'^queryAll/$',views.CartListView.as_view()),    #显示购物车商品
]