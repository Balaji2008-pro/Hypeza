from rest_framework import serializers  # module in drf inside the classe are serializers.serializer
# serializers.seralizer is a class in drf.
from api.models import User
from  api.models import Profilemodel
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profilemodel
        fields = '__all__'

class Postserializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'post', 'user_id']

# class Followserializer(serializers.ModelSerializer):
#     class Meta:
#         model = Follow
#         fields = '__all__'
