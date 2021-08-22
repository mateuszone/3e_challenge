from django.contrib import admin
from django.urls import path
from API.views import UsersViewSet

users_add = UsersViewSet.as_view({
    'post': 'create'
})
users_list = UsersViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/add/', users_add),
    path('users/', users_list)
]

