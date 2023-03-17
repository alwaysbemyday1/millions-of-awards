from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.viewsets.category_viewset import MajorCategoryViewSet
from core.viewsets.awards_viewset import AwardsViewSet

router = DefaultRouter()

router.register('category', MajorCategoryViewSet)
router.register('awards', AwardsViewSet)

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include(router.urls)),
]