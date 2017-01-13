from django.conf.urls import url
from . import views

urlpatterns = [
#As you can see, we're now assigning a view called post_list to the ^$ URL
    url(r'^$', views.post_list, name='post_list'),
]
