from base.views import user_views as views
from django.urls import path

urlpatterns = [
  path('', views.getUsers),
  path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('register/', views.registerUser, name='register'), 
  path('profile/' ,views.getUserProfile,name='user-profile'),
  path('profile/update/', views.updateUserProfile, name='user-profile-update'),
  path('<str:pk>/', views.getUserById, name='user'),
  path('update/<str:pk>/', views.updateUser, name='user-update'),
  path('delete/<str:pk>/', views.deleteUser, name='user-delete')
]
