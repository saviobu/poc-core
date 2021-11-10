from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from accounts.viewsets import AccountsViewSet
from users.viewsets import UsersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'accounts', AccountsViewSet)
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
    # path('users/', include('users.urls')),
    # path('accounts/', include('accounts.urls'))
]
