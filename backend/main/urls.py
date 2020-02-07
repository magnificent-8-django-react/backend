from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user import views as user_views
from restaurant import views as restaurant_views
from account import views as account_views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()

router.register(r'users', account_views.UserViewSet)
router.register(r'groups', account_views.GroupViewSet)
router.register(r'user/profiles', user_views.UserProfileViewSet)
router.register(r'user/favorites', user_views.FavoriteViewSet)
router.register(r'restaurant/profiles', restaurant_views.RestaurantTruckViewSet)
router.register(r'restaurant/reviews', restaurant_views.ReviewViewSet)
router.register(r'restaurant/menu', restaurant_views.MenuViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/', include('account.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)