from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from rest_framework.routers import DefaultRouter

from core.views import BookViewSet, JournalViewSet, RegisterViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'journals', JournalViewSet, basename='journals')
router.register(r'register', RegisterViewSet, basename='register')
urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('core/', include('core.urls')),

    path('auth/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(urlpatterns))
]

