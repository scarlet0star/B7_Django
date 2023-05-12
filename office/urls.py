from django.urls import path, include
from .views import *
urlpatterns = [
    path("views", ProductView.as_view()),
    path("writingcounts", UserWriteCount.as_view()),
    path("counts", ProductCountView.as_view()),
    path("category", CategoryProductCountAPIView.as_view()),
    path("transaction", TransactionStatusCountAPIView.as_view()),
    path("admin/<int:pk>", ToggleIsAdmin.as_view(), name="admin"),
    path("active/<int:pk>", ToggleUserIsActive.as_view(), name="active"),

]
