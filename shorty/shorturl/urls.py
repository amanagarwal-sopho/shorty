from django.conf.urls import url
from shorturl import views


urlpatterns = [
        url(r'^(?P<code>[A-Za-z0-9]{8})/$',views.redirect_url,name='redirect_url'),
        url(r'^$',views.index,name='index'),   
]
