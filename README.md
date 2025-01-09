# AirBnB Clone

Welcome to the **AirBnB Clone** project! This project is a simplified version of the popular AirBnB website. The aim is to build a fully functional web application by the end of the year. This application will cover fundamental concepts of higher-level programming and web development.

## Overview
The project will be developed incrementally and will include the following components:

1. **Command Interpreter**
   - Manipulate data without a visual interface (e.g., Shell-like functionality).
   - Ideal for development and debugging.

2. **Website (Front-End)**
   - Static and dynamic web pages.
   - Showcases the final product to users.

3. **Storage System**
   - Use either file-based storage (JSON) or database storage (MySQL).

4. **API**
   - Provides communication between the front-end and the back-end.
   - Supports operations like Create, Read, Update, and Delete (CRUD).

## Features
- **Command Interpreter**:
  - Create, update, and destroy objects.
  - Manage data using a JSON-based storage system.

- **Web Static**:
  - HTML/CSS-based design for the front-end.

- **MySQL Database**:
  - Use Object Relational Mapping (ORM) to manage data storage.

- **Web Framework**:
  - Create dynamic web pages using templating techniques.

- **RESTful API**:
  - Expose data via JSON web interfaces.
  - Enable client-side interaction with the back-end.

- **Web Dynamic**:
  - Load objects dynamically on the client-side using jQuery.

## Directory Structure
```
AirBnB_clone/
├── models/
│   ├── base_model.py
│   ├── engine/
│   │   └── file_storage.py
├── tests/
│   └── test_models.py
├── console.py
├── web_static/
│   ├── css/
│   ├── images/
│   ├── js/
│   └── html/
```

- **models/**: Contains all the models (classes) used in the project.
  - `base_model.py`: Base class for all models with common attributes and methods.
  - `engine/`: Contains storage classes like `file_storage.py`.

- **tests/**: Unit tests for all project components.

- **console.py**: Command interpreter entry point.

- **web_static/**: Front-end static assets (HTML, CSS, images, etc.).

## Concepts
### 1. Serialization/Deserialization
Convert instances into serializable data structures (e.g., dictionaries) for storage in JSON format. Example:

```python
# Serialization
my_instance.to_json()

# Deserialization
my_instance = MyClass(my_dict)
```

### 2. *args and **kwargs
- `*args`: Used for passing a variable number of arguments to a function.
- `**kwargs`: Used for passing a variable number of keyword arguments to a function.

Example:
```python
def my_function(*args, **kwargs):
    print(args)
    print(kwargs)

my_function(1, 2, name="AirBnB", version=1.0)
```

### 3. datetime Module
Used to manipulate date and time objects.
```python
from datetime import datetime, timedelta

# Current time
date_now = datetime.now()

# Add one day
date_tomorrow = date_now + timedelta(days=1)
```

## Project Steps
1. **Console**
   - Develop a command interpreter to manage objects and their persistence.
   - Store objects in a JSON file.

2. **Web Static**
   - Build static HTML and CSS templates for the front-end.

3. **MySQL Storage**
   - Replace file storage with a MySQL database.
   - Use ORM for database interactions.

4. **Web Framework**
   - Create a Python-based web server.
   - Dynamically render HTML templates using stored objects.

5. **RESTful API**
   - Expose stored data via a RESTful API.
   - Support CRUD operations using JSON.

6. **Web Dynamic**
   - Use jQuery to load objects dynamically from the API.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/AirBnB_clone.git
   cd AirBnB_clone
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the command interpreter:
   ```bash
   ./console.py
   ```

## Usage
- Start the command interpreter:
  ```bash
  ./console.py
  ```

- Example commands:
  ```
  (hbnb) create User name="John Doe" age=30
  (hbnb) show User 123-abc-456
  (hbnb) destroy User 123-abc-456
  (hbnb) quit
  ```

## Testing
Run the test suite using:
```bash
python3 -m unittest discover tests
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributors
- [Precious Chibundu Mozia](https://github.com/Kodedbykenzie)
- [Glory Paul](https://github.com/Glorycodess)
![HBNB Logo](hbnb_logo.png)
