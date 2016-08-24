from django.conf.urls import url
from .                import views

app_name = 'app_attendance'
urlpatterns = [
    url(r'^$',        			views.index,   				name='index'			),
    url(r'^display_per_month/', views.display_per_month, 	name='display_per_month'),
    url(r'^display_per_day/', 	views.display_per_day, 		name='display_per_day'	),
]
