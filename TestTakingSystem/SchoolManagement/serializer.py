from rest_framework.serializers import ModelSerializer 


class ImageSerializer(ModelSerializer):
    class Meta:
        model = ImageTest
        fields = [
            'image'
        ]