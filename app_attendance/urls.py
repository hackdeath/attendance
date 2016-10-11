from django.conf.urls import url
from .                import views

app_name = 'app_attendance'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
