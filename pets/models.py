from django.db import models


class PetType(models.Model):
    """
    Stores the types of pets, i.e: dogs, cats etc.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class PetBreed(models.Model):
    """
    Stores the pets breeds, i.e: persian cat, german shepherd
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # let's just say that we will accept any currency
    # as I do not know the currency requirements
    currency = models.CharField(max_length=50)

class Pet(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    type = models.ForeignKey(PetType, on_delete=models.CASCADE)
    breed = models.ForeignKey(PetBreed, on_delete=models.CASCADE)

    # when order is deleted, the related pets gets deleted as 
    # am not sure what does order deletion mean
    # it could mean refund? in that case we should just set pet's order to null
    order = models.ForeignKey(
                        Order, 
                        null=True, 
                        related_name='pets', 
                        on_delete=models.CASCADE)

    def __str__(self):
        return '{0} is a {1}, {2}'.format(self.name, \
            self.breed, self.type)

