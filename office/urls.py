from django.urls import path, include
from .views import *
urlpatterns = [
    path("views", ProductView.as_view()),
    path("counts", ProductCountView.as_view()),
    path("category", CategoryProductCountAPIView.as_view()),
    path("transaction", TransactionStatusCountAPIView.as_view()),
    path("admin", GiveAdmin.as_view()),
    path("active", ToggleUserIsActive.as_view()),
]
