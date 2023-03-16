from rest_framework.viewsets import ModelViewSet

from core.models import MajorCategory, MinorCategory
from core.serializers.category_serializer import MajorCategorySerializer, MinorCategorySerializer

class MajorCategoryViewSet(ModelViewSet):
    queryset = MajorCategory.objects.all()
    serializer_class = MajorCategorySerializer

class MinorCategoryViewSet(ModelViewSet):
    queryset = MinorCategory.objects.all()
    serializer_class = MinorCategorySerializer