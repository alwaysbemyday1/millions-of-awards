from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import AwardsInfo, Awards, Nominee
from core.serializers.awardsinfo_serializer import AwardsInfoSerializer
from core.serializers.awards_serializer import AwardsSerializer
from core.serializers.nominee_serializer import NomineeSerializer

class AwardsInfoViewSet(ModelViewSet):
    queryset = AwardsInfo.objects.all()
    serializer_class = AwardsInfoSerializer
    awards_queryset = Awards.objects.all()
    awards_serializer = AwardsSerializer
    nominee_queryset = Nominee.objects.all()
    nominee_serializer = NomineeSerializer
    lookup_field = 'name'

    @action(methods=['get'], detail=True, url_path=r'(?P<ceremony>[^/.]+)')
    def several_awards(self, request, name, ceremony):
        queryset = self.awards_queryset.filter(awards_info__name=name, ceremony=ceremony)
        serializer = self.awards_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, url_path=r'(?P<ceremony>[^/.]+)/nominees')
    def several_awards_nominees(self, request, name, ceremony):
        awards = self.awards_queryset.filter(awards_info__name = name, ceremony=ceremony)
        awards_id = awards.values_list('id', flat=True)
        queryset = self.nominee_queryset.filter(awards=awards_id[0])
        serializer = self.nominee_serializer(queryset, many=True)
        return Response(serializer.data)