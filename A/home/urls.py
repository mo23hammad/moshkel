from django.urls import path
from . import views

urlpatterns = [
    path('',views.khooneh,name='home'),
    path('contact/', views.contact,name='contact' ),
    path('detail/<Person_id>',views.detail,name='detail'),
    path('delete/<Person_id>',views.delete, name='delete')
]