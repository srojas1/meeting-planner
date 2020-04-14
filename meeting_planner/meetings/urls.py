from django.urls import path

from .views import detail, rooms_list, new

urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('rooms', rooms_list, name='rooms'),
    path('new', new, name='new')
]