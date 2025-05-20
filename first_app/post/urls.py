from django.urls import path
from .views import PostList, PostDetail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    

]
