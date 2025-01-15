import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Handles serialization and deserialization of objects"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Adds an object to __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                try:
                    obj_dict = json.load(f)  # Attempt to load the data
                except json.JSONDecodeError:
                    print("Warning: The file is empty or corrupted, initializing with an empty dictionary.")
                    obj_dict = {}  # Handle the error by assigning an empty dictionary

                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    # Instead of using eval(), check class names explicitly
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    elif class_name == "User":
                        self.__objects[key] = User(**value)
                    elif class_name == "Place":
                        self.__objects[key] = Place(**value)
                    elif class_name == "State":
                        self.__objects[key] = State(**value)
                    elif class_name == "City":
                        self.__objects[key] = City(**value)
                    elif class_name == "Amenity":
                        self.__objects[key] = Amenity(**value)
                    elif class_name == "Review":
                        self.__objects[key] = Review(**value)
                    else:
                        print(f"Warning: Unrecognized class name {class_name} found in data.")
        except FileNotFoundError:
            print(f"File {self.__file_path} not found. Initializing with an empty dictionary.")
            pass  # If the file doesn't exist, it will continue without crashing

