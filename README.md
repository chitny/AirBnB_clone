# Welcome to # 0x00. AirBnB clone - The console (part 1)

![enter image description here](https://github.com/chitny/AirBnB_clone/blob/main/images/logo.png?raw=true)

# Description of the project

This is the first step of four towards building ourfirst full web application: the **AirBnB clone**.

The objetives of this project are

- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of our future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

![enter image description here](https://github.com/chitny/AirBnB_clone/blob/main/images/esquema.png?raw=true)

# Description of the command interpreter:

### What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### How to start it

If you want to try the console, just type
`./console.py`
Output: prompt: `(hbnb) `

### How to use it

Some usefull commands:
`help` - show the commands of the console, type `help <command>` to specific details from any command.
`all` - Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel` or `$ all`
`count` - Count instances (developing future feature)
`create` - Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel`
`destroy` - Deletes an instance based on the class name and `id` (save the change into the JSON file). Ex: `$ destroy BaseModel 1234-1234-1234`.
`quit` - Exit the console
`show` - Prints the string representation of an instance based on the class name and `id`. Ex: `$ show BaseModel 1234-1234-1234`
`update` - Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"`.
`triforce` - Isn't Zelda the best video games saga?

### Examples

Example of using the console and some of its commands

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
```

# Files

In this moment there are three important files, console.py, base_model.py and file_storage.py.
This files are the project per se. [console.py](https://github.com/chitny/AirBnB_clone/blob/main/console.py) got everything about the console, all the functions and commands to use the Console. [base_model.py](https://github.com/chitny/AirBnB_clone/blob/main/models/base_model.py) is the brain with the mother class BaseModel for all the other classes of the project. [storage.py](https://github.com/chitny/AirBnB_clone/blob/main/models/engine/file_storage.py) got all the functions to work with JSON and dictionaries.

| Directory                      | File                                                                                                                        | Description                                                                                              |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
|                                | [AUTHORS](https://github.com/chitny/AirBnB_clone/blob/main/AUTHORS)                                                         | File containing the Authors of this project                                                              |
|                                | [README.md](https://github.com/chitny/AirBnB_clone/blob/main/README.md)                                                     | This file                                                                                                |
|                                | [console.py](https://github.com/chitny/AirBnB_clone/blob/main/console.py)                                                   | All the console functions                                                                                |
| /images                        | [esquema.png](https://github.com/chitny/AirBnB_clone/blob/main/images/esquema.png)                                          | Image for README.md                                                                                      |
| /images                        | [logo.png](https://github.com/chitny/AirBnB_clone/blob/main/images/logo.png)                                                | Logo image                                                                                               |
| /models                        | [**init**.py](https://github.com/chitny/AirBnB_clone/blob/main/models/__init__.py)                                          | init file                                                                                                |
| /models                        | [amenity.py](https://github.com/chitny/AirBnB_clone/blob/main/models/amenity.py)                                            | Amenity Class File                                                                                       |
| /models                        | [base_model.py](https://github.com/chitny/AirBnB_clone/blob/main/models/base_model.py)                                      | BaseModel Class File, the brain of this project                                                          |
| /models                        | [city.py](https://github.com/chitny/AirBnB_clone/blob/main/models/city.py)                                                  | City Class File                                                                                          |
| /models                        | [place.py](https://github.com/chitny/AirBnB_clone/blob/main/models/place.py)                                                | Place Class File                                                                                         |
| /models                        | [review.py](https://github.com/chitny/AirBnB_clone/blob/main/models/review.py)                                              | Review Class File                                                                                        |
| /models                        | [state.py](https://github.com/chitny/AirBnB_clone/blob/main/models/state.py)                                                | State Class File                                                                                         |
| /models                        | [user.py](https://github.com/chitny/AirBnB_clone/blob/main/models/user.py)                                                  | User Class File                                                                                          |
| /models/engine                 | [**init**.py](https://github.com/chitny/AirBnB_clone/blob/main/models/engine/__init__.py)                                   | init file                                                                                                |
| /models/engine                 | [file_storage.py](https://github.com/chitny/AirBnB_clone/blob/main/models/engine/file_storage.py)                           | file with all the functions to serialize and deserialize data, save to JSON file and load from JSON file |
| /tests                         | [**init**.py](https://github.com/chitny/AirBnB_clone/blob/main/tests/__init__.py)                                           | init file                                                                                                |
| /tests                         | [test_console.py](https://github.com/chitny/AirBnB_clone/blob/main/tests/test_console.py)                                   | file with unittest to console                                                                            |
| /tests/test_models             | [**init**.py](https://github.com/chitny/AirBnB_clone/blob/main/tests/test_models/__init__.py)                               | init file                                                                                                |
| /tests/test_models             | [test_amenity.py](https://github.com/chitny/AirBnB_clone/blob/main/tests/test_models/test_amenity.py)                       | file with unittest                                                                                       |
| /tests/test_models             | [test_base_model.py](https://github.com/chitny/AirBnB_clone/blob/main/tests/test_models/test_base_model.py)                 | file with unittest                                                                                       |
| /tests/test_models             | [test_city.py](https://github.com/chitny/AirBnB_clone/blob/main/tests/test_models/test_city.py)                             | file with unittest                                                                                       |
| /tests/test_models             | [test_place.py](https://github.com/chitny/AirBnB_clone/blob/main/tests/test_models/test_place.py)                           | file with unittest                                                                                       |
| /tests/test_models             | [test_review.py](https://github.com/chitny/AirBnB_clone/blob/main/tests/test_models/test_review.py)                         | file with unittest                                                                                       |
| /tests/test_models             | [test_state.py](https://github.com/chitny/AirBnB_clone/blob/main/tests/test_models/test_state.py)                           | file with unittest                                                                                       |
| /tests/test_models             | [test_user.py](https://github.com/chitny/AirBnB_clone/blob/main/tests/test_models/test_user.py)                             | file with unittest                                                                                       |
| /tests/test_models/test_engine | [**init**.py](https://github.com/chitny/AirBnB_clone/blob/main/tests/test_models/test_engine/__init__.py)                   | init file                                                                                                |
| /tests/test_models/test_engine | [test_file_storage.py](https://github.com/chitny/AirBnB_clone/blob/main/tests/test_models/test_engine/test_file_storage.py) | file with unittest                                                                                       |

## Bugs

At this moment we had some bugs with the console.

## Author

For the first step of this project i worked alone.
Ignacio Chitnisky - C14 - Holberton Uruguay - 2771@holbertonschool.com - [https://github.com/chitny](https://github.com/chitny)
