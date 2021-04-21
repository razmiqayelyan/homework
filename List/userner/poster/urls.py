from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   path('snippet_detail', snippet_detail),
   path('', usblog, name='usblog'),
   path('user_posts/<username>/', userpage, name='userpage'),
   path('profile/<username>/', profile, name='profile'),
   path('profile/<username>/<int:pk>', PostDetailView.as_view(), name='detail'),
   path('profile/<username>/<int:pk>/update', PostUpdateView.as_view(), name='update'),
   path('profile/<username>/<int:pk>/delete', PostDeleteView.as_view(), name='delete'),

]