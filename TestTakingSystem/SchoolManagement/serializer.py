from rest_framework.serializers import ModelSerializer 
from SchoolManagement.models import ImageTest

class ImageSerializer(ModelSerializer):
    class Meta:
        model = ImageTest
        fields = [
            'image'
        ]