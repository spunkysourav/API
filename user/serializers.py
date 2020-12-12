from rest_framework import serializers
from.models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields=("id", "college_name", "branch", "address", "mobile_no")
        model=User