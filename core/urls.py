from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from accounts.views import AccountsViewSet, TransactionsViewSet
from users.views import UsersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'accounts', AccountsViewSet)
router.register(r'users', UsersViewSet)
router.register(r'transactions',TransactionsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
