from .models import Appeal
from rest_framework.serializers import ModelSerializer

class AppealModelSerializer(ModelSerializer):
    class Meta:
        model = Appeal
        fields = '__all__'
        