
from django.conf.urls import url
from userapp import views

urlpatterns=[
    url(r'^register/$',views.RegisterView.as_view()),   #注册
    url(r'^checkUname/$',views.CheckUnameView.as_view()), #判断数据据是否有这个用户
    url(r'^center/$',views.CenterView.as_view()),      #用户个人信息
    url(r'^logout/$',views.LogoutView.as_view()),      #退出
    url(r'^login/$',views.LoginView.as_view()),      #登录
    url(r'^loadCode.jpg$',views.LoadCodeView.as_view()),      #
    url(r'^checkcode/$',views.CheckcodeView.as_view()),      #验证码验证
    url(r'^address/$',views.AddressView.as_view()),      #地址管理界面
    url(r'^loadArea/$',views.LoadAreaView.as_view()),      #地址三级联动
]
