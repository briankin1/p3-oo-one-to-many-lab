class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

        # If the owner is provided, we add the pet to the owner's list
        if owner:
            owner.add_pet(self)  # Ensure the pet is added to the owner

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Private list of pets for this owner

    def pets(self):
        return self._pets  # Return the list of pets for this owner

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        if pet not in self._pets:
            self._pets.append(pet)  # Add pet to the owner's list if it's not already there
            pet.owner = self  # Set the pet's owner

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)  # Sort pets by their name
