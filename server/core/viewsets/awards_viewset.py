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
    ceremony_queryset = Ceremony.objects.all()
    ceremony_serializer = CeremonySerializer
    nominee_queryset = Nominee.objects.all()
    nominee_serializer = NomineeSerializer
    lookup_field = 'name'

    def list(self, request):
        params = request.query_params
        if 'major' in params and 'minor' in params:
            queryset = self.get_queryset().filter(major_category__name_en=params['major'], minor_category__name_en=params['minor'])
        elif 'major' in params:
            queryset = self.get_queryset().filter(major_category__name_en=params['major'])
        else:
            queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, url_path=r'ceremonies')
    def list_ceremony(self, request, name):
        queryset = self.ceremony_queryset.filter(awards__name=name)
        serializer = self.ceremony_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, url_path=r'ceremonies/(?P<ceremony_index>[^/.]+)')
    def detail_ceremony(self, request, name, ceremony_index):
        queryset = self.ceremony_queryset.filter(awards__name=name, index=ceremony_index)
        serializer = self.ceremony_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, url_path=r'ceremonies/(?P<ceremony_index>[^/.]+)/nominees')
    def list_ceremony_nominees(self, request, name, ceremony_index):
        ceremony = self.ceremony_queryset.filter(awards__name = name, index=ceremony_index)
        ceremony_id = ceremony.values_list('id', flat=True)
        queryset = self.nominee_queryset.filter(ceremony=ceremony_id[0])
        serializer = self.nominee_serializer(queryset, many=True)
        return Response(serializer.data)