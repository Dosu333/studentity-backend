from rest_framework import viewsets, status
from .models import Opportunity
from .serializers import OpportunitySerializer

class OpportunityViewsets(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    http_method_names = ['get', ]