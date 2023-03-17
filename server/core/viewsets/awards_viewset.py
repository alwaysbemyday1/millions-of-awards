from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Awards, Ceremony, Nominee
from core.serializers.awards_serializer import AwardsSerializer
from core.serializers.ceremony_serializer import CeremonySerializer
from core.serializers.nominee_serializer import NomineeSerializer

class AwardsViewSet(ModelViewSet):
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer
    awards_queryset = Ceremony.objects.all()
    ceremony_serializer = CeremonySerializer
    nominee_queryset = Nominee.objects.all()
    nominee_serializer = NomineeSerializer
    lookup_field = 'name'

    def list(self, request):
        params = request.query_params
        if 'major' in params and 'minor' in params:
            queryset = self.get_queryset().filter(major_category__name_en=params['major'], minor_cateogry__name_en=params['minor'])
        elif 'major' in params:
            queryset = self.get_queryset().filter(major_category__name_en=params['major'])
        else:
            queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, url_path=r'(?P<ceremony_index>[^/.]+)')
    def several_awards(self, request, name, ceremony_index):
        queryset = self.awards_queryset.filter(awards__name=name, index=ceremony_index)
        serializer = self.ceremony_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, url_path=r'(?P<ceremony_index>[^/.]+)/nominees')
    def several_awards_nominees(self, request, name, ceremony_index):
        awards = self.awards_queryset.filter(awards__name = name, index=ceremony_index)
        awards_id = awards.values_list('id', flat=True)
        queryset = self.nominee_queryset.filter(awards=awards_id[0])
        serializer = self.nominee_serializer(queryset, many=True)
        return Response(serializer.data)