from django.urls import path
from . import views

urlpatterns = [
    path('pools/', views.pool_list, name='pool-list'),
    path('pools/<int:pk>/', views.pool_detail, name='pool-detail'),
    path('billiards/', views.billiard_list, name='billiard-list'),
    path('billiards/<int:pk>/', views.billiard_detail, name='billiard-detail'),
    path('saunas/', views.sauna_list, name='sauna-list'),
    path('saunas/<int:pk>/', views.sauna_detail, name='sauna-detail'),
    path('trainings/', views.training_list, name='training-list'),
    path('trainings/<int:pk>/', views.training_detail, name='training-detail'),
    path('orders/', views.order_list, name='order-list'),
    path('orders/<int:pk>/', views.order_detail, name='order-detail'),
    path('subscription_list/', views.subscription_list, name='subscription_list'),
    path('subscription_detail/<int:pk>/', views.subscription_detail, name='subscription_detail'),
    path('notifications/', views.notification_list, name='notification_list'),
]
