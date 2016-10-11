from django.conf.urls import url 
from .views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^about-us/$', about, name="about"),
    url(r'^about-us/teams/$', Teams_view, name="Teams_view"),
    url(r'^news/$', news, name="news"),
    url(r'^news-single/([a-z0-9-]+)/$', news_single, name="news_single"),
    url(r'^test/$', test, name="test"),
    url(r'^collections/$', Collections, name="collections"),
    url(r'^service-drawing-project/$', Draw_prroject, name='service_drawing_project'),
    url(r'^product-delivery/$', Product_delivery, name='product_delivery'),
    url(r'^references/$', Reference, name='reference'),
    url(r'^reference/(.+?)/$', Collection_menu, name='reference_new'),
    url(r'^contact/$', contact, name="contact"),

]
