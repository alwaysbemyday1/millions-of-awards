from rest_framework.viewsets import ModelViewSet

from core.models import AwardsInfo
from core.serializers.awardsinfo_serializer import AwardsInfoSerializer

class AwardsInfoViewSet(ModelViewSet):
    queryset = AwardsInfo.objects.all()
    serializer_class = AwardsInfoSerializer