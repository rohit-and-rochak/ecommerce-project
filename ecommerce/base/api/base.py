from rest_framework.serializers import ModelSerializer


class BaseSerializer(ModelSerializer):
    """ BaseSerializer to be extended by other Serializers """

    def drop_fields(self, validated_data):
        fields = ('id', 'created_at')
        for field in fields:
            validated_data.pop(field, None)

        return validated_data

    def create(self, validated_data):
        validated_data = self.drop_fields(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = self.drop_fields(validated_data)
        return super().update(instance, validated_data)
