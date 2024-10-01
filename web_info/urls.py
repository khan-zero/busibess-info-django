from django.urls import path, include
from .views import index, about, service, why, team

urlpatterns = [
    path('', index, name = 'index'),
    path('about/', about, name = 'about'),
    path('service/', service, name = 'service'),
    path('why/', why, name = 'why'),
    path('team/', team, name = 'team'),    
    path('login/', index, name='login'),
    path('register/', index, name='register'),
    
]
