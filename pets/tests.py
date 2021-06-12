from rest_framework import status
from rest_framework.test import APITestCase
from pets.models import Pet, Order, PetType, PetBreed


class PetTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Pet.objects.create(
                        name='Max', 
                        birthdate="2021-06-12",
                        type=PetType.objects.filter(name='Dog').first(),
                        breed=PetBreed.objects.filter(name='German Shepherd').first())
        Pet.objects.create(
                        name='Roy', 
                        birthdate="2021-06-12",
                        type=PetType.objects.filter(name='Dog').first(),
                        breed=PetBreed.objects.filter(name='Bulldog').first())

    @staticmethod
    def create_pet():
        pet = Pet.objects.create(
                            name='Rex', 
                            birthdate="2021-06-12",
                            type=PetType.objects.filter(name='Dog').first(),
                            breed=PetBreed.objects.filter(name='Bulldog').first())
        return pet

    @staticmethod
    def create_order():
        order = Order.objects.create(price='567.8', currency="USD")
        return order

    def test_get_all_pets(self):
        """
        Ensures that we can get all pets.
        """
        url = '/pets/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Max')

    def test_get_single_pet(self):
        """
        Ensures that we can get a single pet.
        """
        url = '/pets/2'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Roy')

    def test_delete_single_pet(self):
        """
        Ensures that we can delete a single pet.
        """
        pet = self.create_pet()
        pet_id = pet.id
        url = f'/pets/{pet_id}'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_pet(self):
        """
        Ensures that we can create pets.
        """
        url = '/pets/'
        data = {
            "name": "Rex",
            "birthdate": "2021-06-12",
            "type": "Dog",
            "breed": "German Shepherd"
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_order(self):
        """
        Ensures that we can order pets.
        """
        url = '/orders/'
        data = {
            "price": "1231.4",
            "currency": "EGP",
            "pets": [1,2]
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cant_order_pets_sold_before(self):
        """
        Ensures that we can not order pets that were already sold.
        """
        # create 2 pets and get their ids
        pets = [self.create_pet(), self.create_pet()]
        # order these pets
        order = self.create_order()
        order.pets.set(pets)

        pet_ids = [pet.id for pet in pets]
        url = '/orders/'
        data = {
            "price": "1231.4",
            "currency": "EGP",
            "pets": pet_ids
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_pet_repr(self):
        """
        Ensures that we can print pet properly.
        """
        pet = self.create_pet()
        self.assertEqual(str(pet), 'Rex is a Bulldog, Dog')

    def test_pet_type_repr(self):
        """
        Ensures that we can print pet type properly.
        """
        pet_type = PetType.objects.filter(name='Dog').first()
        self.assertEqual(str(pet_type), 'Dog')

    def test_pet_breed_repr(self):
        """
        Ensures that we can print pet breed properly.
        """
        pet_breed = PetBreed.objects.filter(name='Bulldog').first()
        self.assertEqual(str(pet_breed), 'Bulldog')