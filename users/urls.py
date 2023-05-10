from django.urls import path
from users import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('update/', views.Update.as_view(), name='update'),
    path('detail/', views.Detail.as_view(), name='detail'),
    path('delete/', views.Delete.as_view(), name='delete'),
    path('findpassword/', views.FindPassword.as_view(), name='findpassword'),
    path('changepassword/', views.ChangePassword.as_view(), name='changepassword'),
    path('list/', views.List.as_view(), name='list'),
]
