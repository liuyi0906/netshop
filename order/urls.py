
from django.conf.urls import url
from order import views

urlpatterns=[
    url(r'^$',views.ToOrderView.as_view()),
    url(r'^order.html$',views.OrderView.as_view()),
]