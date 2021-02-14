from django.urls import path
from .views import DataDiriView,DataDiriDetailView,UserView,UserDetailView

urlpatterns = [
    path('', DataDiriView.as_view(), name='data'),
    path('user/', UserView.as_view(), name='user'),
    path('<int:pk>', DataDiriDetailView.as_view(), name='data-detail'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user-detail')
]