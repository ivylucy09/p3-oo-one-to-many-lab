class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet, owner=None):
         self.name = name
         self.pet_type = pet
         self.owner = owner
         Pet.all.append(self)
         if self.pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {self.pet_type}. Must be one of {Pet.PET_TYPES}.")
         

    def __repr__(self):
        return f"Pet(name={self.name}, pet_type={self.pet_type}, owner={self.owner})"

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("The pet must be an instance of the Pet class.")
        pet.owner = self 

    def get_sorted_pets(self):
        owned_pets = self.pets()
        return sorted(owned_pets, key=lambda pet: pet.name)
