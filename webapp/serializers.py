from rest_framework import serializers
from rest_framework import employee

class employeeSerializers(serializers.ModelSerializerd):

    class Meta:
        model = employee
        fields = "__all__"
