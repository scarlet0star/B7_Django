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
    path('findpassword/', views.Find.as_view(), name='findpassword'),
    path('changepassword/', views.Change.as_view(), name='changepassword'),
    path('list/', views.List.as_view(), name='list'),
]

# 로그인
# 로그아웃
# 회원가입
# 회원정보 수정
# 회원상세정보
# 회원탈퇴
# 비밀번호 찾기
# 비밀번호 변경
# 회원목록