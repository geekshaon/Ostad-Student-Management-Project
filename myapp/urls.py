from django.urls import path
from . import views
urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.homeCV.as_view(), name='home'),
    # path('add/', views.add, name='add'),
    path('add/', views.addCV.as_view(), name='add'),
    # path('update/<int:id>/', views.update, name='update'),
    path('update/<int:id>/', views.UpdateCV.as_view(), name='update'),
    # path('delete/<int:id>/', views.delete, name='delete'),
    path('delete/<int:id>/', views.DeleteCV.as_view(), name='delete'),

]


