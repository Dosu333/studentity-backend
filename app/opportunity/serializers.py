from django.contrib.auth import get_user_model
from rest_framework import serializers
from datetime import datetime
from .models import Opportunity

class OpportunitySerializer(serializers.ModelSerializer):
    """Serializer for Opportunity model"""
    class Meta:
        model = Opportunity
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        created_at = datetime.strptime(representation['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ")
        deadline = datetime.strptime(representation['deadline'], "%Y-%m-%dT%H:%M:%SZ")
        representation['author'] = get_user_model().objects.get(id=str(representation['author'])).company
        representation['created_at'] = created_at.strftime("%B %d, %Y")
        representation['deadline'] = deadline.strftime("%B %d, %Y")

        return representation


        