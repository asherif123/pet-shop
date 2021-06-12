from pets.models import Pet, PetType, PetBreed, Order
from rest_framework import serializers, validators


class OrderSerializer(serializers.ModelSerializer):
    def validate_pets(self, value):
        """
        Raises validation error if any of the pet ids provided was sold before.
        """
        pets_ids = [pet.id for pet in value]
        sold_pets = Pet.objects.filter(pk__in=pets_ids, order__isnull=False)
        if sold_pets:
            raise serializers.ValidationError(
                'one or more of the provided pets were already sold.')
        return value


    class Meta:
        model = Order
        fields = ['id', 'price', 'currency', 'pets']
        

class PetSerializer(serializers.ModelSerializer):
    # to send pet type name instead of id in the requests
    type = serializers.SlugRelatedField(
                            slug_field='name', 
                            error_messages={
                                'does_not_exist': 'Pet type does not exist.',
                            },
                            queryset=PetType.objects.all())

    # to send pet breed name instead of id in the requests
    breed = serializers.SlugRelatedField(
                            slug_field='name', 
                            error_messages={
                                'does_not_exist': 'Pet breed does not exist.',
                            },
                            queryset=PetBreed.objects.all())

    order = serializers.PrimaryKeyRelatedField(
                            allow_null=True, 
                            required=False, 
                            queryset=Order.objects.all())

    class Meta:
        model = Pet
        fields = ['id', 'name', 'birthdate', 'type', 'breed', 'order']