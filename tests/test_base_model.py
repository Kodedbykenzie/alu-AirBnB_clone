# test_base_model.py
from models.base_model import BaseModel

# Create an instance of BaseModel
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)  # Should display the string representation with the id and attributes

# Save the instance (update the updated_at)
my_model.save()
print(my_model)  # Should display the updated time in updated_at

# Convert to dictionary format and print
my_model_json = my_model.to_dict()
print(my_model_json)

# Print key-value pairs of the dictionary representation
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

