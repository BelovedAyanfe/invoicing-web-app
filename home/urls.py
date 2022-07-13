from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('select', views.select, name='select'),
    path('address', views.address, name='address'),
    path('logout', views.logout, name='logout'),
    path('list', views.list, name='show-invoices'),
    path('create-pdf', views.pdf_report_create, name='create-pdf'),
    path('show', views.mmdv, name='mmdv'),
]