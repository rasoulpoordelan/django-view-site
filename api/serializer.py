from rest_framework import  serializers
from .models import TrainInfo,Image,Prop


class ImageSerializer(serializers.ModelSerializer):
    address=serializers.ReadOnlyField(default='http://localhost:80/test')
    class Meta:
        model = Image
        fields = ['name','image','address']
    
class PropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prop
        fields = ['name']


class TrainInfoSerializer(serializers.ModelSerializer):
        
    images=ImageSerializer(many=True,source='image_set')
    props=PropSerializer(many=True)
    
    class Meta:
        model = TrainInfo
        fields = ['train_num', 'name','images','props']
