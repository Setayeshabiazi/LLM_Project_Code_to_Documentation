# TA-Scheduling-Application-main Cleaned Repo Documentation

## main  
``/Project/manage.py``  
```def main():
                                   
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)```  

**Documentation:**
```python## Overview
This code serves as the entry point for running a Django application, setting up the necessary environment and executing the command line interface.

## Interface
- **Signature**: `def main()`
- **Parameters**:
  | Name   | Type       | Purpose                         |
  |--------|------------|-----------------------------------|
  |        |            | No parameters accepted.           |

## Inner Workings
1. The function sets the default Django settings module to `'Project.settings'` using `os.environ.setdefault`.
2. It attempts to import `execute_from_command_line` from `django.core.management`. If this fails, it raises an ImportError with a detailed message indicating that Django might not be installed or correctly configured.
3. If the import is successful, `execute_from_command_line` is called with `sys.argv` as its argument, which processes the command line arguments and executes the corresponding Django management command.

## Edge Cases & Preconditions
- The function assumes that Django is properly installed and accessible on the PYTHONPATH.
- If Django is not found, it raises an ImportError with a specific message. This error can be handled by ensuring Django is installed and correctly configured in the environment.

## Result Synopsis
The function initializes the Django settings and executes a command line interface command based on the arguments provided in `sys.argv`.

## Docstring Draft
```python
"""Initializes Django settings and executes a management command from sys.argv.

Args:
    None

Returns:
    None

Raises:
    ImportError: If Django cannot be imported, indicating it's not installed or incorrectly configured.
"""
``````

## User  
``/Project/project_app/models.py``  
```class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    user_type = models.CharField(max_length=10)```  

**Documentation:**
```python## Overview
- This code defines a Django model for a `User` entity, representing typical attributes and data types associated with a user.

## Interface
- **Signature**: class User(models.Model)
- **Parameters**:
  | Name     | Type                | Purpose                          |
  |----------|---------------------|----------------------------------|
  | username | models.CharField    | Unique identifier for the user.  |
  | password | models.CharField    | Password of the user.            |
  | name     | models.CharField    | Full name of the user.           |
  | email    | models.EmailField   | Email address of the user.       |
  | phone    | models.CharField    | Contact phone number of the user.|
  | address  | models.CharField    | Address of the user.             |
  | user_type| models.CharField    | Type or role of the user.        |

## Inner Workings
- The `User` class is a subclass of `models.Model`, which is provided by Django to facilitate database management.
- Each attribute in the `User` model corresponds to a field in the database table.
- The `username`, `password`, and `name` fields are defined as `CharField`, meaning they store textual data with specific maximum lengths.
- The `email` field is defined as an `EmailField`, which ensures that the stored data is a valid email address.
- The `phone` and `address` fields are also `CharField` instances, suitable for storing strings of up to their specified maximum lengths.
- The `user_type` field indicates the type or role of the user, such as 'admin' or 'customer'.

## Edge Cases & Preconditions
- The `username`, `password`, `name`, and `email` fields have specific length restrictions. Ensure that data provided adheres to these limits.
- The `email` field must contain a valid email address format.
- Django's model system will automatically handle validation of the data according to the specified field types and constraints.

## Result Synopsis
- The `User` class does not return any value directly. Instead, it defines the structure for user data in the database, which can be used to store and manage user information within a Django application.
- When creating or updating a `User` instance, Django will automatically handle data validation based on the field types and constraints defined in the model.

## Docstring Draft
```python
"""Django model representing a User entity with typical attributes.

Args:
    models (module): The Django models module from which this class inherits.

Returns:
    None: This is a model class and does not return values directly.
"""
```

This markdown provides a clear, structured overview of the `User` class in your Django application.```

## Skill  
``/Project/project_app/models.py``  
```class Skill(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)```  

**Documentation:**
```python## Overview
The `Skill` class represents a model in a Django application that stores information about skills. Each skill has a name and an owner, which is a reference to a user.

## Interface
- **Signature**: `class Skill(models.Model)`
- **Parameters**: None (this is a class definition)

## Inner Workings
- The `Skill` class extends `models.Model`, which is the base class for Django models.
- It defines two fields:
  - `name`: A `CharField` with a maximum length of 20 characters, used to store the name of the skill.
  - `owner`: A foreign key field that references the `User` model. The `on_delete=models.CASCADE` parameter means that if the referenced user is deleted, all associated skills will also be deleted.

## Edge Cases & Preconditions
- The `name` field has a maximum length of 20 characters, so it must not exceed this length.
- The `owner` field is required and must reference an existing user in the database.
- No specific error handling is provided for invalid input or other potential issues related to Django model operations.

## Result Synopsis
The code defines a Django model for representing skills. Instances of this model will store the name of the skill and a reference to the user who owns it.

## Docstring Draft
```python
"""Represents a skill in the application.

This model includes fields for the name of the skill and its owner, which is a reference to a User model.
"""
```

Note: The provided docstring is a brief summary of what the `Skill` class does. Additional details about specific fields and constraints could be included in a more comprehensive docstring if needed.```

## Course  
``/Project/project_app/models.py``  
```class Course(models.Model):
    name = models.CharField(max_length=20)
    dateTime = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)```  

**Documentation:**
```python## Overview
The `Course` class defines a model for a course in a database, including its name, start date and time, and the associated user.

## Interface
- **Signature**: `class Course(models.Model)`
- **Parameters**:
  | Name     | Type    | Purpose                    |
  |----------|---------|----------------------------|
  | name     | str     | The name of the course.      |
  | dateTime | DateTime| The start date and time of the course. |
  | user_id  | User   | The user associated with the course, nullable. |

## Inner Workings
- The `Course` class inherits from `models.Model`, indicating it is a database model.
- It includes three fields:
  - `name`: A character field (`CharField`) with a maximum length of 20 characters.
  - `dateTime`: A date and time field (`DateTimeField`) to store the start date and time of the course.
  - `user_id`: A foreign key (`ForeignKey`) linking the course to a user, which can be deleted if the user is removed (CASCADE).

## Edge Cases & Preconditions
- There are no explicit error-handling mechanisms defined in this model. However:
  - The `name` field might need validation to ensure it does not exceed 20 characters.
  - The `dateTime` field should be properly formatted and valid dates/times.

## Result Synopsis
The `Course` class provides a structured way to store course information in a database, linking courses to specific users through foreign keys. It does not return any values directly but is used for data persistence and relationships in other parts of the application.

## Docstring Draft
```python
"""Represents a course with its name, start date and time, and associated user.

Attributes:
    name (CharField): The name of the course, limited to 20 characters.
    dateTime (DateTimeField): The start date and time of the course.
    user_id (ForeignKey): A foreign key linking the course to a user.
"""
``````

## Section  
``/Project/project_app/models.py``  
```class Section(models.Model):
    sectionName = models.CharField(max_length=20)          
    owner = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)```  

**Documentation:**
```python## Overview
- This code defines a Django model named `Section` which represents a section within a course, with fields for the name of the section, the owner (a foreign key to a `Course`), and the user ID (a foreign key to a `User`).

## Interface
- **Signature**: `class Section(models.Model):`
- **Parameters**:
  | Name       | Type     | Purpose                           |
  |------------|----------|-----------------------------------|
  | sectionName| CharField| Stores the name of the section.   |
  | owner      | ForeignKey| Links to a `Course` instance, allowing deletion cascade and nullable. |
  | user_id    | ForeignKey| Links to a `User` instance, allowing deletion cascade and nullable. |

## Inner Workings
- The `Section` class is derived from Django's `models.Model`, which makes it a database model.
- It includes three fields:
  - `sectionName`: A character field with a maximum length of 20 characters.
  - `owner`: A foreign key that references the `Course` model. If the referenced course is deleted, this section will also be deleted (`on_delete=models.CASCADE`). It can be null.
  - `user_id`: A foreign key that references the `User` model. Similar to `owner`, if the user is deleted, this section will also be deleted, and it can be null.

## Edge Cases & Preconditions
- The `sectionName` field has a maximum length of 20 characters, so any string longer than this will be truncated.
- Both `owner` and `user_id` fields are nullable (`null=True`), allowing for scenarios where they might not be set.
- There are no direct error-handling mechanisms provided within the code itself.

## Result Synopsis
- The `Section` model represents a section of a course, linked to both a course owner and a user. It is part of the Django ORM and will interact with the database according to the defined schema.

## Docstring Draft
```python
"""
Represents a section within a course.

Attributes:
    sectionName (CharField): The name of the section.
    owner (ForeignKey): The owner of the section, linked to a Course instance.
    user_id (ForeignKey): The user associated with the section, linked to a User instance.

"""

class Section(models.Model):
    sectionName = models.CharField(max_length=20)          
    owner = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
``````

## ProjectAppConfig  
``/Project/project_app/apps.py``  
```class ProjectAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project_app'```  

**Documentation:**
```python## Overview
This code defines a Django application configuration class `ProjectAppConfig`.

## Interface
- **Signature**: `class ProjectAppConfig(AppConfig):`
- **Parameters**:
  | Name       | Type       | Purpose                     |
  |------------|------------|-----------------------------|
  | `default_auto_field` | str | Specifies the default auto-field type for models in this app. |
  | `name`       | str        | The internal name of the application. |

## Inner Workings
- **Data Flow**: Initializes the configuration with specific attributes.
- **Control Flow**:
  - Sets `default_auto_field` to `'django.db.models.BigAutoField'`, which is Django's default primary key type.
  - Assigns `name` to `'project_app'`, which identifies the application within a Django project.

## Edge Cases & Preconditions
- The code assumes that the Django framework is being used, and `AppConfig` is a valid class in this context.
- No error handling is explicitly noted, implying that standard Django mechanisms will handle any issues related to configuration.

## Result Synopsis
The code sets up a basic configuration for a Django application named 'project_app' with default settings for model primary keys.

## Docstring Draft
```python
"""Configuration for the project_app Django app.

This class inherits from AppConfig and configures default settings for the app.

Args:
    None

Returns:
    None

Raises:
    None
"""
``````

## Login  
``/Project/project_app/views.py``  
```class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        name = request.POST.get('name')
        password = request.POST.get('password')
        if Admin().login(name, password):
            request.session['name'] = name
            request.session['password'] = password
            return redirect('/home/')

        else:
            return render(request, "login.html", {"errorMessage": "Invalid username or password"})```  

**Documentation:**
```python## Overview
This code defines a `Login` class that handles both GET and POST requests for the login functionality. The GET request renders the login page, while the POST request processes user credentials to authenticate.

## Interface
- **Signature**: `class Login(View)`
- **Parameters**:
  | Name     | Type   | Purpose                    |
  |----------|--------|------------------------------|
  | request  | HttpRequest | The HTTP request object. |

## Inner Workings
1. The `Login` class inherits from the `View` class.
2. It has two methods: `get` and `post`.
3. When a GET request is made, the `get` method renders the `login.html` template without any context data.
4. When a POST request is made, the `post` method retrieves the `name` and `password` from the request's form data.
5. It calls the `login` method of an instance of `Admin`, passing the `name` and `password`.
6. If the login is successful (i.e., `Admin().login(name, password)` returns `True`), it stores the `name` and `password` in the session and redirects to the `/home/` URL.
7. If the login fails, it renders the `login.html` template again but this time with a context dictionary containing an `errorMessage` key set to "Invalid username or password".

## Edge Cases & Preconditions
- **Assumptions**:
  - The `Admin` class has a method named `login` that takes `name` and `password` as parameters and returns a boolean indicating whether the login is successful.
  - The session management (`request.session`) is properly configured in the Django project.
  
- **Potential Failure Modes**:
  - If `Admin().login(name, password)` raises an exception (e.g., due to database errors), it will not be handled by this code.
  - If the POST request does not include `name` or `password` data, these variables will be `None`, which could lead to unexpected behavior in the login check.

## Result Synopsis
- On a successful GET request, renders the `login.html` page.
- On a successful POST request with valid credentials, redirects to `/home/`.
- On a failed POST request due to invalid credentials, renders the `login.html` page with an error message.

## Docstring Draft
```python
"""Handles user login requests.

Args:
    request (HttpRequest): The HTTP request object. For GET, it is used to render the login form.
                          For POST, it processes the submitted username and password.

Returns:
    HttpResponse: A rendered HTML response for GET, or an HTTP redirect for successful login.
                  On failure, renders the login page with an error message.

Raises:
    ValueError: If `Admin().login` raises a ValueError (though not handled by this code).
"""
``````

## Home  
``/Project/project_app/views.py``  
```class Home(View):
    def get(self, request):
        name = request.session["name"]
        password = request.session['password']
        userInfo = Admin().viewMyInfo(name, password)
        return render(request, "home.html", {"name": userInfo.name, "username": userInfo.username, "password": userInfo.password, "phone": userInfo.phone, "email": userInfo.email, "address": userInfo.address})

    def post(self, request):
        username = request.POST.get('name')
        password = request.POST.get('password')
        userInfo = Admin().viewMyInfo(username, password)
        return render(request, "home.html", {"name": userInfo.name, "username": userInfo.username, "password": userInfo.password, "phone": userInfo.phone, "email": userInfo.email, "address": userInfo.address})```  

**Documentation:**
```python## Overview
The `Home` class is a Django view that handles both GET and POST requests. When accessed via GET, it retrieves user information from the session and passes it to a template for rendering. For POST requests, it retrieves username and password from the request's form data, then fetches the user information and renders it.

## Interface
- **Signature**: `class Home(View)`
- **Parameters**:
  | Name   | Type     | Purpose                      |
  |--------|----------|------------------------------|
  | request| HttpRequest| The current HTTP request |

## Inner Workings
1. **GET Request Handling**:
   - Retrieves the user's name and password from the session.
   - Calls `Admin().viewMyInfo(name, password)` to fetch user information.
   - Passes the fetched user data to the `home.html` template for rendering.

2. **POST Request Handling**:
   - Retrieves username and password from the request's form data using `request.POST.get('name')` and `request.POST.get('password')`.
   - Calls `Admin().viewMyInfo(username, password)` to fetch user information.
   - Passes the fetched user data to the `home.html` template for rendering.

## Edge Cases & Preconditions
- **Session Data**: Assumes that the session contains valid `name` and `password` keys. If not present, it may lead to errors.
- **Form Data**: Assumes that the form submitted via POST includes non-empty `name` and `password`. Absence or invalid data could cause issues when calling `Admin().viewMyInfo`.
- **Admin Class**: Assumes that `Admin().viewMyInfo()` returns a valid user object with attributes `name`, `username`, `password`, `phone`, `email`, and `address`.

## Result Synopsis
The `Home` class renders the `home.html` template, displaying the current user's information if available, or an error message otherwise.

## Docstring Draft
```python
class Home(View):
    def get(self, request):
        """Retrieve user information from session and render home page.

        Args:
            request (HttpRequest): The current HTTP GET request.

        Returns:
            HttpResponse: Rendered HTML response with user information.
        """
        name = request.session["name"]
        password = request.session['password']
        userInfo = Admin().viewMyInfo(name, password)
        return render(request, "home.html", {"name": userInfo.name, "username": userInfo.username, "password": userInfo.password, "phone": userInfo.phone, "email": userInfo.email, "address": userInfo.address})

    def post(self, request):
        """Retrieve user information from form data and render home page.

        Args:
            request (HttpRequest): The current HTTP POST request.

        Returns:
            HttpResponse: Rendered HTML response with user information.
        """
        username = request.POST.get('name')
        password = request.POST.get('password')
        userInfo = Admin().viewMyInfo(username, password)
        return render(request, "home.html", {"name": userInfo.name, "username": userInfo.username, "password": userInfo.password, "phone": userInfo.phone, "email": userInfo.email, "address": userInfo.address})
``````

## AddSection  
``/Project/project_app/views.py``  
```class AddSection(View):
    def get(self, request):
        section_list = list(Section.objects.all())
        return render(request, "addSection.html", {"section_list": section_list})

    def post(self, request):
        courseID = request.POST.get("courseID")
        sectionID = request.POST.get("sectionID")
        message = ''

        courseObj = Course.objects.filter(name__exact=courseID)
        sectionObj = Section.objects.filter(sectionName__exact=sectionID)
        if len(courseObj) == 0:
            message = "Course ID not found in database"

        else:
            for i in sectionObj:
                if i.owner.__eq__(courseObj[0]):
                    message = "Section with same ID already exists"
                    break

        if message == '':
            try:
                Admin().createSection(courseID, sectionID)
                message = "Section created"
            except Exception as e:
                message = e
        section_list = list(Section.objects.all())
        return render(request, "addSection.html", {"Message": message, "section_list": section_list})```  

**Documentation:**
```python## Overview
The `AddSection` class in Django handles both GET and POST requests to add a new section to the database. It renders an HTML template with a list of existing sections and displays messages indicating the success or failure of the operation.

## Interface
- **Signature**: `class AddSection(View)`
- **Parameters**:
  | Name      | Type    | Purpose                                                                                       |
  |-----------|---------|---------------------------------------------------------------------------------------------|
  | request   | HttpRequest | Django's HTTP request object containing data sent from the client.                           |

## Inner Workings
1. The `get` method retrieves a list of all sections from the database and passes it to an HTML template for rendering.
2. The `post` method extracts `courseID` and `sectionID` from the POST request.
3. It checks if a course with the given `courseID` exists in the database:
   - If not, it sets a message indicating that the course ID was not found.
4. If the course exists, it checks if there is already a section with the same `sectionID`:
   - If so, it sets a message indicating that a section with the same ID already exists.
5. If both checks pass and no errors occur, it attempts to create a new section using an `Admin()` method:
   - If successful, it sets a message indicating that the section was created.
   - If an exception occurs during creation, it catches the exception and sets the error message accordingly.
6. Regardless of success or failure, it retrieves the updated list of sections from the database and passes this list along with the message to the HTML template for rendering.

## Edge Cases & Preconditions
- **Assumptions**:
  - The `Admin().createSection` method correctly handles creating a section in the database.
  - Django's ORM methods (`filter`, `all`) are functioning as expected.
  - The request contains valid `courseID` and `sectionID` values.

- **Potential Failure Modes**:
  - A non-existent course ID being provided.
  - An existing section ID being provided.
  - An error occurring during the creation of a new section.

- **Error-Handling Logic**:
  - If the course ID is not found, it sets an appropriate message.
  - If an existing section ID is found, it sets an appropriate message.
  - Any exception thrown by `Admin().createSection` is caught and its message is set as the error message.

## Result Synopsis
- The `get` method returns a rendered HTML page displaying a list of sections.
- The `post` method processes a POST request to add a new section, sets an appropriate message based on the outcome of the operation, and returns a rendered HTML page with the updated list of sections and message.

## Docstring Draft
```python
"""Handles adding a new section via GET and POST requests.

Args:
    request (HttpRequest): The HTTP request object containing data sent from the client.

Returns:
    HttpResponse: A rendered HTML response containing a list of sections and an optional message.

Raises:
    None. Errors are handled by setting appropriate messages.
"""
``````

## CreateDeleteAccount  
``/Project/project_app/views.py``  
```class CreateDeleteAccount(View):
    admin_instance = Admin()
    def get(self, request):
                                 
        account_list = list(User.objects.filter())

                                                    
        return render(request, "createDeleteAccount.html", {"accounts": account_list})

    def post(self, request):
        m = request.session["name"]

        if request.POST.get('username') != None and request.POST.get('username') != '':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            self.admin_instance.create_account(username, password, email)
        userToFind = request.POST.get('userToFind')
        if userToFind != None and userToFind != '':
            self.admin_instance.delete_account(userToFind)

        account_list = list(User.objects.filter())

        return render(request, "createDeleteAccount.html", {"accounts": account_list})```  

**Documentation:**
```python## Overview
The `CreateDeleteAccount` class provides a view for creating and deleting user accounts. It handles GET requests to display a list of users and POST requests to create or delete specific user accounts.

## Interface
- **Signature**: `class CreateDeleteAccount(View)`
- **Parameters**: None explicitly listed; parameters are passed implicitly via the request object.

## Inner Workings
1. **GET Request**:
   - The view retrieves a list of all users from the database.
   - It renders the "createDeleteAccount.html" template, passing the list of users to it.

2. **POST Request**:
   - The view retrieves the username from session data `request.session["name"]`.
   - If a new user is requested (`request.POST.get('username')`), it extracts the username, password, and email from the request.
   - It then uses an instance of `Admin` to create the new account.
   - If an account deletion is requested (`request.POST.get('userToFind')`), it retrieves the username to be deleted and uses the `Admin` instance to delete the account.
   - Regardless of whether a new account was created or an existing one was deleted, the view fetches the updated list of all users from the database.
   - Finally, it renders the "createDeleteAccount.html" template with the updated list of users.

## Edge Cases & Preconditions
- **Session Data**: Assumes that `request.session["name"]` is present and correctly formatted.
- **POST Data**: Expects specific keys ('username', 'password', 'email') in the POST data for creating new accounts. For deleting accounts, expects a key ('userToFind').
- **Error Handling**: The code does not explicitly handle errors such as missing session data or invalid POST parameters.

## Result Synopsis
The view handles both GET and POST requests to manage user accounts. On GET requests, it displays a list of all users. On POST requests, it can create new accounts or delete existing ones, updating the displayed list accordingly.

## Docstring Draft
```python
"""Manages user account creation and deletion.

Args:
    request (HttpRequest): The incoming HTTP request object.

Returns:
    HttpResponse: A rendered HTML response displaying the list of user accounts.

Raises:
    KeyError: If required session or POST data is missing.
"""
```

This Markdown format provides a clear, structured explanation of the code's functionality, parameters, inner workings, potential issues, and expected results.```

## CreateCourse  
``/Project/project_app/views.py``  
```class CreateCourse(View):
    courseList=[]
    def get(self,request):
        course_list = list(Course.objects.all())
        return render(request,"createCourse.html",{"course_list": course_list})

    def post(self, request):
                                   
        name = request.POST.get('courseName')
        time = request.POST.get('courseTime')
        try:
            a = Admin().createCourse(name, time)
        except TypeError:
            a = "Inputs must be text"
        except ValueError:
            a ="Time must be YYYY-MM-DD HR:MN:SC"
        course_list = list(Course.objects.all())
        Message = a
        return render(request, "createCourse.html", {"Message": Message, "course_list": course_list})```  

**Documentation:**
```python## Overview
This code defines a class `CreateCourse` that handles both GET and POST requests to manage courses. It displays a list of courses on the GET request and processes course creation on the POST request.

## Interface
### Signature
```python
class CreateCourse(View):
```

### Parameters
| Name | Type | Purpose |
|------|------|---------|
| None | N/A  | This is a class, not a function, so it does not take parameters. |

## Inner Workings
- **Initialization**: The class `CreateCourse` is defined as inheriting from `View`. It has an empty list `courseList`.
- **GET Request Handling**:
  - Retrieves all courses from the database using `Course.objects.all()`.
  - Renders the `createCourse.html` template with a context containing the course list.
- **POST Request Handling**:
  - Extracts `name` and `time` from the POST request.
  - Attempts to create a new course by calling `Admin().createCourse(name, time)`. This method may raise exceptions if inputs are invalid.
    - If a `TypeError` occurs (e.g., non-text inputs), it sets `a` to "Inputs must be text".
    - If a `ValueError` occurs (e.g., incorrect date format), it sets `a` to "Time must be YYYY-MM-DD HR:MN:SC".
  - Regardless of success, retrieves all courses from the database.
  - Renders the `createCourse.html` template with context containing any error message (`Message`) and the updated course list.

## Edge Cases & Preconditions
- **Inputs**: The code expects `name` to be a string and `time` to be in the format "YYYY-MM-DD HR:MN:SC".
- **Errors**:
  - Raises a `TypeError` if inputs are not text.
  - Raises a `ValueError` if the time is not in the correct format.
  - Handles these exceptions by setting appropriate error messages.

## Result Synopsis
The code updates and displays the list of courses on both GET and POST requests. On POST, it attempts to create a new course and handles any errors that occur during this process.

## Docstring Draft
```python
"""Handles GET and POST requests for managing courses.

Args:
    request (HttpRequest): The incoming HTTP request object.

Returns:
    HttpResponse: The rendered HTML response with updated course list or error message.
"""
``````

## AccountEdit  
``/Project/project_app/views.py``  
```class AccountEdit(View):

    def get(self, request):
        return render(request,"accountEdit.html",{})

    def post(self, request):
        username = request.session['name']
        field_to_change = request.POST.get("user-fields")
        new_value = request.POST.get("newEntry")

                                             
        user = User.objects.get(username=username)

        if field_to_change in ['phone', 'name', 'email', 'address']:
                                                             
            if field_to_change == 'name' and User.objects.filter(username=new_value).exclude(
                    username=user.username).exists():
                message = 'Username already exists'
            elif field_to_change == 'email' and User.objects.filter(email=new_value).exclude(
                    username=user.username).exists():
                message = 'Email already exists'
            else:
                setattr(user, field_to_change, new_value)
                user.save()
                message = 'Information updated successfully'
        else:
            message = 'Invalid field selected'

        return render(request, "accountEdit.html", {"Message": message})```  

**Documentation:**
```python## Overview
This code defines a class `AccountEdit` that extends Django's `View` to handle GET and POST requests for editing user account information.

## Interface
### Signature
```python
class AccountEdit(View):
    def get(self, request)
    def post(self, request)
```

### Parameters
| Parameter | Type | Purpose |
|-----------|------|---------|
| request   | HttpRequest | The HTTP request object. |

## Inner Workings
1. **GET Request**:
   - The `get` method simply renders and returns the `accountEdit.html` template with an empty context.

2. **POST Request**:
   - Retrieves the current user's username from the session.
   - Extracts the field to be changed and the new value from the POST data.
   - Fetches the user object from the database using their username.
   - Checks if the selected field is one of 'phone', 'name', 'email', or 'address'.
     - If 'name' or 'email' is selected, it checks if the new value already exists in the database for another user (excluding the current user).
       - If it does, sets an error message.
       - If not, updates the field with the new value and saves the user object. Sets a success message.
     - For other fields, updates the field directly with the new value and saves the user object. Sets a success message.
   - If an invalid field is selected, sets an error message.
   - Renders and returns the `accountEdit.html` template with a context containing the message.

## Edge Cases & Preconditions
- **Assumptions**:
  - The session contains a valid `username`.
  - The POST data includes `user-fields` and `newEntry`.
  - The user exists in the database.
  
- **Potential Failure Modes**:
  - The selected field is not one of 'phone', 'name', 'email', or 'address'.
  - The new value for 'name' or 'email' already exists for another user.

- **Error Handling**:
  - If an invalid field is selected, returns an error message.
  - If the new value for 'name' or 'email' already exists, returns an error message.

## Result Synopsis
- On a GET request, it renders `accountEdit.html` without any context.
- On a POST request, it updates the user's account information if valid and renders `accountEdit.html` with a success or error message.

## Docstring Draft
```python
"""Handles GET and POST requests for editing user account information.

Args:
    request (HttpRequest): The HTTP request object.

Returns:
    HttpResponse: The rendered HTML response with an optional message.
"""
```
This draft docstring provides a concise summary of the function's purpose, parameters, and return type. It captures the essence of what the code does without delving into the detailed implementation logic.```

## AssignSection  
``/Project/project_app/views.py``  
```class AssignSection(View):
    def get(self, request):
        return render(request,"assignSection.html",{})

    def post(self, request):
        pass```  

**Documentation:**
```python## Overview
This code defines a Django view class `AssignSection` that handles both GET and POST requests for rendering and processing data related to assigning sections.

## Interface
### Signature:
```python
class AssignSection(View):
```

### Parameters:
| Name | Type | Purpose |
|------|------|---------|
| request | HttpRequest | The HTTP request object containing all the information about the client's request. |

## Inner Workings
- The `AssignSection` class inherits from Django's `View` base class.
- It has two methods: `get` and `post`.
  - **GET Method**: This method is responsible for handling GET requests. When a GET request is received, it simply renders the "assignSection.html" template with an empty context dictionary `{}` and returns it to the client.
  - **POST Method**: Currently, this method is empty (`pass`), indicating that it has not been implemented yet.

## Edge Cases & Preconditions
- There are no assumptions made about the input parameters in the provided code snippet. Both methods assume that `request` is an instance of `HttpRequest`.
- The POST method does nothing currently and lacks any logic to handle incoming data, which could lead to unexpected behavior if this method is called with a POST request.

## Result Synopsis
- When a GET request is made, the view renders and returns the "assignSection.html" template with an empty context.
- The POST method does not perform any action and simply passes through without modifying or responding to the request.

## Docstring Draft
```python
"""Handles rendering and processing of the assign section page.

This view handles GET requests by rendering the 'assignSection.html' template.
The POST method is currently unimplemented and does nothing.

Args:
    request (HttpRequest): The HTTP request object.

Returns:
    HttpResponse: An HTTP response with the rendered 'assignSection.html' template if GET, otherwise an empty response for POST.
"""
``````

## AssignCourse  
``/Project/project_app/views.py``  
```class AssignCourse(View):
    def get(self, request):
        user_list = list(User.objects.all())
        course_list = list(Course.objects.all())
        return render(request, "assignCourse.html", {"user_list": user_list, "course_list": course_list})

    def post(self, request):
        courseID = request.POST.get("courseID")
        userToFind = request.POST.get("userToFind")

        message = ''
        try:
            course = Course.objects.get(name=courseID)
            user = User.objects.get(username=userToFind)
            course.user_id = user
            course.save()
            message = 'Course assigned successfully'
        except Course.DoesNotExist:
            message = 'Course not found'
        except User.DoesNotExist:
            message = 'User not found'

        course_list = list(Course.objects.all())
        user_list = list(User.objects.all())
        userSkills = Skill.objects.filter(owner=user)                     

        return render(request, "assignCourse.html",
                      {"Message": message, "course_list": course_list, "user_list": user_list,
                       "userSkills": userSkills})```  

**Documentation:**
```python## Overview
This code defines a Django view class `AssignCourse` that handles both GET and POST requests to assign a course to a user. It renders an HTML template with lists of users and courses, and updates the database based on user input.

## Interface
### Signature
```python
class AssignCourse(View):
    def get(self, request)
    def post(self, request)
```

### Parameters
| Name       | Type   | Purpose                               |
|------------|--------|-----------------------------------------|
| `request`  | `HttpRequest` | The HTTP request object.               |

## Inner Workings
- **GET Request**:
  - Fetches all users and courses from the database.
  - Renders an HTML template (`assignCourse.html`) with the fetched data.

- **POST Request**:
  - Retrieves `courseID` and `userToFind` from the POST request.
  - Tries to find a course by name and a user by username.
  - If both are found, assigns the user to the course and saves the changes.
  - Handles exceptions if either the course or user is not found.
  - Renders the HTML template again with updated data and a message.

## Edge Cases & Preconditions
- **Course Not Found**: If the provided `courseID` does not exist in the database, an exception is caught, and a 'Course not found' message is returned.
- **User Not Found**: If the provided `userToFind` does not exist in the database, an exception is caught, and a 'User not found' message is returned.
- **GET Request**: No assumptions needed; it simply fetches data and renders the template.

## Result Synopsis
The function returns an HTTP response rendering the `assignCourse.html` template with updated data and a success or error message based on the user's action.

## Docstring Draft
```python
"""Handles GET and POST requests for assigning a course to a user.

This view fetches all users and courses from the database. On a GET request,
it renders an HTML form. On a POST request, it attempts to assign a course to a user
and updates the database accordingly, returning a success or error message.

Args:
    request (HttpRequest): The HTTP request object.

Returns:
    HttpResponse: An HTTP response rendering the `assignCourse.html` template.
"""
``````

## AddSkills  
``/Project/project_app/views.py``  
```class AddSkills(View):
    def get(self, request):
        ta1 = request.session["name"]
        mySkills = list(Skill.objects.filter(owner=User.objects.get(username=ta1)))
        return render(request, "addSkills.html", {"mySkills": mySkills})                                                                     

    def post(self, request):
        ta1 = request.session["name"]
                                                           
        skill = request.POST.get('newSkill')
        Message= "Success!"
        mySkills = list(Skill.objects.filter(owner=User.objects.get(username=ta1)))
        if Ta().addSkills(skill, ta1):
            mySkills = list(Skill.objects.filter(owner=User.objects.get(username=ta1)))
        else:
            Message = "Failed to add skill"

        return render(request, "addSkills.html", {"Message": Message, "mySkills": mySkills})```  

**Documentation:**
```python## Overview
This code defines a Django class-based view `AddSkills` that handles both GET and POST requests. For GET requests, it retrieves skills associated with the current user and renders them in an HTML template. For POST requests, it attempts to add a new skill for the current user, updates the skill list accordingly, and returns a success or failure message.

## Interface
- **Signature**: 
  ```python
  class AddSkills(View):
      def get(self, request)
      def post(self, request)
  ```
- **Parameters**:
  | Name       | Type     | Purpose                    |
  |------------|----------|------------------------------|
  | `request`  | `HttpRequest` | The HTTP request object.        |

## Inner Workings
1. **GET Request Handling**:
   - Retrieves the username of the current user from the session.
   - Fetches all skills associated with this user using Django ORM.
   - Renders an HTML template `addSkills.html`, passing the fetched skills to it.

2. **POST Request Handling**:
   - Retrieves the username of the current user from the session.
   - Extracts a new skill name from the POST request data.
   - Attempts to add the new skill using an instance method `Ta().addSkills(skill, ta1)`.
     - If successful, updates the list of skills and sets a success message.
     - If unsuccessful, sets a failure message.
   - Renders the HTML template `addSkills.html`, passing both the message and updated skills list.

## Edge Cases & Preconditions
- **Assumptions**:
  - The user's username is stored in the session under the key `"name"`.
  - There is an instance of `Ta` with a method `addSkills(skill, ta1)` that handles skill addition logic.
  - The `Skill` model has fields `owner` and `name`, and there is a corresponding `User` model.

- **Potential Failure Modes**:
  - If the user's username is not found in the session, this could lead to an error when trying to retrieve skills.
  - If the skill addition fails (e.g., due to validation errors), the failure message will be set.

- **Error-Handling Logic**:
  - Errors related to Django ORM operations are generally handled by the framework, but specific errors within `Ta().addSkills(skill, ta1)` are not caught and rethrown as exceptions. Instead, the method's return value is checked for success or failure.

## Result Synopsis
For GET requests, the view returns an HTML template displaying the user's skills.
For POST requests, the view either adds a new skill (if successful) and updates the display with a success message or shows a failure message if the addition fails.

## Docstring Draft
```python
"""Handles GET and POST requests for adding skills to a user.

Returns:
    HttpResponse: An HTML response rendering `addSkills.html` with appropriate data.

Raises:
    KeyError: If the 'name' key is not found in the session.
"""
```

This docstring provides a brief summary of what the class does, its return type, and mentions a potential exception that could be raised.```

## ViewSkills  
``/Project/project_app/views.py``  
```class ViewSkills(View):
    def get(self, request):
        return render(request, "viewSkills.html", {})

    def post(self, request):
        user = request.POST.get("userToFind")
        message = ''
        try:
            mySkills = list(Skill.objects.filter(owner=User.objects.get(username=user, user_type='ta')))
        except Exception as e:
            message = str(e)
            return render(request, "viewSkills.html", {"userSkills": "", "Message": message})
        return render(request, "viewSkills.html", {"userSkills": mySkills, "Message": message})```  

**Documentation:**
```python## Overview
- This code defines a Django view class `ViewSkills` that handles both GET and POST requests to display skills of a user.

## Interface
- **Signature**: `class ViewSkills(View)`
- **Parameters**:
  | Name        | Type   | Purpose                      |
  |-------------|--------|------------------------------|
  | request     | HttpRequest | The incoming HTTP request object. |

## Inner Workings
1. **GET Request Handling**:
   - Calls the Django `render` function to render the `viewSkills.html` template with an empty context.

2. **POST Request Handling**:
   - Retrieves the `userToFind` parameter from the POST data.
   - Initializes an empty string `message`.
   - Attempts to fetch skills of a user who is a teaching assistant (ta) by querying the database for matching users and their skills.
   - If successful, it assigns the fetched skills to `mySkills`.
   - If an exception occurs during the query (e.g., user not found), catches the exception, stores the error message in `message`, and renders the template with no skills and the error message.
   - Finally, renders the `viewSkills.html` template with the retrieved skills and any error messages.

## Edge Cases & Preconditions
- **Assumptions**:
  - The database contains a valid `User` object with the username provided in the POST request.
  - The `Skill` model has foreign key relationships set up correctly to reference users.
  - The `user_type` field of the user is accurately set to 'ta' for teaching assistants.

- **Potential Failure Modes**:
  - If the user does not exist, a database query will fail, and an exception will be raised.
  - If any other error occurs during the database query, it will also result in an exception.

- **Error-Handling Logic**:
  - Any exceptions caught are stored in `message` and passed to the template. This allows for displaying error messages to the user.

## Result Synopsis
- The view returns a rendered HTML page (`viewSkills.html`) with either the skills of the specified user or an error message if something goes wrong during the database query.

## Docstring Draft
```python
"""Handles GET and POST requests to display skills of a user.

This view class is responsible for rendering the skills of a user who is a teaching assistant (ta).
On a GET request, it renders an empty template.
On a POST request, it attempts to fetch and render the skills of the specified user. If an error occurs,
it catches the exception and passes an error message to the template.

Args:
    request (HttpRequest): The incoming HTTP request object.

Returns:
    HttpResponse: A rendered HTML page containing the skills or an error message.
"""
``````

## SearchUser  
``/Project/project_app/views.py``  
```class SearchUser(View):
    def get(self, request):
        user_to_find = request.GET.get('userToFind')
        mySkills = list(Skill.objects.filter(owner=User.objects.get(username=user_to_find, user_type='ta')))
        return render(request, "viewSkills.html", {"accounts": mySkills})

    def post(self, request):
        userToFind = request.POST.get('userToFind')
        Message = "User found"

        if Admin().searchUser(userToFind):
            ta_user = User.objects.get(username=userToFind, user_type='ta')
            mySkills = list(Skill.objects.filter(owner=ta_user))
        else:
            Message = "No user found"

        return render(request, "viewSkills.html", {"Message": Message, "mySkills": mySkills})```  

**Documentation:**
```python## Overview
This code defines a class `SearchUser` that extends Django's `View` class. It handles GET and POST requests to search for a user by their username and display their skills.

## Interface
### Signature
```python
class SearchUser(View):
    def get(self, request):
        # Implementation details...
    
    def post(self, request):
        # Implementation details...
```

### Parameters
| Name     | Type   | Purpose                      |
|----------|--------|------------------------------|
| `request`| `HttpRequest`| The HTTP request object containing user data. |

## Inner Workings
- **GET Method**:
  - Retrieves the username to find from the GET request.
  - Filters `Skill` objects that belong to a user with the specified username and type 'ta'.
  - Renders the `viewSkills.html` template with the filtered skills.

- **POST Method**:
  - Retrieves the username to find from the POST request.
  - Initializes a message indicating "User found".
  - Calls an `Admin` class method `searchUser` to check if the user exists and is of type 'ta'.
  - If the user is found, it retrieves the skills associated with the user.
  - If no user is found, updates the message to indicate "No user found".
  - Renders the `viewSkills.html` template with the updated message and skills (if any).

## Edge Cases & Preconditions
- **Admin.searchUser**: Assumes that the `Admin` class has a method `searchUser` which returns a boolean indicating whether the user exists and is of type 'ta'.
- **GET Request**: The code assumes that the `userToFind` parameter is provided in the GET request.
- **POST Request**: The code assumes that the `userToFind` parameter is provided in the POST request.

## Result Synopsis
The function returns an HTTP response rendering the `viewSkills.html` template with a list of skills associated with the user, or a message indicating whether the user was found.

## Docstring Draft
```python
class SearchUser(View):
    def get(self, request):
        """Handle GET requests to search for a user by username and display their skills.

        Args:
            request (HttpRequest): The HTTP request object containing user data.

        Returns:
            HttpResponse: Rendered viewSkills.html with the filtered skills.
        """
    
    def post(self, request):
        """Handle POST requests to search for a user by username and display their skills.

        Args:
            request (HttpRequest): The HTTP request object containing user data.

        Returns:
            HttpResponse: Rendered viewSkills.html with the updated message and skills (if any).
        """
``````

## get  
``/Project/project_app/views.py``  
```def get(self, request):
        return render(request, "login.html", {})```  

**Documentation:**
```python## Overview
- This code defines a method for rendering a login page in a Django web application.

## Interface
- **Signature**: `get(self, request)`
- **Parameters**:
  | Name   | Type    | Purpose                 |
  |--------|---------|-------------------------|
  | request| HttpRequest | The HTTP request object |

## Inner Workings
- The method is called when a GET request is made to the associated URL.
- It uses Django's `render` function to render and return the `login.html` template, passing an empty dictionary as context.

## Edge Cases & Preconditions
- There are no assumptions or preconditions explicitly checked in this code. If the `request` parameter is not provided correctly (i.e., it does not conform to the expected type), a TypeError will occur.
- The method does not perform any error handling, so any unexpected errors during rendering will propagate up the call stack.

## Result Synopsis
- The method returns an HTTP response that renders and displays the `login.html` template.

## Docstring Draft
```python
"""Renders the login page.

Args:
    request (HttpRequest): The HTTP request object.

Returns:
    HttpResponse: An HTTP response with the rendered login page.
"""
``````

## post  
``/Project/project_app/views.py``  
```def post(self, request):
        name = request.POST.get('name')
        password = request.POST.get('password')
        if Admin().login(name, password):
            request.session['name'] = name
            request.session['password'] = password
            return redirect('/home/')

        else:
            return render(request, "login.html", {"errorMessage": "Invalid username or password"})```  

**Documentation:**
```python## Overview
The `post` function handles the login process for an admin user. It retrieves the name and password from a POST request, attempts to log in using these credentials, and sets session variables if successful.

## Interface
**Signature**: `def post(self, request)`

| Parameter | Type     | Purpose                     |
|-----------|----------|-----------------------------|
| request   | HttpRequest | Django HTTP request object |

## Inner Workings
- Retrieve the `name` and `password` from the POST data using `request.POST.get`.
- Create an instance of `Admin()` and attempt to log in with the retrieved credentials.
  - If login is successful, store the `name` and `password` in the session and redirect the user to `/home/`.
  - If login fails, render the "login.html" template with an error message.

## Edge Cases & Preconditions
- The function assumes that the request method is POST. If not, it will not process any data.
- It expects that the `Admin` class has a method `login(name, password)` which returns `True` if the credentials are correct and `False` otherwise.
- If `name` or `password` is not provided in the POST data, they will default to `None`.

## Result Synopsis
The function redirects the user to `/home/` if the login is successful. Otherwise, it renders the "login.html" template with an error message.

## Docstring Draft
```python
"""Handles the admin login process.

Args:
    request (HttpRequest): The Django HTTP request object containing POST data.

Returns:
    HttpResponse: A redirect response to '/home/' if login is successful, otherwise a rendered "login.html" template with an error message.
"""
``````

## get  
``/Project/project_app/views.py``  
```def get(self, request):
        name = request.session["name"]
        password = request.session['password']
        userInfo = Admin().viewMyInfo(name, password)
        return render(request, "home.html", {"name": userInfo.name, "username": userInfo.username, "password": userInfo.password, "phone": userInfo.phone, "email": userInfo.email, "address": userInfo.address})```  

**Documentation:**
```python## Overview
The `get` function retrieves user information from the session and passes it to a template for rendering.

## Interface
### Signature
```python
def get(self, request)
```

### Parameters
| Name   | Type   | Purpose                          |
|--------|--------|----------------------------------|
| request| object | The Django HTTP request object.  |

## Inner Workings
1. **Retrieve Session Data**: The function accesses the user's name and password from the session.
2. **Fetch User Info**: It creates an instance of `Admin` and calls its method `viewMyInfo` with the retrieved credentials to fetch user information.
3. **Render Template**: Finally, it renders a template named "home.html" using the fetched user data.

## Edge Cases & Preconditions
- The function assumes that the necessary session keys (`name` and `password`) are present and valid.
- It relies on the `Admin().viewMyInfo` method to return user information in a structured format (e.g., an object with attributes like `name`, `username`, etc.).
- If the session data is missing or invalid, it may lead to errors when trying to access dictionary keys.

## Result Synopsis
The function returns an HTTP response rendering the "home.html" template with user information passed as context variables.

## Docstring Draft
```python
"""Retrieve user information from the session and render the home page.

Args:
    request (HttpRequest): The Django HTTP request object containing session data.

Returns:
    HttpResponse: An HTTP response rendering the 'home.html' template with user information.

Raises:
    KeyError: If necessary session keys ('name' or 'password') are missing.
"""
``````

## post  
``/Project/project_app/views.py``  
```def post(self, request):
        username = request.POST.get('name')
        password = request.POST.get('password')
        userInfo = Admin().viewMyInfo(username, password)
        return render(request, "home.html", {"name": userInfo.name, "username": userInfo.username, "password": userInfo.password, "phone": userInfo.phone, "email": userInfo.email, "address": userInfo.address})```  

**Documentation:**
```python## Overview
This code handles a POST request to retrieve user information and render it on the home page.

## Interface
- **Signature**: `post(self, request)`
- **Parameters**:
  | Name   | Type     | Purpose                 |
  |--------|----------|-------------------------|
  | request| HttpRequest| Django HTTP request object|

## Inner Workings
1. The function retrieves the username and password from the POST data of the incoming request.
2. It then calls `Admin().viewMyInfo(username, password)` to fetch user information.
3. Finally, it renders an HTML template named "home.html" and passes the retrieved user information as context.

## Edge Cases & Preconditions
- The function assumes that the `request.POST` dictionary contains keys 'name' and 'password'.
- It does not handle cases where `Admin().viewMyInfo(username, password)` might fail or return invalid data.
- Potential errors include missing POST parameters, incorrect username/password combinations in the database, or issues with rendering the template.

## Result Synopsis
The function returns an HTTP response that renders the "home.html" template with user information embedded as context variables. If there are any issues, it may raise an exception or return a default error page depending on how the `Admin().viewMyInfo()` method is implemented.

## Docstring Draft
```python
"""Handles a POST request to retrieve and display user information.

Args:
    request (HttpRequest): Django HTTP request object containing POST data with 'name' and 'password'.

Returns:
    HttpResponse: Rendered HTML response using "home.html" template with user information.

Raises:
    ValueError: If the `Admin().viewMyInfo()` method raises an error due to invalid input or database issues.
"""
``````

## get  
``/Project/project_app/views.py``  
```def get(self, request):
        section_list = list(Section.objects.all())
        return render(request, "addSection.html", {"section_list": section_list})```  

**Documentation:**
```python## Overview
This code defines a method for rendering a template with a list of sections in a Django application.

## Interface
- **Signature**: `def get(self, request)`
- **Parameters**:
  | Name     | Type    | Purpose                      |
  |----------|---------|------------------------------|
  | `request`| `HttpRequest`| The HTTP request object.       |

## Inner Workings
1. **Retrieve Section Data**: 
   - Fetches all sections from the database using `Section.objects.all()`, which returns a queryset of section objects.
   
2. **Convert to List**:
   - Converts the queryset to a list using `list(Section.objects.all())`.

3. **Render Template**:
   - Renders the template "addSection.html" by passing the list of sections as context.

## Edge Cases & Preconditions
- **Assumptions**: 
  - The `request` parameter is always an instance of `HttpRequest`.
  - The `Section` model exists and has a valid implementation in the Django project.
  
- **Potential Failure Modes**:
  - If there are issues with fetching data from the database (e.g., database connection error), it may lead to a failure during the `render` call.
  
- **Error Handling**: 
  - The code does not explicitly handle exceptions. Any database-related errors or template rendering errors would propagate up the call stack.

## Result Synopsis
The function returns an HTTP response that renders the "addSection.html" template with the list of sections passed as context.

## Docstring Draft
```python
"""Retrieves all sections from the database and renders the 'addSection.html' template.

Args:
    request (HttpRequest): The HTTP request object containing client data.

Returns:
    HttpResponse: An HTTP response rendering the 'addSection.html' template with a list of sections.

Raises:
    Exception: Any exceptions that occur during database query or template rendering.
"""
``````

## post  
``/Project/project_app/views.py``  
```def post(self, request):
        courseID = request.POST.get("courseID")
        sectionID = request.POST.get("sectionID")
        message = ''

        courseObj = Course.objects.filter(name__exact=courseID)
        sectionObj = Section.objects.filter(sectionName__exact=sectionID)
        if len(courseObj) == 0:
            message = "Course ID not found in database"

        else:
            for i in sectionObj:
                if i.owner.__eq__(courseObj[0]):
                    message = "Section with same ID already exists"
                    break

        if message == '':
            try:
                Admin().createSection(courseID, sectionID)
                message = "Section created"
            except Exception as e:
                message = e
        section_list = list(Section.objects.all())
        return render(request, "addSection.html", {"Message": message, "section_list": section_list})```  

**Documentation:**
```python## Overview
This code defines a method `post` within a class that handles the creation of a new section for a course based on the provided request parameters.

## Interface
- **Signature**: `def post(self, request)`
- **Parameters**:
  | Name     | Type    | Purpose                    |
  |----------|---------|----------------------------|
  | `request`| `HttpRequest`| The HTTP request object containing form data.|

## Inner Workings
1. The method retrieves the `courseID` and `sectionID` from the POST request.
2. It initializes an empty string `message` to store any error or success messages.
3. It attempts to fetch a course object based on the `courseID`. If no such course exists, it sets the `message` to "Course ID not found in database".
4. If the course exists, it iterates through the fetched sections to check if there is already a section with the same ID. If such a section exists, it sets the `message` to "Section with same ID already exists".
5. If no errors have been detected, it attempts to create a new section using the `Admin().createSection` method. If successful, it sets the `message` to "Section created". If an exception occurs during this process, it catches the exception and sets the `message` to the error description.
6. Finally, it retrieves all sections from the database and renders the `addSection.html` template with the `message` and section list.

## Edge Cases & Preconditions
- **Assumptions**:
  - The `courseID` and `sectionID` are provided in the POST request.
  - The `Admin().createSection` method correctly handles the creation of a new section.
  - The database models (`Course`, `Section`) are properly configured.

- **Potential Failure Modes**:
  - If the `courseID` is not found, an error message will be set.
  - If a section with the same ID already exists for the course, an error message will be set.
  - Any exceptions thrown by the `Admin().createSection` method will be caught and displayed as an error message.

## Result Synopsis
The function returns an HTTP response rendering the `addSection.html` template with a message indicating whether the section was successfully created or if there were errors during the process. It also passes all current sections in the database to the template for display.

## Docstring Draft
```python
"""Handles creating a new section for a course based on POST request parameters.

Args:
    request (HttpRequest): The HTTP request object containing form data with 'courseID' and 'sectionID'.

Returns:
    HttpResponse: A response rendering the 'addSection.html' template with a message and list of sections.
"""
``````

## get  
``/Project/project_app/views.py``  
```def get(self, request):
                                 
        account_list = list(User.objects.filter())

                                                    
        return render(request, "createDeleteAccount.html", {"accounts": account_list})```  

**Documentation:**
```python## Overview
This code defines a method `get` within an unspecified class. It retrieves a list of user accounts from the database and renders them in an HTML template.

## Interface
- **Signature**: `def get(self, request)`
  - `self`: The instance of the class.
  - `request`: An HTTP request object.

- **Parameters**:
  | Name     | Type   | Purpose                        |
  |----------|--------|----------------------------------|
  | self     | object | Instance of the class.           |
  | request  | object | The incoming HTTP request.       |

## Inner Workings
1. **Retrieve User Accounts**: The method fetches a list of all user accounts from the database using `User.objects.filter()`, which presumably returns a queryset containing all users.
2. **Convert to List**: The queryset is converted into a list using `list(User.objects.filter())`.
3. **Render Template**: The retrieved list of accounts is passed to the `render` function along with the template name `"createDeleteAccount.html"` and context data.

## Edge Cases & Preconditions
- **No Users in Database**: If there are no user accounts in the database, `User.objects.filter()` will return an empty queryset. Converting this to a list will result in an empty list.
- **Database Connection Issues**: The method assumes that the database connection is working correctly and that `User.objects.filter()` can retrieve data without issues.

## Result Synopsis
The function returns an HTTP response rendered by the template `"createDeleteAccount.html"`, passing the list of user accounts as context data. If there are no users, it will pass an empty list.

## Docstring Draft
```python
"""Retrieves a list of all user accounts and renders them in an HTML template.

Args:
    self (object): Instance of the class.
    request (object): The incoming HTTP request.

Returns:
    HttpResponse: An HTTP response rendered by the template "createDeleteAccount.html" with context data containing the list of user accounts.

Raises:
    None
"""
``````

## post  
``/Project/project_app/views.py``  
```def post(self, request):
        m = request.session["name"]

        if request.POST.get('username') != None and request.POST.get('username') != '':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            self.admin_instance.create_account(username, password, email)
        userToFind = request.POST.get('userToFind')
        if userToFind != None and userToFind != '':
            self.admin_instance.delete_account(userToFind)

        account_list = list(User.objects.filter())

        return render(request, "createDeleteAccount.html", {"accounts": account_list})```  

**Documentation:**
```python## Overview
This code processes a POST request to handle user account creation and deletion, then renders a template with a list of all accounts.

## Interface
- **Signature**: `post(self, request)`
- **Parameters**:
  | Name   | Type    | Purpose                 |
  |--------|---------|---------------------------|
  | `request` | HttpRequest | The HTTP request object |

## Inner Workings
1. **Retrieve User Data from Session**:
   - The username of the currently logged-in user is retrieved from the session.

2. **Handle Account Creation**:
   - If a non-empty `username`, `password`, and `email` are provided in the POST data, an account is created using the `create_account` method of `self.admin_instance`.

3. **Handle Account Deletion**:
   - If a non-empty `userToFind` is provided in the POST data, an account with that username is deleted using the `delete_account` method of `self.admin_instance`.

4. **Retrieve and Prepare Account List**:
   - All user accounts are retrieved from the database.
   - The list of accounts is passed to the template.

5. **Render Template**:
   - The `createDeleteAccount.html` template is rendered with the account list.

## Edge Cases & Preconditions
- **Precondition**: A user must be logged in and have session data containing their name.
- **Error Handling**: If `username`, `password`, or `email` are not provided for creation, no action is taken. If `userToFind` is not provided for deletion, no action is taken.

## Result Synopsis
The function returns an HTTP response rendering the `createDeleteAccount.html` template with a list of all user accounts.

## Docstring Draft
```python
"""Handles POST requests to create and delete user accounts.

Args:
    request (HttpRequest): The HTTP request object containing form data.

Returns:
    HttpResponse: A response rendering the 'createDeleteAccount.html' template with a list of all accounts.

Raises:
    None
"""
``````

## get  
``/Project/project_app/views.py``  
```def get(self,request):
        course_list = list(Course.objects.all())
        return render(request,"createCourse.html",{"course_list": course_list})```  

**Documentation:**
```python## Overview
This code defines a method `get` within a class that retrieves all courses from the database and renders them in a template.

## Interface
- **Signature**: `def get(self, request)`
- **Parameters**:
  | Name     | Type    | Purpose                  |
  |----------|---------|--------------------------|
  | self     | object  | Reference to the instance. |
  | request  | HttpRequest | Django HTTP request object |

## Inner Workings
1. The method retrieves all courses from the database using `Course.objects.all()`.
2. It converts the queryset returned by `Course.objects.all()` into a list.
3. It renders the `createCourse.html` template, passing the list of courses as context.

## Edge Cases & Preconditions
- **Assumptions**:
  - The `Course` model is defined and accessible in the application's Django models.
  - The `createCourse.html` template exists in the `templates` directory.
- **Potential Failure Modes**:
  - If the `Course` model does not exist, calling `Course.objects.all()` will raise an error.
  - If the `createCourse.html` template is missing or misnamed, rendering it will fail.
- **Error Handling**:
  - No explicit error handling is present. Any issues with database access or template rendering will propagate as exceptions.

## Result Synopsis
The method returns an HTTP response that renders the `createCourse.html` template, passing a list of all courses in the database as context.

## Docstring Draft
```python
"""Retrieves all courses and renders them in the createCourse.html template.

Args:
    request (HttpRequest): The Django HTTP request object.

Returns:
    HttpResponse: An HTTP response rendering the `createCourse.html` template with a list of courses.
"""
``````

## post  
``/Project/project_app/views.py``  
```def post(self, request):
                                   
        name = request.POST.get('courseName')
        time = request.POST.get('courseTime')
        try:
            a = Admin().createCourse(name, time)
        except TypeError:
            a = "Inputs must be text"
        except ValueError:
            a ="Time must be YYYY-MM-DD HR:MN:SC"
        course_list = list(Course.objects.all())
        Message = a
        return render(request, "createCourse.html", {"Message": Message, "course_list": course_list})```  

**Documentation:**
```python## Overview
The `post` method handles the creation of a new course by extracting data from an HTTP POST request, attempting to create the course using an `Admin` object, and then rendering a template with either a success message or error information.

## Interface
### Signature
```python
def post(self, request)
```

### Parameters
| Name | Type    | Purpose                          |
|------|---------|----------------------------------|
| request | HttpRequest | The HTTP request object containing form data. |

## Inner Workings
1. **Extract Data**: Retrieves the course name and time from the `request.POST` dictionary.
2. **Create Course**:
   - Attempts to create a new course using an `Admin` object's `createCourse` method with the extracted name and time.
   - Catches exceptions that might occur during the creation process, such as `TypeError` if inputs are not valid text types and `ValueError` if the time format is incorrect.
3. **Process Course List**:
   - Fetches all courses from the database using `Course.objects.all()` and stores them in a list named `course_list`.
4. **Prepare Response**:
   - Sets the `Message` variable based on whether the course creation was successful or if an error occurred.
   - Renders the `createCourse.html` template with the `Message` and `course_list`.

## Edge Cases & Preconditions
- **Assumptions**: The `Admin` class has a method `createCourse` that can handle both string inputs for name and time. The time format must be "YYYY-MM-DD HR:MN:SC".
- **Potential Failure Modes**:
  - If the inputs are not strings, a `TypeError` will be raised.
  - If the time is not in the correct format, a `ValueError` will be raised.
- **Error Handling**: Specific exceptions (`TypeError` and `ValueError`) are caught and handled to provide user-friendly error messages.

## Result Synopsis
The method returns an HTTP response rendering the `createCourse.html` template with either a success message or an error message related to course creation. The template is passed a list of all courses in the database for display purposes.

## Docstring Draft
```python
"""Handles creating a new course from POST request data and renders the createCourse.html template.

Args:
    request (HttpRequest): The HTTP request object containing form data.

Returns:
    HttpResponse: An HTTP response rendering the createCourse.html template with a message.
"""
``````

## get  
``/Project/project_app/views.py``  
```def get(self, request):
        return render(request,"accountEdit.html",{})```  

**Documentation:**
```python## Overview
The code defines a method named `get` that handles HTTP GET requests for rendering the "accountEdit.html" template.

## Interface
- **Signature**: `def get(self, request)`
  - **Parameters**:
    | Name   | Type     | Purpose                 |
    |--------|----------|-------------------------|
    | self   |          | The class instance.       |
    | request| HttpRequest| The incoming HTTP request. |

## Inner Workings
- The method receives an `HttpRequest` object.
- It calls the `render` function to render the "accountEdit.html" template with an empty context dictionary `{}`.
- The rendered template is returned as an HttpResponse.

## Edge Cases & Preconditions
- Assumes that the "accountEdit.html" template exists in the correct directory structure.
- No assumptions about the state of the request or user authentication. It simply renders the specified template without any specific checks or actions based on the request content.

## Result Synopsis
The method returns an HttpResponse object containing the rendered version of "accountEdit.html".

## Docstring Draft
```python
"""Handles GET requests to render the account edit page.

Args:
    request (HttpRequest): The incoming HTTP request.

Returns:
    HttpResponse: A response containing the rendered 'accountEdit.html' template.
"""
``````

## post  
``/Project/project_app/views.py``  
```def post(self, request):
        username = request.session['name']
        field_to_change = request.POST.get("user-fields")
        new_value = request.POST.get("newEntry")

                                             
        user = User.objects.get(username=username)

        if field_to_change in ['phone', 'name', 'email', 'address']:
                                                             
            if field_to_change == 'name' and User.objects.filter(username=new_value).exclude(
                    username=user.username).exists():
                message = 'Username already exists'
            elif field_to_change == 'email' and User.objects.filter(email=new_value).exclude(
                    username=user.username).exists():
                message = 'Email already exists'
            else:
                setattr(user, field_to_change, new_value)
                user.save()
                message = 'Information updated successfully'
        else:
            message = 'Invalid field selected'

        return render(request, "accountEdit.html", {"Message": message})```  

**Documentation:**
```python## Overview
This code defines a `post` method within an unspecified class. The method handles a POST request to update user information in a web application.

## Interface
- **Signature**: `def post(self, request)`
- **Parameters**:
  | Name     | Type     | Purpose                             |
  |----------|----------|-------------------------------------|
  | `request` | `HttpRequest` | HTTP request object containing form data |

## Inner Workings
1. The method retrieves the username from the user's session.
2. It extracts the field to be changed and the new value from the POST request.
3. It fetches the current user instance based on the retrieved username.
4. If the field to change is one of `phone`, `name`, `email`, or `address`:
   - For the 'name' field, it checks if the new name already exists for another user and raises an error if so.
   - For the 'email' field, it checks if the new email already exists for another user and raises an error if so.
   - If no conflicts are found, it updates the specified field with the new value, saves the changes to the database, and sets a success message.
5. If the field to change is not one of the allowed fields, it sets an invalid field message.
6. Finally, it renders the `accountEdit.html` template, passing the appropriate message.

## Edge Cases & Preconditions
- The method assumes that the user's session contains a valid username and that POST data includes both `user-fields` and `newEntry`.
- It checks for duplicate usernames and emails to prevent conflicts.
- If an invalid field is selected, it sets an error message.

## Result Synopsis
The method returns an HTTP response rendering the `accountEdit.html` template with a message indicating whether the update was successful or if there was an error.

## Docstring Draft
```python
"""Handles POST request to update user information.

Args:
    request (HttpRequest): HTTP request object containing form data.

Returns:
    HttpResponse: Response rendering the account edit template with a success or error message.
"""
``````

## get  
``/Project/project_app/views.py``  
```def get(self, request):
        return render(request,"assignSection.html",{})```  

**Documentation:**
```python## Overview
This code defines a method `get` that handles HTTP GET requests to render an HTML template.

## Interface
**Signature**: 
```python
def get(self, request)
```

**Parameters**:
| Name     | Type   | Purpose                |
|----------|--------|--------------------------|
| request  | object | Django HttpRequest object|

## Inner Workings
- The method `get` is called when an HTTP GET request is made to the associated URL.
- It takes a single parameter, `request`, which is an instance of Django's `HttpRequest`.
- The method calls `render` from Django's templating system, passing it three arguments:
  - `request`: The original HttpRequest object.
  - `"assignSection.html"`: The name of the HTML template file to render.
  - `{}`: A dictionary containing context data to pass to the template. Currently, this dictionary is empty.

## Edge Cases & Preconditions
- This method does not have any parameters that could cause errors under normal circumstances.
- There are no assumptions being made about the state of the application or external systems.

## Result Synopsis
The method returns an HTTP response with the rendered HTML content from `assignSection.html`.

## Docstring Draft
```python
"""Handles an HTTP GET request by rendering the 'assignSection.html' template.

Args:
    request (HttpRequest): The current Django HttpRequest object.

Returns:
    HttpResponse: An HTTP response containing the rendered template.
"""
``````

## post  
``/Project/project_app/views.py``  
```def post(self, request):
        pass```  

**Documentation:**
```python## Overview
The code appears to define a method named `post`, which takes a `request` object as its parameter and does not currently implement any logic.

## Interface
- **Signature**: `post(self, request)`
  - **Parameters**:
    | Name   | Type   | Purpose                   |
    |--------|--------|---------------------------|
    | `self` | object | The instance of the class.|
    | `request`| object | A Django HTTP request object containing information about the client’s request |

## Inner Workings
- Currently, this method contains no code and simply passes.

## Edge Cases & Preconditions
- None are explicitly handled as there is no logic to trigger any potential issues.

## Result Synopsis
- This method currently does not return anything meaningful. It simply receives a request but does nothing with it.

## Docstring Draft
```python
"""Handles the post request for the view.

This method currently receives a Django HTTP request object but performs no actions.

Args:
    request (HttpRequest): The HTTP request object containing information about the client’s request.

Returns:
    None: This method does not return anything meaningful.
"""
``````

## get  
``/Project/project_app/views.py``  
```def get(self, request):
        user_list = list(User.objects.all())
        course_list = list(Course.objects.all())
        return render(request, "assignCourse.html", {"user_list": user_list, "course_list": course_list})```  

**Documentation:**
```python## Overview
This code defines a function that retrieves lists of users and courses from the database and passes them to a template for rendering.

## Interface
- **Signature**: `get(self, request)`
- **Parameters**:
  | Name   | Type     | Purpose                      |
  |--------|----------|------------------------------|
  | request| HttpRequest | The HTTP request object containing metadata about the incoming request. |

## Inner Workings
1. The function retrieves all users from the database using `User.objects.all()` and converts the queryset to a list.
2. It then retrieves all courses from the database using `Course.objects.all()` and also converts the queryset to a list.
3. Finally, it renders an HTML template named "assignCourse.html" with the user_list and course_list passed as context variables.

## Edge Cases & Preconditions
- The function assumes that there is at least one user and one course in the database.
- If the database is empty, both `user_list` and `course_list` will be empty lists.
- No specific error handling is provided for cases where database queries fail or return no results.

## Result Synopsis
The function returns an HTTP response rendering the "assignCourse.html" template with two context variables: `user_list` and `course_list`.

## Docstring Draft
```python
"""Retrieves all users and courses from the database and renders them in the 'assignCourse.html' template.

Args:
    request (HttpRequest): The HTTP request object containing metadata about the incoming request.

Returns:
    HttpResponse: An HTTP response rendering the 'assignCourse.html' template with user_list and course_list context variables.
"""
``````

## post  
``/Project/project_app/views.py``  
```def post(self, request):
        courseID = request.POST.get("courseID")
        userToFind = request.POST.get("userToFind")

        message = ''
        try:
            course = Course.objects.get(name=courseID)
            user = User.objects.get(username=userToFind)
            course.user_id = user
            course.save()
            message = 'Course assigned successfully'
        except Course.DoesNotExist:
            message = 'Course not found'
        except User.DoesNotExist:
            message = 'User not found'

        course_list = list(Course.objects.all())
        user_list = list(User.objects.all())
        userSkills = Skill.objects.filter(owner=user)                     

        return render(request, "assignCourse.html",
                      {"Message": message, "course_list": course_list, "user_list": user_list,
                       "userSkills": userSkills})```  

**Documentation:**
```python## Overview
The `post` function in the `views.py` file handles the assignment of a user to a course and renders an HTML template with relevant messages and lists.

## Interface
**Signature**: 
```python
def post(self, request)
```

**Parameters**:
| Name         | Type   | Purpose                                      |
|--------------|--------|----------------------------------------------|
| `self`       | object | The instance of the view class.              |
| `request`    | object | The HTTP request containing form data.     |

## Inner Workings
- Extracts `courseID` and `userToFind` from the POST request.
- Initializes an empty `message` string.
- Tries to retrieve a course with the provided name:
  - If successful, attempts to retrieve a user with the provided username.
    - If successful, assigns the retrieved user to the course and saves it, setting `message` to 'Course assigned successfully'.
    - If the user is not found, sets `message` to 'User not found'.
  - If the course is not found, sets `message` to 'Course not found'.
- Retrieves all courses and users from the database.
- Filters skills owned by the retrieved user.
- Renders the `assignCourse.html` template with the message, list of courses, list of users, and user's skills.

## Edge Cases & Preconditions
- Assumes that `courseID` is a string representing the name of an existing course.
- Assumes that `userToFind` is a string representing the username of an existing user.
- Handles cases where the specified course or user does not exist by setting appropriate error messages.

## Result Synopsis
The function returns an HTTP response rendering the `assignCourse.html` template with the following data:
- A message indicating whether the course was successfully assigned, or if errors occurred.
- A list of all courses in the database.
- A list of all users in the database.
- A filtered list of skills owned by the user.

## Docstring Draft
```python
"""Handles assigning a user to a course and renders an HTML template with relevant messages and lists.

Args:
    request (HttpRequest): The HTTP request containing form data.

Returns:
    HttpResponse: Renders the 'assignCourse.html' template with relevant data.
"""
``````

## get  
``/Project/project_app/views.py``  
```def get(self, request):
        ta1 = request.session["name"]
        mySkills = list(Skill.objects.filter(owner=User.objects.get(username=ta1)))
        return render(request, "addSkills.html", {"mySkills": mySkills})```  

**Documentation:**
```python## Overview
This function retrieves the skills of a user from the database and renders them in an HTML template.

## Interface
- **Signature**: `def get(self, request)`
- **Parameters**:
  | Name     | Type   | Purpose                 |
  |----------|--------|-------------------------|
  | `request` | object | The HTTP request object |

## Inner Workings
1. **Retrieve User from Session**: 
   - Extracts the username of the currently logged-in user from the session using `request.session["name"]`.
   
2. **Filter Skills**:
   - Uses Django's ORM to filter skills that belong to the user identified by the username retrieved above.
   - Retrieves the corresponding `User` object using `User.objects.get(username=ta1)`, where `ta1` is the username obtained from the session.
   - Filters the `Skill` objects based on this user with `Skill.objects.filter(owner=User.objects.get(username=ta1))`.

3. **Render Template**:
   - Converts the filtered skills into a list using `list()` to ensure they are in a form that can be passed to the template.
   - Renders the "addSkills.html" template, passing the list of skills as a context variable `mySkills`.

## Edge Cases & Preconditions
- **Assumptions**:
  - The session contains a key `"name"` with a valid username corresponding to an existing user in the database.
  - The `Skill` and `User` models are correctly set up with appropriate foreign keys and relationships.

- **Potential Failure Modes**:
  - If there is no `"name"` key in the session, accessing `request.session["name"]` will raise a `KeyError`.
  - If the username from the session does not correspond to an existing user, `User.objects.get(username=ta1)` will raise a `User.DoesNotExist` exception.

- **Error-Handling Logic**:
  The code does not explicitly handle these exceptions. In a production environment, proper error handling should be implemented using try-except blocks to catch and respond to potential errors gracefully.

## Result Synopsis
The function returns an HTTP response rendering the "addSkills.html" template with context data containing the skills of the currently logged-in user.

## Docstring Draft
```python
"""Retrieves the skills of the current user from the database and renders them in an HTML template.

Args:
    request (HttpRequest): The HTTP request object.

Returns:
    HttpResponse: A response rendering the "addSkills.html" template with context data containing the user's skills.

Raises:
    KeyError: If there is no 'name' key in the session.
    User.DoesNotExist: If the username from the session does not correspond to an existing user.
"""
``````

## post  
``/Project/project_app/views.py``  
```def post(self, request):
        ta1 = request.session["name"]
                                                           
        skill = request.POST.get('newSkill')
        Message= "Success!"
        mySkills = list(Skill.objects.filter(owner=User.objects.get(username=ta1)))
        if Ta().addSkills(skill, ta1):
            mySkills = list(Skill.objects.filter(owner=User.objects.get(username=ta1)))
        else:
            Message = "Failed to add skill"

        return render(request, "addSkills.html", {"Message": Message, "mySkills": mySkills})```  

**Documentation:**
```python## Overview
The `post` method handles a form submission where a new skill is added for the currently logged-in user. It updates the session with the updated list of skills and returns a response based on whether the skill addition was successful or not.

## Interface
- **Signature**: `def post(self, request)`
- **Parameters**:
  | Name      | Type     | Purpose                     |
  |-----------|----------|-----------------------------|
  | `request` | HttpRequest | The HTTP request object containing form data and session information. |

## Inner Workings
1. Extracts the current user's name from the session.
2. Retrieves the new skill submitted via POST request.
3. Initializes a success message.
4. Fetches the list of existing skills for the current user.
5. Calls `Ta().addSkills(skill, ta1)` to attempt adding the new skill.
6. If the skill is added successfully, fetches the updated list of skills.
7. If the skill addition fails, sets an error message.
8. Renders and returns the "addSkills.html" template with the updated message and skills list.

## Edge Cases & Preconditions
- Assumes that `request.session["name"]` exists and contains a valid username.
- Assumes that `request.POST.get('newSkill')` retrieves a non-empty skill name.
- Handles potential errors in the `Ta().addSkills(skill, ta1)` method by setting an error message if it fails.

## Result Synopsis
The function returns an HTTP response rendering the "addSkills.html" template with either a success or failure message and the updated list of skills for the current user.

## Docstring Draft
```python
"""Handles form submission to add a new skill for the logged-in user.

Args:
    request (HttpRequest): The HTTP request object containing form data and session information.

Returns:
    HttpResponse: A response rendering the "addSkills.html" template with a success or failure message and updated skills list.

Raises:
    KeyError: If the current user's name is not found in the session.
"""
``````

## get  
``/Project/project_app/views.py``  
```def get(self, request):
        return render(request, "viewSkills.html", {})```  

**Documentation:**
```python## Overview
This code defines a view function for rendering an HTML template named `viewSkills.html`.

## Interface
- **Signature**: `get(self, request)`
- **Parameters**:
  | Name     | Type    | Purpose                 |
  |----------|---------|-------------------------|
  | request  | HttpRequest | The HTTP request object |

## Inner Workings
1. The function is called when handling a GET request.
2. It takes the `request` parameter, which represents the current HTTP request.
3. It calls the `render` function from Django's templating system to render the `viewSkills.html` template with an empty context dictionary `{}`.

## Edge Cases & Preconditions
- No assumptions are made about the content of the `request` object beyond it being a valid `HttpRequest`.
- The function does not handle any potential errors that might occur during the rendering process, such as issues with the template file or data type mismatches in the context dictionary.
- If an error occurs while rendering the template, Django's default error handling will take over.

## Result Synopsis
The function returns an HTTP response object containing the rendered `viewSkills.html` template, effectively serving the skills view to the user.

## Docstring Draft
```python
"""
Renders the 'viewSkills.html' template for displaying skills information.

Args:
    request (HttpRequest): The HTTP request object.

Returns:
    HttpResponse: An HTTP response containing the rendered template.
"""
``````

## post  
``/Project/project_app/views.py``  
```def post(self, request):
        user = request.POST.get("userToFind")
        message = ''
        try:
            mySkills = list(Skill.objects.filter(owner=User.objects.get(username=user, user_type='ta')))
        except Exception as e:
            message = str(e)
            return render(request, "viewSkills.html", {"userSkills": "", "Message": message})
        return render(request, "viewSkills.html", {"userSkills": mySkills, "Message": message})```  

**Documentation:**
```python## Overview
This code processes a POST request to retrieve skills associated with a user specified in the request. It then renders a template with the retrieved skills and any error messages.

## Interface
### Signature
```python
def post(self, request):
```
- **Parameters**:
  | Name   | Type    | Purpose                        |
  |--------|---------|--------------------------------|
  | `request` | HttpRequest | The HTTP request object containing user data. |

## Inner Workings
1. **Retrieve User Data**: Extracts the username of the user to find from the POST request.
2. **Initialize Message**: Sets an initial empty message string.
3. **Fetch Skills**:
   - Attempts to retrieve skills associated with the specified user who has a `user_type` of 'ta'.
   - If successful, it converts the queryset to a list and assigns it to `mySkills`.
4. **Error Handling**:
   - If an exception occurs during the retrieval process (e.g., user not found), catches the exception, captures its message as `message`, and sets `mySkills` to an empty list.
5. **Render Template**: Renders the "viewSkills.html" template with the skills data and error message.

## Edge Cases & Preconditions
- The function assumes that there is a model named `Skill` and it has a foreign key relationship with a `User` model.
- If the user specified in the request does not exist or does not have a `user_type` of 'ta', an exception may be raised, which is caught and handled by setting an error message.
- The function requires that the POST request contains a parameter named "userToFind".

## Result Synopsis
The function returns an HTTP response rendering the "viewSkills.html" template with either the retrieved skills or an error message.

## Docstring Draft
```python
"""
Handles the POST request to retrieve and display user skills.

Args:
    request (HttpRequest): The HTTP request object containing user data.

Returns:
    HttpResponse: A response rendering the "viewSkills.html" template.

Raises:
    ValueError: If any exception occurs during skill retrieval, e.g., user not found.
"""
``````

## get  
``/Project/project_app/views.py``  
```def get(self, request):
        user_to_find = request.GET.get('userToFind')
        mySkills = list(Skill.objects.filter(owner=User.objects.get(username=user_to_find, user_type='ta')))
        return render(request, "viewSkills.html", {"accounts": mySkills})```  

**Documentation:**
```python## Overview
This code defines a method `get` in a class that handles a request to retrieve and display the skills of a specific user.

## Interface
- **Signature**: 
  ```python
  def get(self, request)
  ```
- **Parameters**:
  | Name      | Type   | Purpose                     |
  |-----------|--------|-----------------------------|
  | `request` | `HttpRequest` | The HTTP request object containing the query parameters. |

## Inner Workings
1. The method retrieves a value for the parameter `userToFind` from the GET request.
2. It then queries the database to find all skills associated with a user whose username matches `user_to_find` and has a user type of 'ta'.
3. The results are stored in the list `mySkills`.
4. Finally, it renders a template named "viewSkills.html" with the context containing the `mySkills`.

## Edge Cases & Preconditions
- **Assumptions**:
  - The request contains a parameter `userToFind`.
  - There is a user in the database with the specified username and user type.
  - The `Skill` model has a foreign key relationship to the `User` model.

- **Potential Failure Modes**:
  - If no `userToFind` parameter is provided, `request.GET.get('userToFind')` will return `None`.
  - If there is no user matching the specified username and user type, `Skill.objects.filter()` will return an empty queryset.
  - If the `User` or `Skill` models are not properly defined in the database schema.

- **Error Handling**:
  - The code does not explicitly handle errors related to the database query. However, if a database-related error occurs (e.g., connection issues), it would typically raise an exception that is propagated up the call stack.

## Result Synopsis
The method returns an HTTP response rendering the "viewSkills.html" template with context data containing the skills of the specified user.

## Docstring Draft
```python
"""Handles a request to retrieve and display the skills of a specific user.

Args:
    request (HttpRequest): The HTTP request object containing the query parameters.

Returns:
    HttpResponse: A rendered HTTP response displaying the skills of the specified user.
"""
``````

## post  
``/Project/project_app/views.py``  
```def post(self, request):
        userToFind = request.POST.get('userToFind')
        Message = "User found"

        if Admin().searchUser(userToFind):
            ta_user = User.objects.get(username=userToFind, user_type='ta')
            mySkills = list(Skill.objects.filter(owner=ta_user))
        else:
            Message = "No user found"

        return render(request, "viewSkills.html", {"Message": Message, "mySkills": mySkills})```  

**Documentation:**
```python## Overview
This code handles a POST request to search for a user and display their skills if the user is found.

## Interface
- **Signature**: `def post(self, request)`
- **Parameters**:
  | Name   | Type   | Purpose            |
  |--------|--------|--------------------|
  | request| HttpRequest | The incoming HTTP request object. |

## Inner Workings
1. Extracts the username to search for from the POST data.
2. Initializes a message indicating "User found".
3. Checks if the user exists using `Admin().searchUser(userToFind)`.
4. If the user exists, retrieves the associated TA user and their skills.
5. If the user does not exist, changes the message to "No user found".
6. Renders the "viewSkills.html" template with the message and skills.

## Edge Cases & Preconditions
- **Assumptions**:
  - The `Admin().searchUser` method correctly identifies the user based on the provided username.
  - The `User.objects.get` method can find a user with the specified username and type.
  - The `Skill.objects.filter` method returns skills associated with the user.
  
- **Potential Failure Modes**:
  - If `Admin().searchUser` returns `False`, it may indicate that the user does not exist or an error occurred during the search.
  - If `User.objects.get` raises a `DoesNotExist` exception, it indicates that no user with the specified username and type was found.
  
- **Error Handling**:
  - The code does not explicitly handle exceptions. It relies on Django's default behavior for rendering templates when an exception occurs.

## Result Synopsis
The function returns an HTTP response rendering the "viewSkills.html" template, which displays a message indicating whether a user was found and, if so, their skills.

## Docstring Draft
```python
"""Handles a POST request to search for a user and display their skills.

Args:
    request (HttpRequest): The incoming HTTP request object containing user data.

Returns:
    HttpResponse: A response rendering the "viewSkills.html" template with a message and skills.
"""
``````

## Migration  
``/Project/project_app/migrations/0001_initial.py``  
```class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('dateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('user_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionName', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_app.course')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_app.user'),
        ),
    ]```  

**Documentation:**
```python## Overview
This code defines a Django migration for creating several models in a database schema.

## Interface
- **Signature**: class Migration(migrations.Migration)
- **Parameters**:
  | Name         | Type   | Purpose                          |
  |--------------|--------|----------------------------------|
  | initial      | bool   | Indicates if this is the initial migration. |
  | dependencies | list   | List of dependencies for this migration. |

## Inner Workings
1. **Migration Initialization**: The `Migration` class inherits from `migrations.Migration`, indicating that it's a Django migration.
2. **Model Creation**:
   - **Course**: A model representing courses with fields like `id`, `name`, and `dateTime`.
   - **User**: A model for users with fields such as `id`, `username`, `password`, etc.
   - **Skill**: A model for skills linked to a user.
   - **Section**: A model for sections within a course or owned by a user, with optional foreign keys to both the course and the user.
3. **Foreign Key Relationships**:
   - Some models have foreign key relationships to other models (e.g., `Skill` references `User`, `Section` can reference `Course` and `User`).

## Edge Cases & Preconditions
- The migration is set as initial, meaning it's meant to be run for the first time.
- There are no explicit dependencies listed, which might imply that this migration does not depend on any other migrations.
- Foreign key relationships allow for null values, indicating optional associations.

## Result Synopsis
This code sets up a Django database schema with models for `Course`, `User`, `Skill`, and `Section`, establishing necessary foreign key relationships between them.

## Docstring Draft
```python
"""
Initial migration for creating the basic models of the application.

This migration sets up the database schema for core entities such as Course, User, Skill,
and Section. Each model is designed to represent different aspects of the application's data.

Args:
    initial (bool): Indicates if this is the first-time migration.
    dependencies (list): List of migration dependencies.

Returns:
    None

Raises:
    None
"""
``````

## user  
``/Project/project_app/classes/user.py``  
```class user(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def login(self, name, password):
        pass

    @abstractmethod
    def viewMyInfo(self, name, password):
        pass

    @abstractmethod
    def searchCourse(self,course):
        pass

    @abstractmethod
    def searchUser(self, name):
        pass

    @abstractmethod
    def editInfo(self, username, new_phone, new_name, new_email, new_address ):
        pass```  

**Documentation:**
```python## Overview
- This code defines an abstract base class `user` with several methods that need to be implemented by concrete user types.

## Interface
- **Signature**: 
  ```python
  class user(ABC):
      def __init__(self):
          pass

      @abstractmethod
      def login(self, name, password):
          pass

      @abstractmethod
      def viewMyInfo(self, name, password):
          pass

      @abstractmethod
      def searchCourse(self, course):
          pass

      @abstractmethod
      def searchUser(self, name):
          pass

      @abstractmethod
      def editInfo(self, username, new_phone, new_name, new_email, new_address ):
          pass
  ```
- **Parameters**:
    - `name` (str): Typically a username or user identifier.
    - `password` (str): The password for the user account.
    - `course` (str): A course name to search for.
    - `new_phone` (str): New phone number.
    - `new_name` (str): New name.
    - `new_email` (str): New email address.
    - `new_address` (str): New address.

## Inner Workings
- The class `user` is an abstract base class (ABC) that defines a template for user-related operations. Each method marked with `@abstractmethod` must be implemented by any concrete subclass of `user`.
  - `login`: Authenticates a user based on the provided name and password.
  - `viewMyInfo`: Returns or displays information about the logged-in user.
  - `searchCourse`: Searches for courses based on a given course name.
  - `searchUser`: Searches for users by their names.
  - `editInfo`: Updates the information of an existing user, such as phone number, name, email, and address.

## Edge Cases & Preconditions
- The methods assume that the inputs are valid and correctly formatted.
- There is no explicit error handling in the abstract base class itself. Error handling should be implemented by subclasses or when specific methods are called.
- Each method assumes that it will receive the correct types of parameters (e.g., strings for names, passwords, courses).

## Result Synopsis
- The code does not return any values directly; instead, it enforces the implementation of various user-related operations through abstract methods. Subclasses will need to provide concrete implementations for these methods.

## Docstring Draft
```python
"""Abstract base class defining user-related operations.

Methods:
    login: Authenticates a user.
    viewMyInfo: Displays or returns information about the user.
    searchCourse: Searches for courses by name.
    searchUser: Searches for users by name.
    editInfo: Updates user information such as phone, name, email, and address.
"""
``````

## __init__  
``/Project/project_app/classes/user.py``  
```def __init__(self):
        pass```  

**Documentation:**
```python## Overview
The code initializes a new instance of the `User` class. This function does not take any parameters and performs no operations.

## Interface
- **Signature**: `__init__(self)`
  - **Parameters**:
    - None

## Inner Workings
- The function is the constructor for the `User` class.
- It currently contains a single statement: `pass`, which indicates that no actions are taken during initialization.

## Edge Cases & Preconditions
- There are no parameters, so there are no assumptions or preconditions to check.
- Since the function does nothing, there are no potential failure modes or error-handling logic.

## Result Synopsis
The function initializes a new instance of the `User` class without any side effects. It returns implicitly when the constructor completes.

## Docstring Draft
```python
"""Initializes a new User instance.

Args:
    None

Returns:
    None
"""
``````

## login  
``/Project/project_app/classes/user.py``  
```def login(self, name, password):
        pass```  

**Documentation:**
```python## Overview
This code defines a method for user login within an application. It takes in a username and password as parameters and processes the login attempt.

## Interface
- **Signature**: `login(self, name: str, password: str)`
- **Parameters**:
  | Name    | Type   | Purpose                |
  |---------|--------|--------------------------|
  | name    | str    | The username of the user |
  | password| str    | The password of the user |

## Inner Workings
- The function `login` is intended to be implemented by a subclass or object that has the responsibility of authenticating users.
- It currently does nothing (`pass`) and needs to be filled with logic to handle the login process, such as checking credentials against a database.

## Edge Cases & Preconditions
- **Preconditions**: Assumes `name` and `password` are non-empty strings. The actual implementation should validate these inputs.
- **Potential Failures**: If not implemented correctly, this method will fail silently or without proper error handling, leading to security vulnerabilities or user confusion.
- **Error Handling**: There is no error handling provided in the current implementation.

## Result Synopsis
The function does not return any value (`None`) and has no side effects unless properly implemented. The intended outcome is for it to authenticate a user based on the provided credentials.

## Docstring Draft
```python
"""Authenticate a user with the given username and password.

Args:
    name (str): The username of the user attempting to log in.
    password (str): The password of the user attempting to log in.

Returns:
    None

Raises:
    ValueError: If the input credentials are invalid or if there is an error during authentication.
"""
``````

## viewMyInfo  
``/Project/project_app/classes/user.py``  
```def viewMyInfo(self, name, password):
        pass```  

**Documentation:**
```python## Overview
- The code defines a method `viewMyInfo` within a class, presumably for user authentication or profile retrieval.

## Interface
- **Signature**: `def viewMyInfo(self, name, password)`
- **Parameters**:
  | Name   | Type | Purpose          |
  |--------|------|------------------|
  | `self` | obj  | The instance of the class. |
  | `name` | str  | The username or identifier for the user. |
  | `password` | str  | The password for the user. |

## Inner Workings
- The method `viewMyInfo` is currently empty and does not perform any operations.

## Edge Cases & Preconditions
- No specific assumptions are made, but typically such methods would include checks to validate inputs (e.g., non-empty strings).
- Potential failure modes without implementation include missing or incorrect parameters.
- Error handling is nonexistent, which could lead to runtime errors if the method is used with no proper input validation.

## Result Synopsis
- The function currently has no return value or side effects. It does nothing when called.

## Docstring Draft
```python
"""Retrieves user information based on provided credentials.

Args:
    self (obj): The instance of the class.
    name (str): The username or identifier for the user.
    password (str): The password for the user.

Returns:
    bool: Always returns False currently as the method is empty and does nothing.

Raises:
    ValueError: Not applicable as error handling is not implemented.
"""
``````

## searchCourse  
``/Project/project_app/classes/user.py``  
```def searchCourse(self,course):
        pass```  

**Documentation:**
```python## Overview
- The `searchCourse` method is intended to perform a search operation for courses based on the provided course name.

## Interface
| Parameter Name | Type  | Purpose                                      |
|----------------|-------|----------------------------------------------|
| self           | object| The instance of the class.                   |
| course         | str   | The name of the course to search for.          |

## Inner Workings
- This function is currently a placeholder and does not contain any logic or implementation.
- It is structured to accept an instance (`self`) and a course name as parameters.

## Edge Cases & Preconditions
- There are no specific preconditions or assumptions in this method as it's empty.
- Errors are not handled explicitly; the function simply passes without performing any operations.

## Result Synopsis
- The method does not return anything meaningful as it is currently unimplemented. It will not affect system state beyond leaving it unchanged.

## Docstring Draft
```python
"""Performs a search operation for courses based on the provided course name.

Args:
    self (User): The instance of the User class.
    course (str): The name of the course to search for.

Returns:
    None: The method does not return anything meaningful as it is unimplemented.

Raises:
    NotImplementedError: This method has not been implemented yet.
"""
``````

## searchUser  
``/Project/project_app/classes/user.py``  
```def searchUser(self, name):
        pass```  

**Documentation:**
```python## Overview
- The code defines a method to search for a user by their name within a class.

## Interface
- **Signature**: `def searchUser(self, name)`
  - **Parameters**:
    | Name  | Type   | Purpose          |
    |-------|--------|------------------|
    | `self` | object | The instance of the class. |
    | `name` | str    | The name of the user to search for. |

## Inner Workings
- This method is currently empty and does not perform any operations.

## Edge Cases & Preconditions
- Assumes that the `self` parameter is an instance of a class with appropriate attributes and methods.
- There are no parameters to validate or error conditions to handle since the method body is empty.

## Result Synopsis
- The method returns `None` as there is nothing computed or returned in the current implementation.

## Docstring Draft
```python
"""Search for a user by their name within the class.

Args:
    name (str): The name of the user to search for.

Returns:
    None: Since the method does not perform any operations, it returns None.
"""
``````

## editInfo  
``/Project/project_app/classes/user.py``  
```def editInfo(self, username, new_phone, new_name, new_email, new_address ):
        pass```  

**Documentation:**
```python## Overview
This function is intended to edit user information in a system. It takes parameters for the current username and new phone number, name, email, and address, but currently does nothing.

## Interface
- **Signature**: `def editInfo(self, username, new_phone, new_name, new_email, new_address)`
- **Parameters**:
  | Name         | Type   | Purpose                |
  |--------------|--------|--------------------------|
  | username     | str    | The current username of the user. |
  | new_phone    | str    | The new phone number for the user. |
  | new_name     | str    | The new name for the user.       |
  | new_email    | str    | The new email address for the user. |
  | new_address  | str    | The new address for the user.      |

## Inner Workings
- The function is currently empty and does not perform any operations.

## Edge Cases & Preconditions
- **Preconditions**: None explicitly checked in the provided code.
- **Assumptions**: It assumes that `username` is a valid identifier for an existing user.
- **Failure Modes**: Since no operation is performed, there are no failure modes to handle.
- **Error-Handling**: No error handling logic is implemented.

## Result Synopsis
The function does not return anything (`None`) and has no side effects.

## Docstring Draft
```python
"""Edit user information in the system.

Args:
    username (str): The current username of the user.
    new_phone (str): The new phone number for the user.
    new_name (str): The new name for the user.
    new_email (str): The new email address for the user.
    new_address (str): The new address for the user.

Returns:
    None: This function does not return anything.

Raises:
    ValueError: Not applicable as no operations are performed.
"""
``````

## Instructor  
``/Project/project_app/classes/instructor.py``  
```class Instructor(user):
    def login(self, name, password):
        if not isinstance(name, str): raise TypeError("Username must be a string")
        if not isinstance(password, str): raise TypeError("Password must be a string")
        try:
            myUser = User.objects.get(username=name)
        except User.DoesNotExist:
            return False
        if myUser.password == password:
            return True
        else:
            return False

    def editInfo(self, username, new_phone, new_name, new_email, new_address):
        pass

    def viewMyInfo(self, name, password):
        if isinstance(name, str) == False: raise TypeError("must be string")
        if isinstance(password, str) == False: raise TypeError("must be string")
        myUser = User.objects.filter(username=name)
        myUser = myUser.filter(password=password).first()
        return myUser

    def searchCourse(self,course):
        if isinstance(course, str) == False: raise TypeError("must be string")
        courseList = list(Course.objects.filter(name__exact=course))
        return (len(courseList) == 1)

    def searchUser(self, name):
        pass
    def assignSection(self, course, section, assignee):
        s = list(Section.objects.filter(sectionName__exact=section))
        c = list(Course.objects.filter(name__exact=course))
        u = list(User.objects.filter(username__exact=assignee))

        if len(u) == 0:                                                       
            raise ValueError("Assignee not found")
        else:
            myUser = u[0]

        if len(c) == 0:                                    
            raise ValueError("Course not found")

        if len(s) == 0:                                     
            raise ValueError("Section not found")

        for i in s:                                                                      
            if i.owner == c[0]:
                secToAssign = i
                break
            raise ValueError("Section entered is not a part of the course entered")                                 

        if secToAssign.user_id == myUser:                                        
            raise ValueError("Assignee is already assigned to this section")

        secToAssign.user_id = myUser
        secToAssign.save()
        return True```  

**Documentation:**
```python## Overview
This code defines an `Instructor` class that extends a base `user` class. The class provides methods for logging in, editing information, viewing user info, searching courses, and assigning sections.

## Interface
- **Signature**: `class Instructor(user)`
- **Parameters**:
  - None

## Inner Workings
- The `login` method checks if the provided username and password match an existing user's credentials.
- The `editInfo` method is a placeholder for editing user information.
- The `viewMyInfo` method retrieves a user's information based on the provided username and password.
- The `searchCourse` method checks if a course exists by name.
- The `searchUser` method is a placeholder for searching users.
- The `assignSection` method assigns an assignee to a section of a course, checking for various conditions such as existence of user, course, and section, and whether the assignee is already assigned to the section.

## Edge Cases & Preconditions
- The code assumes that the `User`, `Course`, and `Section` models have certain fields (`username`, `password`, `name`, `sectionName`, `owner`, `user_id`) which are used for filtering.
- Errors are handled through exceptions such as `TypeError` and `ValueError`.
- It is expected that the input parameters (`name`, `password`, `new_phone`, `new_name`, `new_email`, `new_address`, `course`, `section`, `assignee`) are strings.

## Result Synopsis
The `login` method returns a boolean indicating whether the login credentials are correct. The `viewMyInfo` method returns a user object if the provided credentials are valid, otherwise it returns `None`. The `searchCourse` and `assignSection` methods return booleans indicating success or failure, while others do not return anything.

## Docstring Draft
```python
"""Instructor class with methods for managing users and course sections.

Methods:
    login(name: str, password: str) -> bool: Check if the provided credentials are correct.
    editInfo(username: str, new_phone: str, new_name: str, new_email: str, new_address: str) -> None: Edit user information (placeholder).
    viewMyInfo(name: str, password: str) -> User: Retrieve user information based on credentials.
    searchCourse(course: str) -> bool: Check if a course exists by name.
    searchUser(name: str) -> None: Search for users (placeholder).
    assignSection(course: str, section: str, assignee: str) -> bool: Assign an assignee to a section of a course.
"""
``````

## login  
``/Project/project_app/classes/instructor.py``  
```def login(self, name, password):
        if not isinstance(name, str): raise TypeError("Username must be a string")
        if not isinstance(password, str): raise TypeError("Password must be a string")
        try:
            myUser = User.objects.get(username=name)
        except User.DoesNotExist:
            return False
        if myUser.password == password:
            return True
        else:
            return False```  

**Documentation:**
```python## Overview
The `login` method is used to authenticate a user by checking the provided username and password against the stored user data.

## Interface
- **Signature**: `def login(self, name: str, password: str) -> bool`
- **Parameters**:
  | Name     | Type   | Purpose                         |
  |----------|--------|---------------------------------|
  | name     | str    | The username of the user to log in. |
  | password | str    | The password of the user to log in. |

## Inner Workings
1. **Type Checking**: The method first checks if `name` and `password` are both strings using `isinstance`. If not, it raises a `TypeError`.
2. **User Retrieval**: It attempts to retrieve a `User` object from the database where the username matches the provided `name`.
   - If the user does not exist (`User.DoesNotExist`), the method returns `False`.
3. **Password Comparison**: If the user exists, it compares the provided `password` with the stored password of the retrieved user.
   - If they match, the method returns `True`.
   - If they do not match, the method returns `False`.

## Edge Cases & Preconditions
- The method assumes that the input `name` and `password` are strings. If not, it will raise a `TypeError`.
- If no user with the provided username exists in the database, the method returns `False`.
- If the password does not match the stored password for the given username, the method also returns `False`.

## Result Synopsis
The method returns `True` if the user is successfully authenticated (i.e., the username and password match), otherwise it returns `False`.

## Docstring Draft
```python
"""Authenticates a user by checking the provided username and password.

Args:
    name (str): The username of the user to log in.
    password (str): The password of the user to log in.

Returns:
    bool: True if authentication is successful, False otherwise.

Raises:
    TypeError: If `name` or `password` is not a string.
"""
``````

## editInfo  
``/Project/project_app/classes/instructor.py``  
```def editInfo(self, username, new_phone, new_name, new_email, new_address):
        pass```  

**Documentation:**
```python## Overview
- This code defines a method `editInfo` in a class that appears to be used to update user information such as phone number, name, email, and address.

## Interface
- **Signature**: 
  ```python
  def editInfo(self, username, new_phone, new_name, new_email, new_address):
  ```
- **Parameters**:
  | Name         | Type   | Purpose                          |
  |--------------|--------|----------------------------------|
  | `self`       | object | The instance of the class.       |
  | `username`   | str    | The username of the user.        |
  | `new_phone`  | str    | The new phone number to update.  |
  | `new_name`   | str    | The new name to update.          |
  | `new_email`  | str    | The new email to update.         |
  | `new_address`| str    | The new address to update.       |

## Inner Workings
- The current implementation of the function is empty (`pass`). This means that no actions are taken when this method is called.

## Edge Cases & Preconditions
- **Assumptions**: No assumptions are made about the input parameters.
- **Potential Failure Modes**: None, as the function does nothing.
- **Error-Handling Logic**: None, as there is no error handling code.

## Result Synopsis
- The function currently has no effect and returns `None` by default if it were to have a return statement. If it had a return statement, it would return whatever value was specified in the return clause.

## Docstring Draft
```python
"""Updates user information such as phone number, name, email, and address.

Args:
    self (object): The instance of the class.
    username (str): The username of the user.
    new_phone (str): The new phone number to update.
    new_name (str): The new name to update.
    new_email (str): The new email to update.
    new_address (str): The new address to update.

Returns:
    None: This method does not return any value.

Raises:
    ValueError: Not applicable in this current implementation.
"""
``````

## viewMyInfo  
``/Project/project_app/classes/instructor.py``  
```def viewMyInfo(self, name, password):
        if isinstance(name, str) == False: raise TypeError("must be string")
        if isinstance(password, str) == False: raise TypeError("must be string")
        myUser = User.objects.filter(username=name)
        myUser = myUser.filter(password=password).first()
        return myUser```  

**Documentation:**
```python## Overview
- The `viewMyInfo` function is designed to retrieve user information from a database based on provided username and password.

## Interface
- **Signature**: 
  ```python
  def viewMyInfo(self, name, password)
  ```
- **Parameters**:
  | Name     | Type   | Purpose                 |
  |----------|--------|-------------------------|
  | `name`   | str    | The username of the user. |
  | `password` | str  | The password of the user. |

## Inner Workings
- The function first checks if both `name` and `password` are strings. If either is not a string, it raises a `TypeError`.
- It then queries the database for users where the username matches `name`.
- From these filtered results, it further filters to find the user whose password also matches `password`.
- The function returns the first matching user object or `None` if no match is found.

## Edge Cases & Preconditions
- **Assumptions**: 
  - Both `name` and `password` should be strings.
  - The database contains users with unique usernames and passwords.
- **Potential Failure Modes**:
  - If `name` or `password` are not provided as strings, a `TypeError` will be raised.
  - If no user matches the given username and password, the function returns `None`.
- **Error Handling**: 
  - The function raises a `TypeError` if the input types are incorrect.

## Result Synopsis
- The function returns a `User` object if a match is found; otherwise, it returns `None`.

## Docstring Draft
```python
"""Retrieves user information based on username and password.

Args:
    name (str): The username of the user.
    password (str): The password of the user.

Returns:
    User: A User object if a match is found; otherwise, None.

Raises:
    TypeError: When `name` or `password` is not a string.
"""
``````

## searchCourse  
``/Project/project_app/classes/instructor.py``  
```def searchCourse(self,course):
        if isinstance(course, str) == False: raise TypeError("must be string")
        courseList = list(Course.objects.filter(name__exact=course))
        return (len(courseList) == 1)```  

**Documentation:**
```python## Overview
This code defines a method `searchCourse` within an unspecified class. The purpose of this method is to check if there is exactly one course in the database with a name that matches the given string.

## Interface
- **Signature**: `def searchCourse(self, course)`
  - **Parameters**:
    | Name   | Type     | Purpose                     |
    |--------|----------|-----------------------------|
    | `course` | `str`    | The name of the course to search for. |

## Inner Workings
1. The method first checks if the `course` parameter is a string using `isinstance(course, str)`. If it is not a string, a `TypeError` is raised with the message "must be string".
2. It then queries the database for courses whose names exactly match the given `course` name using Django ORM (`Course.objects.filter(name__exact=course)`).
3. The results are converted to a list and stored in `courseList`.
4. Finally, the method returns `True` if there is exactly one course in the list (i.e., `len(courseList) == 1`), otherwise it returns `False`.

## Edge Cases & Preconditions
- **Assumptions**:
  - The `Course` model and its `name` field exist in the database.
  - The `filter` method of Django ORM works as expected.
  
- **Potential Failure Modes**:
  - If `course` is not a string, a `TypeError` will be raised.
  - If there are no courses or more than one course with the given name, the function will return `False`.

- **Error Handling**:
  - The method does not handle database-related errors (e.g., connection issues).
  - It does not handle cases where the `Course` model is not available.

## Result Synopsis
The function returns a boolean value indicating whether there is exactly one course in the database with the specified name. If the input is not a string, it raises a `TypeError`.

## Docstring Draft
```python
"""Checks if there is exactly one course with the given name.

Args:
    course (str): The name of the course to search for.

Returns:
    bool: True if exactly one course matches the given name, False otherwise.

Raises:
    TypeError: When `course` is not a string.
"""
``````

## searchUser  
``/Project/project_app/classes/instructor.py``  
```def searchUser(self, name):
        pass```  

**Documentation:**
```python## Overview
The `searchUser` method is intended to search for a user by their name within an application.

## Interface
- **Signature**: `searchUser(self, name)`
- **Parameters**:
  | Name | Type | Purpose |
  |------|------|---------|
  | `name` | str | The name of the user to search for. |

## Inner Workings
The current implementation of `searchUser` does nothing (`pass`). There is no data flow or control flow described.

## Edge Cases & Preconditions
- No assumptions or error handling are specified.
- The method currently does not perform any actions and returns without results.

## Result Synopsis
The method does not return anything meaningful. It simply passes through the call without performing any operations.

## Docstring Draft
```python
"""Search for a user by name within the application.

Args:
    name (str): The name of the user to search for.

Returns:
    None: The method does not return anything.
"""
``````

## assignSection  
``/Project/project_app/classes/instructor.py``  
```def assignSection(self, course, section, assignee):
        s = list(Section.objects.filter(sectionName__exact=section))
        c = list(Course.objects.filter(name__exact=course))
        u = list(User.objects.filter(username__exact=assignee))

        if len(u) == 0:                                                       
            raise ValueError("Assignee not found")
        else:
            myUser = u[0]

        if len(c) == 0:                                    
            raise ValueError("Course not found")

        if len(s) == 0:                                     
            raise ValueError("Section not found")

        for i in s:                                                                      
            if i.owner == c[0]:
                secToAssign = i
                break
            raise ValueError("Section entered is not a part of the course entered")                                 

        if secToAssign.user_id == myUser:                                        
            raise ValueError("Assignee is already assigned to this section")

        secToAssign.user_id = myUser
        secToAssign.save()
        return True```  

**Documentation:**
```python## Overview
This code defines a method `assignSection` in the `instructor.py` file of the `project_app/classes/instructor.py` module. The method assigns an instructor to a specific section of a course if the instructor is not already assigned to that section.

## Interface
- **Signature**: 
  ```python
  def assignSection(self, course, section, assignee)
  ```
- **Parameters**:
  | Name    | Type   | Purpose                                                                 |
  |---------|--------|-------------------------------------------------------------------------|
  | `course`  | str    | The name of the course.                                                   |
  | `section` | str    | The name of the section to be assigned.                                 |
  | `assignee` | str    | The username of the instructor to assign to the section.                 |

## Inner Workings
1. **Filter and Validate Inputs**:
   - Filters sections, courses, and users based on their names.
   - Raises a `ValueError` if any of the inputs (course, section, assignee) are not found.

2. **Ownership Check**:
   - Iterates through the sections to find one that matches the given course.
   - Raises a `ValueError` if no matching section is found or if the section is not part of the specified course.

3. **Assignment Logic**:
   - Checks if the assignee is already assigned to the section.
   - If the assignee is already assigned, raises a `ValueError`.
   - Otherwise, assigns the user to the section and saves the changes.

## Edge Cases & Preconditions
- **Assumptions**:
  - The inputs (course, section, assignee) are all strings representing valid identifiers for courses, sections, and users.
  - The database contains entries for all provided course, section, and user names.

- **Potential Failure Modes**:
  - If the course, section, or assignee is not found in the database, a `ValueError` is raised.
  - If the assignee is already assigned to the section, a `ValueError` is raised.

## Result Synopsis
The function returns `True` if the assignment is successful. It raises exceptions if any of the inputs are invalid or if the assignee is already assigned to the section.

## Docstring Draft
```python
"""Assigns an instructor to a specific section of a course.

Args:
    self (Instructor): The instance of the Instructor class.
    course (str): The name of the course.
    section (str): The name of the section to be assigned.
    assignee (str): The username of the instructor to assign to the section.

Returns:
    bool: True if the assignment is successful.

Raises:
    ValueError: If the course, section, or assignee is not found in the database.
    ValueError: If the assignee is already assigned to this section.
"""
``````

## Admin  
``/Project/project_app/classes/admin.py``  
```class Admin(user):

    def login(self, name, password):
        if not isinstance(name, str): raise TypeError("Username must be a string")
        if not isinstance(password, str): raise TypeError("Password must be a string")
        try:
            myUser = User.objects.get(username=name)
        except User.DoesNotExist:
            return False
        if myUser.password == password:
            return True
        else:
            return False


    def viewMyInfo(self, name, password):
        if isinstance(name, str) == False: raise TypeError("must be string")
        if isinstance(password, str) == False: raise TypeError("must be string")
        myUser = User.objects.filter(username=name)
        myUser = myUser.filter(password=password).first()
        return myUser

    def searchCourse(self,course):
        if isinstance(course, str) == False: raise TypeError("must be string")
        courseList = list(Course.objects.filter(name__exact=course))
        return (len(courseList) == 1)

    def searchUser(self, username):
        if not isinstance(username, str):
            raise TypeError("username must be a string")
        skillList = User.objects.filter(username=username, user_type='ta')
        return skillList
                                                             
    def createCourse(self, name, time):
        if isinstance(name, str) == False: raise TypeError("must be string")
        if isinstance(time, str) == False: raise TypeError("must be string")
        if datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S") == False: raise ValueError("must be string in datetime format")
        if self.searchCourse(name):
            return "Course already exists"

        Course.objects.create(name=name, dateTime=time)
        return "Course creation successful"
                                           
                                          


    def create_account(self, username, password, email):
        if not isinstance(username, str) or not isinstance(password, str) or not isinstance(email, str):
            raise TypeError("Invalid argument type")

                                                                                          

                                                             
                          
        if User.objects.filter(username=username).exists():
            return False
        else:
            account = User.objects.create(username=username, password=password, email=email)
            return True

    def delete_account(self, username):
        if not isinstance(username, str):
            raise TypeError("Invalid argument type")

        try:
            account = User.objects.get(username=username)
            account.delete()
            return True
        except User.DoesNotExist:
            return False

    def createSection(self, courseID, sectionID):
        if not isinstance(courseID, str) or not isinstance(sectionID, str):
            raise TypeError("Invalid argument type")
        if self.searchCourse(courseID):
            secCourse = list(Course.objects.filter(name__exact=courseID))[0]
        else:
            raise ValueError("Course not found in database")

        if len(list(Section.objects.filter(sectionName=sectionID))) != 0:
            raise ValueError("Duplicate section found in database")

        Section.objects.create(sectionName=sectionID, owner=secCourse)
        return True

    def viewSkills(self, ta):
        pass

    def editInfo(self, username, new_phone, new_name, new_email, new_address):
        if not isinstance(username, str) or not isinstance(new_phone, str) or not isinstance(new_name, str) or not isinstance(new_email, str) or not isinstance(new_address, str):
            raise TypeError("Invalid argument type")

        try:
            user_to_update = User.objects.get(username=username)

                                                    
            if User.objects.filter(username=new_name).exclude(username=username).exists():
                raise ValueError("Username already exists")
            if User.objects.filter(email=new_email).exclude(username=username).exists():
                raise ValueError("Email already exists")

            user_to_update.phone = new_phone
            user_to_update.username = new_name
            user_to_update.email = new_email
            user_to_update.address = new_address
            user_to_update.save()
            return True

        except User.DoesNotExist:
            raise ValueError("User not found in database")


    def assignCourse(self, assignee_username, course_name):
                              
        if not isinstance(assignee_username, str):
            raise TypeError("assignee_username must be a string")
        if not isinstance(course_name, str):
            raise TypeError("course_name must be a string")

                                                           
        try:
            user = User.objects.get(username=assignee_username)
        except User.DoesNotExist:
            raise ValueError(f"User '{assignee_username}' not found in database")

        try:
            course = Course.objects.get(name=course_name)
        except Course.DoesNotExist:
            raise ValueError(f"Course '{course_name}' not found in database")

                                                             
        if course.user_id == user:
            raise ValueError(f"User '{assignee_username}' is already assigned to course '{course_name}'")

                                                       
        course.user_id = user
        course.save()

                                
        return f"Course '{course_name}' assigned to user '{assignee_username}'"```  

**Documentation:**
```python## Overview
- The `Admin` class in the `admin.py` file provides methods for managing users and courses, including login verification, information retrieval, searching, creating, editing, and assigning.

## Interface
**Signature**: 
```python
class Admin(user):
```

**Parameters**:
| Name          | Type     | Purpose                                                                                           |
|---------------|----------|---------------------------------------------------------------------------------------------------|
| username      | str      | Username of the admin user.                                                                         |
| password      | str      | Password of the admin user.                                                                         |

## Inner Workings
- **login**: Verifies if a user exists and if the provided password matches.
  - Data flow: Takes `name` and `password`, checks if they are strings, retrieves the user from the database, compares passwords, returns `True` or `False`.
  - Control flow: Raises `TypeError` if inputs are not strings, handles `User.DoesNotExist` to return `False`.

- **viewMyInfo**: Retrieves a user's information based on provided credentials.
  - Data flow: Takes `name` and `password`, checks if they are strings, filters users by these criteria, returns the first matching user or `None`.
  - Control flow: Raises `TypeError` if inputs are not strings.

- **searchCourse**: Checks if a course exists in the database.
  - Data flow: Takes `course`, checks if it is a string, filters courses by name, returns `True` if exactly one course matches, otherwise `False`.
  - Control flow: Raises `TypeError` if input is not a string.

- **searchUser**: Retrieves users of type 'ta' with a given username.
  - Data flow: Takes `username`, checks if it is a string, filters users by username and type, returns the filtered queryset.
  - Control flow: Raises `TypeError` if input is not a string.

- **createCourse**: Creates a new course in the database.
  - Data flow: Takes `name` and `time`, checks if they are strings and valid datetime, checks if course already exists, creates and returns success message or "Course already exists".
  - Control flow: Raises `TypeError` for invalid input types, `ValueError` for invalid datetime format.

- **create_account**: Creates a new user account.
  - Data flow: Takes `username`, `password`, `email`, checks if they are strings, checks if username and email already exist, creates the user and returns `True`.
  - Control flow: Raises `TypeError` for invalid input types, `ValueError` for existing usernames or emails.

- **delete_account**: Deletes a user account.
  - Data flow: Takes `username`, checks if it is a string, deletes the user if exists and returns `True`, otherwise returns `False`.
  - Control flow: Raises `TypeError` for invalid input types, handles `User.DoesNotExist`.

- **createSection**: Creates a new section for an existing course.
  - Data flow: Takes `courseID` and `sectionID`, checks if they are strings, verifies course existence, checks for duplicate sections, creates the section and returns `True`.
  - Control flow: Raises `TypeError` for invalid input types, `ValueError` for non-existent courses or duplicate sections.

- **viewSkills**: (Not implemented) Placeholder method for viewing skills of TAs.

- **editInfo**: Updates user information.
  - Data flow: Takes `username`, new phone, name, email, address, checks if they are valid, updates the user's details and returns `True`.
  - Control flow: Raises `TypeError` for invalid input types, `ValueError` for existing usernames or emails.

- **assignCourse**: Assigns a course to a user.
  - Data flow: Takes `assignee_username` and `course_name`, checks if they are strings, verifies both users and courses exist, ensures the user is not already assigned the course, assigns the course and returns success message.
  - Control flow: Raises `TypeError` for invalid input types, `ValueError` for non-existent users or courses, or if the user is already assigned to the course.

## Edge Cases and Error Handling
- The class includes comprehensive error handling using `TypeError` and `ValueError` to ensure proper data integrity.
- Methods like `login`, `createCourse`, `create_account`, `delete_account`, `createSection`, and `editInfo` include checks for valid input types and handle specific exceptions related to database operations.```

## login  
``/Project/project_app/classes/admin.py``  
```def login(self, name, password):
        if not isinstance(name, str): raise TypeError("Username must be a string")
        if not isinstance(password, str): raise TypeError("Password must be a string")
        try:
            myUser = User.objects.get(username=name)
        except User.DoesNotExist:
            return False
        if myUser.password == password:
            return True
        else:
            return False```  

**Documentation:**
```python## Overview
This code defines the `login` method within a class, which authenticates a user by checking if the provided username and password match those stored in a database.

## Interface
- **Signature**: `def login(self, name, password)`
- **Parameters**:
  | Name   | Type   | Purpose                         |
  |--------|--------|-----------------------------------|
  | `name` | `str`  | The username of the user.         |
  | `password` | `str` | The password of the user.       |

## Inner Workings
1. **Type Checking**: The method first checks if both `name` and `password` are strings. If not, it raises a `TypeError`.
2. **User Retrieval**: It attempts to retrieve a `User` object from the database using the provided username.
   - If the user does not exist (`User.DoesNotExist`), the method returns `False`.
   - If the user exists, it proceeds to compare the password with the stored password.
3. **Password Verification**:
   - If the passwords match, the method returns `True`.
   - If the passwords do not match, the method returns `False`.

## Edge Cases & Preconditions
- **Type Error**: If either `name` or `password` is not a string, a `TypeError` will be raised.
- **User Not Found**: If no user with the given username exists in the database, the method returns `False`.
- **Password Mismatch**: If the provided password does not match the stored password, the method returns `False`.

## Result Synopsis
The function returns `True` if the provided username and password match those in the database, otherwise it returns `False`. It also raises a `TypeError` if the input types are incorrect.

## Docstring Draft
```python
"""Authenticate a user by checking the provided username and password against those stored in the database.

Args:
    name (str): The username of the user.
    password (str): The password of the user.

Returns:
    bool: True if authentication is successful, False otherwise.

Raises:
    TypeError: If `name` or `password` is not a string.
"""
``````

## viewMyInfo  
``/Project/project_app/classes/admin.py``  
```def viewMyInfo(self, name, password):
        if isinstance(name, str) == False: raise TypeError("must be string")
        if isinstance(password, str) == False: raise TypeError("must be string")
        myUser = User.objects.filter(username=name)
        myUser = myUser.filter(password=password).first()
        return myUser```  

**Documentation:**
```python## Overview
- This code defines a method `viewMyInfo` within a class that retrieves user information based on the provided username and password.

## Interface
- **Signature**: `def viewMyInfo(self, name: str, password: str)`
- **Parameters**:
  | Name    | Type   | Purpose                     |
  |---------|--------|-----------------------------|
  | `name`  | `str`  | The username to search for. |
  | `password` | `str` | The password corresponding to the username. |

## Inner Workings
- **Type Checking**: The method first checks if both `name` and `password` are strings. If not, it raises a `TypeError`.
- **Database Query**: It then constructs a query to find users in the database where the `username` matches `name`.
- **Password Filtering**: Further filters the results by checking if the `password` matches.
- **Result Handling**: The first matching user is returned using `.first()`. If no match is found, it returns `None`.

## Edge Cases & Preconditions
- **Type Error**: Raises a `TypeError` if either `name` or `password` is not a string.
- **No Match**: Returns `None` if no user with the specified username and password exists.

## Result Synopsis
- The method returns a `User` object if a matching user is found, otherwise returns `None`.

## Docstring Draft
```python
"""Retrieve user information based on username and password.

Args:
    name (str): The username to search for.
    password (str): The password corresponding to the username.

Returns:
    User: A User object if a match is found, otherwise None.

Raises:
    TypeError: If `name` or `password` is not a string.
"""
``````

## searchCourse  
``/Project/project_app/classes/admin.py``  
```def searchCourse(self,course):
        if isinstance(course, str) == False: raise TypeError("must be string")
        courseList = list(Course.objects.filter(name__exact=course))
        return (len(courseList) == 1)```  

**Documentation:**
```python## Overview
The `searchCourse` function is a method that checks if there is exactly one course with the given name in the database.

## Interface
- **Signature**: 
    ```python
    def searchCourse(self, course: str) -> bool:
    ```
- **Parameters**:
    | Name     | Type  | Purpose                     |
    |----------|-------|-----------------------------|
    | `course` | `str` | The name of the course to search for. |

## Inner Workings
1. The function first checks if the input `course` is a string using `isinstance(course, str)`.
   - If it's not a string, it raises a `TypeError` with the message "must be string".
2. It then filters the `Course` objects in the database where the name exactly matches the provided course name.
3. The filtered courses are converted to a list.
4. Finally, it checks if the length of this list is exactly one. If so, it returns `True`; otherwise, it returns `False`.

## Edge Cases & Preconditions
- **Assumptions**: The function assumes that the input `course` is a string. If not, it raises an error.
- **Potential Failure Modes**: 
  - If `course` is not a string, a `TypeError` will be raised.
  - If there are no courses with the exact name, or if multiple courses have the same name, the function will return `False`.
- **Error Handling Logic**: The function uses a type check to ensure that the input is a string. If it's not, an error is raised immediately.

## Result Synopsis
The function returns `True` if there is exactly one course with the given name in the database; otherwise, it returns `False`.

## Docstring Draft
```python
"""Checks if there is exactly one course with the given name in the database.

Args:
    course (str): The name of the course to search for.

Returns:
    bool: True if exactly one course matches the name, False otherwise.

Raises:
    TypeError: If `course` is not a string.
"""
``````

## searchUser  
``/Project/project_app/classes/admin.py``  
```def searchUser(self, username):
        if not isinstance(username, str):
            raise TypeError("username must be a string")
        skillList = User.objects.filter(username=username, user_type='ta')
        return skillList```  

**Documentation:**
```python## Overview
- This code defines a method to search for a user with a specific username who is of type 'ta' ( Teaching Assistant).

## Interface
- **Signature**: `def searchUser(self, username)`
  - **Parameters**:
    | Name   | Type | Purpose         |
    |--------|------|-----------------|
    | username | str  | The username to search for. Must be a string. |

## Inner Workings
- The method starts by checking if the `username` parameter is a string. If it's not, a `TypeError` is raised with a message indicating that the `username` must be a string.
- A query is performed using Django's ORM to filter users based on the provided `username` and `user_type='ta'`. This filters out only those users who are TAs.
- The method returns the filtered list of users.

## Edge Cases & Preconditions
- **Assumptions**:
  - The `User.objects.filter()` method is correctly implemented and works as expected with the given parameters.
- **Potential Failure Modes**:
  - If a non-string value is passed to the function, it will raise a `TypeError`.
- **Error Handling**:
  - The method handles type mismatches by raising a `TypeError`.

## Result Synopsis
- The function returns a list of users that match the given username and have a user type of 'ta'. If no such user exists or an invalid parameter is provided, it will raise an error.

## Docstring Draft
```python
"""
Searches for a user with the specified username who is of type 'ta'.

Args:
    username (str): The username to search for. Must be a string.

Returns:
    QuerySet: A queryset containing users that match the given username and are TAs.

Raises:
    TypeError: When `username` is not a string.
"""
``````

## createCourse  
``/Project/project_app/classes/admin.py``  
```def createCourse(self, name, time):
        if isinstance(name, str) == False: raise TypeError("must be string")
        if isinstance(time, str) == False: raise TypeError("must be string")
        if datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S") == False: raise ValueError("must be string in datetime format")
        if self.searchCourse(name):
            return "Course already exists"

        Course.objects.create(name=name, dateTime=time)
        return "Course creation successful"```  

**Documentation:**
```python## Overview
This function is designed to create a new course in the system. It checks for valid input types and formats, ensures the course name does not already exist, and creates the course if all conditions are met.

## Interface
- **Signature**: `createCourse(self, name, time)`
- **Parameters**:
  | Name     | Type   | Purpose                 |
  |----------|--------|-------------------------|
  | `name`   | str    | The name of the course.   |
  | `time`   | str    | The scheduled time for the course in "YYYY-MM-DD HH:MM:SS" format. |

## Inner Workings
1. **Type and Format Checks**:
   - Validates that both `name` and `time` are strings.
   - Attempts to parse `time` into a datetime object using the specified format. If parsing fails, it raises a `ValueError`.

2. **Course Existence Check**:
   - Calls `self.searchCourse(name)` to verify if a course with the same name already exists in the system.
   - If a course with the same name exists, it returns "Course already exists".

3. **Creating the Course**:
   - Uses Django ORM (`Course.objects.create`) to create a new course object with the provided `name` and `time`.
   - Returns "Course creation successful" upon successful creation.

## Edge Cases & Preconditions
- If `name` or `time` is not a string, it raises a `TypeError`.
- If `time` does not match the expected datetime format, it raises a `ValueError`.
- If a course with the same name already exists, it returns "Course already exists".

## Result Synopsis
The function either successfully creates a new course and returns "Course creation successful", or indicates an error if the course already exists or input types/formats are incorrect.

## Docstring Draft
```python
"""Create a new course in the system.

Args:
    name (str): The name of the course.
    time (str): The scheduled time for the course in "YYYY-MM-DD HH:MM:SS" format.

Returns:
    str: A message indicating success or failure.

Raises:
    TypeError: When `name` or `time` is not a string.
    ValueError: When `time` does not match the datetime format.
"""
``````

## create_account  
``/Project/project_app/classes/admin.py``  
```def create_account(self, username, password, email):
        if not isinstance(username, str) or not isinstance(password, str) or not isinstance(email, str):
            raise TypeError("Invalid argument type")

                                                                                          

                                                             
                          
        if User.objects.filter(username=username).exists():
            return False
        else:
            account = User.objects.create(username=username, password=password, email=email)
            return True```  

**Documentation:**
```python## Overview
This code defines a method to create a new user account in a system. It checks if the provided username already exists and creates a new account if it does not.

## Interface
- **Signature**: `def create_account(self, username: str, password: str, email: str) -> bool`
- **Parameters**:
  | Name     | Type   | Purpose                     |
  |----------|--------|-----------------------------|
  | username | str    | The username of the new account. |
  | password | str    | The password for the new account. |
  | email    | str    | The email address of the new account. |

## Inner Workings
- The function first checks if any of the provided arguments (`username`, `password`, `email`) are not strings, and raises a `TypeError` if so.
- It then checks if a user with the given username already exists in the database using Django's ORM (`User.objects.filter(username=username).exists()`).
  - If such a user exists, it returns `False`.
  - If no user exists with that username, it creates a new user account with the provided details using `User.objects.create(username=username, password=password, email=email)` and returns `True`.

## Edge Cases & Preconditions
- **Preconditions**: The function expects `username`, `password`, and `email` to be strings.
- **Potential Failure Modes**:
  - If any of the parameters are not strings, a `TypeError` is raised.
  - If a user with the given username already exists, the function returns `False`.
- **Error Handling**: The function does not handle other exceptions such as database errors.

## Result Synopsis
The function returns `True` if the account was successfully created, and `False` if a user with the same username already exists. It raises a `TypeError` if any of the input arguments are not strings.

## Docstring Draft
```python
"""Creates a new user account.

Args:
    username (str): The username for the new account.
    password (str): The password for the new account.
    email (str): The email address for the new account.

Returns:
    bool: True if the account was created, False if the username already exists.

Raises:
    TypeError: If any of the input arguments are not strings.
"""
``````

## delete_account  
``/Project/project_app/classes/admin.py``  
```def delete_account(self, username):
        if not isinstance(username, str):
            raise TypeError("Invalid argument type")

        try:
            account = User.objects.get(username=username)
            account.delete()
            return True
        except User.DoesNotExist:
            return False```  

**Documentation:**
```python## Overview
- The `delete_account` method is designed to remove a user account from the system based on the provided username.

## Interface
### Signature
```python
def delete_account(self, username)
```
### Parameters
| Name    | Type   | Purpose                           |
|---------|--------|-----------------------------------|
| username | str    | The username of the account to be deleted. |

## Inner Workings
- The method first checks if the `username` parameter is a string. If not, it raises a `TypeError`.
- It then attempts to retrieve the user object from the database using the provided `username`. If the user exists, it deletes the account and returns `True`.
- If the user does not exist in the database, the method catches the `User.DoesNotExist` exception and returns `False`.

## Edge Cases & Preconditions
- The method assumes that the `username` is a string. It raises a `TypeError` if this assumption is not met.
- If no account with the specified username exists, the method handles this gracefully by returning `False` without raising an error.

## Result Synopsis
- The function returns `True` if the account was successfully deleted, and `False` if no account with the given username exists.

## Docstring Draft
```python
"""Deletes a user account based on the provided username.

Args:
    username (str): The username of the account to be deleted.

Returns:
    bool: True if the account was successfully deleted, False otherwise.

Raises:
    TypeError: If the `username` is not a string.
"""
``````

## createSection  
``/Project/project_app/classes/admin.py``  
```def createSection(self, courseID, sectionID):
        if not isinstance(courseID, str) or not isinstance(sectionID, str):
            raise TypeError("Invalid argument type")
        if self.searchCourse(courseID):
            secCourse = list(Course.objects.filter(name__exact=courseID))[0]
        else:
            raise ValueError("Course not found in database")

        if len(list(Section.objects.filter(sectionName=sectionID))) != 0:
            raise ValueError("Duplicate section found in database")

        Section.objects.create(sectionName=sectionID, owner=secCourse)
        return True```  

**Documentation:**
```python## Overview
This code defines a method `createSection` within an admin class that creates a new section for a course if it does not already exist. It checks the validity of the input parameters and ensures that the course exists and no duplicate sections are created.

## Interface
- **Signature**: `def createSection(self, courseID, sectionID)`
- **Parameters**:
  | Name     | Type   | Purpose                        |
  |----------|--------|----------------------------------|
  | `courseID` | str    | The identifier of the course.      |
  | `sectionID` | str    | The identifier of the section to be created. |

## Inner Workings
- **Input Validation**: Checks if both `courseID` and `sectionID` are strings, raising a `TypeError` if not.
- **Course Existence Check**: Uses the `searchCourse` method (assumed to exist) to verify if the course exists in the database. If the course does not exist, it raises a `ValueError`.
- **Duplicate Section Check**: Queries the database for sections with the same name as `sectionID`. If any are found, it raises a `ValueError`.
- **Section Creation**: Creates a new section using Django's ORM and returns `True` upon successful creation.

## Edge Cases & Preconditions
- **Input Types**: Assumes both parameters are strings. Raises `TypeError` if not.
- **Course Existence**: Requires the course to be present in the database. Raises `ValueError` if not found.
- **Duplicate Sections**: Prevents duplicate sections from being created. Raises `ValueError` if a duplicate is detected.

## Result Synopsis
The function returns `True` if the section is successfully created, or raises appropriate errors for invalid inputs or existing sections.

## Docstring Draft
```python
"""Creates a new section for a course.

Args:
    courseID (str): The identifier of the course.
    sectionID (str): The identifier of the section to be created.

Returns:
    bool: True if the section is successfully created.

Raises:
    TypeError: When `courseID` or `sectionID` is not a string.
    ValueError: When `courseID` is not found in the database, or when a duplicate section exists.
"""
``````

## viewSkills  
``/Project/project_app/classes/admin.py``  
```def viewSkills(self, ta):
        pass```  

**Documentation:**
```python## Overview
This code defines a method named `viewSkills` within an unspecified class. The purpose of this method is to provide functionality for viewing skills related to a Teaching Assistant (TA).

## Interface
- **Signature**: `def viewSkills(self, ta)`
- **Parameters**:
  | Name | Type | Purpose |
  |------|------|---------|
  | `ta`   | Any  | The Teaching Assistant object whose skills are being viewed. |

## Inner Workings
The current implementation of the `viewSkills` method is entirely empty (`pass`). This suggests that no specific functionality has been implemented yet, and the method serves as a placeholder or stub.

## Edge Cases & Preconditions
- **Assumptions**: None explicitly stated.
- **Potential Failure Modes**: The method will not perform any operations because it is currently empty.
- **Error-Handling Logic**: The method does not contain any error-handling mechanisms.

## Result Synopsis
The method does not return any value (`None`) and has no side effects. It simply exists to be overridden or implemented in a subclass.

## Docstring Draft
```python
"""Displays the skills of a Teaching Assistant.

Args:
    ta (Any): The Teaching Assistant object whose skills are being viewed.

Returns:
    None

Raises:
    NotImplementedError: If this method is not implemented by subclasses.
"""
``````

## editInfo  
``/Project/project_app/classes/admin.py``  
```def editInfo(self, username, new_phone, new_name, new_email, new_address):
        if not isinstance(username, str) or not isinstance(new_phone, str) or not isinstance(new_name, str) or not isinstance(new_email, str) or not isinstance(new_address, str):
            raise TypeError("Invalid argument type")

        try:
            user_to_update = User.objects.get(username=username)

                                                    
            if User.objects.filter(username=new_name).exclude(username=username).exists():
                raise ValueError("Username already exists")
            if User.objects.filter(email=new_email).exclude(username=username).exists():
                raise ValueError("Email already exists")

            user_to_update.phone = new_phone
            user_to_update.username = new_name
            user_to_update.email = new_email
            user_to_update.address = new_address
            user_to_update.save()
            return True

        except User.DoesNotExist:
            raise ValueError("User not found in database")```  

**Documentation:**
```python## Overview
This code defines a method to edit user information in a system, ensuring that the username and email remain unique.

## Interface
- **Signature**: `editInfo(self, username: str, new_phone: str, new_name: str, new_email: str, new_address: str) -> bool`
- **Parameters**:
  | Name       | Type   | Purpose                 |
  |------------|--------|-------------------------|
  | username   | str    | Current user's username   |
  | new_phone  | str    | New phone number        |
  | new_name   | str    | New username            |
  | new_email  | str    | New email address         |
  | new_address| str    | New user address          |

## Inner Workings
1. **Type Checking**: The function checks if all input parameters are strings and raises a `TypeError` if any of them is not.
2. **Fetching User**: It attempts to retrieve the user with the given `username` from the database using Django ORM's `User.objects.get()`.
3. **Username Uniqueness Check**: Before updating the username, it checks if another user already exists with the new username (`new_name`). If so, it raises a `ValueError`.
4. **Email Uniqueness Check**: Similarly, it ensures that no other user has the same email as `new_email`. If such a user exists, it raises a `ValueError`.
5. **Updating User Information**: If all checks pass, it updates the user's phone number, username, email, and address.
6. **Saving Changes**: The updated user details are saved to the database using the `save()` method.
7. **Return Value**: The function returns `True` if the update is successful.

## Edge Cases & Preconditions
- **Type Mismatch**: If any of the parameters is not a string, a `TypeError` is raised.
- **User Not Found**: If no user exists with the given `username`, a `ValueError` indicating "User not found in database" is raised.
- **Duplicate Username**: If another user already has the same `new_name`, a `ValueError` stating "Username already exists" is thrown.
- **Duplicate Email**: If another user has the same `new_email`, a `ValueError` stating "Email already exists" is thrown.

## Result Synopsis
The function updates user information if all checks pass and returns `True`. It raises an error with an appropriate message in case of any failure (type mismatch, missing user, duplicate username, or duplicate email).

## Docstring Draft
```python
"""Edits the information of a user in the system.

Args:
    username (str): The current username of the user.
    new_phone (str): The new phone number to update.
    new_name (str): The new username to update.
    new_email (str): The new email address to update.
    new_address (str): The new address to update.

Returns:
    bool: True if the information is successfully updated, otherwise raises an error.

Raises:
    TypeError: If any of the arguments are not strings.
    ValueError: If the user does not exist, or if the username or email already exists for another user.
"""
``````

## assignCourse  
``/Project/project_app/classes/admin.py``  
```def assignCourse(self, assignee_username, course_name):
                              
        if not isinstance(assignee_username, str):
            raise TypeError("assignee_username must be a string")
        if not isinstance(course_name, str):
            raise TypeError("course_name must be a string")

                                                           
        try:
            user = User.objects.get(username=assignee_username)
        except User.DoesNotExist:
            raise ValueError(f"User '{assignee_username}' not found in database")

        try:
            course = Course.objects.get(name=course_name)
        except Course.DoesNotExist:
            raise ValueError(f"Course '{course_name}' not found in database")

                                                             
        if course.user_id == user:
            raise ValueError(f"User '{assignee_username}' is already assigned to course '{course_name}'")

                                                       
        course.user_id = user
        course.save()

                                
        return f"Course '{course_name}' assigned to user '{assignee_username}'"```  

**Documentation:**
```python## Overview
The `assignCourse` method assigns a course to a user, ensuring that the user and course exist in the database and that the user is not already assigned to the course.

## Interface
- **Signature**: `def assignCourse(self, assignee_username: str, course_name: str)`
- **Parameters**:
  | Name              | Type   | Purpose                          |
  |-------------------|--------|----------------------------------|
  | assignee_username | str    | Username of the user to assign.  |
  | course_name       | str    | Name of the course to assign.    |

## Inner Workings
1. **Parameter Validation**:
   - Checks if `assignee_username` and `course_name` are strings, raising a `TypeError` if not.
   
2. **Database Lookup**:
   - Attempts to retrieve a user from the database using `assignee_username`. If the user does not exist, raises a `ValueError`.
   - Attempts to retrieve a course from the database using `course_name`. If the course does not exist, raises a `ValueError`.

3. **Assignment Check**:
   - Checks if the user is already assigned to the course by comparing `user.id` with `course.user_id`. If they are the same, raises a `ValueError`.

4. **Course Assignment**:
   - Assigns the user to the course by setting `course.user_id = user`.
   - Saves the updated course in the database.

5. **Return Statement**:
   - Returns a string indicating successful assignment of the course to the user.

## Edge Cases & Preconditions
- The method assumes that `assignee_username` and `course_name` are non-empty strings.
- If the user or course does not exist, it raises a `ValueError`.
- If the user is already assigned to the course, it raises a `ValueError`.

## Result Synopsis
The function returns a string confirming the assignment of the course to the user. It modifies the database by updating the `user_id` field in the `Course` model.

## Docstring Draft
```python
"""Assigns a course to a user.

Args:
    assignee_username (str): Username of the user to assign.
    course_name (str): Name of the course to assign.

Returns:
    str: A confirmation message indicating successful assignment.

Raises:
    TypeError: If `assignee_username` or `course_name` is not a string.
    ValueError: If the user or course does not exist, or if the user is already assigned to the course.
"""
``````

## Ta  
``/Project/project_app/classes/ta.py``  
```class Ta(user):

    def login(self, name, password):
        if not isinstance(name, str): raise TypeError("Username must be a string")
        if not isinstance(password, str): raise TypeError("Password must be a string")
        try:
            myUser = User.objects.get(username=name)
        except User.DoesNotExist:
            return False
        if myUser.password == password:
            return True
        else:
            return False


    def viewMyInfo(self, name, password):
        if isinstance(name, str) == False: raise TypeError("must be string")
        if isinstance(password, str) == False: raise TypeError("must be string")
        myUser = User.objects.filter(username=name)
        myUser = myUser.filter(password=password).first()
        return myUser

    def searchCourse(self,course):
        if isinstance(course, str) == False: raise TypeError("must be string")
        courseList = list(Course.objects.filter(name__exact=course))
        return (len(courseList) == 1)

    def searchUser(self, name):
        pass

    def editInfo(self, username, new_phone, new_name, new_email, new_address ):
        pass

    def addSkills(self,skill, ta):
       if(User.objects.filter(username=ta) is None): return False
       print(User.objects.get(username=ta).user_type)
       print("TA")
       if((User.objects.get(username=ta).user_type) != "ta"): return False
       if(len(list((Skill.objects.filter(name=skill, owner=User.objects.get(username=ta)))))>0): return False
       Skill.objects.create(name=skill, owner=User.objects.get(username=ta))
       return True```  

**Documentation:**
```python## Overview
This class `Ta` provides methods for a Teaching Assistant to perform various actions such as logging in, viewing personal information, searching for courses and users, editing personal information, and adding skills.

## Interface
### Signature
```python
class Ta(user):
    def login(self, name: str, password: str) -> bool:
    def viewMyInfo(self, name: str, password: str) -> User:
    def searchCourse(self, course: str) -> bool:
    def searchUser(self, name: str) -> None:
    def editInfo(self, username: str, new_phone: str, new_name: str, new_email: str, new_address: str) -> None:
    def addSkills(self, skill: str, ta: str) -> bool:
```

### Parameters
| Name       | Type     | Purpose                           |
|------------|----------|-----------------------------------|
| name       | str      | Username or user information.     |
| password   | str      | Password for authentication.      |
| course     | str      | Course name to search.            |
| username   | str      | Username of the user.             |
| new_phone  | str      | New phone number.                 |
| new_name   | str      | New name.                         |
| new_email  | str      | New email address.                |
| new_address| str      | New address.                      |
| skill      | str      | Skill to be added.                |
| ta         | str      | Username of the Teaching Assistant |

## Inner Workings
- **login**: Validates user credentials and returns `True` if the login is successful, otherwise returns `False`.
  - **Data Flow**: Checks if the provided username and password match any existing user.
  - **Control Flow**: Raises a `TypeError` if `name` or `password` is not a string.

- **viewMyInfo**: Fetches user information based on credentials and returns it.
  - **Data Flow**: Filters users by username and password to find a matching user.
  - **Control Flow**: Raises a `TypeError` if `name` or `password` is not a string.

- **searchCourse**: Searches for a specific course and returns whether the course exists.
  - **Data Flow**: Filters courses by name.
  - **Control Flow**: Raises a `TypeError` if `course` is not a string.

- **addSkills**: Adds a skill to a Teaching Assistant's profile if they have the necessary permissions.
  - **Data Flow**: Checks if the provided username corresponds to a valid TA and if the skill already exists for that user.
  - **Control Flow**: Raises a `TypeError` if `skill` or `ta` is not a string.

## Edge Cases & Preconditions
- All input parameters must be strings. Non-string inputs will raise a `TypeError`.
- The `login` method checks if the provided username and password match any existing user.
- The `addSkills` method ensures that only TAs can add skills to their profiles and checks if the skill already exists.

## Result Synopsis
The `Ta` class provides methods for logging in, viewing personal information, searching for courses and users, editing personal information, and adding skills. Each method includes error handling for invalid input types.

## Docstring Draft
```python
"""Teaching Assistant operations for user management and course searches.

Args:
    name (str): Username or user information.
    password (str): Password for authentication.
    course (str): Course name to search.
    username (str): Username of the user.
    new_phone (str): New phone number.
    new_name (str): New name.
    new_email (str): New email address.
    new_address (str): New address.
    skill (str): Skill to be added.
    ta (str): Username of the Teaching Assistant.

Returns:
    bool: True if login or addSkills is successful, User object for viewMyInfo, otherwise None.
    
Raises:
    TypeError: If input parameters are not strings.
    ValueError: When `foo` is negative.
"""
``````

## login  
``/Project/project_app/classes/ta.py``  
```def login(self, name, password):
        if not isinstance(name, str): raise TypeError("Username must be a string")
        if not isinstance(password, str): raise TypeError("Password must be a string")
        try:
            myUser = User.objects.get(username=name)
        except User.DoesNotExist:
            return False
        if myUser.password == password:
            return True
        else:
            return False```  

**Documentation:**
```python## Overview
- This function checks whether the provided username and password match those of an existing user in the system.

## Interface
**Signature**: `def login(self, name: str, password: str) -> bool`
**Parameters**:
| Name    | Type   | Purpose                     |
|---------|--------|-----------------------------|
| name    | str    | The username provided by the caller. |
| password | str  | The password provided by the caller. |

## Inner Workings
- **Type Checking**: Validates that `name` and `password` are both strings, raising a `TypeError` if not.
- **User Lookup**: Tries to fetch a user object from the database using the provided username.
  - If the user exists (`User.DoesNotExist` is not raised), proceeds to check the password.
  - If the user does not exist, returns `False`.
- **Password Verification**: Compares the provided password with the stored password of the retrieved user.
  - If they match, returns `True`.
  - If they do not match, returns `False`.

## Edge Cases & Preconditions
- **Type Errors**: The function assumes that both `name` and `password` are strings. Providing non-string types will raise a `TypeError`.
- **User Existence**: If no user with the provided username exists in the database, the function will return `False`.
- **Password Accuracy**: If the password is incorrect, regardless of whether the user exists or not, the function returns `False`.

## Result Synopsis
- The function returns `True` if the provided username and password match those of an existing user, otherwise it returns `False`.

## Docstring Draft
```python
"""Check if the provided username and password match those of an existing user.

Args:
    name (str): The username to check.
    password (str): The password to verify.

Returns:
    bool: True if the credentials are correct, False otherwise.

Raises:
    TypeError: If `name` or `password` is not a string.
"""
``````

## viewMyInfo  
``/Project/project_app/classes/ta.py``  
```def viewMyInfo(self, name, password):
        if isinstance(name, str) == False: raise TypeError("must be string")
        if isinstance(password, str) == False: raise TypeError("must be string")
        myUser = User.objects.filter(username=name)
        myUser = myUser.filter(password=password).first()
        return myUser```  

**Documentation:**
```python## Overview
The `viewMyInfo` function is designed to retrieve user information from a database based on the provided username and password. It ensures that both inputs are strings before querying the database.

## Interface
- **Signature**: `def viewMyInfo(self, name, password)`
- **Parameters**:
  | Name   | Type   | Purpose                |
  |--------|--------|--------------------------|
  | `name` | `str`  | Username of the user     |
  | `password` | `str` | Password of the user |

## Inner Workings
1. The function checks if both `name` and `password` are strings using `isinstance`. If either is not a string, it raises a `TypeError`.
2. It then queries the database to find users whose `username` matches the provided `name`.
3. Further filtering is done on the query set to match the `password` with the provided one.
4. The `first()` method retrieves the first result from the filtered queryset or returns `None` if no matching user is found.

## Edge Cases & Preconditions
- If either `name` or `password` is not a string, the function raises a `TypeError`.
- The function assumes that there is a `User` model with fields `username` and `password` in the database.
- It does not handle cases where multiple users have the same username but different passwords.

## Result Synopsis
The function returns the first user object that matches both the provided username and password. If no such user exists, it returns `None`.

## Docstring Draft
```python
"""Retrieve user information based on username and password.

Args:
    name (str): Username of the user.
    password (str): Password of the user.

Returns:
    User: The first user object that matches both credentials or None if no match is found.

Raises:
    TypeError: If `name` or `password` is not a string.
"""
``````

## searchCourse  
``/Project/project_app/classes/ta.py``  
```def searchCourse(self,course):
        if isinstance(course, str) == False: raise TypeError("must be string")
        courseList = list(Course.objects.filter(name__exact=course))
        return (len(courseList) == 1)```  

**Documentation:**
```python## Overview
This code defines a method `searchCourse` that checks if there is exactly one course with the given name in the database.

## Interface
- **Signature**: `def searchCourse(self, course)`
- **Parameters**:
  - `course (str)`: The name of the course to search for.

## Inner Workings
1. The method first checks if the input `course` is a string. If not, it raises a `TypeError`.
2. It then filters the `Course` objects in the database where the name exactly matches the input `course`.
3. The filtered results are converted into a list.
4. The method returns `True` if the length of the list is exactly 1 (indicating one course with that name exists), otherwise it returns `False`.

## Edge Cases & Preconditions
- **Assumption**: The `Course.objects.filter(name__exact=course)` method works as expected and correctly filters the database.
- **Potential Failure Modes**:
  - If `course` is not a string, a `TypeError` will be raised.
  - If no course with the given name exists, it returns `False`.
  - If multiple courses with the same name exist, it returns `False`.
- **Error-Handling Logic**: The method raises a `TypeError` if the input is not a string.

## Result Synopsis
The method returns `True` if exactly one course with the given name exists in the database, otherwise it returns `False`.

## Docstring Draft
```python
"""Checks if there is exactly one course with the given name.

Args:
    course (str): The name of the course to search for.

Returns:
    bool: True if exactly one course with the given name exists, False otherwise.

Raises:
    TypeError: When `course` is not a string.
"""
``````

## searchUser  
``/Project/project_app/classes/ta.py``  
```def searchUser(self, name):
        pass```  

**Documentation:**
```python## Overview
The `searchUser` method appears to be a function designed to search for a user by their name within an application or system.

## Interface
- **Signature**: `def searchUser(self, name):`
- **Parameters**:
  | Name | Type | Purpose |
  |------|------|---------|
  | name | str  | The name of the user to search for. |

## Inner Workings
The function signature and body are currently empty (`pass`). This means that no logic is implemented to perform any search operation based on the provided `name`.

## Edge Cases & Preconditions
- **Assumptions**: 
  - The existence of a user database or data structure where users can be searched.
  - Proper handling of user input, such as checking if the `name` parameter is not None or an empty string.

- **Potential Failure Modes**:
  - If no matching user is found in the database, the function currently does nothing and returns nothing (`None`).
  - If the `name` parameter is invalid (e.g., None or an empty string), it may lead to unexpected behavior if not handled properly elsewhere in the code.

- **Error Handling**:
  - No error handling logic is present. If the application relies on this function, potential errors (e.g., database connection issues) would propagate up the call stack without being caught or logged.

## Result Synopsis
The function does not currently perform any action and returns `None`. To be useful, it needs to be implemented with logic that searches for a user in a data structure based on the provided `name`.

## Docstring Draft
```python
"""Searches for a user by name within the application's database.

Args:
    name (str): The name of the user to search for.

Returns:
    User: The user object if found, otherwise None.
"""
``````

## editInfo  
``/Project/project_app/classes/ta.py``  
```def editInfo(self, username, new_phone, new_name, new_email, new_address ):
        pass```  

**Documentation:**
```python## Overview
This code snippet defines a method `editInfo` within an unknown class. The purpose is to update user information such as phone number, name, email, and address.

## Interface
- **Signature**: `def editInfo(self, username, new_phone, new_name, new_email, new_address)`
- **Parameters**:
  - `username (str)`: The username of the user whose information needs to be updated.
  - `new_phone (str)`: The new phone number for the user.
  - `new_name (str)`: The new name for the user.
  - `new_email (str)`: The new email address for the user.
  - `new_address (str)`: The new address for the user.

## Inner Workings
- The function is currently empty (`pass` statement), meaning it does nothing when called. It accepts five parameters but has no implementation to process or store these values.

## Edge Cases & Preconditions
- Since there's no actual code, there are no data validation checks or error handling mechanisms.
- Calling this method will always return without making any changes to the user's information.

## Result Synopsis
The function does not return anything (`None`) and has no side effects. It simply accepts parameters without processing them.

## Docstring Draft
```python
"""Updates user information.

Args:
    username (str): The username of the user whose information needs to be updated.
    new_phone (str): The new phone number for the user.
    new_name (str): The new name for the user.
    new_email (str): The new email address for the user.
    new_address (str): The new address for the user.

Returns:
    None: This function does not return anything.

Raises:
    None: There are no error handling mechanisms in this method.
"""
``````

## addSkills  
``/Project/project_app/classes/ta.py``  
```def addSkills(self,skill, ta):
       if(User.objects.filter(username=ta) is None): return False
       print(User.objects.get(username=ta).user_type)
       print("TA")
       if((User.objects.get(username=ta).user_type) != "ta"): return False
       if(len(list((Skill.objects.filter(name=skill, owner=User.objects.get(username=ta)))))>0): return False
       Skill.objects.create(name=skill, owner=User.objects.get(username=ta))
       return True```  

**Documentation:**
```python## Overview
This code defines a method `addSkills` that attempts to add a new skill to a Teaching Assistant (TA) user.

## Interface
- **Signature**: 
  ```python
  def addSkills(self, skill, ta)
  ```
- **Parameters**:
  | Name    | Type     | Purpose                      |
  |---------|----------|------------------------------|
  | `skill` | `str`    | The name of the skill to add.  |
  | `ta`    | `str`    | The username of the TA user. |

## Inner Workings
- **Check if TA exists**: The function first checks if a user with the given username (`ta`) exists in the database using `User.objects.filter(username=ta)`. If no such user exists, it returns `False`.
- **Print User Type**: It prints the user type of the found user.
- **Check User Type**: It then checks if the user type is "ta". If not, it returns `False`.
- **Check if Skill Exists**: The function checks if a skill with the given name and owner (TA) already exists in the database using `Skill.objects.filter(name=skill, owner=User.objects.get(username=ta))`. If such a skill exists, it returns `False`.
- **Create Skill**: If all checks pass, it creates a new skill entry in the database using `Skill.objects.create(name=skill, owner=User.objects.get(username=ta))` and returns `True`.

## Edge Cases & Preconditions
- The function assumes that there is a `User` model with a method `objects.filter()` and a method `get()`.
- It also assumes that there is a `Skill` model with methods `objects.filter()`, `objects.create()`, and attributes `name` and `owner`.
- If the user does not exist or if the user type is not "ta", the function returns `False`.
- If the skill already exists for the given TA, the function also returns `False`.

## Result Synopsis
The function returns `True` if it successfully adds a new skill to the TA user's profile. Otherwise, it returns `False`.

## Docstring Draft
```python
"""Adds a new skill to a Teaching Assistant (TA) user.

Args:
    skill (str): The name of the skill to add.
    ta (str): The username of the TA user.

Returns:
    bool: True if the skill is successfully added, False otherwise.

Raises:
    ValueError: When `foo` is negative.
"""
``````

## TestHome  
``/Project/project_app/acceptance_tests/test_home.py``  
```class TestHome(TestCase):
    supervisor = None
    def setUp(self):
        self.supervisor = Client()
        self.user = User.objects.create(username="JDog", password="HipH0popotimu$", name="Jemaine Clement", email="fotconch@gmail.com", phone="(212) 123-2000", address="2125 Cardrona Valley Road, Cardrona 9382, NZ")

    def test_viewMyInfo(self):
        self.supervisor.post('/', {"name": "JDog", "password": "HipH0popotimu$"}, follow=True)
        rsp = self.supervisor.post('/home', {"name": "JDog", "password": "HipH0popotimu$"}, follow=True)
        self.assertEqual(rsp.context['username'], "JDog", msg="Returned user has the wrong username")
        self.assertEqual(rsp.context['password'], "HipH0popotimu$", msg="Returned user has the wrong password")
        self.assertEqual(rsp.context['name'], "Jemaine Clement", msg="Returned user has the wrong name")
        self.assertEqual(rsp.context['email'], "fotconch@gmail.com", msg="Returned user has the wrong email")
        self.assertEqual(rsp.context['phone'], "(212) 123-2000", msg="Returned user has the wrong phone")
        self.assertEqual(rsp.context['address'], "2125 Cardrona Valley Road, Cardrona 9382, NZ", msg="Returned user has the wrong address")```  

**Documentation:**
```python## Overview
This code defines a test class `TestHome` that extends `TestCase` from a testing framework. It sets up a supervisor (client) and creates a user. The class contains a single test method `test_viewMyInfo` that performs post requests to simulate viewing user information and asserts the correctness of the returned data.

## Interface
- **Signature**: `class TestHome(TestCase)`
- **Parameters**: None

## Inner Workings
- Initializes a client (`self.supervisor`) in the `setUp` method, which is run before each test.
- Creates a new user with specified attributes using Django's ORM (`User.objects.create`).
- The `test_viewMyInfo` method performs two post requests:
  - The first request to `/` (likely authenticating the user).
  - The second request to `/home`, passing the username and password, which is expected to return the user's information.
- Asserts that the returned context data for the user matches the expected values for username, password, name, email, phone, and address.

## Edge Cases & Preconditions
- Assumes there is a `Client` class available from a testing framework (likely Django test client).
- Assumes there is a `User` model with the specified attributes (`username`, `password`, `name`, `email`, `phone`, `address`).
- The test relies on the presence of a view at `/home` that handles user information requests.
- Error handling is implicit through assertions; if any assertion fails, the test will raise an `AssertionError`.

## Result Synopsis
The code asserts that after posting to `/home` with valid credentials, the returned context data matches the expected attributes of the created user. If all assertions pass, the test passes; otherwise, it will fail.

## Docstring Draft
```python
"""Test class for home-related functionalities.

This class sets up a client and a user before each test, and includes a method to test viewing user information.
"""

class TestHome(TestCase):
    supervisor = None

    def setUp(self):
        """Setup method to initialize the client and create a test user."""
        self.supervisor = Client()
        self.user = User.objects.create(username="JDog", password="HipH0popotimu$", name="Jemaine Clement", email="fotconch@gmail.com", phone="(212) 123-2000", address="2125 Cardrona Valley Road, Cardrona 9382, NZ")

    def test_viewMyInfo(self):
        """Test the viewMyInfo functionality by posting to /home and asserting the returned user data."""
        self.supervisor.post('/', {"name": "JDog", "password": "HipH0popotimu$"}, follow=True)
        rsp = self.supervisor.post('/home', {"name": "JDog", "password": "HipH0popotimu$"}, follow=True)
        self.assertEqual(rsp.context['username'], "JDog", msg="Returned user has the wrong username")
        self.assertEqual(rsp.context['password'], "HipH0popotimu$", msg="Returned user has the wrong password")
        self.assertEqual(rsp.context['name'], "Jemaine Clement", msg="Returned user has the wrong name")
        self.assertEqual(rsp.context['email'], "fotconch@gmail.com", msg="Returned user has the wrong email")
        self.assertEqual(rsp.context['phone'], "(212) 123-2000", msg="Returned user has the wrong phone")
        self.assertEqual(rsp.context['address'], "2125 Cardrona Valley Road, Cardrona 9382, NZ", msg="Returned user has the wrong address")
``````

## setUp  
``/Project/project_app/acceptance_tests/test_home.py``  
```def setUp(self):
        self.supervisor = Client()
        self.user = User.objects.create(username="JDog", password="HipH0popotimu$", name="Jemaine Clement", email="fotconch@gmail.com", phone="(212) 123-2000", address="2125 Cardrona Valley Road, Cardrona 9382, NZ")```  

**Documentation:**
```python## Overview
The `setUp` method initializes a client and creates a user for testing purposes.

## Interface
- **Signature**: `def setUp(self)`
- **Parameters**:
    | Name   | Type         | Purpose                              |
    |--------|--------------|--------------------------------------|
    | self   | object       | The instance of the class            |

## Inner Workings
1. The method initializes a client by creating an instance of the `Client` class.
2. It creates a user using Django's ORM (`User.objects.create`). The user is given specific attributes such as username, password, name, email, phone, and address.

## Edge Cases & Preconditions
- Assumes that the `Client` class has been correctly implemented and can be instantiated without errors.
- Assumes that Django's ORM is properly set up and configured to create a new user instance with the provided attributes.
- Does not handle exceptions related to database operations or user creation failures, which could lead to test failures if an error occurs.

## Result Synopsis
The `setUp` method initializes a client and creates a user, setting up the environment for subsequent tests. If successful, it prepares the system for testing specific functionalities that require authentication or interaction with external services.

## Docstring Draft
```python
"""Sets up the test environment by initializing a client and creating a test user.

Args:
    self (object): The instance of the class.

Raises:
    Exception: If there is an error during the initialization of the client or creation of the user.
"""
``````

## test_viewMyInfo  
``/Project/project_app/acceptance_tests/test_home.py``  
```def test_viewMyInfo(self):
        self.supervisor.post('/', {"name": "JDog", "password": "HipH0popotimu$"}, follow=True)
        rsp = self.supervisor.post('/home', {"name": "JDog", "password": "HipH0popotimu$"}, follow=True)
        self.assertEqual(rsp.context['username'], "JDog", msg="Returned user has the wrong username")
        self.assertEqual(rsp.context['password'], "HipH0popotimu$", msg="Returned user has the wrong password")
        self.assertEqual(rsp.context['name'], "Jemaine Clement", msg="Returned user has the wrong name")
        self.assertEqual(rsp.context['email'], "fotconch@gmail.com", msg="Returned user has the wrong email")
        self.assertEqual(rsp.context['phone'], "(212) 123-2000", msg="Returned user has the wrong phone")
        self.assertEqual(rsp.context['address'], "2125 Cardrona Valley Road, Cardrona 9382, NZ", msg="Returned user has the wrong address")```  

**Documentation:**
```python## Overview
This code defines a unit test method `test_viewMyInfo` that verifies the functionality of viewing user information by making HTTP POST requests to specific endpoints.

## Interface
- **Signature**: `def test_viewMyInfo(self)`
- **Parameters**: None

## Inner Workings
1. The method sends an HTTP POST request to the root endpoint (`/`) with a payload containing user credentials, and follows the redirect.
2. It then sends another HTTP POST request to the `/home` endpoint with the same user credentials and also follows the redirect.
3. The response from the `/home` endpoint is checked for various attributes such as `username`, `password`, `name`, `email`, `phone`, and `address`.
4. Each attribute is compared against expected values, and an assertion error is raised if any of the checks fail with a specific message.

## Edge Cases & Preconditions
- Assumes that the user credentials provided in the POST requests are correct.
- Assumes that the `/home` endpoint returns the expected context data.
- If any assertions fail, the test method will raise an `AssertionError` with a detailed message indicating which attribute is incorrect.

## Result Synopsis
The code asserts that the attributes retrieved from the response match the expected values. If all checks pass, the test method completes successfully without raising any exceptions.

## Docstring Draft
```python
"""Tests the functionality of viewing user information by making HTTP POST requests to specific endpoints.

Args:
    None

Returns:
    None

Raises:
    AssertionError: When any of the retrieved attributes do not match the expected values.
"""
``````

## TestCreateSection  
``/Project/project_app/acceptance_tests/createSection_acceptanceTests.py``  
```class TestCreateSection(TestCase):
    def setUp(self):
        self.Supervisor = Client()
        self.User = User.objects.create(username="admin", password="admin")
        self.course1 = Course.objects.create(name="361", dateTime="2022-02-12 14:30:34").save()
        self.section1 = Section.objects.create(sectionName="891", owner=self.course1)

    def test_addSection(self):
        self.Supervisor.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.Supervisor.post('/home/addSection/', {'courseID': '361', 'sectionID': "101"})
        self.assertEqual(response.context['Message'], "Section created", msg="Section not created from post")

    def test_duplicate(self):
        self.Supervisor.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.Supervisor.post('/home/addSection/', {'courseID': '361', 'sectionID': "891"})
        self.assertEqual(response.context['Message'], "Section with same ID already exists", msg="Duplicate section should not be made")

    def test_courseDNE(self):
        self.Supervisor.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.Supervisor.post('/home/addSection/', {'courseID': '1234', 'sectionID': "101"})
        self.assertEqual(response.context['Message'], "Course ID not found in database", msg="Section should not be made for a course that DNE")

    def test_sectionList(self):
        self.Supervisor.post('/', {"name": "admin", "password": "admin"}, follow=True)
        rsp = self.Supervisor.post('/home/addSection/')
        self.assertEqual("891", rsp.context['section_list'][0].sectionName, msg="Section list inaccurate/not found")

    def test_sectionList_add(self):
        self.Supervisor.post('/', {"name": "admin", "password": "admin"}, follow=True)
        rsp = self.Supervisor.post('/home/addSection/', {'courseID': '361', 'sectionID': "101"})
        self.assertEqual("891", rsp.context['section_list'][0].sectionName, msg="Section list inaccurate/not found")
        self.assertEqual("101", rsp.context['section_list'][1].sectionName, msg="Section list inaccurate/not found")```  

**Documentation:**
```python## Overview
This code is part of an acceptance test suite for a section creation feature in an application. It tests various scenarios for adding sections to courses, including handling duplicates and non-existent courses.

## Interface
### Signature
```python
class TestCreateSection(TestCase):
```

### Parameters
| Name       | Type     | Purpose                     |
|------------|----------|-----------------------------|
| None       | N/A      | This is a class, not a function. It has no parameters in the traditional sense. |

## Inner Workings
- The `TestCreateSection` class inherits from `TestCase`, which is part of Django's testing framework.
- The `setUp` method initializes necessary objects and data for testing:
  - A supervisor client (`Client`) to simulate user actions.
  - An admin user.
  - A course with a specific ID and date/time.
  - A section associated with the created course.
  
- Several test methods are defined to verify different scenarios:
  - `test_addSection`: Tests adding a new section successfully.
  - `test_duplicate`: Ensures that attempting to add an already existing section results in an error message.
  - `test_courseDNE`: Checks that trying to add a section for a non-existent course returns an appropriate error message.
  - `test_sectionList`: Verifies that the list of sections includes the expected section after adding it.
  - `test_sectionList_add`: Tests that multiple sections can be added and are correctly reflected in the section list.

## Edge Cases & Preconditions
- The code assumes that the database is properly configured and accessible for creating users, courses, and sections.
- It checks for a duplicate section ID by attempting to add an existing one and expecting a specific error message.
- It verifies that adding a section for a non-existent course returns an appropriate error.

## Result Synopsis
The `TestCreateSection` class provides several tests to ensure the functionality of adding sections to courses. It confirms successful addition, handling of duplicates, and correct behavior when attempting to add sections for non-existent courses or displaying updated section lists.

## Docstring Draft
```python
"""Base class for acceptance tests related to section creation.

Args:
    None: This is a class, not a function. It has no parameters in the traditional sense.

Returns:
    None: This is a class, not a function. It does not return anything.
"""
```

This code snippet demonstrates how to structure and document a test class for an acceptance test suite using Python's unittest framework.```

## setUp  
``/Project/project_app/acceptance_tests/createSection_acceptanceTests.py``  
```def setUp(self):
        self.Supervisor = Client()
        self.User = User.objects.create(username="admin", password="admin")
        self.course1 = Course.objects.create(name="361", dateTime="2022-02-12 14:30:34").save()
        self.section1 = Section.objects.create(sectionName="891", owner=self.course1)```  

**Documentation:**
```python## Overview
This code sets up the necessary objects and environment for acceptance tests by creating a supervisor client, a user object, and course and section objects.

## Interface
- **Signature**: `setUp(self)`
- **Parameters**:
  | Name    | Type   | Purpose                   |
  |---------|--------|---------------------------|
  | self    | Object | The instance of the test class |

## Inner Workings
1. A new instance of a client is created and assigned to `self.Supervisor`.
2. A user object with username "admin" and password "admin" is created using Django's ORM and assigned to `self.User`.
3. A course object named "361" with a specific date and time is created and saved, then assigned to `self.course1`.
4. A section object with the name "891" and an owner set as `self.course1` is created.

## Edge Cases & Preconditions
- Assumes Django's ORM (Object-Relational Mapping) is available.
- Assumes a `Client` class exists and can be instantiated without arguments.
- Assumes `User`, `Course`, and `Section` models are defined in the project with the specified attributes.

## Result Synopsis
This function sets up the environment for further acceptance tests by creating essential objects such as a client, a user, a course, and a section. It does not return any value; its side effect is to prepare the test fixture.

## Docstring Draft
```python
"""Sets up the necessary objects and environment for acceptance tests by creating a supervisor client, a user object, and course and section objects.

Args:
    self (Object): The instance of the test class

Returns:
    None: No return value; sets up test fixtures.
"""
``````

## test_addSection  
``/Project/project_app/acceptance_tests/createSection_acceptanceTests.py``  
```def test_addSection(self):
        self.Supervisor.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.Supervisor.post('/home/addSection/', {'courseID': '361', 'sectionID': "101"})
        self.assertEqual(response.context['Message'], "Section created", msg="Section not created from post")```  

**Documentation:**
```python## Overview
This code tests the functionality of adding a section through an HTTP POST request in a web application.

## Interface
- **Signature**: `test_addSection(self)`
- **Parameters**: None explicitly defined, but uses attributes and methods of the class instance `self`.

## Inner Workings
1. The method first logs into the system as a supervisor using another method (`self.Supervisor.post`) with username "admin" and password "admin".
2. It then attempts to add a section by making another POST request to `/home/addSection/` with parameters `courseID` set to '361' and `sectionID` set to '101'.
3. The response from the server is checked to ensure that the context contains a message indicating "Section created".

## Edge Cases & Preconditions
- Assumes that there are routes (`/`, `/home/addSection/`) available in the application.
- Assumes that the Supervisor object has a `post` method that can be used to send HTTP POST requests and handle responses.
- Assumes that the login credentials ("admin", "admin") are valid for accessing supervisor functionalities.
- The test assumes that adding a section with the provided courseID and sectionID should succeed, as it checks for a specific message in the response context.

## Result Synopsis
The function tests whether adding a section through a POST request results in the correct message being returned in the response context. It does not return any value itself but asserts the correctness of the operation based on the presence of the expected message.

## Docstring Draft
```python
"""Tests adding a section by making an HTTP POST request to '/home/addSection/'.

Asserts that the server responds with a message indicating successful creation of a section.

Raises:
    AssertionError: If the section is not created as expected.
"""
``````

## test_duplicate  
``/Project/project_app/acceptance_tests/createSection_acceptanceTests.py``  
```def test_duplicate(self):
        self.Supervisor.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.Supervisor.post('/home/addSection/', {'courseID': '361', 'sectionID': "891"})
        self.assertEqual(response.context['Message'], "Section with same ID already exists", msg="Duplicate section should not be made")```  

**Documentation:**
```python## Overview
This code is a test function for creating a duplicate section in an application. It posts login credentials to access the system, then attempts to add a section with a duplicate ID and verifies that an appropriate error message is returned.

## Interface
- **Signature**: `test_duplicate(self)`
- **Parameters**:
  | Name      | Type   | Purpose                          |
  |-----------|--------|----------------------------------|
  | `self`    | object | The instance of the test class. |

## Inner Workings
1. The function first calls `self.Supervisor.post('/', {"name": "admin", "password": "admin"}, follow=True)` to log in as an admin user.
2. It then attempts to add a section with `courseID='361'` and `sectionID='891'` by posting to `/home/addSection/`.
3. The function asserts that the response context contains the message "Section with same ID already exists" to confirm that the system correctly handles attempting to create a duplicate section.

## Edge Cases & Preconditions
- **Preconditions**:
  - The application must be configured to allow admin login.
  - There should be an existing user with the username 'admin' and password 'admin'.
  - The `/home/addSection/` endpoint must be accessible and handle POST requests for adding sections.
  
- **Edge Cases**:
  - If the `sectionID` does not already exist, the function will fail because it expects to receive a duplicate error message.

## Result Synopsis
The function tests whether attempting to create a section with an ID that already exists results in the correct error message being returned. It uses assertions to verify that the expected message is present in the response context.

## Docstring Draft
```python
"""Tests creating a duplicate section and verifies the appropriate error message is returned.

Args:
    self (object): The instance of the test class.

Raises:
    AssertionError: If the expected error message is not found in the response context.
"""
``````

## test_courseDNE  
``/Project/project_app/acceptance_tests/createSection_acceptanceTests.py``  
```def test_courseDNE(self):
        self.Supervisor.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.Supervisor.post('/home/addSection/', {'courseID': '1234', 'sectionID': "101"})
        self.assertEqual(response.context['Message'], "Course ID not found in database", msg="Section should not be made for a course that DNE")```  

**Documentation:**
```python## Overview
The code tests the behavior of adding a section when the specified course does not exist in the database.

## Interface
- **Signature**: `test_courseDNE(self)`
- **Parameters**:
  | Name    | Type   | Purpose                       |
  |---------|--------|-------------------------------|
  | self    | object | The test case instance.       |

## Inner Workings
1. The method `self.Supervisor.post('/', {"name": "admin", "password": "admin"}, follow=True)` logs in as an administrator.
2. It then attempts to add a section using the endpoint `/home/addSection/` with parameters `courseID='1234'` and `sectionID='101'`.
3. The response from the server is captured, and it checks if the context contains a message indicating that the course ID was not found in the database.

## Edge Cases & Preconditions
- **Assumptions**:
  - There is an administrator account with username "admin" and password "admin".
  - The `/home/addSection/` endpoint exists and can be accessed.
- **Potential Failure Modes**:
  - If the course ID '1234' does not exist in the database, the response should indicate this error.
- **Error-Handling Logic**:
  - No explicit error handling is shown in the code. The assertion `self.assertEqual(response.context['Message'], "Course ID not found in database", msg="Section should not be made for a course that DNE")` implicitly checks for an error and fails if it doesn't match the expected message.

## Result Synopsis
The function tests whether adding a section with a non-existent course ID results in an appropriate error message being returned. It asserts that the response context contains the expected error message "Course ID not found in database".

## Docstring Draft
```python
"""Tests attempting to add a section when the specified course does not exist.

This test logs in as an administrator and tries to add a section for a non-existent course.
It checks if the server returns an appropriate error message indicating that the course was not found.

Args:
    self (object): The test case instance.

Returns:
    None

Raises:
    AssertionError: If the expected error message is not returned from the server.
"""
``````

## test_sectionList  
``/Project/project_app/acceptance_tests/createSection_acceptanceTests.py``  
```def test_sectionList(self):
        self.Supervisor.post('/', {"name": "admin", "password": "admin"}, follow=True)
        rsp = self.Supervisor.post('/home/addSection/')
        self.assertEqual("891", rsp.context['section_list'][0].sectionName, msg="Section list inaccurate/not found")```  

**Documentation:**
```python## Overview
The `test_sectionList` function is an acceptance test method within a Python class. It simulates posting data to add a section and then verifies that the section was added correctly.

## Interface
- **Signature**: `def test_sectionList(self)`
- **Parameters**:
  | Name     | Type   | Purpose                                      |
  |----------|--------|----------------------------------------------|
  | `self`   | object | The instance of the class containing this method. |

## Inner Workings
1. **Authentication**: The function first authenticates as an admin by posting a request to `'/'` with JSON data containing an admin name and password. This is done using `self.Supervisor.post('/', {"name": "admin", "password": "admin"}, follow=True)`.
2. **Adding Section**: After authentication, the function attempts to add a section by posting to `'/home/addSection/'`. The response from this request is stored in `rsp`.
3. **Validation**: The function checks if the added section appears correctly in the `section_list` context variable. It asserts that the first element of `section_list` has a `sectionName` attribute equal to `"891"`. If this condition is not met, it raises an assertion error with the message "Section list inaccurate/not found".

## Edge Cases & Preconditions
- **Authentication**: Assumes that the admin credentials provided are correct and that the authentication endpoint (`'/'`) accepts these credentials.
- **Adding Section**: Assumes that the `'/home/addSection/'` endpoint can handle POST requests and will add a section with the name `"891"` if it is correctly posted.
- **Error Handling**: If the authentication fails or the section is not added as expected, an assertion error will be raised.

## Result Synopsis
The function asserts that after authenticating and adding a section, the newly added section's name is correctly retrieved from the context variable `section_list`.

## Docstring Draft
```python
"""Simulates posting data to add a section and verifies that it was added correctly.

Raises:
    AssertionError: If the section list does not contain the expected section.
"""
``````

## test_sectionList_add  
``/Project/project_app/acceptance_tests/createSection_acceptanceTests.py``  
```def test_sectionList_add(self):
        self.Supervisor.post('/', {"name": "admin", "password": "admin"}, follow=True)
        rsp = self.Supervisor.post('/home/addSection/', {'courseID': '361', 'sectionID': "101"})
        self.assertEqual("891", rsp.context['section_list'][0].sectionName, msg="Section list inaccurate/not found")
        self.assertEqual("101", rsp.context['section_list'][1].sectionName, msg="Section list inaccurate/not found")```  

**Documentation:**
```python## Overview
This code tests the addition of a section to a section list by simulating user login and subsequent section creation. It verifies that the new section is correctly added to the list.

## Interface
- **Signature**: `test_sectionList_add(self)`
- **Parameters**: None

## Inner Workings
1. The function starts by logging in as an administrator using the `/` endpoint with the credentials `name=admin` and `password=admin`.
2. It then attempts to add a new section using the `/home/addSection/` endpoint with parameters `courseID=361` and `sectionID=101`.
3. The response context is checked to ensure that the newly added section (`sectionName="891"`) and another existing section (`sectionName="101"`) are present in the `section_list`.

## Edge Cases & Preconditions
- **Preconditions**:
  - There must be an administrator user with credentials `name=admin` and `password=admin`.
  - The course with `courseID=361` must exist.
  - The section list must be accessible and modifiable via the specified endpoints.
  
- **Potential Failure Modes**:
  - If the login fails, the subsequent post request to add a section will also fail.
  - If the new section is not added correctly, or if an existing section is incorrectly identified in the response, the test will fail.

## Result Synopsis
The function asserts that the newly added section is correctly named "891" and another existing section is named "101". It does not explicitly return a value but indicates success through assertions.

## Docstring Draft
```python
"""Tests adding a section to the section list.

Asserts that after logging in as an admin and attempting to add a new section,
the new section and an existing section are correctly identified in the response context.
"""
``````

## EditInfoTest  
``/Project/project_app/acceptance_tests/account_edit_info.py``  
```class EditInfoTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="userone", password="1234", name="userone",
                                        email="userone@example.com", phone="1234567890",
                                        address="123 Roadrage lane, Springfield, Illinois ", user_type="instructor")

    def test_editMyInfo_validField(self):
        self.client.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.client.post('/home/accountEdit/', {'user-fields': 'phone', 'newEntry': '0987654321'})
        self.user.refresh_from_db()
        self.assertEqual(self.user.phone, '0987654321', msg="Phone number should be updated successfully")
        self.assertEqual(response.context['Message'], "Information updated successfully", msg="Invalid Message")

    def test_editMyInfo_invalidField(self):
        self.client.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.client.post('/home/accountEdit/', {'user-fields': 'invalidField', 'newEntry': 'newValue'})
        self.assertEqual(response.context['Message'], "Invalid field selected", msg="Invalid Message")

    def test_editMyInfo_noFieldProvided(self):
        self.client.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.client.post('/home/accountEdit/', {'user-fields': '', 'newEntry': 'newValue'})
        self.assertEqual(response.context['Message'], "Invalid field selected", msg="Invalid Message")```  

**Documentation:**
```python## Overview
This code defines a test class `EditInfoTest` that extends `TestCase` to perform unit tests for updating user information through an account edit form.

## Interface
### Signature
```python
class EditInfoTest(TestCase):
```
### Parameters
| Name     | Type    | Purpose                           |
|----------|---------|-----------------------------------|
| None     |         | This is a class, not a function. |

## Inner Workings
1. **Setup Method (`setUp`)**:
   - Creates a test client and a user with specified attributes.
2. **Test Case Methods**:
   - `test_editMyInfo_validField`: Tests updating a valid field (phone number) through the account edit form.
     - Asserts that the phone number is updated successfully in the database.
     - Checks that the response context contains the correct success message.
   - `test_editMyInfo_invalidField`: Tests attempting to update an invalid field.
     - Asserts that the response context contains the correct error message indicating an invalid field.
   - `test_editMyInfo_noFieldProvided`: Tests providing no field for updating.
     - Asserts that the response context contains the correct error message indicating an invalid field.

## Edge Cases & Preconditions
- Assumes that a user can log in and access the account edit form.
- Handles cases where an invalid or empty field is provided for updating, returning an appropriate error message.
- Does not assume any specific state of the database beyond the existence of a test user.

## Result Synopsis
The code tests the functionality of updating user information through an account edit form. It ensures that valid updates are handled correctly and that errors are properly reported when attempting to update invalid or empty fields.

## Docstring Draft
```python
class EditInfoTest(TestCase):
    """Tests for updating user information through the account edit form."""

    def setUp(self):
        """Sets up a test client and a user."""
        self.client = Client()
        self.user = User.objects.create(username="userone", password="1234", name="userone",
                                        email="userone@example.com", phone="1234567890",
                                        address="123 Roadrage lane, Springfield, Illinois ", user_type="instructor")

    def test_editMyInfo_validField(self):
        """Tests updating a valid field (phone number) through the account edit form."""
        self.client.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.client.post('/home/accountEdit/', {'user-fields': 'phone', 'newEntry': '0987654321'})
        self.user.refresh_from_db()
        self.assertEqual(self.user.phone, '0987654321', msg="Phone number should be updated successfully")
        self.assertEqual(response.context['Message'], "Information updated successfully", msg="Invalid Message")

    def test_editMyInfo_invalidField(self):
        """Tests attempting to update an invalid field."""
        self.client.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.client.post('/home/accountEdit/', {'user-fields': 'invalidField', 'newEntry': 'newValue'})
        self.assertEqual(response.context['Message'], "Invalid field selected", msg="Invalid Message")

    def test_editMyInfo_noFieldProvided(self):
        """Tests providing no field for updating."""
        self.client.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.client.post('/home/accountEdit/', {'user-fields': '', 'newEntry': 'newValue'})
        self.assertEqual(response.context['Message'], "Invalid field selected", msg="Invalid Message")
``````

## setUp  
``/Project/project_app/acceptance_tests/account_edit_info.py``  
```def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="userone", password="1234", name="userone",
                                        email="userone@example.com", phone="1234567890",
                                        address="123 Roadrage lane, Springfield, Illinois ", user_type="instructor")```  

**Documentation:**
```python## Overview
This code snippet is responsible for setting up an environment before running tests in the `acceptance_tests/account_edit_info.py` file. Specifically, it initializes a client and creates a test user.

## Interface
- **Signature**: 
  ```python
  def setUp(self):
  ```
- **Parameters**:
  | Name | Type | Purpose |
  |------|------|---------|
  | self | object | The instance of the class containing this method. |

## Inner Workings
- The `setUp` method initializes a client instance.
- A test user is created using Django's ORM (`User.objects.create`). The user has attributes such as username, password, name, email, phone, address, and user type.

## Edge Cases & Preconditions
- Assumes that the Django environment is properly configured and running.
- If the `Client` class or `User.objects.create` method fails due to issues like database connection problems, it will raise an exception which needs to be handled by the test framework.
- The password is hardcoded and should not be used in real-world tests for security reasons.

## Result Synopsis
The `setUp` method sets up the testing environment by initializing a client and creating a test user. It does not return any value directly but prepares the state for subsequent tests in the same class.

## Docstring Draft
```python
"""Initializes the testing environment before running tests.

This method initializes a client instance and creates a test user with predefined attributes.
It should be called by the test framework before each test method to ensure that the environment is clean and consistent.

Args:
    self (object): The instance of the class containing this method.

Returns:
    None

Raises:
    Any exceptions raised during client initialization or user creation need to be handled by the test framework.
"""
``````

## test_editMyInfo_validField  
``/Project/project_app/acceptance_tests/account_edit_info.py``  
```def test_editMyInfo_validField(self):
        self.client.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.client.post('/home/accountEdit/', {'user-fields': 'phone', 'newEntry': '0987654321'})
        self.user.refresh_from_db()
        self.assertEqual(self.user.phone, '0987654321', msg="Phone number should be updated successfully")
        self.assertEqual(response.context['Message'], "Information updated successfully", msg="Invalid Message")```  

**Documentation:**
```python## Overview
This code is a unit test for updating account information in an application. It ensures that the phone number can be updated successfully and that the appropriate message is returned to the user.

## Interface
### Signature
```python
def test_editMyInfo_validField(self):
```
- **Parameters**: None

## Inner Workings
1. **Initial Setup**: The code sends a POST request to the root URL (`'/'`) with a payload containing `name` and `password`. This likely sets up or authenticates the user session.
2. **Update Account Information**: A POST request is sent to the `/home/accountEdit/` URL with a payload specifying that the `user-fields` should be updated to `'phone'` and the new entry as `'0987654321'`. This updates the phone number of the user.
3. **Refresh User Data**: The user's data is refreshed from the database to ensure any changes are applied.
4. **Validation Check**: It asserts that the `user.phone` attribute has been updated to `'0987654321'`.
5. **Response Validation**: It checks that the response context contains a message indicating successful information update.

## Edge Cases & Preconditions
- **Assumptions**:
  - The user is authenticated and exists.
  - The `/home/accountEdit/` endpoint is accessible and correctly handles updates to user fields.
  - The `user.phone` field is correctly updated in the database.
  
- **Potential Failure Modes**:
  - The update might fail if there are validation errors or if the user does not have permission to modify certain fields.

## Result Synopsis
The code asserts that after updating the phone number, it is successfully saved in the database and that a message indicating successful update is returned to the user.

## Docstring Draft
```python
"""Tests updating account information with valid field data.

This test ensures that the phone number can be updated successfully and that the appropriate message is returned to the user.
"""
```

This code tests the functionality of updating user account information, specifically focusing on updating the phone number. It verifies both the update in the database and the message response from the server.```

## test_editMyInfo_invalidField  
``/Project/project_app/acceptance_tests/account_edit_info.py``  
```def test_editMyInfo_invalidField(self):
        self.client.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.client.post('/home/accountEdit/', {'user-fields': 'invalidField', 'newEntry': 'newValue'})
        self.assertEqual(response.context['Message'], "Invalid field selected", msg="Invalid Message")```  

**Documentation:**
```python## Overview
This function tests the behavior of editing account information with an invalid field by sending a POST request to `/home/accountEdit/` and asserting that the response context contains the expected error message.

## Interface
- **Signature**: `test_editMyInfo_invalidField(self)`
- **Parameters**:
  | Name      | Type   | Purpose                          |
  |-----------|--------|----------------------------------|
  | self      |        | The test case instance.            |

## Inner Workings
1. Send a POST request to the root path `'/'` with data `{"name": "userone", "password": "1234"}` using `self.client.post()`. This step is likely setting up user authentication or initial context.
2. Send another POST request to `/home/accountEdit/` with data `{'user-fields': 'invalidField', 'newEntry': 'newValue'}` using `self.client.post()` and store the response in `response`.
3. Assert that the value of `response.context['Message']` is `"Invalid field selected"` using `self.assertEqual()`. This checks if the server correctly handles the invalid field selection.

## Edge Cases & Preconditions
- **Assumptions**: The server correctly processes POST requests to `/home/accountEdit/`, the context contains a key `'Message'`, and the request data has the expected structure.
- **Potential Failure Modes**: The server might not handle the invalid field correctly, leading to an incorrect error message or no error at all.
- **Error-Handling Logic**: If the assertion fails, it will raise an `AssertionError`.

## Result Synopsis
The function tests that sending a request with an invalid field results in the expected error message being returned in the response context.

## Docstring Draft
```python
"""Tests editing account information with an invalid field.

This test sends a POST request to '/home/accountEdit/' with an invalid field and checks if the server responds with the correct error message.

Args:
    self (unittest.TestCase): The test case instance.

Raises:
    AssertionError: If the response context does not contain the expected error message.
"""
``````

## test_editMyInfo_noFieldProvided  
``/Project/project_app/acceptance_tests/account_edit_info.py``  
```def test_editMyInfo_noFieldProvided(self):
        self.client.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.client.post('/home/accountEdit/', {'user-fields': '', 'newEntry': 'newValue'})
        self.assertEqual(response.context['Message'], "Invalid field selected", msg="Invalid Message")```  

**Documentation:**
```python## Overview
The code defines a test method to ensure that the system correctly handles cases where no fields are provided when attempting to edit account information.

## Interface
- **Signature**: `test_editMyInfo_noFieldProvided(self)`
- **Parameters**:
  | Name       | Type   | Purpose                         |
  |------------|--------|-----------------------------------|
  | self       | object | The test case instance.           |

## Inner Workings
1. The method initializes the test environment by making a POST request to the root URL (`'/'`) with user credentials, simulating a login or initial setup.
2. It then makes another POST request to `/home/accountEdit/` with an empty field selection and a new entry value, mimicking an attempt to edit account information without selecting any fields.
3. The method asserts that the response context contains a message indicating "Invalid field selected," validating that the system correctly handles the error when no fields are provided.

## Edge Cases & Preconditions
- **Preconditions**:
  - Assumes that the `self.client` object is properly configured and can make HTTP requests.
  - Assumes that the URLs (`'/'` and `/home/accountEdit/`) exist in the application being tested.
- **Assumptions**:
  - The system has a mechanism to handle account edits and provide feedback when no fields are selected.
  - The response context contains a `Message` key upon failure.

## Result Synopsis
The method asserts that the response from `/home/accountEdit/` indicates an "Invalid field selected" message, indicating successful error handling for cases where no fields are provided during account editing.

## Docstring Draft
```python
"""Tests the behavior of the system when attempting to edit account information without selecting any fields.

Args:
    self (object): The test case instance.

Raises:
    AssertionError: If the expected "Invalid field selected" message is not present in the response context.
"""
``````

## AssignCourseTest  
``/Project/project_app/acceptance_tests/assign_course.py``  
```class AssignCourseTest(TestCase):
    def setUp(self):
        self.admin = Client()
        self.ADMIN = User.objects.create(username="admin", password="admin", name="admin",
                                         email="admin@example.com", phone="1234567890",
                                         address="123 Admin lane, Springfield, Illinois ", user_type="admin")
        self.INS = User.objects.create(username="userone", password="1234", name="userone",
                                       email="userone@example.com", phone="1234567890",
                                       address="123 Roadrage lane, Springfield, Illinois ", user_type="instructor")
        self.course1 = Course.objects.create(name="courseone", dateTime="2023-05-15 10:00:00")

    def test_assignCourse(self):
        self.admin.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.admin.post('/home/assignCourse/', {'courseID': 'courseone', 'userToFind': "userone"})
        self.assertEqual(response.context['Message'], "Course assigned successfully", msg="Course Not Assigned")

    def test_assignCourse_InvalidCourse(self):
        self.admin.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.admin.post('/home/assignCourse/', {'courseID': 'nonexistentcourse', 'userToFind': "userone"})
        self.assertEqual(response.context['Message'], "Course not found", msg="Invalid Course Assigned")

    def test_assignCourse_InvalidUser(self):
        self.admin.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.admin.post('/home/assignCourse/', {'courseID': 'courseone', 'userToFind': "nonexistentuser"})
        self.assertEqual(response.context['Message'], "User not found", msg="Invalid User Assigned")

    def test_assignCourse_AlreadyAssigned(self):
        self.admin.post('/', {"name": "admin", "password": "admin"}, follow=True)
        self.admin.post('/home/assignCourse/', {'courseID': 'courseone', 'userToFind': "userone"})
        response = self.admin.post('/home/assignCourse/', {'courseID': 'courseone', 'userToFind': "userone"})
        self.assertEqual(response.context['Message'], "Course already assigned", msg="Course Reassigned")```  

**Documentation:**
```python## Overview
This code defines a test class `AssignCourseTest` for testing the assignment of courses to users in an application. It includes methods to validate course and user assignments, handling cases where the course or user does not exist, or if the course is already assigned.

## Interface
- **Signature**: `class AssignCourseTest(TestCase)`
- **Parameters**:
  | Name          | Type   | Purpose                                                                 |
  |---------------|--------|-------------------------------------------------------------------------|
  | None         |        | This class does not accept any parameters.                             |

## Inner Workings
1. The `setUp` method initializes a test client, admin user, instructor user, and a course.
2. The `test_assignCourse` method logs in as an admin and attempts to assign a valid course to a valid user, asserting that the message "Course assigned successfully" is returned.
3. The `test_assignCourse_InvalidCourse` method attempts to assign a non-existent course to a valid user, asserting that the message "Course not found" is returned.
4. The `test_assignCourse_InvalidUser` method attempts to assign a valid course to a non-existent user, asserting that the message "User not found" is returned.
5. The `test_assignCourse_AlreadyAssigned` method attempts to reassign a valid course to a valid user who already has the course assigned, asserting that the message "Course already assigned" is returned.

## Edge Cases & Preconditions
- **Assumptions**: 
  - There is an admin and instructor user created in the database.
  - A course exists with the name "courseone".
  - The login credentials are correct.
  - The course assignment logic correctly handles cases where a course or user does not exist.

- **Potential Failure Modes**:
  - Invalid course or user inputs.
  - Reassigning a course that is already assigned to the user.

## Result Synopsis
The test class `AssignCourseTest` verifies that courses can be assigned to users, and it correctly handles cases where the course or user does not exist, or if the course is already assigned. It asserts expected messages returned by the application.

## Docstring Draft
```python
"""Tests for course assignment functionality.

This class includes methods to validate the assignment of courses to users,
handling various scenarios including valid assignments and invalid inputs.

Args:
    None

Returns:
    None

Raises:
    None
"""
``````

## setUp  
``/Project/project_app/acceptance_tests/assign_course.py``  
```def setUp(self):
        self.admin = Client()
        self.ADMIN = User.objects.create(username="admin", password="admin", name="admin",
                                         email="admin@example.com", phone="1234567890",
                                         address="123 Admin lane, Springfield, Illinois ", user_type="admin")
        self.INS = User.objects.create(username="userone", password="1234", name="userone",
                                       email="userone@example.com", phone="1234567890",
                                       address="123 Roadrage lane, Springfield, Illinois ", user_type="instructor")
        self.course1 = Course.objects.create(name="courseone", dateTime="2023-05-15 10:00:00")```  

**Documentation:**
```python## Overview
This code sets up the initial state for acceptance tests by creating test users and a course.

## Interface
**Signature**: `setUp(self)`

**Parameters**:
| Name | Type   | Purpose                 |
|------|--------|-------------------------|
| self | Method | Reference to the class instance |

## Inner Workings
- Creates an admin user using Django's ORM.
- Creates an instructor user using Django's ORM.
- Creates a course object using Django's ORM.

The code initializes test data required for acceptance tests, ensuring that each test has a consistent starting point.

## Edge Cases & Preconditions
- Assumes that the Django environment is properly set up and accessible.
- No explicit error handling is provided in this function; any issues with database operations would typically be handled by Django's ORM.

## Result Synopsis
This function does not return any value (`None`). It sets up test users and a course, which are available as attributes of the `setUp` class instance for use in subsequent tests.

## Docstring Draft
```python
"""Sets up the initial state for acceptance tests by creating test users and a course.

Args:
    self (Method): Reference to the class instance.

Returns:
    None

Raises:
    ValueError: If Django's ORM encounters an error during object creation.
"""
``````

## test_assignCourse  
``/Project/project_app/acceptance_tests/assign_course.py``  
```def test_assignCourse(self):
        self.admin.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.admin.post('/home/assignCourse/', {'courseID': 'courseone', 'userToFind': "userone"})
        self.assertEqual(response.context['Message'], "Course assigned successfully", msg="Course Not Assigned")```  

**Documentation:**
```python## Overview
This code defines a unit test method `test_assignCourse` to verify that the course assignment functionality works correctly. It logs in as an admin, sends a request to assign a course to a user, and checks if the response indicates successful assignment.

## Interface
- **Signature**: `def test_assignCourse(self)`
- **Parameters**:
  | Name       | Type   | Purpose                              |
  |------------|--------|--------------------------------------|
  | self       | object | The instance of the test class.      |

## Inner Workings
1. **Admin Login**: The method logs in as an admin by sending a POST request to the root URL with admin credentials.
2. **Course Assignment**: After logging in, it sends another POST request to `/home/assignCourse/` with the course ID and user ID to assign a course to a user.
3. **Assertion**: It asserts that the message in the response context is "Course assigned successfully" using `self.assertEqual`.

## Edge Cases & Preconditions
- **Preconditions**:
  - An admin account must be available with credentials "admin" for login.
  - A course named "courseone" and a user named "userone" should exist.

- **Assumptions**:
  - The server correctly handles the POST requests to `/` and `/home/assignCourse/`.
  - The `response.context['Message']` contains the expected string upon successful assignment.
  
- **Potential Failure Modes**:
  - If the login fails, or if the course/user does not exist, the assertions may fail.

## Result Synopsis
The function returns `None`. It asserts that the message in the response context indicates a successful course assignment.

## Docstring Draft
```python
"""Logs in as an admin and assigns a course to a user. Verifies if the assignment is successful.

Args:
    self (object): The instance of the test class.

Raises:
    AssertionError: If the course assignment is not confirmed successfully.
"""
``````

## test_assignCourse_InvalidCourse  
``/Project/project_app/acceptance_tests/assign_course.py``  
```def test_assignCourse_InvalidCourse(self):
        self.admin.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.admin.post('/home/assignCourse/', {'courseID': 'nonexistentcourse', 'userToFind': "userone"})
        self.assertEqual(response.context['Message'], "Course not found", msg="Invalid Course Assigned")```  

**Documentation:**
```python## Overview
This code tests the functionality of assigning a course with an invalid course ID by ensuring that an appropriate error message is returned.

## Interface
- **Signature**: `test_assignCourse_InvalidCourse(self)`
- **Parameters**:
  | Name       | Type   | Purpose                  |
  |------------|--------|--------------------------|
  | self       | object | The instance of the test class |

## Inner Workings
1. The method logs in as an admin user by sending a POST request to `/` with the username and password.
2. It then attempts to assign a course to a user by sending another POST request to `/home/assignCourse/`, providing an invalid `courseID`.
3. It checks if the response context contains the expected error message "Course not found".
4. If the message is present, it asserts that the test passed; otherwise, it fails with the provided message.

## Edge Cases & Preconditions
- **Precondition**: There must be a user named "admin" with the password "admin" in the system.
- **Edge Case**: The code assumes that a course with the ID "nonexistentcourse" does not exist in the system.
- **Potential Failure Mode**: If the course is found or another error occurs, the test will fail.

## Result Synopsis
The function asserts that attempting to assign a non-existent course results in the message "Course not found" being returned in the response context.

## Docstring Draft
```python
"""Test assigning a course with an invalid course ID.

This method logs in as an admin user and attempts to assign a non-existent course.
It verifies that the appropriate error message is returned.

Args:
    self (object): The instance of the test class.

Raises:
    AssertionError: If the expected error message is not found in the response context.
"""
``````

## test_assignCourse_InvalidUser  
``/Project/project_app/acceptance_tests/assign_course.py``  
```def test_assignCourse_InvalidUser(self):
        self.admin.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.admin.post('/home/assignCourse/', {'courseID': 'courseone', 'userToFind': "nonexistentuser"})
        self.assertEqual(response.context['Message'], "User not found", msg="Invalid User Assigned")```  

**Documentation:**
```python## Overview
This code tests the functionality of assigning a course to a user in a web application, specifically handling the case where the user does not exist.

## Interface
- **Signature**: `test_assignCourse_InvalidUser(self)`
- **Parameters**:
  | Name         | Type   | Purpose                          |
  |--------------|--------|----------------------------------|
  | `self`       | object | The test class instance.           |

## Inner Workings
1. The method logs in as an admin user using a POST request to the `/` endpoint with credentials "admin" and "admin".
2. It then attempts to assign a course to a non-existent user by sending another POST request to the `/home/assignCourse/` endpoint with `courseID` set to 'courseone' and `userToFind` set to 'nonexistentuser'.
3. The method asserts that the response context contains a message indicating "User not found".
4. If the assertion fails, an error message stating "Invalid User Assigned" is provided.

## Edge Cases & Preconditions
- The user does not exist in the system.
- No login credentials are provided or incorrect credentials are used (though this case is not handled within the snippet).

## Result Synopsis
The code tests that attempting to assign a course to a non-existent user returns an appropriate error message indicating that the user was not found.

## Docstring Draft
```python
"""Tests assigning a course to a non-existent user.

This test logs in as an admin, attempts to assign a course to a nonexistent user,
and verifies that the response indicates "User not found".

Args:
    self (object): The test class instance.

Returns:
    None

Raises:
    AssertionError: If the expected message is not returned.
"""
``````

## test_assignCourse_AlreadyAssigned  
``/Project/project_app/acceptance_tests/assign_course.py``  
```def test_assignCourse_AlreadyAssigned(self):
        self.admin.post('/', {"name": "admin", "password": "admin"}, follow=True)
        self.admin.post('/home/assignCourse/', {'courseID': 'courseone', 'userToFind': "userone"})
        response = self.admin.post('/home/assignCourse/', {'courseID': 'courseone', 'userToFind': "userone"})
        self.assertEqual(response.context['Message'], "Course already assigned", msg="Course Reassigned")```  

**Documentation:**
```python## Overview
This code tests the functionality of assigning a course to a user in an application. It verifies that if a course is already assigned to a user, the system correctly handles this scenario by displaying a message indicating that the course is already assigned.

## Interface
- **Signature**: `test_assignCourse_AlreadyAssigned(self)`
- **Parameters**:
  | Name          | Type   | Purpose                   |
  |---------------|--------|---------------------------|
  | self          |        | Instance of the test class |

## Inner Workings
1. The method first logs in as an admin user by sending a POST request to `/` with appropriate credentials.
2. It then attempts to assign a course (`courseone`) to a user (`userone`) by sending another POST request to `/home/assignCourse/`.
3. The method is called a second time to simulate the scenario where the same course is assigned again.
4. After the second attempt, it checks if the response context contains a message indicating that the course is already assigned.
5. It asserts that this message matches the expected value and provides an error message if the assertion fails.

## Edge Cases & Preconditions
- **Preconditions**: The test assumes that:
  - There is an admin user with credentials "admin" and "admin".
  - There is a course named "courseone".
  - There is a user named "userone".
  - The first assignment of the course to the user was successful.
- **Edge Cases**: The method does not handle edge cases such as network errors, authentication failures, or non-existent courses/users. It assumes that these conditions are already met by other parts of the application.

## Result Synopsis
The function asserts that attempting to assign a course to a user who already has that course assigned results in the expected message "Course already assigned" being displayed in the response context.

## Docstring Draft
```python
"""Tests the functionality of assigning a course to a user when the course is already assigned.

Asserts that the system correctly handles the scenario by displaying a message indicating that the course is already assigned.

Args:
    self (object): Instance of the test class.

Raises:
    AssertionError: If the response context does not contain the expected message.
"""
``````

## TestCreateCourse  
``/Project/project_app/acceptance_tests/add_skills_test.py``  
```class TestCreateCourse(TestCase):
    supervisor = None
    thingList = None
    def setUp(self):
        self.supervisor = Client()
        self.validUser = User.objects.create(username="alidz", password="star", user_type="ta")
        self.validUser2 = User.objects.create(username="lucy", password="star", user_type="ta")
        self.invalidUser = User.objects.create(username="bob", password="star", user_type="prof")
        self.skill = Skill.objects.create(name="math", owner=self.validUser)

    def test_addSkill(self):
        self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/addSkills/', {'newSkill': 'science', "name": "alidz"})
        self.assertEqual(rsp.context['Message'], "Success!", msg="skill should be added")
        self.assertEqual(list(Skill.objects.filter(owner=self.validUser)).__len__(), 2)
        self.assertEqual(rsp.context['mySkills'], [self.skill, Skill.objects.get(name='science')], msg="list should be updated with new item added")

    def test_invalidUser(self):
        self.supervisor.post('/', {"name": "bob", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/addSkills/', {'newSkill': 'science', "name": "alidz"})
        self.assertEqual(rsp.context['Message'], "Failed to add skill", msg="skill should not be added")
        self.assertEqual(list(Skill.objects.filter(owner=self.invalidUser)).__len__(), 0)
        self.assertEqual(rsp.context['mySkills'], [],msg="list should still be empty")

    def test_duplicateSkill(self):
        self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/addSkills/', {'newSkill': 'math', "name": "alidz"})
        self.assertEqual(rsp.context['Message'], "Failed to add skill", msg="skill should not be added")
        self.assertEqual(list(Skill.objects.filter(owner=self.validUser)).__len__(), 1)

    def test_sameSkill_multiUser(self):
        self.supervisor.post('/', {"name": "lucy", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/addSkills/', {'newSkill': 'math', "name": "lucy"})
        self.assertEqual(rsp.context['Message'], "Success!", msg="skill should be added")
        self.assertEqual(list(Skill.objects.filter(owner=self.validUser2)).__len__(), 1)
        self.assertEqual(rsp.context['mySkills'], list(Skill.objects.filter(owner=self.validUser2)), msg="list should still be empty")```  

**Documentation:**
```python## Overview
The `TestCreateCourse` class contains several test methods to validate the functionality of adding skills in a course system, specifically focusing on permissions, duplicate handling, and user-specific skill lists.

## Interface
- **Signature**: `class TestCreateCourse(TestCase)`
- **Parameters**: None (all properties are initialized within the class)

## Inner Workings
1. **setUp()**:
   - Initializes a test client (`self.supervisor`).
   - Creates three users: a valid TA, another valid TA, and an invalid professor.
   - Creates one skill owned by the first valid user.

2. **test_addSkill()**:
   - Logs in as the first valid TA.
   - Attempts to add a new skill 'science' under the name 'alidz'.
   - Verifies that the skill was added successfully, updating both the database and the context variable `mySkills`.

3. **test_invalidUser()**:
   - Logs in as the invalid professor.
   - Tries adding a skill 'science' under the name 'alidz'.
   - Verifies that no changes were made to either the database or the context, confirming failure.

4. **test_duplicateSkill()**:
   - Logs in as the first valid TA.
   - Attempts to add an existing skill 'math' under the name 'alidz'.
   - Ensures that no new skill was added and the operation is flagged as a failure.

5. **test_sameSkill_multiUser()**:
   - Logs in as the second valid TA.
   - Adds the existing skill 'math' under the name 'lucy'.
   - Confirms that the skill is not added for the second user, but remains in the database and context list of the first user.

## Edge Cases & Preconditions
- **Preconditions**: The system assumes that the `User` and `Skill` models are correctly configured in Django. It also relies on the presence of a login endpoint (`/`) that authenticates users.
- **Assumptions**:
  - Only TA (TAs) can add skills, not professors or other user types.
  - Skills cannot be duplicated for a single user.
- **Potential Failure Modes**: 
  - Invalid user attempts to add a skill.
  - Duplicate skill addition by the same user.
- **Error Handling**: No explicit error handling is shown in the code; any exceptions raised by Django (e.g., `ObjectDoesNotExist`, `ValidationError`) will bubble up and may need to be caught elsewhere.

## Result Synopsis
The class tests various scenarios for adding skills, including successful additions, failures due to user permissions, and duplication checks. It updates both the database and context variables accordingly.

## Docstring Draft
```python
"""
A test case class for verifying skill creation in a course system.

Attributes:
    supervisor (Client): A test client instance.
    validUser (User): A valid TA user object.
    validUser2 (User): Another valid TA user object.
    invalidUser (User): An invalid professor user object.
    skill (Skill): An existing skill created by the validUser.
"""

def setUp(self):
    """Sets up test environment with users and an initial skill."""
    self.supervisor = Client()
    self.validUser = User.objects.create(username="alidz", password="star", user_type="ta")
    self.validUser2 = User.objects.create(username="lucy", password="star", user_type="ta")
    self.invalidUser = User.objects.create(username="bob", password="star", user_type="prof")
    self.skill = Skill.objects.create(name="math", owner=self.validUser)

def test_addSkill(self):
    """Tests successful addition of a new skill by a valid TA."""
    # Log in and add skill
    # Verify success message, updated database, and context

def test_invalidUser(self):
    """Tests unsuccessful addition of a skill by an invalid user."""
    # Log in as invalid user and attempt to add skill
    # Verify failure message, no changes to database or context

def test_duplicateSkill(self):
    """Tests handling of adding an existing skill for the same user."""
    # Log in and attempt to add an already existing skill
    # Verify failure message and unchanged count of skills

def test_sameSkill_multiUser(self):
    """Tests unsuccessful addition of a skill by another valid TA."""
    # Log in as second valid user and attempt to add an existing skill
    # Verify success for first user, no changes for second user
``````

## setUp  
``/Project/project_app/acceptance_tests/add_skills_test.py``  
```def setUp(self):
        self.supervisor = Client()
        self.validUser = User.objects.create(username="alidz", password="star", user_type="ta")
        self.validUser2 = User.objects.create(username="lucy", password="star", user_type="ta")
        self.invalidUser = User.objects.create(username="bob", password="star", user_type="prof")
        self.skill = Skill.objects.create(name="math", owner=self.validUser)```  

**Documentation:**
```python## Overview
This code sets up the environment for a test by creating users and a skill object.

## Interface
- **Signature**: `setUp(self)`
- **Parameters**:
  - None

## Inner Workings
1. The function initializes a client (`self.supervisor`) to interact with some system or API.
2. It creates three user objects: 
   - `validUser` with username "alidz" and type "ta".
   - `validUser2` with username "lucy" and type "ta".
   - `invalidUser` with username "bob" and type "prof". Note that this user should not be able to create a skill as they are of the wrong type.
3. It creates a skill object (`self.skill`) owned by `validUser`.

## Edge Cases & Preconditions
- Assumes that there is an existing User model and Skill model in the database or ORM being used.
- Assumes that the Client class can be instantiated without any parameters.
- Potential failure mode: If the User or Skill models are not available, or if the client instantiation fails, this setup method will not run successfully.

## Result Synopsis
This function sets up the environment by creating necessary user and skill objects, making them available for further tests in the test class.

## Docstring Draft
```python
"""Sets up the environment for the test suite.

Args:
    None

Returns:
    None

Raises:
    None
"""
``````

## test_addSkill  
``/Project/project_app/acceptance_tests/add_skills_test.py``  
```def test_addSkill(self):
        self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/addSkills/', {'newSkill': 'science', "name": "alidz"})
        self.assertEqual(rsp.context['Message'], "Success!", msg="skill should be added")
        self.assertEqual(list(Skill.objects.filter(owner=self.validUser)).__len__(), 2)
        self.assertEqual(rsp.context['mySkills'], [self.skill, Skill.objects.get(name='science')], msg="list should be updated with new item added")```  

**Documentation:**
```python## Overview
This code is a test function for adding a skill to a user's profile in a web application. It asserts that the skill is successfully added and updates the user's skills list accordingly.

## Interface
- **Signature**: `test_addSkill(self)`
  - **Parameters**: None, as it is an instance method of a class.
  
## Inner Workings
1. The supervisor logs in with credentials (`"name": "alidz", "password": "star"`).
2. It then attempts to add a new skill (`'science'`) for the user `"alidz"`.
3. It checks if the response context contains the message "Success!" indicating that the skill was added successfully.
4. It verifies that the number of skills owned by `self.validUser` is now 2, assuming there was one skill initially.
5. Finally, it confirms that the updated list of skills in the response context includes both the original skill and the newly added 'science' skill.

## Edge Cases & Preconditions
- **Preconditions**: 
  - There must be an existing user with the name "alidz".
  - The user must have at least one skill initially.
  - The supervisor must have valid credentials to log in.
  
- **Potential Failure Modes**:
  - If `self.validUser` does not exist, or if there is no initial skill for that user, the test will fail.
  - If the login fails, subsequent requests may fail.

## Result Synopsis
The function asserts that a new skill is successfully added to the user's profile and updates the skills list accordingly. It checks both the response message and the updated database entries.

## Docstring Draft
```python
"""Tests adding a skill to a user's profile.

Args:
    None, as it is an instance method of a class.

Raises:
    AssertionError: If any of the assertions fail.
"""
``````

## test_invalidUser  
``/Project/project_app/acceptance_tests/add_skills_test.py``  
```def test_invalidUser(self):
        self.supervisor.post('/', {"name": "bob", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/addSkills/', {'newSkill': 'science', "name": "alidz"})
        self.assertEqual(rsp.context['Message'], "Failed to add skill", msg="skill should not be added")
        self.assertEqual(list(Skill.objects.filter(owner=self.invalidUser)).__len__(), 0)
        self.assertEqual(rsp.context['mySkills'], [],msg="list should still be empty")```  

**Documentation:**
```python## Overview
- This code tests the functionality of adding a skill to a user's account when the user is invalid. It ensures that an error message is returned and no new skills are added.

## Interface
- **Signature**: `test_invalidUser(self)`
- **Parameters**:
  | Name    | Type   | Purpose                          |
  |---------|--------|----------------------------------|
  | `self`  | object | The test case instance.          |

## Inner Workings
- The function starts by posting to the root URL with a valid user credentials.
- It then attempts to add a skill ('science') for an invalid user.
- It checks that the response context contains the expected error message "Failed to add skill".
- It verifies that no new skills have been added to the database for the invalid user.
- Finally, it asserts that the 'mySkills' list in the response context is empty.

## Edge Cases & Preconditions
- The function assumes that `self.supervisor` and `self.invalidUser` are properly initialized and available for use.
- It also assumes that the `Skill.objects.filter()` method works as expected to retrieve skills from the database.

## Result Synopsis
- The function asserts that attempting to add a skill for an invalid user results in an error message and no new skills being added to the database.

## Docstring Draft
```python
"""Tests adding a skill for an invalid user.

This test ensures that when a user is invalid, attempting to add a skill does not succeed and the appropriate error message is returned.

Args:
    self (object): The test case instance.

Returns:
    None

Raises:
    AssertionError: If any of the assertions fail.
"""
``````

## test_duplicateSkill  
``/Project/project_app/acceptance_tests/add_skills_test.py``  
```def test_duplicateSkill(self):
        self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/addSkills/', {'newSkill': 'math', "name": "alidz"})
        self.assertEqual(rsp.context['Message'], "Failed to add skill", msg="skill should not be added")
        self.assertEqual(list(Skill.objects.filter(owner=self.validUser)).__len__(), 1)```  

**Documentation:**
```python## Overview
The `test_duplicateSkill` function tests the behavior of adding a duplicate skill for a user, ensuring that it fails gracefully and does not add an additional skill record.

## Interface
- **Signature**: `def test_duplicateSkill(self)`
- **Parameters**: None

## Inner Workings
1. The function logs in as the supervisor using the POST request to `/` with credentials.
2. It then attempts to add a new skill (`'math'`) for the user `"alidz"` using a POST request to `/home/addSkills/`.
3. The response context is checked to ensure that the message indicates a failure to add the skill, as expected.
4. Finally, it verifies that only one skill record exists in the database for the user, indicating that the duplicate addition was not successful.

## Edge Cases & Preconditions
- **Preconditions**:
  - The supervisor should have the necessary permissions to add skills.
  - The `validUser` should be defined and correctly mapped to a user in the system.
- **Edge Cases**:
  - If the skill already exists for the user, the function should handle this gracefully without adding another record.

## Result Synopsis
The function does not return any value explicitly; instead, it asserts that the response context contains the expected error message and that the number of skills in the database remains unchanged after attempting to add a duplicate skill.

## Docstring Draft
```python
"""Tests the behavior of attempting to add a duplicate skill for a user.

This test logs in as the supervisor, attempts to add a duplicate skill, and verifies
that the skill is not added and an error message is returned.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If the response context does not contain the expected error message.
"""
``````

## test_sameSkill_multiUser  
``/Project/project_app/acceptance_tests/add_skills_test.py``  
```def test_sameSkill_multiUser(self):
        self.supervisor.post('/', {"name": "lucy", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/addSkills/', {'newSkill': 'math', "name": "lucy"})
        self.assertEqual(rsp.context['Message'], "Success!", msg="skill should be added")
        self.assertEqual(list(Skill.objects.filter(owner=self.validUser2)).__len__(), 1)
        self.assertEqual(rsp.context['mySkills'], list(Skill.objects.filter(owner=self.validUser2)), msg="list should still be empty")```  

**Documentation:**
```python## Overview
This function tests the addition of a skill by a supervisor to another user's account, verifying that the skill is added correctly without affecting the original user's skills.

## Interface
- **Signature**: `test_sameSkill_multiUser(self)`
- **Parameters**: None

## Inner Workings
1. The test first logs in as a supervisor using a POST request with the path `'/'` and data containing the username "lucy" and password "star".
2. It then attempts to add a skill 'math' for the user "lucy" using a POST request with the path `'/home/addSkills/'` and data containing the new skill.
3. The response is checked to ensure that the context variable `'Message'` contains the string "Success!".
4. It verifies that the number of skills associated with `self.validUser2` (the second user) is 1.
5. Finally, it checks that the list of skills in the context variable `'mySkills'` for the second user matches the list of skills retrieved from the database.

## Edge Cases & Preconditions
- Assumes that `self.supervisor`, `self.validUser2`, and related setup are properly configured and initialized before this test is run.
- The function does not handle any exceptions or errors in the process, relying on assertions to catch failures. If any assertion fails, it will raise an AssertionError.

## Result Synopsis
The code returns no explicit value; it relies on assertions to validate that the skill was added successfully and that the second user's skills list is correctly updated.

## Docstring Draft
```python
"""
Tests adding a skill by a supervisor to another user's account, ensuring that the skill is added correctly without affecting the original user's skills.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If any of the assertions fail.
"""
``````

## ViewSkillsTest  
``/Project/project_app/acceptance_tests/view_TA_skills.py``  
```class ViewSkillsTest(TestCase):
    def setUp(self):
        self.Admin = Client()
                                        
        self.ta_user = User.objects.create(username='joe', user_type='ta')
                                            
        Skill.objects.create(name='math', owner=self.ta_user)
        Skill.objects.create(name='science', owner=self.ta_user)
    def test_ta_user_in_system(self):
        self.Admin.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.Admin.post('/home/viewSkills/', {'userToFind': 'joe'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(Skill.objects.filter(owner=User.objects.get(username='joe', user_type='ta'))).__len__(), 2,
                         msg='not correct count of TAs skills')

    def test_ta_user_not_in_system(self):
        self.Admin.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.Admin.post('/home/viewSkills/', {'userToFind': 'nobody'})
        self.assertEqual(response.context['Message'], "User matching query does not exist.", msg="Non existent TA Not Caught")```  

**Documentation:**
```python## Overview
The code defines a test class `ViewSkillsTest` that inherits from `TestCase` to verify the functionality of viewing skills for a Teaching Assistant (TA) user.

## Interface
- **Signature**: `class ViewSkillsTest(TestCase)`
- **Parameters**:
  - None

## Inner Workings
1. **Setup Method (`setUp`)**:
   - Creates an admin client and a TA user.
   - Assigns two skills ('math' and 'science') to the TA user.

2. **Test Method (`test_ta_user_in_system`)**:
   - Logs in as an admin using the admin client.
   - Attempts to view skills for a user named 'joe'.
   - Verifies that the response status code is 200 (OK).
   - Checks that the number of skills associated with the TA user 'joe' is 2.

3. **Test Method (`test_ta_user_not_in_system`)**:
   - Logs in as an admin using the admin client.
   - Attempts to view skills for a non-existent user named 'nobody'.
   - Verifies that the response context contains the message "User matching query does not exist."

## Edge Cases & Preconditions
- Assumes the existence of an `admin` user with username 'admin' and password 'admin'.
- Assumes the existence of the `Client`, `User`, and `Skill` models from Django and a database setup.
- Checks for proper error handling when attempting to view skills for a non-existent user.

## Result Synopsis
The code returns HTTP responses with status codes 200 or an error message, confirming whether the skills for a TA user are correctly displayed or if an error is raised when trying to access non-existent data.

## Docstring Draft
```python
"""Tests the functionality of viewing skills for a Teaching Assistant (TA) user.

Returns:
    None: This method does not return any value.
"""
``````

## setUp  
``/Project/project_app/acceptance_tests/view_TA_skills.py``  
```def setUp(self):
        self.Admin = Client()
                                        
        self.ta_user = User.objects.create(username='joe', user_type='ta')
                                            
        Skill.objects.create(name='math', owner=self.ta_user)
        Skill.objects.create(name='science', owner=self.ta_user)```  

**Documentation:**
```python## Overview
This code initializes a test environment by creating an admin client and several skills associated with a TA (Teaching Assistant) user.

## Interface
### Signature
```python
def setUp(self):
```

### Parameters
| Parameter | Type | Purpose |
|-----------|------|---------|
| self      | object | The instance of the class, typically used to access attributes and methods of that class. |

## Inner Workings
1. **Admin Client Creation**: 
   - A new admin client is instantiated using `Client()`. This likely sets up an environment for testing administrative functionalities.
   
2. **TA User Creation**:
   - A user object is created with the username 'joe' and type 'ta'. This represents a Teaching Assistant in the system.

3. **Skill Creation**:
   - Two skill objects are created, each owned by the TA user. The skills have names 'math' and 'science'.

## Edge Cases & Preconditions
- The function assumes that `Client` and `User` models are properly defined and accessible within the environment.
- No explicit error handling is included for cases where creating users or skills fails.
- It is assumed that the database connection is active during the execution of this method.

## Result Synopsis
The `setUp` method initializes a test environment by setting up an admin client and creating a TA user along with two associated skills. No value is returned; it primarily sets up state for further tests.

## Docstring Draft
```python
"""Sets up the test environment.

This method creates an admin client and several skills associated with a TA (Teaching Assistant) user.

Args:
    self: The instance of the class, used to access attributes and methods of that class.

Returns:
    None

Raises:
    None
"""
``````

## test_ta_user_in_system  
``/Project/project_app/acceptance_tests/view_TA_skills.py``  
```def test_ta_user_in_system(self):
        self.Admin.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.Admin.post('/home/viewSkills/', {'userToFind': 'joe'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(Skill.objects.filter(owner=User.objects.get(username='joe', user_type='ta'))).__len__(), 2,
                         msg='not correct count of TAs skills')```  

**Documentation:**
```python## Overview
This code tests whether a TA ( Teaching Assistant) user's skills are correctly displayed in the system.

## Interface
- **Signature**: `test_ta_user_in_system(self)`
- **Parameters**:
    - None

## Inner Workings
1. The function sends a POST request to the root URL (`/`) with admin credentials to log in as an administrator.
2. It then sends another POST request to the `/home/viewSkills/` URL, specifying `'joe'` as the `userToFind`.
3. The function asserts that the response status code is 200, indicating a successful HTTP request.
4. Finally, it checks if the number of skills associated with the user 'joe', who is classified as a TA (`user_type='ta'`), matches the expected count.

## Edge Cases & Preconditions
- The test assumes that there are exactly two skills associated with the user 'joe'.
- If the count does not match the expected value, an assertion error will be raised.
- The function relies on the `Admin.post()` method to log in, and it expects this method to handle the session state correctly.

## Result Synopsis
The code asserts that when a TA user's skills are viewed, the correct number of skills (two in this case) is displayed. If not, an assertion error will be raised.

## Docstring Draft
```python
"""Tests whether a TA user's skills are correctly displayed in the system.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If the count of TAs skills does not match the expected value.
"""
``````

## test_ta_user_not_in_system  
``/Project/project_app/acceptance_tests/view_TA_skills.py``  
```def test_ta_user_not_in_system(self):
        self.Admin.post('/', {"name": "admin", "password": "admin"}, follow=True)
        response = self.Admin.post('/home/viewSkills/', {'userToFind': 'nobody'})
        self.assertEqual(response.context['Message'], "User matching query does not exist.", msg="Non existent TA Not Caught")```  

**Documentation:**
```python## Overview
This code tests the functionality of handling a non-existent user query in a system where only administrators are allowed to access skills information. It involves logging in as an admin and attempting to view skills for a non-existent user, then asserting that the appropriate error message is returned.

## Interface
- **Signature**: `test_ta_user_not_in_system(self)`
- **Parameters**:
  | Name    | Type   | Purpose                         |
  |---------|--------|-----------------------------------|
  | self    | object | The test case instance.           |

## Inner Workings
1. **Admin Login**: The code logs in as an admin user by sending a POST request to the root URL with admin credentials (`name="admin"`, `password="admin"`). The response is followed to ensure session persistence.
2. **View Skills Request**: After logging in, the code sends another POST request to the `/home/viewSkills/` endpoint with a payload containing a non-existent user's name (`userToFind='nobody'`).
3. **Validation of Response**: The code checks that the context variable `Message` from the response contains the expected error message `"User matching query does not exist."`. If this condition is met, it passes; otherwise, it fails with the message "Non existent TA Not Caught".

## Edge Cases & Preconditions
- **Precondition**: The test assumes that there is no user named 'nobody' in the system.
- **Assumptions**: 
  - The `Admin` object has methods `.post(url, data, follow=True)` to send POST requests and persist session cookies.
  - The server correctly handles login and view skills requests.
- **Potential Failure Modes**:
  - If the user 'nobody' exists, the test will fail because it expects an error message indicating non-existence.
  - Network issues or server errors could cause unexpected behavior.

## Result Synopsis
The code tests that attempting to access a user's skills information as an admin for a non-existent user results in the correct error message being returned. If successful, it passes; otherwise, it fails with the specified message.

## Docstring Draft
```python
"""Tests handling of querying skills for a non-existent user as an admin.

This function logs in as an admin and attempts to view skills for a user that does not exist.
It then asserts that the appropriate error message is returned.

Args:
    self (object): The test case instance.

Raises:
    AssertionError: If the expected error message is not found in the response context.
"""
``````

## TestCreateCourse  
``/Project/project_app/acceptance_tests/create_course_test.py``  
```class TestCreateCourse(TestCase):
    supervisor = None
    thingList = None
    def setUp(self):
        self.supervisor = Client()
        self.user = User.objects.create(username="alidz", password="star")
        self.course1 = Course.objects.create(name="CS 150", dateTime="2022-02-12 14:30:34").save()
        self.course2 = Course.objects.create(name="CS 250", dateTime="2022-02-12 14:30:34").save()

    def test_addCourse(self):
        self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/createCourse/', {'courseName': 'CS 351', 'courseTime': "2022-02-12 14:30:34"})
        self.assertEqual(rsp.context['Message'], "course creation successful", msg="list should be updated with new item added")
        self.assertEqual(list(Course.objects.all()).__len__(), 3)

    def test_duplicateCourse(self):
        self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/createCourse/', {'courseName': 'CS 250', 'courseTime': "2022-02-12 14:30:34"})
        self.assertEqual(rsp.context['Message'], "course already exists", msg="duplicate courses should cause error")
        self.assertEqual(list(Course.objects.all()).__len__(), 2, msg='number of courses should not change from original set up')

    def test_invalidFormat(self):
        self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/createCourse/', {'courseName': "CS 550", 'courseTime': "5:15"})
        self.assertEqual(rsp.context['Message'], "time must be YYYY-MM-DD HR:MN:SC",
                         msg="should not add course with invalid time")
        self.assertEqual(list(Course.objects.all()).__len__(), 2, msg='courses in db should not change')

    def test_courseList(self):
        self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/createCourse/')
        self.assertEqual("CS 150", rsp.context['course_list'][0].name, msg="Course list inaccurate/not found")
        self.assertEqual("CS 250", rsp.context['course_list'][1].name, msg="Course list inaccurate/not found")

    def test_courseList_add(self):
        self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/createCourse/', {'courseName': "CS 550", 'courseTime': "2022-02-12 14:30:34"})
        self.assertEqual("CS 150", rsp.context['course_list'][0].name, msg="Course list inaccurate/not found")
        self.assertEqual("CS 250", rsp.context['course_list'][1].name, msg="Course list inaccurate/not found")
        self.assertEqual("CS 550", rsp.context['course_list'][2].name, msg="Course list inaccurate/not found")```  

**Documentation:**
```python## Overview
This code defines a test class `TestCreateCourse` that tests the functionality of creating courses in an application. It uses Django's testing framework and interacts with a database to ensure courses are created correctly.

## Interface
### Signature:
```python
class TestCreateCourse(TestCase):
```

### Parameters:
| Name | Type | Purpose |
|------|------|---------|
| None | None | This is a test class, so there are no parameters passed to the constructor. |

## Inner Workings
- The `setUp` method initializes a supervisor client and creates two courses in the database.
- The `test_addCourse` method tests creating a new course and verifies that it is added successfully.
- The `test_duplicateCourse` method attempts to create a duplicate course and checks if an error message is returned.
- The `test_invalidFormat` method tries to create a course with an invalid time format and verifies the error message.
- The `test_courseList` method retrieves a list of courses and checks if the correct courses are present.
- The `test_courseList_add` method creates a new course and then retrieves the list again, verifying that the new course is included.

## Edge Cases & Preconditions
- **Edge Case**: Attempting to create a duplicate course should return an error message indicating that the course already exists.
- **Edge Case**: Creating a course with an invalid time format should return an error message indicating the correct time format.
- **Precondition**: The test assumes that there are no existing courses in the database before running. If there are, they might interfere with the tests.

## Result Synopsis
The tests ensure that courses can be created and retrieved correctly, and that errors are returned when invalid inputs are provided. They also verify that duplicate courses cannot be added without an error message.

## Docstring Draft
```python
"""Test class for creating courses in the application.

Attributes:
    supervisor (Client): A client used to simulate user actions.
    course1 (Course): A test course object.
    course2 (Course): Another test course object.

Methods:
    setUp(): Initializes the test environment with necessary objects.
    test_addCourse(): Tests creating a new course and verifies its existence.
    test_duplicateCourse(): Tests handling of duplicate courses.
    test_invalidFormat(): Tests error handling for invalid time formats.
    test_courseList(): Retrieves and tests the list of courses.
    test_courseList_add(): Creates a new course and verifies its inclusion in the list.
"""
``````

## setUp  
``/Project/project_app/acceptance_tests/create_course_test.py``  
```def setUp(self):
        self.supervisor = Client()
        self.user = User.objects.create(username="alidz", password="star")
        self.course1 = Course.objects.create(name="CS 150", dateTime="2022-02-12 14:30:34").save()
        self.course2 = Course.objects.create(name="CS 250", dateTime="2022-02-12 14:30:34").save()```  

**Documentation:**
```python## Overview
This code snippet is responsible for setting up the environment before running tests in a test class.

## Interface
### Signature
```python
def setUp(self):
```

### Parameters
| Name | Type | Purpose |
|------|------|---------|
| None | - | This method does not take any parameters. |

## Inner Workings
- The `setUp` method initializes several objects and variables required for running tests in a test class.
- It creates an instance of the `Client` class, likely used to simulate user actions or API requests during testing.
- It creates two instances of the `User` model with specific usernames and passwords. This could be used for authorization checks during tests.
- It creates two instances of the `Course` model with identical names but different datetime values. This might be used to test scenarios involving multiple courses.

## Edge Cases & Preconditions
- The method does not make any assumptions about the state of the database before it runs, so it is safe to call it at the start of each test.
- There are no error-handling mechanisms in this code snippet, and the creation of objects might fail if there are issues with the database or model constraints. However, given that `save()` is not called without creating an instance first, the assumption here is that the models are correctly defined and can be instantiated.

## Result Synopsis
The `setUp` method initializes a test environment by setting up instances of `Client`, `User`, and `Course`. This setup allows subsequent tests to perform actions as if they were running in a real-world scenario without interference from other test cases.

## Docstring Draft
```python
"""Initializes the test environment for each test method.

This method sets up an instance of the Client class, creates two users, and creates two courses.
These are intended to be used in subsequent tests to simulate real scenarios.

Args:
    None

Returns:
    None

Raises:
    None
"""
``````

## test_addCourse  
``/Project/project_app/acceptance_tests/create_course_test.py``  
```def test_addCourse(self):
        self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/createCourse/', {'courseName': 'CS 351', 'courseTime': "2022-02-12 14:30:34"})
        self.assertEqual(rsp.context['Message'], "course creation successful", msg="list should be updated with new item added")
        self.assertEqual(list(Course.objects.all()).__len__(), 3)```  

**Documentation:**
```python## Overview
The `test_addCourse` function tests the process of adding a course by simulating a supervisor posting to a create course endpoint and verifying that the course is successfully created.

## Interface
- **Signature**: `def test_addCourse(self)`
- **Parameters**:
  | Name    | Type   | Purpose                  |
  |---------|--------|--------------------------|
  | self    | object | Instance of the test class |

## Inner Workings
1. The function first simulates a supervisor posting to the root URL (`/`) with a payload containing `name` and `password`. This is done using the `post` method, and the `follow=True` parameter ensures that any redirects are followed.
2. Next, it posts to the `/home/createCourse/` endpoint with a payload containing `courseName` and `courseTime`.
3. It then asserts that the response context contains a message indicating "course creation successful".
4. Finally, it checks if the number of courses in the database is 3 by comparing the length of the list returned by `Course.objects.all()` to 3.

## Edge Cases & Preconditions
- Assumes that there are already two courses in the database before this test runs.
- Any failure during the posting process or if the course creation fails will result in a test failure.
- If an error occurs during the execution of these steps, it is not explicitly handled within this function. The assertions will raise exceptions if any condition is not met.

## Result Synopsis
The function asserts that a course is successfully added and that the number of courses in the database increases to 3.

## Docstring Draft
```python
"""Tests the process of adding a course by simulating a supervisor posting to the create course endpoint and verifying that the course is successfully created.

Args:
    self (object): Instance of the test class

Returns:
    None

Raises:
    AssertionError: If any of the assertions fail, indicating a failure in the course creation process.
"""
``````

## test_duplicateCourse  
``/Project/project_app/acceptance_tests/create_course_test.py``  
```def test_duplicateCourse(self):
        self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/createCourse/', {'courseName': 'CS 250', 'courseTime': "2022-02-12 14:30:34"})
        self.assertEqual(rsp.context['Message'], "course already exists", msg="duplicate courses should cause error")
        self.assertEqual(list(Course.objects.all()).__len__(), 2, msg='number of courses should not change from original set up')```  

**Documentation:**
```python## Overview
This code tests the functionality of creating a course that already exists in the system. It ensures that attempting to create a duplicate course results in an error and that the total number of courses remains unchanged.

## Interface
- **Signature**: `test_duplicateCourse(self)`
- **Parameters**:
  | Name     | Type   | Purpose                      |
  |----------|--------|------------------------------|
  | self     | object | The test class instance.       |

## Inner Workings
1. **Login as Supervisor**: The method first logs in the supervisor user using `self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)`.
2. **Create Course**: It then attempts to create a course with the name 'CS 250' and time '2022-02-12 14:30:34' using `self.supervisor.post('/home/createCourse/', {'courseName': 'CS 250', 'courseTime': "2022-02-12 14:30:34"})`.
3. **Verify Error Message**: The method checks if the response context contains the message "course already exists" using `self.assertEqual(rsp.context['Message'], "course already exists", msg="duplicate courses should cause error")`. This ensures that attempting to create a duplicate course results in an error.
4. **Check Course Count**: Finally, it verifies that the total number of courses remains unchanged by asserting the length of `Course.objects.all()` is 2 using `self.assertEqual(list(Course.objects.all()).__len__(), 2, msg='number of courses should not change from original set up')`.

## Edge Cases & Preconditions
- **Preconditions**: The test assumes that there is already one course created before running the test.
- **Edge Cases**: None explicitly handled; however, implicit assumptions include that the course creation logic correctly identifies duplicates and does not add new courses if a duplicate is detected.

## Result Synopsis
The code successfully tests the scenario where attempting to create a course that already exists results in an error and does not alter the total number of courses in the system.

## Docstring Draft
```python
"""Tests creating a duplicate course.

This method logs in as a supervisor, attempts to create a course that already exists,
and verifies that an appropriate error message is returned while ensuring the total
number of courses remains unchanged.

Args:
    self (object): The test class instance.

Raises:
    AssertionError: If the expected error message is not received or if the course count changes.
"""
``````

## test_invalidFormat  
``/Project/project_app/acceptance_tests/create_course_test.py``  
```def test_invalidFormat(self):
        self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/createCourse/', {'courseName': "CS 550", 'courseTime': "5:15"})
        self.assertEqual(rsp.context['Message'], "time must be YYYY-MM-DD HR:MN:SC",
                         msg="should not add course with invalid time")
        self.assertEqual(list(Course.objects.all()).__len__(), 2, msg='courses in db should not change')```  

**Documentation:**
```python## Overview
This code tests the functionality of creating a course with an invalid format for the course time.

## Interface
- **Signature**: `test_invalidFormat(self)`
- **Parameters**:
  | Name    | Type     | Purpose                |
  |---------|----------|------------------------|
  | self    | object   | The test case instance |

## Inner Workings
1. The method `test_invalidFormat` is invoked on an instance of a class that inherits from some form of test framework (likely `unittest.TestCase` or a similar structure).
2. It sends a POST request to the root URL (`/`) with data containing an invalid user name and password.
3. Subsequently, it sends another POST request to `/home/createCourse/` with valid course name but an invalid time format ("5:15").
4. The response context is checked to ensure that the message returned matches the expected error message ("time must be YYYY-MM-DD HR:MN:SC").
5. The number of courses in the database is verified to remain unchanged (i.e., it should still have 2 courses).

## Edge Cases & Preconditions
- The function assumes that there are already 2 courses in the database before running the test.
- It checks for a specific error message related to time format, which must be present in the response context.
- There is no explicit error handling within this method; any exceptions would propagate up to the test framework.

## Result Synopsis
The function asserts that creating a course with an invalid time format results in the correct error message being displayed and does not alter the number of courses in the database.

## Docstring Draft
```python
"""Tests creating a course with an invalid time format.

This method sends POST requests to simulate user actions, checks the response for the expected error message,
and verifies that the course count remains unchanged.

Args:
    self (object): The test case instance.

Returns:
    None

Raises:
    AssertionError: If the response context does not contain the expected error message or if the number of courses changes.
"""
``````

## test_courseList  
``/Project/project_app/acceptance_tests/create_course_test.py``  
```def test_courseList(self):
        self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/createCourse/')
        self.assertEqual("CS 150", rsp.context['course_list'][0].name, msg="Course list inaccurate/not found")
        self.assertEqual("CS 250", rsp.context['course_list'][1].name, msg="Course list inaccurate/not found")```  

**Documentation:**
```python## Overview
This code tests the functionality of retrieving a course list from a web application. It simulates a user logging in and then checking if the correct courses are listed.

## Interface
- **Signature**: `test_courseList(self)`
- **Parameters**:
  | Name   | Type   | Purpose                  |
  |--------|--------|----------------------------|
  | self   | object | The test case instance     |

## Inner Workings
1. The method logs in a user with the username "alidz" and password "star" using `self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)`.
2. It then posts to `/home/createCourse/` to retrieve the course list.
3. It asserts that the first course in the list has the name "CS 150".
4. It asserts that the second course in the list has the name "CS 250".

## Edge Cases & Preconditions
- The test assumes that there are at least two courses named "CS 150" and "CS 250" in the database.
- It also assumes that the login credentials provided ("alidz", "star") are valid and that the user has permission to access the course list.

## Result Synopsis
The code does not return any value explicitly but asserts conditions based on the retrieved course list. If any of the assertions fail, the test will raise an `AssertionError`.

## Docstring Draft
```python
"""Tests retrieving a course list from the web application.

Asserts that the correct courses are listed after logging in with valid credentials.
"""
``````

## test_courseList_add  
``/Project/project_app/acceptance_tests/create_course_test.py``  
```def test_courseList_add(self):
        self.supervisor.post('/', {"name": "alidz", "password": "star"}, follow=True)
        rsp = self.supervisor.post('/home/createCourse/', {'courseName': "CS 550", 'courseTime': "2022-02-12 14:30:34"})
        self.assertEqual("CS 150", rsp.context['course_list'][0].name, msg="Course list inaccurate/not found")
        self.assertEqual("CS 250", rsp.context['course_list'][1].name, msg="Course list inaccurate/not found")
        self.assertEqual("CS 550", rsp.context['course_list'][2].name, msg="Course list inaccurate/not found")```  

**Documentation:**
```python## Overview
The function `test_courseList_add` in the file `Project/project_app/acceptance_tests/create_course_test.py` is designed to test the addition of a course to a list of courses. It simulates a user logging in and then creating a new course, verifying that the new course appears correctly in the list.

## Interface
- **Signature**: `def test_courseList_add(self)`
  - **Parameters**:
    - None

## Inner Workings
1. The function first logs in as a supervisor by posting to the root URL with credentials (`name` and `password`).
2. It then creates a new course by posting to the `/home/createCourse/` endpoint with details about the course (`courseName` and `courseTime`).
3. Finally, it asserts that the courses listed in the response context contain specific names (`"CS 150"`, `"CS 250"`, and `"CS 550"`), ensuring that the new course has been added correctly.

## Edge Cases & Preconditions
- **Preconditions**:
  - There must be a supervisor account with credentials `{"name": "alidz", "password": "star"}`.
  - The courses with names `"CS 150"`, `"CS 250"`, and `"CS 550"` must already exist in the system to be found in the list.
- **Potential Failure Modes**:
  - If the supervisor login fails, the test will fail.
  - If the course creation fails, the test will fail.
  - If any of the courses specified (`"CS 150"`, `"CS 250"`, `"CS 550"`) are not found in the list, the test will fail.

## Result Synopsis
The function asserts that the new course (`"CS 550"`) has been added to the list of courses correctly by verifying its presence along with other known courses (`"CS 150"` and `"CS 250"`).

## Docstring Draft
```python
"""Tests adding a course to the course list.

This test logs in as a supervisor, creates a new course, and verifies that the course appears in the course list.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If any of the courses are not found in the list.
"""
``````

## TestLogin  
``/Project/project_app/acceptance_tests/login_test.py``  
```class TestLogin(TestCase):
    def setUp(self):
        self.supervisor = Client()
        self.user = User.objects.create(username="user", password="1234", user_type='ta')

    def test_validLogin(self):
        rsp = self.supervisor.post('/', {"name": "user", "password": "1234"}, follow=True)
        self.assertRedirects(rsp, '/home/')
        self.assertEqual('_auth_user_id', self.supervisor.session, msg="User should be logged in and session should contain _auth_user_id key")

    def test_invalidUsername(self):
        rsp = self.supervisor.post('/', {"name": "wronguser", "password": "1234"}, follow=True)
        self.assertEqual(rsp, "Incorrect username or password.", msg="Should not be able to login with incorrect username")


    def test_invalidPassword(self):
        rsp = self.supervisor.post('/', {"name": "user", "password": "wrongpassword"}, follow=True)
        self.assertEqual(rsp, "Incorrect username or password.", msg="Should not be able to login with incorrect password")


    def test_missingFields(self):
        rsp = self.supervisor.post('/', {"name": "", "password": ""}, follow=True)
        self.assertEqual(rsp, "This field is required.", msg="Should not be able to login with missing fields")```  

**Documentation:**
```python## Overview
- This code defines a set of test cases for the login functionality in a web application using Django's `TestCase`. It tests various scenarios such as valid login, invalid username, invalid password, and missing fields.

## Interface
### Signature
```python
class TestLogin(TestCase):
    # Class methods and attributes are defined here.
```
### Parameters
| Name      | Type   | Purpose                         |
|-----------|--------|---------------------------------|
| None      |        | The class `TestLogin` does not take any parameters directly. All functionality is part of the class methods. |

## Inner Workings
- **setUp**: Initializes a client and creates a user for testing.
- **test_validLogin**: Sends a POST request with valid credentials and checks if the response redirects to `/home/` and contains `_auth_user_id` in the session.
- **test_invalidUsername**: Sends a POST request with an invalid username and checks if the response message indicates incorrect login details.
- **test_invalidPassword**: Sends a POST request with an invalid password and checks if the response message indicates incorrect login details.
- **test_missingFields**: Sends a POST request without any fields filled in and checks if the response message indicates required field errors.

## Edge Cases & Preconditions
- Assumes that Django's `Client` can be used to simulate HTTP requests.
- Assumes that the user model has fields for `username`, `password`, and `user_type`.
- Assumes that the URLs `/` and `/home/` exist in the application.
- If any of the test cases fail, they will raise an assertion error with a message indicating the failure.

## Result Synopsis
- The code does not return any values directly. It performs assertions to check if the login functionality behaves as expected under different conditions.

## Docstring Draft
```python
"""Tests for the login functionality.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If any of the test cases fail.
"""
``````

## setUp  
``/Project/project_app/acceptance_tests/login_test.py``  
```def setUp(self):
        self.supervisor = Client()
        self.user = User.objects.create(username="user", password="1234", user_type='ta')```  

**Documentation:**
```python## Overview
This code sets up the test environment by creating a `Client` instance and a `User` object for testing purposes.

## Interface
- **Signature**: `def setUp(self)`
- **Parameters**:
  | Name   | Type     | Purpose                     |
  |--------|----------|-----------------------------|
  | self   | Testcase | The test case instance.       |

## Inner Workings
1. A `Client` object is instantiated and assigned to the `self.supervisor` attribute, which represents a client for testing purposes.
2. A `User` object is created with the username "user", password "1234", and user type 'ta'. This user is then assigned to the `self.user` attribute.

## Edge Cases & Preconditions
- The code assumes that there are no existing users with the username "user" in the database, as creating a new user with an existing username would fail.
- If the `Client` class or `User.objects.create()` method raises any exceptions, they will not be caught by this function.

## Result Synopsis
This function does not return anything (`None`) but initializes two attributes of the test case instance: `self.supervisor` and `self.user`.

## Docstring Draft
```python
"""Set up the test environment.

Args:
    self (Testcase): The test case instance.

Returns:
    None

Raises:
    AssertionError: If there is already a user with the username 'user'.
"""
```

This docstring provides a brief summary of what the function does, its parameters, and expected behavior. It also mentions that an assertion error might be raised if a pre-existing user with the specified username exists.```

## test_validLogin  
``/Project/project_app/acceptance_tests/login_test.py``  
```def test_validLogin(self):
        rsp = self.supervisor.post('/', {"name": "user", "password": "1234"}, follow=True)
        self.assertRedirects(rsp, '/home/')
        self.assertEqual('_auth_user_id', self.supervisor.session, msg="User should be logged in and session should contain _auth_user_id key")```  

**Documentation:**
```python## Overview
- This code tests a valid login scenario by posting user credentials to the root URL and asserting that the response redirects to the home page and contains a specific session key indicating the user is logged in.

## Interface
### Signature
```python
def test_validLogin(self)
```
### Parameters
| Name    | Type  | Purpose                |
|---------|-------|------------------------|
| self    | obj   | The instance of the class|

## Inner Workings
- **POST Request**: The code sends a POST request to the root URL (`'/'`) with JSON data containing user credentials `{"name": "user", "password": "1234"}`. The `follow=True` parameter ensures that any redirects are followed.
- **Redirect Assertion**: It uses `self.assertRedirects(rsp, '/home/')` to verify that the response redirects to `/home/`.
- **Session Key Verification**: The code checks if `_auth_user_id` is present in the session by comparing it with the expected value (`self.supervisor.session`). If not found, an assertion error is raised with the message "User should be logged in and session should contain _auth_user_id key".

## Edge Cases & Preconditions
- **Valid Login Credentials**: Assumes that the credentials `"user"` and `"1234"` are valid.
- **Session Management**: Assumes that the `supervisor` object has a `session` attribute where user authentication status is stored.
- **Error Handling**: If `_auth_user_id` key is not found in the session, an assertion error is raised, indicating failure to log in.

## Result Synopsis
- The function asserts that a valid login redirects to `/home/` and sets `_auth_user_id` in the session, indicating successful user authentication.

## Docstring Draft
```python
"""Tests a valid login scenario by posting user credentials and asserting redirection and session state.

Args:
    self (obj): The instance of the class.

Returns:
    None

Raises:
    AssertionError: If the expected redirection or session key is not met.
"""
``````

## test_invalidUsername  
``/Project/project_app/acceptance_tests/login_test.py``  
```def test_invalidUsername(self):
        rsp = self.supervisor.post('/', {"name": "wronguser", "password": "1234"}, follow=True)
        self.assertEqual(rsp, "Incorrect username or password.", msg="Should not be able to login with incorrect username")```  

**Documentation:**
```python## Overview
The `test_invalidUsername` function tests the behavior of a login system when an invalid username is provided.

## Interface
- **Signature**: `def test_invalidUsername(self)`
- **Parameters**:
  | Name   | Type  | Purpose                          |
  |--------|-------|----------------------------------|
  | self   | object| The instance of the test class. |

## Inner Workings
1. The function sends a POST request to the root URL (`'/'`) with a dictionary containing an invalid username (`"wronguser"`) and a password (`"1234"`).
2. It follows any redirection that might occur after sending the request.
3. It asserts that the response from the server is equal to the string `"Incorrect username or password."`, indicating that the login attempt was unsuccessful due to an invalid username.

## Edge Cases & Preconditions
- The function assumes that there is a login system in place and that it can handle POST requests.
- It does not handle any specific exceptions, relying on the assertion to catch unexpected responses.

## Result Synopsis
The function asserts that attempting to log in with an incorrect username returns the expected error message.

## Docstring Draft
```python
"""Tests the behavior of the login system when an invalid username is provided.

Args:
    self (object): The instance of the test class.

Returns:
    None

Raises:
    AssertionError: If the response from the server does not match the expected error message.
"""
``````

## test_invalidPassword  
``/Project/project_app/acceptance_tests/login_test.py``  
```def test_invalidPassword(self):
        rsp = self.supervisor.post('/', {"name": "user", "password": "wrongpassword"}, follow=True)
        self.assertEqual(rsp, "Incorrect username or password.", msg="Should not be able to login with incorrect password")```  

**Documentation:**
```python## Overview
- This code tests the functionality of a login system by attempting to log in with an invalid password and verifying that the expected error message is returned.

## Interface
- **Signature**: `test_invalidPassword(self)`
- **Parameters**:
  | Name   | Type     | Purpose                         |
  |--------|----------|-----------------------------------|
  | self   | object   | Reference to the test class instance. |

## Inner Workings
1. The method `test_invalidPassword` is called within a test class, likely extending `unittest.TestCase`.
2. The `post` method of an attribute named `supervisor` (which is assumed to be an HTTP client) is used to send a POST request to the root URL (`'/'`) with form data containing a username and an incorrect password.
3. The `follow=True` parameter ensures that redirects are followed automatically.
4. The response from the server, stored in `rsp`, is compared using `self.assertEqual`.
5. If the response does not match the expected error message `"Incorrect username or password."`, the test will fail with the provided message.

## Edge Cases & Preconditions
- **Assumptions**: 
  - There exists an HTTP client named `supervisor` that can send POST requests and follow redirects.
  - The root URL (`'/'`) is accessible and contains a login form or mechanism.
  - The username `"user"` has been previously created and exists in the system.
  
- **Potential Failure Modes**:
  - If the server responds with a different error message or does not return an error at all, the test will fail.
  - If the `supervisor` HTTP client fails to send the request correctly or encounters network issues, it could lead to unexpected behavior.

## Result Synopsis
- The code returns nothing directly but asserts that the login attempt with an invalid password results in the expected error message being returned by the server.

## Docstring Draft
```python
"""Test the login functionality with an incorrect password and verify the error response.

This method sends a POST request to the root URL with an incorrect password and checks if the response is as expected.

Args:
    self (unittest.TestCase): Reference to the test class instance.

Raises:
    AssertionError: If the server does not return the expected error message upon login attempt.
"""
``````

## test_missingFields  
``/Project/project_app/acceptance_tests/login_test.py``  
```def test_missingFields(self):
        rsp = self.supervisor.post('/', {"name": "", "password": ""}, follow=True)
        self.assertEqual(rsp, "This field is required.", msg="Should not be able to login with missing fields")```  

**Documentation:**
```python## Overview
The code defines a method `test_missingFields` that tests the behavior of a web application's login functionality when submitted with missing name and password fields.

## Interface
- **Signature**: `test_missingFields(self)`
  - **Parameters**:
    | Name     | Type   | Purpose                          |
    |----------|--------|----------------------------------|
    | self     | object | The instance of the test class. |

## Inner Workings
1. The method sends a POST request to the root URL (`'/'`) with an empty `name` and `password`.
2. It follows any redirects that might occur after sending the request.
3. It asserts that the response from the server is equal to the string `"This field is required."`, which indicates that the login attempt failed due to missing fields.

## Edge Cases & Preconditions
- **Assumptions**: The web application responds with a specific message when any of the required fields are missing.
- **Potential Failure Modes**: If the web application does not return the expected error message, or if it behaves differently in other edge cases (e.g., empty spaces instead of actual empty strings), this test will fail.
- **Error Handling**: The method does not explicitly handle errors but relies on the assertion to catch failures.

## Result Synopsis
The function asserts that attempting to log in with missing fields results in a specific error message being returned from the web application.

## Docstring Draft
```python
"""Tests the behavior of logging in with missing name and password fields.

Asserts that submitting an empty name and password results in an appropriate error message.

Raises:
    AssertionError: If the expected error message is not received.
"""
```

This function is part of a test suite for login functionality, ensuring that the system properly handles requests lacking required information.```

## TestCreateDeleteAccount  
``/Project/project_app/acceptance_tests/create_delete_account_tests.py``  
```class TestCreateDeleteAccount(TestCase):
    supervisor = None

    def setUp(self):
        self.supervisor = Client()
        self.user = User.objects.create(username="tony", password="stark", name="Tony Stark", email="tonystark@gmail.com", phone = "(123) 555-5555", address = "999 Van Ness Ave, San Francisco, CA 94109")
        self.user1 = User.objects.create(username="user1", password="pass01", email="user1@gmail.com", phone = "(312) 555-5555", address = "999 Van Ness Ave, San Francisco, CA 94109")
        self.user2 = User.objects.create(username="user2", password="pass02", email="user2@gmail.com", phone = "(231) 555-5555", address = "999 Van Ness Ave, San Francisco, CA 94109")

    def test_createAccount(self):
        self.supervisor.post('/', {"name": "tony", "password": "stark"}, follow=True)
        rsp = self.supervisor.post('/home/createDeleteAccount/',
                                   {'action': 'create', 'username': 'newuser', 'password': 'newpassword', 'email': 'email@email.com', 'userToFind': ''}, follow=True)
        self.assertEqual(User.objects.count(), 4)
        new_user = User.objects.get(username="newuser")
        self.assertIsNotNone(new_user)
        self.assertEqual(new_user.username, "newuser")
        self.assertEqual(new_user.password, "newpassword")
                                                                  
                                                                                  

    def test_duplicateAccount(self):
        self.supervisor.login(username="tony", password="stark")
        rsp = self.supervisor.post('/home/createDeleteAccounts/', {'name': 'user1', 'password': 'pass01', 'email': 'user1@gmail.com'})
        self.assertEqual(User.objects.count(), 3)

    def test_deleteAccount(self):
        self.supervisor.login(username="tony", password="stark")
        rsp = self.supervisor.post('/home/createDeleteAccounts/', {'action': 'delete', 'account_id': self.user2.pk})
        self.assertEqual(User.objects.count(), 3)                                        

    def test_deleteNonexistentAccount(self):
        self.supervisor.login(username="user4", password="pass04")
        non_existent_account_id = -1
        rsp = self.supervisor.post('/home/createDeleteAccounts/', {'action': 'delete', 'account_id': non_existent_account_id})
        self.assertEqual(User.objects.count(), 3)

    def test_account_list(self):
        resp = self.supervisor.post('/', {'name': "tony", 'password': "stark"})
        response = self.client.get('/home/createDeleteAccount/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tony")
        self.assertContains(response, "user1")
        self.assertContains(response, "user2")

    def test_add_to_list(self):
        resp = self.supervisor.post('/', {'name': "tony", 'password':"stark"})
        rsp = self.supervisor.post('/home/createDeleteAccount/', {'username': "user3"
            , 'password': "user3", 'email': "user3@uwm.edu"})
        self.assertEqual(list(User.objects.all()).__len__(), 4,
                         msg='number of users should not change from original set up')

    def test_delete_from_list(self):
        resp = self.supervisor.post('/', {'name': "tony", 'password': "stark"})
        instance = User.objects.get(id=self.user2.pk)
        instance.delete()
        self.assertEqual(list(User.objects.all()).__len__(), 2,
                         msg='number of users should not change from original set up')```  

**Documentation:**
```python## Overview
This class `TestCreateDeleteAccount` is a unit test class for creating and deleting user accounts in an application. It uses Django's `TestCase` framework and interacts with a client (`Client()`) to simulate HTTP requests and manage user creation, deletion, and listing operations.

## Interface
- **Signature**: `class TestCreateDeleteAccount(TestCase)`
- **Parameters**:
  | Name         | Type   | Purpose                             |
  |--------------|--------|-------------------------------------|
  | supervisor   | Client | A client for making HTTP requests.    |

## Inner Workings
1. **setUp Method**: Initializes a client (`self.supervisor`) and creates three users (`self.user`, `self.user1`, `self.user2`). This is done to set up the initial state of the test environment.
2. **test_createAccount Method**: 
   - Simulates logging in as "tony".
   - Creates a new user account through a POST request with parameters for username, password, email, and an empty string for another parameter.
   - Verifies that the total number of users increases by one and checks if the newly created user exists with correct details.
3. **test_duplicateAccount Method**: 
   - Simulates logging in as "tony".
   - Attempts to create a duplicate account using a username that already exists.
   - Verifies that the total number of users remains unchanged, indicating the creation was prevented due to duplicates.
4. **test_deleteAccount Method**: 
   - Simulates logging in as "tony".
   - Deletes an existing user account by its primary key.
   - Verifies that the total number of users remains unchanged after attempting to delete a non-existent account.
5. **test_deleteNonexistentAccount Method**: 
   - Simulates logging in as "user4", who does not have permission to perform this action.
   - Attempts to delete a user by passing a non-existent account ID (-1).
   - Verifies that the total number of users remains unchanged, indicating proper error handling.
6. **test_account_list Method**: 
   - Simulates logging in as "tony".
   - Retrieves and verifies the list of accounts by checking for specific usernames in the response.
7. **test_add_to_list Method**: 
   - Simulates logging in as "tony".
   - Adds a new user account through a POST request with parameters for username, password, and email.
   - Verifies that the total number of users increases by one after adding a new user.
8. **test_delete_from_list Method**: 
   - Simulates logging in as "tony".
   - Deletes an existing user account by its primary key.
   - Verifies that the total number of users decreases by one after deleting a user.

## Edge Cases & Preconditions
- All methods assume that the `Client` instance (`self.supervisor`) is properly configured and has access to the application under test.
- The existence of users (`self.user`, `self.user1`, `self.user2`) affects the outcome of some tests, making their presence necessary for these scenarios.
- Error handling checks are in place for attempting to create a duplicate account and deleting a non-existent user.

## Result Synopsis
This class runs several tests to ensure that user accounts can be created, deleted, and listed correctly within an application. It uses Django's `Client` to simulate HTTP requests and checks the database to validate the actions taken during these operations.

## Docstring Draft
```python
"""Unit tests for creating and deleting user accounts in an application.

Attributes:
    supervisor (Client): A client for making HTTP requests.
"""
```

This Markdown format provides a detailed breakdown of the code's functionality, parameters, logic, and assumptions, ensuring clarity and maintainability.```

## setUp  
``/Project/project_app/acceptance_tests/create_delete_account_tests.py``  
```def setUp(self):
        self.supervisor = Client()
        self.user = User.objects.create(username="tony", password="stark", name="Tony Stark", email="tonystark@gmail.com", phone = "(123) 555-5555", address = "999 Van Ness Ave, San Francisco, CA 94109")
        self.user1 = User.objects.create(username="user1", password="pass01", email="user1@gmail.com", phone = "(312) 555-5555", address = "999 Van Ness Ave, San Francisco, CA 94109")
        self.user2 = User.objects.create(username="user2", password="pass02", email="user2@gmail.com", phone = "(231) 555-5555", address = "999 Van Ness Ave, San Francisco, CA 94109")```  

**Documentation:**
```python## Overview
The `setUp` method is used to initialize test data and resources before running any tests in the `create_delete_account_tests.py` file. It creates instances of `Client`, `User`, and sets up multiple user accounts for testing purposes.

## Interface
- **Signature**: `def setUp(self)`
- **Parameters**:
  - None

## Inner Workings
- The method initializes a test client instance using `Client()`.
- Three `User` objects are created with different usernames, passwords, emails, phone numbers, and addresses. Each user is stored in an instance variable (`self.user`, `self.user1`, `self.user2`) for use in subsequent tests.

## Edge Cases & Preconditions
- The method assumes that the `Client()` class can be instantiated without errors.
- The method assumes that Django's ORM (`User.objects.create()`) can successfully create new user instances with the provided attributes. If any of these assumptions fail, it will raise an exception during the test setup phase.

## Result Synopsis
The method sets up three user accounts and a client instance, which can be used in the subsequent tests to perform actions like creating or deleting accounts.

## Docstring Draft
```python
"""Sets up necessary resources for the acceptance tests.

This method initializes a test client and creates three user instances with different attributes.

Args:
    None

Returns:
    None

Raises:
    Exception: If any step fails during setup.
"""
``````

## test_createAccount  
``/Project/project_app/acceptance_tests/create_delete_account_tests.py``  
```def test_createAccount(self):
        self.supervisor.post('/', {"name": "tony", "password": "stark"}, follow=True)
        rsp = self.supervisor.post('/home/createDeleteAccount/',
                                   {'action': 'create', 'username': 'newuser', 'password': 'newpassword', 'email': 'email@email.com', 'userToFind': ''}, follow=True)
        self.assertEqual(User.objects.count(), 4)
        new_user = User.objects.get(username="newuser")
        self.assertIsNotNone(new_user)
        self.assertEqual(new_user.username, "newuser")
        self.assertEqual(new_user.password, "newpassword")```  

**Documentation:**
```python## Overview
This code snippet is a unit test for creating an account in a web application. It uses Django's testing framework and asserts that the user creation process works as expected.

## Interface
- **Signature**: `test_createAccount(self)`
  - **Parameters**:
    - None

## Inner Workings
1. The test sends a POST request to the root endpoint `/` with a payload containing user credentials (`name: "tony"`, `password: "stark"`).
2. It then sends another POST request to `/home/createDeleteAccount/` with an action of `create`, along with details for the new user (`username: "newuser"`, `password: "newpassword"`, `email: "email@email.com"`, and `userToFind: ""`).
3. The test checks that the total count of users in the database has increased by one.
4. It retrieves the newly created user from the database using the username `"newuser"` and asserts that:
   - The user object is not `None`.
   - The username of the new user matches `"newuser"`.
   - The password of the new user matches `"newpassword"`.

## Edge Cases & Preconditions
- **Assumptions**:
  - The Django test client (`self.supervisor`) is properly configured and connected to a test database.
  - The `User` model has fields for `username`, `password`, and `email`.
  - There are initially three users in the database before this test runs.
  
- **Potential Failure Modes**:
  - If the user creation process fails, the total count of users might not increase by one.
  - If the new user is not correctly saved to the database, assertions about the user's attributes will fail.

## Result Synopsis
The code asserts that a new user is created successfully and that the test environment is clean after the test runs. It does not return any value; it only affects the state of the test database.

## Docstring Draft
```python
"""Tests the account creation process.

This test sends a series of POST requests to create an account and verifies that the user is added to the database with the correct details.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If the user creation process does not work as expected.
"""
``````

## test_duplicateAccount  
``/Project/project_app/acceptance_tests/create_delete_account_tests.py``  
```def test_duplicateAccount(self):
        self.supervisor.login(username="tony", password="stark")
        rsp = self.supervisor.post('/home/createDeleteAccounts/', {'name': 'user1', 'password': 'pass01', 'email': 'user1@gmail.com'})
        self.assertEqual(User.objects.count(), 3)```  

**Documentation:**
```python## Overview
- This code tests the functionality of creating duplicate accounts by attempting to create an account with a name that already exists.

## Interface
### Signature:
```python
def test_duplicateAccount(self):
```

### Parameters:
| Name    | Type   | Purpose                         |
|---------|--------|-----------------------------------|
| `self`  | object | Instance of the test class.       |

## Inner Workings
- The code performs the following steps:
1. Logs in as a supervisor using the username "tony" and password "stark".
2. Makes a POST request to '/home/createDeleteAccounts/' with the payload containing `{'name': 'user1', 'password': 'pass01', 'email': 'user1@gmail.com'}`.
3. Asserts that the number of users in the database is 3, indicating that the account creation was successful.

## Edge Cases & Preconditions
- **Precondition**: The supervisor must be logged in to perform the POST request.
- **Edge Case**: If a user with the name 'user1' already exists, the code should handle this case and not increase the count of users. However, the current implementation does not include error handling for duplicate account creation.

## Result Synopsis
- The function asserts that the number of users in the database is 3 after attempting to create an account.

## Docstring Draft
```python
"""Tests creating a duplicate account.

Asserts that the number of users in the database remains unchanged when attempting to create an existing account.

Args:
    self (object): Instance of the test class.

Raises:
    AssertionError: If the count of users is not as expected after attempting to create a duplicate account.
"""
``````

## test_deleteAccount  
``/Project/project_app/acceptance_tests/create_delete_account_tests.py``  
```def test_deleteAccount(self):
        self.supervisor.login(username="tony", password="stark")
        rsp = self.supervisor.post('/home/createDeleteAccounts/', {'action': 'delete', 'account_id': self.user2.pk})
        self.assertEqual(User.objects.count(), 3)```  

**Documentation:**
```python## Overview
The `test_deleteAccount` function is a unit test method designed to verify the functionality of deleting an account in a system. It logs in as a supervisor, sends a request to delete an account, and then checks that the user count remains unchanged.

## Interface
- **Signature**: `def test_deleteAccount(self)`
  - Parameters:
    - None

## Inner Workings
1. The function begins by calling `self.supervisor.login(username="tony", password="stark")` to authenticate as a supervisor.
2. It then sends a POST request to the `/home/createDeleteAccounts/` endpoint with the action set to `'delete'` and the account ID of the user to be deleted, which is stored in `self.user2.pk`.
3. After sending the request, it asserts that the number of users in the database remains 3 using `self.assertEqual(User.objects.count(), 3)`.

## Edge Cases & Preconditions
- **Preconditions**: 
  - The supervisor must have login credentials (`username="tony"`, `password="stark"`).
  - There must be at least one user (`self.user2`) with a valid primary key.
- **Potential Failure Modes**:
  - If the supervisor credentials are incorrect, the login may fail.
  - If the account ID provided is invalid or does not exist in the database, the delete action might not occur as expected.
- **Error Handling**: 
  - The code does not explicitly handle errors. It relies on assertions to check for correctness.

## Result Synopsis
The function asserts that after attempting to delete an account, the total number of users remains unchanged at 3.

## Docstring Draft
```python
"""Verifies the functionality of deleting an account.

This method logs in as a supervisor, sends a request to delete an account,
and checks that the user count remains unchanged.

Args:
    None

Raises:
    AssertionError: If the user count does not remain 3 after attempting to delete an account.
"""
``````

## test_deleteNonexistentAccount  
``/Project/project_app/acceptance_tests/create_delete_account_tests.py``  
```def test_deleteNonexistentAccount(self):
        self.supervisor.login(username="user4", password="pass04")
        non_existent_account_id = -1
        rsp = self.supervisor.post('/home/createDeleteAccounts/', {'action': 'delete', 'account_id': non_existent_account_id})
        self.assertEqual(User.objects.count(), 3)```  

**Documentation:**
```python## Overview
The `test_deleteNonexistentAccount` function tests the behavior of deleting a nonexistent account by attempting to delete an account with an invalid ID.

## Interface
### Signature
```python
def test_deleteNonexistentAccount(self):
```

### Parameters
| Name | Type | Purpose |
|------|------|---------|
| None | -    | This is a method of a class, so it does not take external parameters. |

## Inner Workings
1. The function logs in as a supervisor using the username "user4" and password "pass04".
2. It defines `non_existent_account_id` with a value of `-1`, which represents an invalid account ID.
3. It sends a POST request to `/home/createDeleteAccounts/` with parameters `action='delete'` and `account_id=non_existent_account_id`.
4. The function asserts that the number of user objects in the database remains unchanged, specifically expecting 3 user objects.

## Edge Cases & Preconditions
- Assumes that there are initially 3 user accounts in the database.
- The test does not handle errors related to the login process or the deletion request itself, as it is assumed to fail gracefully without raising exceptions.

## Result Synopsis
The function asserts that the count of user objects remains unchanged after attempting to delete a nonexistent account. If this assertion passes, it indicates that the system correctly handles requests for deleting non-existent accounts.

## Docstring Draft
```python
"""Tests the behavior of deleting a nonexistent account.

This test ensures that attempting to delete an account with an invalid ID does not alter the user count in the database.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If the number of user objects changes after the deletion attempt.
"""
``````

## test_account_list  
``/Project/project_app/acceptance_tests/create_delete_account_tests.py``  
```def test_account_list(self):
        resp = self.supervisor.post('/', {'name': "tony", 'password': "stark"})
        response = self.client.get('/home/createDeleteAccount/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tony")
        self.assertContains(response, "user1")
        self.assertContains(response, "user2")```  

**Documentation:**
```python## Overview
The function `test_account_list` in the file `create_delete_account_tests.py` is designed to test the functionality of listing accounts by sending a POST request to create an account and then verifying that the new user is included in the list when accessing a specific endpoint.

## Interface
- **Signature**: `def test_account_list(self)`
- **Parameters**:
  | Name   | Type    | Purpose                     |
  |--------|---------|-----------------------------|
  | self   | object  | The instance of the test class |

## Inner Workings
- The function sends a POST request to the root URL (`'/'`) with a payload containing `name` set to `"tony"` and `password` set to `"stark"`.
- It then makes a GET request to the `/home/createDeleteAccount/` endpoint.
- The response status code is checked to ensure it is `200`.
- The function asserts that the string `"tony"`, `"user1"`, and `"user2"` are present in the response, indicating that these accounts are part of the list.

## Edge Cases & Preconditions
- **Preconditions**: 
  - There must be an endpoint at `/home/createDeleteAccount/` that returns a list of users.
  - The POST request to create a user should succeed.
- **Edge Cases**:
  - If the POST request fails, the test will fail because it relies on the successful creation of the `tony` account.
  - If any of the strings `"tony"`, `"user1"`, or `"user2"` are not present in the response, the assertion will fail.

## Result Synopsis
The function asserts that after creating a user and accessing a specific endpoint, the new user and predefined users (`"user1"`, `"user2"`) are included in the list of accounts.

## Docstring Draft
```python
"""Tests listing accounts after creating a new user.

This test verifies that a newly created user appears in the list when accessing
the `/home/createDeleteAccount/` endpoint after successfully creating a user via POST request.

Args:
    self (object): The instance of the test class.

Raises:
    AssertionError: If any assertions fail indicating that the expected users are not present.
"""
``````

## test_add_to_list  
``/Project/project_app/acceptance_tests/create_delete_account_tests.py``  
```def test_add_to_list(self):
        resp = self.supervisor.post('/', {'name': "tony", 'password':"stark"})
        rsp = self.supervisor.post('/home/createDeleteAccount/', {'username': "user3"
            , 'password': "user3", 'email': "user3@uwm.edu"})
        self.assertEqual(list(User.objects.all()).__len__(), 4,
                         msg='number of users should not change from original set up')```  

**Documentation:**
```python## Overview
This code snippet defines a test function `test_add_to_list` that adds a user to an account system and verifies the number of users remains unchanged.

## Interface
- **Signature**: `def test_add_to_list(self):`
  - No parameters are explicitly defined for this method.
- **Parameters**:
  | Name        | Type    | Purpose                          |
  |-------------|---------|----------------------------------|
  | self        | object  | The instance of the class.       |

## Inner Workings
- The function makes two POST requests to different endpoints using an attribute `self.supervisor`.
  - The first request posts data with keys `'name'` and `'password'`, presumably to create a supervisor or administrative user.
  - The second request posts data with keys `'username'`, `'password'`, and `'email'` to create a new user account.
- It then asserts that the number of users in the database remains unchanged after adding the new user.

## Edge Cases & Preconditions
- Assumption: The `self.supervisor` object is properly initialized and can make HTTP POST requests.
- Potential failure mode: If the second POST request fails (e.g., due to network issues or invalid data), the assertion will fail, leading to a test failure.
- Error-handling logic: There are no explicit error handling blocks in this function. Any exceptions raised by `self.supervisor.post` calls would propagate up and cause the test to fail.

## Result Synopsis
The code tests that adding a new user does not change the total number of users in the system. If successful, it means the addition was properly handled without altering the existing user count.

## Docstring Draft
```python
"""Tests that adding a new user does not change the total number of users in the system.

This test ensures that the number of users remains unchanged after attempting to add a new user through the account creation endpoint.
"""
```

### Notes:
- The current implementation assumes that `self.supervisor` is a properly configured test client or similar object capable of making HTTP POST requests.
- The function does not provide specific details about the structure of the data being sent or how the users are stored in the database, which could be important for understanding its behavior in different scenarios.```

## test_delete_from_list  
``/Project/project_app/acceptance_tests/create_delete_account_tests.py``  
```def test_delete_from_list(self):
        resp = self.supervisor.post('/', {'name': "tony", 'password': "stark"})
        instance = User.objects.get(id=self.user2.pk)
        instance.delete()
        self.assertEqual(list(User.objects.all()).__len__(), 2,
                         msg='number of users should not change from original set up')```  

**Documentation:**
```python## Overview
This code is a unit test function that verifies the behavior of deleting an instance from a list and ensures that the total number of users remains unchanged.

## Interface
- **Signature**: `test_delete_from_list(self)`
  - Parameters: None

## Inner Workings
1. The function sends a POST request to the root endpoint ('/') with a payload containing 'name' and 'password'.
2. It retrieves an instance of the `User` model using its primary key (`self.user2.pk`).
3. This user instance is then deleted.
4. Finally, it asserts that the total number of users in the database remains unchanged by comparing the length of the list returned by `User.objects.all()` to 2.

## Edge Cases & Preconditions
- **Preconditions**: The existence of a `supervisor` object with a `post` method and a `user2` instance in the user database.
- **Assumptions**: The `User` model is correctly set up and the primary key `self.user2.pk` refers to an existing user.
- **Potential Failure Modes**:
  - If `self.user2.pk` does not refer to a valid user, attempting to delete it will raise a `User.DoesNotExist` exception.
  - The assertion might fail if any other operations during the test setup or teardown affect the user count.

## Result Synopsis
The function asserts that deleting an instance from the list and retrieving all users results in a list of length 2, indicating no change in the total number of users.

## Docstring Draft
```python
"""Verifies that deleting an instance from the list does not change the total number of users.

Raises:
    AssertionError: If the number of users changes after deletion.
"""
``````

## TestAssignSection  
``/Project/project_app/acceptance_tests/assignSection_acceptanceTests.py``  
```class TestAssignSection(TestCase):
    def setUp(self):
        self.instructor = Client()
        self.INS = User.objects.create(username="userone", password="1234", name="userone",
                                       email="userone@example.com", phone="1234567890",
                                       address="123 Roadrage lane, Springfield, Illinois ", user_type="instructor")
        self.TA = User.objects.create(username="usertwo", password="4321", name="usertwo",
                                      email="usertwo@example.com", phone="0987654321",
                                      address="1325 Barrington Rd, Hoffman Estates, IL 60169", user_type="ta")
        self.course1 = Course.objects.create(name="courseone", dateTime="2023-05-15 10:00:00")
        self.section1 = Section.objects.create(sectionName="891", owner=self.course1, user_id=self.INS)

    def test_assignSection(self):
        self.instructor.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.instructor.post('/home/assignSection/', {'courseID': 'courseone', 'sectionID': "891", 'assigneeID': "usertwo"})
        self.assertEqual(response.context['Message'], "Section assign successful!", msg="Basic Section Not Created")


    def test_assignSection_InvalidCourse(self):
        self.instructor.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.instructor.post('/home/assignSection/', {'courseID': 'WrongCourse', 'sectionID': "891", 'assigneeID': "usertwo"})
        self.assertEqual(response.context['Message'], "Course not found", msg="Incorrect Course Not Caught")

    def test_assignSection_InvalidSection(self):
        self.instructor.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.instructor.post('/home/assignSection/', {'courseID': 'courseone', 'sectionID': "WrongSection", 'assigneeID': "usertwo"})
        self.assertEqual(response.context['Message'], "Section not found", msg="Incorrect Section Not Caught")

    def test_assignSection_InvalidAssignee(self):
        self.instructor.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.instructor.post('/home/assignSection/', {'courseID': 'courseone', 'sectionID': "891", 'assigneeID': "WrongAssignee"})
        self.assertEqual(response.context['Message'], "Assignee not found", msg="Incorrect Assignee Not Caught")

    def test_assignSection_AlreadyAssigned(self):
        self.instructor.post('/', {"name": "userone", "password": "1234"}, follow=True)
        self.instructor.post('/home/assignSection/', {'courseID': 'courseone', 'sectionID': "891", 'assigneeID': "usertwo"})
        response = self.instructor.post('/home/assignSection/', {'courseID': 'courseone', 'sectionID': "891", 'assigneeID': "usertwo"})
        self.assertEqual(response.context['Message'], "Assignee is already assigned to this section", msg="Shouldn't be able to assign someone to the same section twice")

    def test_assignSection_SectionNotInCourse(self):
        course2 = Course.objects.create(name="coursetwo", dateTime="2023-05-15 10:00:00")
        section2 = Section.objects.create(sectionName="222", owner=course2, user_id=self.INS)
        self.instructor.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.instructor.post('/home/assignSection/', {'courseID': 'courseone', 'sectionID': "222", 'assigneeID': "usertwo"})
        self.assertEqual(response.context['Message'], "Section entered is not a part of the course entered", msg="Error must be raised if section doesn't match course")```  

**Documentation:**
```python## Overview
This code contains a series of unit tests for a function that assigns a TA to a section within a course. The tests verify various scenarios, including successful assignments and error handling for invalid inputs.

## Interface
- **Signature**: N/A (These are test methods, not standalone functions)
- **Parameters**:
  - `self`: Reference to the current instance of the test class.

## Inner Workings
- Each method performs a different test case for assigning a TA to a section.
- The `setUp` method initializes users and sections for testing.
- Tests involve posting data through a mock client (`instructor`) to simulate user actions on a web application. 
- Responses are checked to ensure they contain the expected messages, indicating whether the assignment was successful or if an error occurred.

## Edge Cases & Preconditions
- Assumes that the `Client` and `User`, `Course`, and `Section` classes exist and have the required methods/attributes.
- Verifies that the test data (users, courses, sections) is created correctly before each test method runs.
- Checks for various invalid inputs such as non-existent courses, sections, or assignees to ensure proper error handling.

## Result Synopsis
Each test method asserts whether the response from the mock client contains the expected message. If a test fails, it raises an assertion error with a custom message indicating what went wrong.

## Docstring Draft
```python
"""Tests for the assignSection functionality.

Args:
    self (TestAssignSection): Reference to the current test class instance.
"""
``````

## setUp  
``/Project/project_app/acceptance_tests/assignSection_acceptanceTests.py``  
```def setUp(self):
        self.instructor = Client()
        self.INS = User.objects.create(username="userone", password="1234", name="userone",
                                       email="userone@example.com", phone="1234567890",
                                       address="123 Roadrage lane, Springfield, Illinois ", user_type="instructor")
        self.TA = User.objects.create(username="usertwo", password="4321", name="usertwo",
                                      email="usertwo@example.com", phone="0987654321",
                                      address="1325 Barrington Rd, Hoffman Estates, IL 60169", user_type="ta")
        self.course1 = Course.objects.create(name="courseone", dateTime="2023-05-15 10:00:00")
        self.section1 = Section.objects.create(sectionName="891", owner=self.course1, user_id=self.INS)```  

**Documentation:**
```python## Overview
This code sets up a test environment by creating instances of `Client`, `User`, and `Course` objects.

## Interface
- **Signature**: `def setUp(self)`
- **Parameters**:
  | Name     | Type        | Purpose                              |
  |----------|-------------|--------------------------------------|
  | self     | object      | The instance of the test class.       |

## Inner Workings
- Creates a new `Client` object and assigns it to `self.instructor`.
- Creates two `User` objects: one for an instructor (`INS`) and one for a teaching assistant (`TA`). Both users are saved to the database.
- Creates a `Course` object with a specific name and date/time, then saves it to the database.
- Creates a `Section` object associated with the previously created course and instructor, and assigns it to `self.section1`.

## Edge Cases & Preconditions
- Assumes that the Django ORM (`User`, `Course`, `Section`) is properly configured and accessible.
- Errors are not explicitly handled in this snippet; any database-related errors (e.g., duplicate usernames) will cause an exception to be raised.

## Result Synopsis
The `setUp` method initializes the test environment with a client, two users (instructor and TA), and a course section. It sets up the necessary objects for subsequent acceptance tests.

## Docstring Draft
```python
"""Sets up the test environment by creating instances of Client, User, and Course objects.

Args:
    self: The instance of the test class.

Raises:
    Exception: Any database-related errors (e.g., duplicate usernames) will propagate.
"""
``````

## test_assignSection  
``/Project/project_app/acceptance_tests/assignSection_acceptanceTests.py``  
```def test_assignSection(self):
        self.instructor.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.instructor.post('/home/assignSection/', {'courseID': 'courseone', 'sectionID': "891", 'assigneeID': "usertwo"})
        self.assertEqual(response.context['Message'], "Section assign successful!", msg="Basic Section Not Created")```  

**Documentation:**
```python## Overview
This code is an acceptance test for the `test_assignSection` function. It verifies that a section assignment request to a course is handled correctly and that a success message is returned.

## Interface
- **Signature**: `def test_assignSection(self)`
- **Parameters**: 
  | Name          | Type     | Purpose                       |
  |---------------|----------|-------------------------------|
  | self          | object   | The test instance               |

## Inner Workings
1. **Login as an Instructor**:
   - The test first logs in the user with the username "userone" and password "1234" using a POST request to the root URL (`/`). The `follow=True` parameter ensures that any redirects are followed.
   
2. **Assign Section**:
   - After logging in, the test makes another POST request to the `/home/assignSection/` endpoint with payload data containing `courseID`, `sectionID`, and `assigneeID`. These parameters specify which section is being assigned to which user.

3. **Verify Success Message**:
   - The response from the assignment attempt is checked to ensure that the context variable `Message` contains the string "Section assign successful!". This confirms that the section assignment was processed successfully.

## Edge Cases & Preconditions
- **Precondition**: The test assumes that there are users with usernames "userone", "usertwo" and a course with ID "courseone".
- **Assumption**: The function correctly handles valid input parameters.
- **Error Handling**: If the `Message` context variable does not contain "Section assign successful!", the test will fail, indicating an issue in section assignment logic.

## Result Synopsis
The code asserts that after successfully assigning a section, the response context contains the expected success message "Section assign successful!".

## Docstring Draft
```python
"""Verifies that a section assignment request is handled correctly and returns a success message.

Args:
    self (object): The test instance.

Returns:
    None: This method does not return anything but raises an assertion error on failure.

Raises:
    AssertionError: If the expected success message is not found in the response context.
"""
``````

## test_assignSection_InvalidCourse  
``/Project/project_app/acceptance_tests/assignSection_acceptanceTests.py``  
```def test_assignSection_InvalidCourse(self):
        self.instructor.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.instructor.post('/home/assignSection/', {'courseID': 'WrongCourse', 'sectionID': "891", 'assigneeID': "usertwo"})
        self.assertEqual(response.context['Message'], "Course not found", msg="Incorrect Course Not Caught")```  

**Documentation:**
```python## Overview
This code tests the functionality of assigning a section to an invalid course.

## Interface
- **Signature**: `test_assignSection_InvalidCourse(self)`
- **Parameters**:
  | Name     | Type   | Purpose                         |
  |----------|--------|-----------------------------------|
  | self     | object | Instance of the test class.       |

## Inner Workings
1. The instructor logs in by posting to the root URL with a username and password.
2. An attempt is made to assign a section to an invalid course by posting to `/home/assignSection/` with `courseID`, `sectionID`, and `assigneeID`.
3. The response context is checked to ensure that the message "Course not found" is present.

## Edge Cases & Preconditions
- Assumes that the instructor has the necessary permissions to attempt such an assignment.
- Validates that the course ID provided is incorrect, triggering the expected error message.
- Confirms that the system correctly handles and reports invalid course IDs.

## Result Synopsis
The function asserts that when attempting to assign a section to an invalid course, the system correctly returns the message "Course not found".

## Docstring Draft
```python
"""Tests the assignment of a section to an invalid course.

This test logs in as an instructor, attempts to assign a section to a non-existent course,
and verifies that the correct error message is returned.

Args:
    self (object): Instance of the test class.

Raises:
    AssertionError: If the expected error message is not received.
"""
``````

## test_assignSection_InvalidSection  
``/Project/project_app/acceptance_tests/assignSection_acceptanceTests.py``  
```def test_assignSection_InvalidSection(self):
        self.instructor.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.instructor.post('/home/assignSection/', {'courseID': 'courseone', 'sectionID': "WrongSection", 'assigneeID': "usertwo"})
        self.assertEqual(response.context['Message'], "Section not found", msg="Incorrect Section Not Caught")```  

**Documentation:**
```python## Overview
This code tests the functionality of assigning a section to an instructor when an invalid section ID is provided. It ensures that the system correctly handles the error and displays the appropriate message.

## Interface
### Signature
```python
def test_assignSection_InvalidSection(self):
```

### Parameters
| Name        | Type   | Purpose                                      |
|-------------|--------|----------------------------------------------|
| self        | object | The instance of the test class               |

## Inner Workings
- The method `test_assignSection_InvalidSection` is called, which is a part of a test class.
- The instructor logs in using the POST request to `/`, providing username and password.
- An attempt to assign a section is made by posting to `/home/assignSection/`. The data includes an invalid `sectionID`.
- The response from the server is captured.
- The method asserts that the context of the response contains the message "Section not found" to ensure the correct error handling.

## Edge Cases & Preconditions
- **Preconditions**: 
  - An instructor must be logged in to attempt assigning a section.
  - The system should handle an invalid `sectionID` gracefully and return an appropriate error message.
  
- **Edge Cases**:
  - Providing an invalid `sectionID` (e.g., "WrongSection") should result in the server returning a message indicating that the section is not found.

## Result Synopsis
The code tests whether the system correctly identifies and handles the assignment of a non-existent section, ensuring the appropriate error message is returned to the user.

## Docstring Draft
```python
"""Tests the functionality of assigning a section when an invalid section ID is provided.

Args:
    self (object): The instance of the test class.

Returns:
    None

Raises:
    AssertionError: If the response does not contain the expected error message.
"""
```

This docstring provides a clear summary of the test case, its parameters, and what it checks.```

## test_assignSection_InvalidAssignee  
``/Project/project_app/acceptance_tests/assignSection_acceptanceTests.py``  
```def test_assignSection_InvalidAssignee(self):
        self.instructor.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.instructor.post('/home/assignSection/', {'courseID': 'courseone', 'sectionID': "891", 'assigneeID': "WrongAssignee"})
        self.assertEqual(response.context['Message'], "Assignee not found", msg="Incorrect Assignee Not Caught")```  

**Documentation:**
```python## Overview
This code defines a test case to verify that the `assignSection` function correctly handles an invalid assignee ID by returning a specific message.

## Interface
- **Signature**: `test_assignSection_InvalidAssignee(self)`
- **Parameters**:
  - `self`: The instance of the test class.

## Inner Workings
1. The method first logs in as an instructor using the `/` endpoint with a POST request containing user credentials.
2. It then attempts to assign a section by making a POST request to `/home/assignSection/` with course and section IDs, but uses an invalid `assigneeID`.
3. After attempting the assignment, it asserts that the response context contains the message "Assignee not found" as expected.

## Edge Cases & Preconditions
- The test assumes that there is an instructor object (`self.instructor`) available in the test class.
- It also assumes that the `/` and `/home/assignSection/` endpoints are properly set up to handle POST requests with the required parameters.
- Potential failure modes include network issues or incorrect endpoint URLs.

## Result Synopsis
This code tests whether the `assignSection` function correctly identifies an invalid assignee ID and responds with "Assignee not found".

## Docstring Draft
```python
"""Tests that assigning a section to an invalid assignee ID returns the correct error message.

Args:
    self: The instance of the test class.

Returns:
    None

Raises:
    AssertionError: If the expected error message is not returned.
"""
``````

## test_assignSection_AlreadyAssigned  
``/Project/project_app/acceptance_tests/assignSection_acceptanceTests.py``  
```def test_assignSection_AlreadyAssigned(self):
        self.instructor.post('/', {"name": "userone", "password": "1234"}, follow=True)
        self.instructor.post('/home/assignSection/', {'courseID': 'courseone', 'sectionID': "891", 'assigneeID': "usertwo"})
        response = self.instructor.post('/home/assignSection/', {'courseID': 'courseone', 'sectionID': "891", 'assigneeID': "usertwo"})
        self.assertEqual(response.context['Message'], "Assignee is already assigned to this section", msg="Shouldn't be able to assign someone to the same section twice")```  

**Documentation:**
```python## Overview
This code snippet tests a function that attempts to assign an instructor to a section in a course. It checks that if the assignee is already assigned to the section, the system should return a specific message.

## Interface
- **Signature**: `test_assignSection_AlreadyAssigned(self)`
- **Parameters**:
  | Name         | Type   | Purpose                 |
  |--------------|--------|-------------------------|
  | self         | object | The test case instance. |

## Inner Workings
1. The instructor posts a login request with credentials for a user named "userone" and password "1234".
2. The instructor then posts an initial assignment request to assign the assignee "usertwo" to section "891" of course "courseone".
3. The instructor posts another assignment request attempting to reassign "usertwo" to the same section "891".
4. The test asserts that the response context contains the message "Assignee is already assigned to this section", indicating that the system correctly prevents duplicate assignments.

## Edge Cases & Preconditions
- Assumes that the initial assignment was successful.
- Assumes that the `post` method of the `self.instructor` object works as expected and returns a valid response.
- Assumes that the context of the response contains a key named 'Message'.

## Result Synopsis
The code asserts that attempting to assign an already assigned user to a section results in a specific message being returned.

## Docstring Draft
```python
"""Tests that attempting to assign an already assigned instructor to a section returns the correct error message.

Args:
    self (object): The test case instance.

Returns:
    None

Raises:
    AssertionError: If the expected message is not found in the response context.
"""
``````

## test_assignSection_SectionNotInCourse  
``/Project/project_app/acceptance_tests/assignSection_acceptanceTests.py``  
```def test_assignSection_SectionNotInCourse(self):
        course2 = Course.objects.create(name="coursetwo", dateTime="2023-05-15 10:00:00")
        section2 = Section.objects.create(sectionName="222", owner=course2, user_id=self.INS)
        self.instructor.post('/', {"name": "userone", "password": "1234"}, follow=True)
        response = self.instructor.post('/home/assignSection/', {'courseID': 'courseone', 'sectionID': "222", 'assigneeID': "usertwo"})
        self.assertEqual(response.context['Message'], "Section entered is not a part of the course entered", msg="Error must be raised if section doesn't match course")```  

**Documentation:**
```python## Overview
This code snippet tests the functionality of assigning a section to a course when the specified section does not belong to the given course.

## Interface
- **Signature**: `test_assignSection_SectionNotInCourse(self)`
- **Parameters**:
  - `self`: The instance of the test class, which inherits from Django's `TestCase`.

## Inner Workings
1. A new `Course` object named "coursetwo" is created with a specified date and time.
2. A new `Section` object named "222" is created and associated with the course "coursetwo".
3. An instructor logs in using POST request to `/`.
4. Another user tries to assign the section "222" to a different course "courseone" by making a POST request to `/home/assignSection/` with parameters `{'courseID': 'courseone', 'sectionID': "222", 'assigneeID': "usertwo"}`.
5. The response is checked to ensure that the context variable `Message` contains the expected error message "Section entered is not a part of the course entered".

## Edge Cases & Preconditions
- Assumes that the test user has permissions to perform actions on courses and sections.
- The function checks if the section exists and belongs to the specified course. If not, it raises an appropriate error.

## Result Synopsis
The code asserts that attempting to assign a section to a course that does not contain the section results in the expected error message being returned in the context of the response.

## Docstring Draft
```python
"""Tests the functionality of assigning a section to a course when the specified section is not part of the given course.

Args:
    self: The instance of the test class, which inherits from Django's `TestCase`.

Returns:
    None

Raises:
    AssertionError: If the expected error message is not present in the response context.
"""
``````

## TestEditMyInfo  
``/Project/unit_tests/test_edit_my_info.py``  
```class TestEditMyInfo(TestCase):
    def setUp(self):
        self.admin = Admin()
        self.user1 = User.objects.create(username="userone", password="1234", email="userone@example.com", address="123 Roadrage lane, Springfield, Illinois", phone="555-1234")
        self.user2 = User.objects.create(username="usertwo", password="4321", email="usertwo@example.com", address="1325 Barrington Rd, Hoffman Estates, IL 60169", phone="555-5678")

    def test_edit_info_success(self):
        result = self.admin.editInfo("userone", "555-4321", "userthree", "userthree@example.com", "987 New St, Springfield, Illinois")
        self.assertTrue(result, msg="error: Failed to update user information")

    def test_edit_info_duplicate_username(self):
        with self.assertRaises(ValueError, msg="Duplicate username, must raise error"):
            self.admin.editInfo("userone", "555-4321", "usertwo", "userone_modified@example.com",
                                "987 New St, Springfield, Illinois")

    def test_edit_info_duplicate_email(self):
        with self.assertRaises(ValueError, msg="Duplicate email, must raise error"):
            self.admin.editInfo("userone", "555-4321", "userone_modified", "usertwo@example.com",
                                "987 New St, Springfield, Illinois")

    def test_edit_info_invalid_username(self):
        with self.assertRaises(ValueError, msg="User not found in database, must raise error"):
            self.admin.editInfo("nonexistent_user", "555-4321", "userone_modified", "userone_modified@example.com",
                                "987 New St, Springfield, Illinois")

    def test_edit_info_invalid_input_type(self):
        with self.assertRaises(TypeError, msg="Invalid argument type, must raise error"):
            self.admin.editInfo("userone", 5554321, "userone_modified", "userone_modified@example.com",
                                "987 New St, Springfield, Illinois")```  

**Documentation:**
```python## Overview
The `TestEditMyInfo` class contains unit tests for the `editInfo` method of an `Admin` object. It verifies the correctness of the method under various scenarios including successful updates and failure cases due to duplicate usernames or emails.

## Interface
- **Signature**: Not explicitly provided in the code snippet, but it is a subclass of `TestCase`.
- **Parameters**:
  | Name          | Type     | Purpose                                                                                       |
  |---------------|----------|---------------------------------------------------------------------------------------------|
  | `self`        | `None`   | Refers to the instance of the class.                                                             |

## Inner Workings
1. **setUp Method**:
   - Creates an instance of `Admin`.
   - Creates two instances of `User`: `user1` and `user2`.

2. **test_edit_info_success Method**:
   - Calls `editInfo` with valid parameters to update `userone`'s information.
   - Asserts that the method returns `True`, indicating a successful update.

3. **test_edit_info_duplicate_username Method**:
   - Calls `editInfo` with a username that already exists (`usertwo`).
   - Asserts that a `ValueError` is raised, indicating a duplicate username.

4. **test_edit_info_duplicate_email Method**:
   - Calls `editInfo` with an email that already exists (`usertwo@example.com`).
   - Asserts that a `ValueError` is raised, indicating a duplicate email.

5. **test_edit_info_invalid_username Method**:
   - Calls `editInfo` with a non-existent username (`nonexistent_user`).
   - Asserts that a `ValueError` is raised, indicating the user was not found.

6. **test_edit_info_invalid_input_type Method**:
   - Calls `editInfo` with an invalid phone number type (an integer instead of a string).
   - Asserts that a `TypeError` is raised, indicating an invalid argument type.

## Edge Cases & Preconditions
- The tests assume the existence of a class `Admin` and a method `editInfo`.
- It assumes the existence of a model `User` with methods for creating users.
- The tests expect specific exceptions to be raised under certain conditions (e.g., duplicate username, non-existent user).

## Result Synopsis
The tests verify that the `editInfo` method behaves correctly when passed valid parameters and raises appropriate exceptions when given invalid input or existing usernames/emails.

## Docstring Draft
```python
"""Tests for the editInfo method of the Admin class.

This class contains several unit tests to ensure the editInfo method functions as expected under various conditions.

Args:
    None

Returns:
    None

Raises:
    ValueError: When trying to update with a username or email that already exists.
    TypeError: When passing invalid argument types to the method.
"""
``````

## setUp  
``/Project/unit_tests/test_edit_my_info.py``  
```def setUp(self):
        self.admin = Admin()
        self.user1 = User.objects.create(username="userone", password="1234", email="userone@example.com", address="123 Roadrage lane, Springfield, Illinois", phone="555-1234")
        self.user2 = User.objects.create(username="usertwo", password="4321", email="usertwo@example.com", address="1325 Barrington Rd, Hoffman Estates, IL 60169", phone="555-5678")```  

**Documentation:**
```python## Overview
The `setUp` method initializes the test environment by creating an `Admin` instance and two `User` instances. This setup is essential for running subsequent tests that require user data.

## Interface
- **Signature**: `def setUp(self):`
- **Parameters**: None

## Inner Workings
1. Creates an `Admin` instance and assigns it to the variable `self.admin`.
2. Uses Django's ORM to create two `User` instances:
   - The first user is named "userone" with a password of "1234", email "userone@example.com", address "123 Roadrage lane, Springfield, Illinois", and phone number "555-1234".
   - The second user is named "usertwo" with a password of "4321", email "usertwo@example.com", address "1325 Barrington Rd, Hoffman Estates, IL 60169", and phone number "555-5678".

## Edge Cases & Preconditions
- The method assumes that Django's ORM is correctly configured and available within the test environment.
- There are no assumptions about the existence of `Admin` or `User` classes; they must be defined elsewhere in the codebase.
- Errors are implicitly handled by Django's ORM if the model definitions or database configuration are incorrect. If an error occurs during user creation, it will raise an exception.

## Result Synopsis
The `setUp` method initializes the test environment with one `Admin` instance and two `User` instances, which can be used in subsequent tests.

## Docstring Draft
```python
"""Sets up the test environment by creating an admin and two users.

Returns:
    None
"""
``````

## test_edit_info_success  
``/Project/unit_tests/test_edit_my_info.py``  
```def test_edit_info_success(self):
        result = self.admin.editInfo("userone", "555-4321", "userthree", "userthree@example.com", "987 New St, Springfield, Illinois")
        self.assertTrue(result, msg="error: Failed to update user information")```  

**Documentation:**
```python## Overview
This code tests the success scenario for editing user information in a system.

## Interface
- **Signature**: `test_edit_info_success(self)`
- **Parameters**: None

## Inner Workings
- The method calls the `editInfo` method of `self.admin` with specified parameters to update user information.
- It asserts that the result of the `editInfo` call is `True`, indicating a successful update.

## Edge Cases & Preconditions
- Assumes that the `admin` object has an `editInfo` method that can be called with the provided parameters.
- Assumes that updating "userone" with the new information will succeed.
- The method does not handle any exceptions or errors raised by `editInfo`.

## Result Synopsis
The method asserts that editing user information is successful, returning no value directly but asserting the success of the operation.

## Docstring Draft
```python
"""Tests the successful update of user information.

Args:
    self: Reference to the test class instance.

Raises:
    AssertionError: If the editInfo call does not return True.
"""
``````

## test_edit_info_duplicate_username  
``/Project/unit_tests/test_edit_my_info.py``  
```def test_edit_info_duplicate_username(self):
        with self.assertRaises(ValueError, msg="Duplicate username, must raise error"):
            self.admin.editInfo("userone", "555-4321", "usertwo", "userone_modified@example.com",
                                "987 New St, Springfield, Illinois")```  

**Documentation:**
```python## Overview
This code defines a test method `test_edit_info_duplicate_username` to verify that the function raises a `ValueError` when attempting to edit user information with a duplicate username.

## Interface
### Signature
```python
def test_edit_info_duplicate_username(self)
```
- **Parameters**: None

## Inner Workings
- The method uses the `assertRaises` context manager from Python's unittest framework to ensure that calling `self.admin.editInfo` with specific parameters results in a `ValueError`.
- The specific parameters provided are designed to trigger an error due to a duplicate username.

## Edge Cases & Preconditions
- The method assumes that:
  - The `editInfo` method of `self.admin` can be called and will raise a `ValueError` under certain conditions.
  - The `assertRaises` context manager is correctly configured to validate the expected exception.

## Result Synopsis
The method asserts that calling `self.admin.editInfo` with the specified parameters raises a `ValueError`, indicating that the username "userone" is duplicated and an error should be thrown.

## Docstring Draft
```python
"""Tests that attempting to edit user information with a duplicate username raises a ValueError.

This test checks if the function correctly handles the scenario where the new username already exists in the system.
"""
```

### Full Markdown Format

```markdown
## Overview
This code defines a test method `test_edit_info_duplicate_username` to verify that the function raises a `ValueError` when attempting to edit user information with a duplicate username.

## Interface
### Signature
```python
def test_edit_info_duplicate_username(self)
```
- **Parameters**: None

## Inner Workings
- The method uses the `assertRaises` context manager from Python's unittest framework to ensure that calling `self.admin.editInfo` with specific parameters results in a `ValueError`.
- The specific parameters provided are designed to trigger an error due to a duplicate username.

## Edge Cases & Preconditions
- The method assumes that:
  - The `editInfo` method of `self.admin` can be called and will raise a `ValueError` under certain conditions.
  - The `assertRaises` context manager is correctly configured to validate the expected exception.

## Result Synopsis
The method asserts that calling `self.admin.editInfo` with the specified parameters raises a `ValueError`, indicating that the username "userone" is duplicated and an error should be thrown.

## Docstring Draft
```python
"""Tests that attempting to edit user information with a duplicate username raises a ValueError.

This test checks if the function correctly handles the scenario where the new username already exists in the system.
"""
```
``````

## test_edit_info_duplicate_email  
``/Project/unit_tests/test_edit_my_info.py``  
```def test_edit_info_duplicate_email(self):
        with self.assertRaises(ValueError, msg="Duplicate email, must raise error"):
            self.admin.editInfo("userone", "555-4321", "userone_modified", "usertwo@example.com",
                                "987 New St, Springfield, Illinois")```  

**Documentation:**
```python## Overview
This code snippet is a unit test function for the `editInfo` method in an admin class. It specifically tests the behavior of the method when attempting to set a duplicate email address.

## Interface
- **Signature**: `def test_edit_info_duplicate_email(self)`
- **Parameters**:
  - `self`: The instance of the test case class, which provides access to the methods and attributes of the class under test (in this case, the admin class).

## Inner Workings
1. The function uses a context manager `with self.assertRaises(ValueError, msg="Duplicate email, must raise error")` to assert that a `ValueError` is raised when calling the method under test.
2. Inside the context manager, it calls the `editInfo` method of the `admin` object with the specified parameters:
   - `"userone"`: The username for which information is being edited.
   - `"555-4321"`: A new phone number (not used in this test).
   - `"userone_modified"`: A new username.
   - `"usertwo@example.com"`: The email address that would be set, causing a duplicate since it already exists for another user.
   - `"987 New St, Springfield, Illinois"`: A new address (not used in this test).

## Edge Cases & Preconditions
- **Preconditions**: 
  - There must be at least two users with different usernames but the same email address (`usertwo@example.com`).
  - The `editInfo` method must support editing usernames and phone numbers.
  
- **Assumptions**:
  - The `editInfo` method should raise a `ValueError` when an attempt is made to set a duplicate email address.

- **Potential Failure Modes**: 
  - If the `editInfo` method does not handle duplicate emails correctly, it might not raise a `ValueError`, or it might raise a different type of error.
  - The test assumes that the email address in use (`usertwo@example.com`) is already linked to another user and attempting to link it again should fail.

## Result Synopsis
The function tests whether calling the `editInfo` method with a duplicate email address correctly raises a `ValueError`.

## Docstring Draft
```python
"""Tests that attempting to edit an info with a duplicate email address raises a ValueError.

This test ensures that when trying to set a duplicate email address, the method raises the appropriate error.
"""
```

Note: The docstring draft provided does not include parameter and return type information as they are not applicable for this test function. The focus is on the purpose of the test and its expected outcome.```

## test_edit_info_invalid_username  
``/Project/unit_tests/test_edit_my_info.py``  
```def test_edit_info_invalid_username(self):
        with self.assertRaises(ValueError, msg="User not found in database, must raise error"):
            self.admin.editInfo("nonexistent_user", "555-4321", "userone_modified", "userone_modified@example.com",
                                "987 New St, Springfield, Illinois")```  

**Documentation:**
```python## Overview
The `test_edit_info_invalid_username` function tests the behavior of an admin's ability to edit a user's information when the provided username does not exist in the database.

## Interface
- **Signature**: `test_edit_info_invalid_username(self)`
  - **Parameters**:
    | Name        | Type     | Purpose                         |
    |-------------|----------|---------------------------------|
    | self        | object   | The test case instance.         |

## Inner Workings
- The function asserts that calling the `editInfo` method of an admin with a non-existent username will raise a `ValueError`.
- The expected error message is "User not found in database, must raise error".

## Edge Cases & Preconditions
- The test assumes that the `editInfo` method should validate if the username exists before proceeding.
- The function relies on the admin object to have an `editInfo` method that performs this validation and raises a `ValueError` if the user does not exist.

## Result Synopsis
The function asserts that attempting to edit information for a non-existent user will correctly raise a `ValueError`.

## Docstring Draft
```python
"""Test editing user info with an invalid username.

Raises:
    ValueError: When attempting to edit information for a non-existent user.
"""
``````

## test_edit_info_invalid_input_type  
``/Project/unit_tests/test_edit_my_info.py``  
```def test_edit_info_invalid_input_type(self):
        with self.assertRaises(TypeError, msg="Invalid argument type, must raise error"):
            self.admin.editInfo("userone", 5554321, "userone_modified", "userone_modified@example.com",
                                "987 New St, Springfield, Illinois")```  

**Documentation:**
```python## Overview
This code tests the `editInfo` method of an admin object to ensure it raises a `TypeError` when provided with invalid input types.

## Interface
- **Signature**: 
  ```python
  def test_edit_info_invalid_input_type(self)
  ```
- **Parameters**:
  | Name     | Type   | Purpose                                                                 |
  |----------|--------|-------------------------------------------------------------------------|
  | None     | N/A    | This is a method within a class and does not accept external parameters. |

## Inner Workings
1. The `test_edit_info_invalid_input_type` method is part of a test case.
2. It uses the `assertRaises` context manager to verify that calling `self.admin.editInfo` with invalid input types raises a `TypeError`.
3. The specific arguments provided are intended to cause an error:
  - "userone" (str): User ID
  - 5554321 (int): Invalid type for phone number (should be str)
  - "userone_modified" (str): New username
  - "userone_modified@example.com" (str): New email
  - "987 New St, Springfield, Illinois" (str): New address

## Edge Cases & Preconditions
- The method assumes that the `editInfo` method should only accept string values for phone number.
- The test expects a `TypeError` to be raised if any of the arguments are not strings.

## Result Synopsis
The code will pass if calling `self.admin.editInfo` with non-string types for arguments results in a `TypeError`. If no error is raised or the wrong type of error is raised, the test will fail.

## Docstring Draft
```python
"""Tests that the editInfo method raises a TypeError when provided with invalid input types.

Raises:
    AssertionError: When the expected TypeError is not raised.
"""
``````

## TestAssignCourse  
``/Project/unit_tests/test_assignCourse.py``  
```class TestAssignCourse(TestCase):
    def setUp(self):
        self.admin = Admin()
        self.user1 = User.objects.create(username="userone", password="1234", name="User One",
                                         email="userone@example.com", phone="1234567890",
                                         address="123 Roadrage lane, Springfield, Illinois ", user_type="instructor")
        self.user2 = User.objects.create(username="usertwo", password="4321", name="User Two",
                                         email="usertwo@example.com", phone="0987654321",
                                         address="1325 Barrington Rd, Hoffman Estates, IL 60169", user_type="ta")
        self.course1 = Course.objects.create(name="courseone", dateTime="2023-05-15 10:00:00")
        self.course2 = Course.objects.create(name="coursetwo", dateTime="2023-05-20 13:00:00")

    def test_assignCourse_validInput(self):
        self.admin.assignCourse("userone", "courseone")
        assigned_course = Course.objects.get(name="courseone")
        self.assertEqual(assigned_course.user_id, self.user1, msg="User's assigned courses not updated in database")

    def test_assignCourse_invalidUser(self):
        with self.assertRaises(ValueError, msg="assignCourse() failed to raise error for invalid user"):
            self.admin.assignCourse("userthree", "courseone")

    def test_assignCourse_invalidCourse(self):
        with self.assertRaises(ValueError, msg="assignCourse() failed to raise error for invalid course"):
            self.admin.assignCourse("userone", "coursethree")

    def test_assignCourse_userAlreadyAssigned(self):
        self.course1.user_id = self.user1
        self.course1.save()
        with self.assertRaises(ValueError, msg="assignCourse() failed to raise error for user already assigned"):
            self.admin.assignCourse("userone", "courseone")```  

**Documentation:**
```python## Overview
This code defines a test class `TestAssignCourse` that tests the functionality of assigning courses to users by an admin. It includes methods to set up test data, and methods to test various scenarios for assigning courses.

## Interface
- **Signature**: The class `TestAssignCourse(TestCase)`.
- **Parameters**: None directly parameterized; it uses Django's `TestCase` framework which handles setup and teardown.

## Inner Workings
- The `setUp` method initializes an admin user, two instructor users, two TA users, and two courses.
- Each test method (`test_assignCourse_validInput`, `test_assignCourse_invalidUser`, `test_assignCourse_invalidCourse`, `test_assignCourse_userAlreadyAssigned`) uses the `admin.assignCourse` method to assign a course and then checks if the operation was successful or if an error was raised as expected.
- The test methods utilize Django's assertion methods like `assertEqual` and `assertRaises` to validate the outcomes.

## Edge Cases & Preconditions
- **Assumptions**: The existence of `Admin`, `User`, and `Course` models with the expected attributes.
- **Potential Failure Modes**:
  - Assigning a course to an invalid user should raise a `ValueError`.
  - Assigning a course to an invalid course name should raise a `ValueError`.
  - Attempting to assign a course to a user who is already assigned that course should raise a `ValueError`.
- **Error-Handling Logic**: Each test method uses `assertRaises` to check for the expected exceptions.

## Result Synopsis
The code tests the `assignCourse` method of the `Admin` class, ensuring it correctly handles valid input and raises appropriate errors when given invalid data. It also ensures that a user cannot be assigned a course they are already assigned.

## Docstring Draft
```python
"""Test cases for assigning courses to users by an admin.

These tests ensure that the assignCourse method behaves as expected under various conditions, including valid inputs and edge cases like invalid users or courses.
"""

class TestAssignCourse(TestCase):
    def setUp(self):
        """Set up test data."""
        self.admin = Admin()
        self.user1 = User.objects.create(username="userone", password="1234", name="User One",
                                         email="userone@example.com", phone="1234567890",
                                         address="123 Roadrage lane, Springfield, Illinois ", user_type="instructor")
        self.user2 = User.objects.create(username="usertwo", password="4321", name="User Two",
                                         email="usertwo@example.com", phone="0987654321",
                                         address="1325 Barrington Rd, Hoffman Estates, IL 60169", user_type="ta")
        self.course1 = Course.objects.create(name="courseone", dateTime="2023-05-15 10:00:00")
        self.course2 = Course.objects.create(name="coursetwo", dateTime="2023-05-20 13:00:00")

    def test_assignCourse_validInput(self):
        """Test assigning a valid course to a valid user."""
        self.admin.assignCourse("userone", "courseone")
        assigned_course = Course.objects.get(name="courseone")
        self.assertEqual(assigned_course.user_id, self.user1, msg="User's assigned courses not updated in database")

    def test_assignCourse_invalidUser(self):
        """Test assigning a course to an invalid user."""
        with self.assertRaises(ValueError, msg="assignCourse() failed to raise error for invalid user"):
            self.admin.assignCourse("userthree", "courseone")

    def test_assignCourse_invalidCourse(self):
        """Test assigning a course to an invalid course."""
        with self.assertRaises(ValueError, msg="assignCourse() failed to raise error for invalid course"):
            self.admin.assignCourse("userone", "coursethree")

    def test_assignCourse_userAlreadyAssigned(self):
        """Test assigning a course to a user who is already assigned that course."""
        self.course1.user_id = self.user1
        self.course1.save()
        with self.assertRaises(ValueError, msg="assignCourse() failed to raise error for user already assigned"):
            self.admin.assignCourse("userone", "courseone")
```

This docstring provides a clear summary of the test cases and the conditions they are designed to validate.```

## setUp  
``/Project/unit_tests/test_assignCourse.py``  
```def setUp(self):
        self.admin = Admin()
        self.user1 = User.objects.create(username="userone", password="1234", name="User One",
                                         email="userone@example.com", phone="1234567890",
                                         address="123 Roadrage lane, Springfield, Illinois ", user_type="instructor")
        self.user2 = User.objects.create(username="usertwo", password="4321", name="User Two",
                                         email="usertwo@example.com", phone="0987654321",
                                         address="1325 Barrington Rd, Hoffman Estates, IL 60169", user_type="ta")
        self.course1 = Course.objects.create(name="courseone", dateTime="2023-05-15 10:00:00")
        self.course2 = Course.objects.create(name="coursetwo", dateTime="2023-05-20 13:00:00")```  

**Documentation:**
```python## Overview
This code sets up test environment by creating instances of `Admin`, `User`, and `Course` objects for use in unit tests.

## Interface
### Signature
```python
def setUp(self):
```
### Parameters
| Name | Type | Purpose |
|------|------|---------|
| None | -    | This is a method of a test class, no parameters are explicitly defined within the signature. |

## Inner Workings
- An `Admin` object is created and stored in `self.admin`.
- Two `User` objects (`user1` and `user2`) are created using Django's ORM, each with specific attributes including username, password, name, email, phone, address, and user type.
- Two `Course` objects (`course1` and `course2`) are created, each with a unique name and date/time.

## Edge Cases & Preconditions
- The code assumes the existence of Django models (`Admin`, `User`, `Course`) and their respective fields.
- It does not explicitly check if the user or course creation is successful; any errors during object creation would likely be caught by Django's ORM error handling.
- It assumes that usernames and other unique constraints are respected, such as having unique email addresses.

## Result Synopsis
The function sets up a test environment with an admin, two users (one instructor and one TA), and two courses. These objects can then be used in subsequent tests to simulate various scenarios involving user roles and course management.

## Docstring Draft
```python
"""Sets up the test environment by creating instances of Admin, User, and Course objects.

This method is intended to be called automatically by a testing framework before each test case runs.
"""
```

This documentation provides a clear understanding of what the `setUp` method does, its parameters (none), and how it initializes the necessary objects for further testing.```

## test_assignCourse_validInput  
``/Project/unit_tests/test_assignCourse.py``  
```def test_assignCourse_validInput(self):
        self.admin.assignCourse("userone", "courseone")
        assigned_course = Course.objects.get(name="courseone")
        self.assertEqual(assigned_course.user_id, self.user1, msg="User's assigned courses not updated in database")```  

**Documentation:**
```python## Overview
This code is a unit test method for assigning a course to a user and verifying that the assignment is correctly recorded in the database.

## Interface
- **Signature**: `test_assignCourse_validInput(self)`
- **Parameters**: None

## Inner Workings
1. The test calls the `assignCourse` method on an instance of the `admin` object, passing the username "userone" and course name "courseone".
2. It then attempts to retrieve the course named "courseone" from the database.
3. Using `assertEqual`, it checks that the `user_id` attribute of the retrieved course matches the expected user ID (`self.user1`).

## Edge Cases & Preconditions
- **Assumptions**: The `admin` object has a valid method `assignCourse` that correctly assigns courses to users.
- **Potential Failure Modes**: 
  - If the course does not exist in the database, retrieving it will raise an exception.
  - If the user ID stored in the database does not match `self.user1`, the assertion will fail.
- **Error-Handling Logic**: The code does not explicitly handle exceptions; if they occur (e.g., due to a non-existent course), the test will fail.

## Result Synopsis
The test confirms that when a course is assigned using the `admin` object, the assignment is correctly recorded in the database by checking the `user_id` attribute of the retrieved course.

## Docstring Draft
```python
"""Verifies that assigning a course to a user updates the course's user ID in the database.

This test calls the assignCourse method and checks if the course's user_id matches the expected user ID.
"""
``````

## test_assignCourse_invalidUser  
``/Project/unit_tests/test_assignCourse.py``  
```def test_assignCourse_invalidUser(self):
        with self.assertRaises(ValueError, msg="assignCourse() failed to raise error for invalid user"):
            self.admin.assignCourse("userthree", "courseone")```  

**Documentation:**
```python## Overview
This code snippet is a unit test method that verifies the behavior of the `assignCourse` function when it is called with an invalid user.

## Interface
- **Signature**: `test_assignCourse_invalidUser(self)`
- **Parameters**:
  | Name     | Type    | Purpose                    |
  |----------|---------|------------------------------|
  | self     | object  | The test case instance.      |

## Inner Workings
1. The method calls the `assignCourse` function on an object named `self.admin`, passing two parameters: `"userthree"` and `"courseone"`.
2. It uses a context manager to catch exceptions using `with self.assertRaises(ValueError, msg="...")`. This ensures that the `ValueError` is raised as expected when the invalid user scenario is encountered.
3. The error message provided in the context manager (`msg="assignCourse() failed to raise error for invalid user"`) helps identify the specific issue if the test fails.

## Edge Cases & Preconditions
- **Assumption**: The `assignCourse` function should raise a `ValueError` when attempting to assign a course to an invalid user.
- **Potential Failure Modes**: If the `assignCourse` function does not raise the expected `ValueError`, or if it raises a different exception, the test will fail.
- **Error-Handling Logic**: The test uses `self.assertRaises` to handle the expected error.

## Result Synopsis
The method tests that calling `assignCourse` with an invalid user correctly raises a `ValueError`.

## Docstring Draft
```python
"""Tests that assignCourse() raises ValueError for invalid user.

Raises:
    AssertionError: If ValueError is not raised for invalid user.
"""
``````

## test_assignCourse_invalidCourse  
``/Project/unit_tests/test_assignCourse.py``  
```def test_assignCourse_invalidCourse(self):
        with self.assertRaises(ValueError, msg="assignCourse() failed to raise error for invalid course"):
            self.admin.assignCourse("userone", "coursethree")```  

**Documentation:**
```python## Overview
This code tests the `test_assignCourse_invalidCourse` function in a unit test scenario. It verifies that an exception is raised when attempting to assign an invalid course.

## Interface
- **Signature**: `def test_assignCourse_invalidCourse(self)`
- **Parameters**:
  | Name     | Type    | Purpose                   |
  |----------|---------|-----------------------------|
  | self     | object  | Reference to the current instance |

## Inner Workings
- The function uses a context manager (`with`) to assert that a `ValueError` is raised when calling `self.admin.assignCourse("userone", "coursethree")`.
- If the `assignCourse` method does not raise a `ValueError`, the test will fail.

## Edge Cases & Preconditions
- The function assumes that the `admin` object has a method `assignCourse` which should handle invalid courses by raising a `ValueError`.

## Result Synopsis
The code asserts that attempting to assign an invalid course raises a `ValueError`. If this condition is met, the test passes. Otherwise, it fails.

## Docstring Draft
```python
"""Tests that assignCourse() raises a ValueError for invalid courses.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If ValueError is not raised when an invalid course is attempted to be assigned.
"""
``````

## test_assignCourse_userAlreadyAssigned  
``/Project/unit_tests/test_assignCourse.py``  
```def test_assignCourse_userAlreadyAssigned(self):
        self.course1.user_id = self.user1
        self.course1.save()
        with self.assertRaises(ValueError, msg="assignCourse() failed to raise error for user already assigned"):
            self.admin.assignCourse("userone", "courseone")```  

**Documentation:**
```python## Overview
This code tests the `assignCourse` method in a system that manages course assignments, ensuring it raises a `ValueError` when attempting to assign a course to a user who is already assigned.

## Interface
- **Signature**: `test_assignCourse_userAlreadyAssigned(self)`
- **Parameters**:
  | Name       | Type   | Purpose                                          |
  |------------|--------|--------------------------------------------------|
  | self       | object | The test case instance.                          |

## Inner Workings
1. **Setup**:
   - The method sets up a course (`self.course1`) and assigns it to a user (`self.user1`).
   - It saves the course to persist the assignment.
2. **Test Execution**:
   - The method attempts to assign the same course to the same user again using `admin.assignCourse("userone", "courseone")`.
   - It uses `with self.assertRaises(ValueError, msg="assignCourse() failed to raise error for user already assigned")` to verify that a `ValueError` is raised.

## Edge Cases & Preconditions
- **Precondition**: The course must be initially assigned to the user.
- **Edge Case**: Attempting to reassign the same course to the same user should fail and raise a `ValueError`.

## Result Synopsis
The method asserts that attempting to assign a course to a user who is already assigned raises a `ValueError`, indicating that the assignment process correctly handles this edge case.

## Docstring Draft
```python
"""Tests that assigning a course to a user who is already assigned raises a ValueError.

Raises:
    AssertionError: If no ValueError is raised when attempting to assign an already assigned course.
"""
```

This function ensures that the `assignCourse` method behaves as expected in a specific edge case, maintaining the integrity of the assignment system.```

## TestLogIn  
``/Project/unit_tests/test_login.py``  
```class TestLogIn(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="user", password="1234", email="user@example.com")
        self.admin1 = Admin()

    def test_validLogin(self):
        self.assertTrue(self.admin1.login("user", "1234"), msg='should have returned true since username and password are correct')

    def test_invalidPassword(self):
        self.assertFalse(self.admin1.login("user", "wrong"), msg='should have returned false since password is incorrect')

    def test_nonexistentUser(self):
        self.assertFalse(self.admin1.login("nonexistentuser", "password"),
                         msg='should have returned false since user does not exist')

    def test_invalidUsername(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid username type"):
            self.admin1.login(123, "password")

    def test_invalidPasswordType(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid password type"):
            self.admin1.login("user", 123)```  

**Documentation:**
```python## Overview
This code defines a series of unit tests to validate the login functionality of an `Admin` class. It includes test cases for valid and invalid usernames and passwords.

## Interface
### Signature
- None, as this is a class containing multiple methods rather than a single function.

### Parameters
| Name         | Type   | Purpose                     |
|--------------|--------|-----------------------------|
| self         | object | The instance of the `TestLogIn` class. |

## Inner Workings
- **setUp**: Initializes test data by creating a user and an admin instance.
- **test_validLogin**: Verifies that login returns `True` for correct username and password.
- **test_invalidPassword**: Checks that login returns `False` for incorrect password.
- **test_nonexistentUser**: Tests that login returns `False` for non-existent users.
- **test_invalidUsername**: Ensures that passing a non-string value as the username raises a `TypeError`.
- **test_invalidPasswordType**: Verifies that passing a non-string value as the password raises a `TypeError`.

## Edge Cases & Preconditions
- Assumes the existence of a `User` model with attributes like `username`, `password`, and `email`.
- Assumes the `Admin` class has a method `login` which takes a username and password, and returns `True` or `False`.
- Potential failure modes include passing invalid types for username and password.
- Error handling is done through assertions in each test method.

## Result Synopsis
The tests check various scenarios of user login attempts, ensuring correct behavior under different conditions.

## Docstring Draft
```python
"""
A class containing unit tests to validate the login functionality of an Admin class.

Attributes:
    self.user1 (User): A user instance for testing.
    self.admin1 (Admin): An admin instance for testing.

Methods:
    test_validLogin(): Tests valid username and password combination.
    test_invalidPassword(): Tests incorrect password scenario.
    test_nonexistentUser(): Tests non-existent user scenario.
    test_invalidUsername(): Ensures TypeError is raised with invalid username type.
    test_invalidPasswordType(): Ensures TypeError is raised with invalid password type.
"""
``````

## setUp  
``/Project/unit_tests/test_login.py``  
```def setUp(self):
        self.user1 = User.objects.create(username="user", password="1234", email="user@example.com")
        self.admin1 = Admin()```  

**Documentation:**
```python## Overview
- This code sets up test environment by creating a user and an admin object.

## Interface
### Signature:
```python
def setUp(self):
```

### Parameters:
| Name | Type | Purpose |
|------|------|---------|
| `self` | Class instance | The instance of the class containing this method. |

## Inner Workings
- Creates a user with username "user", password "1234", and email "user@example.com" using Django's ORM (`User.objects.create()`).
- Initializes an admin object (`Admin()`).

## Edge Cases & Preconditions
- Assumes the existence of `User` model from Django ORM and `Admin` class.
- No explicit error handling is performed. If `User.objects.create()` fails due to database issues or invalid input, it will raise an exception.

## Result Synopsis
- Returns no value explicitly (`None` by default). Sets up the test environment with a user and an admin object.

## Docstring Draft
```python
"""
Sets up the test environment by creating a user and an admin object.

Args:
    self (unittest.TestCase): The instance of the unittest TestCase class containing this method.

Returns:
    None

Raises:
    Any exceptions raised during database operations or object creation.
"""
```
This draft docstring provides a concise summary, describes the parameters, indicates that no return value is explicitly returned, and mentions potential exceptions.```

## test_validLogin  
``/Project/unit_tests/test_login.py``  
```def test_validLogin(self):
        self.assertTrue(self.admin1.login("user", "1234"), msg='should have returned true since username and password are correct')```  

**Documentation:**
```python## Overview
- This code snippet is a unit test method for validating a login operation in an application.

## Interface
### Signature
```python
def test_validLogin(self)
```

### Parameters
| Name   | Type  | Purpose                           |
|--------|-------|-----------------------------------|
| self   | object| The instance of the test class.   |

## Inner Workings
- The method `test_validLogin` is a unit test that asserts whether the login operation for an admin user with a username and password returns `True`.
- It calls the `login` method on `self.admin1`, passing "user" as the username and "1234" as the password.
- The assertion checks if the return value of the `login` method is `True`.

## Edge Cases & Preconditions
- Assumes that `self.admin1` is an instance of a class with a `login` method.
- Assumes that the `login` method correctly authenticates users based on the provided username and password.
- No error handling is explicitly shown in the snippet.

## Result Synopsis
- The method asserts that the login operation returns `True`, indicating successful authentication.

## Docstring Draft
```python
"""Tests the valid login functionality of the admin user.

Args:
    self (object): The instance of the test class.

Raises:
    AssertionError: If the login operation does not return True for a correct username and password.
"""
``````

## test_invalidPassword  
``/Project/unit_tests/test_login.py``  
```def test_invalidPassword(self):
        self.assertFalse(self.admin1.login("user", "wrong"), msg='should have returned false since password is incorrect')```  

**Documentation:**
```python## Overview
The `test_invalidPassword` function checks that the login method returns `False` when provided with an invalid password.

## Interface
- **Signature**: `test_invalidPassword(self)`
  - **Parameters**:
    - None

## Inner Workings
1. The function asserts that calling `self.admin1.login("user", "wrong")` returns `False`.
2. It uses the `assertFalse` method to verify that the login attempt with an incorrect password fails.
3. A message is provided to clarify the expected behavior if the assertion fails.

## Edge Cases & Preconditions
- The function assumes that:
  - There is an admin user named `admin1`.
  - The method `self.admin1.login("user", "wrong")` exists and behaves as expected.
- Potential failure modes include:
  - If the login method does not exist or has a different signature.
  - If the method returns unexpected types (e.g., `None`, `True`).

## Result Synopsis
The function asserts that attempting to log in with an incorrect password returns `False`.

## Docstring Draft
```python
"""Checks that logging in with an invalid password returns False.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If the login method does not return False for an invalid password.
"""
``````

## test_nonexistentUser  
``/Project/unit_tests/test_login.py``  
```def test_nonexistentUser(self):
        self.assertFalse(self.admin1.login("nonexistentuser", "password"),
                         msg='should have returned false since user does not exist')```  

**Documentation:**
```python## Overview
This code is a unit test method for verifying that the `login` function of an admin user returns `False` when attempting to log in with a non-existent username.

## Interface
- **Signature**: `test_nonexistentUser(self)`
- **Parameters**:
  | Name    | Type   | Purpose                                |
  |---------|--------|------------------------------------------|
  | self    | object | The test class instance                  |

## Inner Workings
- The method calls the `login` function of an admin user with a non-existent username and password.
- It asserts that the result of this login attempt is `False`.
- If the result is not `False`, it raises an assertion error with the message 'should have returned false since user does not exist'.

## Edge Cases & Preconditions
- The method assumes that there is no user named "nonexistentuser" in the system.
- It checks for a failure mode where the login function incorrectly returns `True` for non-existent usernames, which would trigger an assertion error.

## Result Synopsis
This code performs a unit test to ensure that the `login` function correctly handles attempts to log in with non-existent usernames by returning `False`.

## Docstring Draft
```python
"""Verifies that logging in with a non-existent username returns False.

Args:
    self (unittest.TestCase): The test class instance.

Returns:
    None

Raises:
    AssertionError: If the login function does not return False for a non-existent user.
"""
``````

## test_invalidUsername  
``/Project/unit_tests/test_login.py``  
```def test_invalidUsername(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid username type"):
            self.admin1.login(123, "password")```  

**Documentation:**
```python## Overview
The `test_invalidUsername` function in the `test_login.py` file is designed to test that the `login` method of an admin user raises a `TypeError` when provided with an invalid username type (non-string).

## Interface
- **Signature**: `def test_invalidUsername(self)`
  - **Parameters**: None

## Inner Workings
1. The function uses the `with` statement along with `self.assertRaises(TypeError, msg="should raise exception for invalid username type")` to ensure that a `TypeError` is raised when calling the `login` method.
2. It attempts to call `self.admin1.login(123, "password")`, where `123` is an integer and `"password"` is a string.
3. Since the first argument (`username`) should be a string, passing an integer raises a `TypeError`.

## Edge Cases & Preconditions
- The function assumes that the `login` method will raise a `TypeError` when the username parameter is not of type string.
- No explicit error-handling logic within this test case.

## Result Synopsis
The function passes if the `login` method correctly raises a `TypeError` when an invalid username (non-string) is provided. It does not return any value directly; instead, it relies on the assertion to validate correct behavior.

## Docstring Draft
```python
"""Test that the login method raises a TypeError when given an invalid username type.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If the login method does not raise a TypeError for non-string usernames.
"""
``````

## test_invalidPasswordType  
``/Project/unit_tests/test_login.py``  
```def test_invalidPasswordType(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid password type"):
            self.admin1.login("user", 123)```  

**Documentation:**
```python## Overview
This code snippet is a unit test method named `test_invalidPasswordType`. It checks that the `login` method of an object `self.admin1` raises a `TypeError` when provided with a non-string password type.

## Interface
- **Signature**: `def test_invalidPasswordType(self)`
  - **Parameters**:
    - None

## Inner Workings
- The test method uses a context manager (`with self.assertRaises(TypeError, msg="should raise exception for invalid password type")`) to check that calling the `login` method on `self.admin1` with non-string password (specifically an integer) raises a `TypeError`.
- Inside the context manager, the `login` method is invoked with parameters `"user"` and `123`, where `"user"` is expected to be a username and `123` is intended to be a password but is passed as an integer.
- The `msg` parameter within `assertRaises` provides a custom error message that will be displayed if the test fails.

## Edge Cases & Preconditions
- **Assumptions**:
  - The `login` method of `self.admin1` expects the second argument (password) to be of type string.
- **Potential Failure Modes**:
  - If the `login` method does not enforce the password type check or if it handles non-string passwords incorrectly, this test will fail by not raising a `TypeError`.
- **Error-Handling Logic**:
  - The test itself uses Python’s built-in `assertRaises` to handle errors. If no exception is raised when the `login` method is called with an integer password, the test will fail.

## Result Synopsis
The code tests that attempting to log in with a non-string password type results in a `TypeError`. If successful, it confirms that the `login` method correctly identifies invalid password types and raises the appropriate exception.

## Docstring Draft
```python
"""Verifies that the login method raises a TypeError when provided with a non-string password.

Args:
    None

Raises:
    AssertionError: When the expected TypeError is not raised during the test.
"""
``````

## TestSearchUser  
``/Project/unit_tests/test_searchUser.py``  
```class TestSearchUser(TestCase):
    def setUp(self):
        self.ta1 = User.objects.create(username="bob", user_type="ta")                        
        self.ta2 = User.objects.create(username="pam", user_type="ta")
        self.skill = Skill.objects.create(owner=self.ta1, name="science")
        self.instructor = User.objects.create(username="alice", user_type="instructor")
        self.admin1 = Admin()

    def test_userExists(self):
        self.assertTrue(self.admin1.searchUser("bob"), msg='should have returned true since TA is in db')

    def test_noUser(self):
        self.assertFalse(self.admin1.searchUser("joe"), msg='should have returned false since TA is not in db')

    def test_invalidInput(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid search type"):
            self.admin1.searchUser(143)

    def test_invalidUserType(self):
        self.assertFalse(self.admin1.searchUser("alice"), msg="should not find user with user_type not ta")```  

**Documentation:**
```python## Overview
This code is a unit test class `TestSearchUser` that tests the functionality of an `Admin` class's `searchUser` method. It creates various users and skills in the database to simulate real-world scenarios and checks if the `searchUser` method correctly identifies the existence of users.

## Interface
- **Signature**: `class TestSearchUser(TestCase)`
  - `TestCase`: This is a built-in Python class for creating test cases.
  
- **Parameters**:
  | Name   | Type          | Purpose                     |
  |--------|---------------|-----------------------------|
  | None   |               | This class does not take any parameters directly. |

## Inner Workings
1. **setUp Method**: 
   - Creates instances of `User` objects for different user types (`ta`, `instructor`).
   - Creates a `Skill` object owned by one of the `TA` users.
   - Instantiates an `Admin` object.

2. **test_userExists Method**:
   - Asserts that searching for a user who exists in the database returns `True`.

3. **test_noUser Method**:
   - Asserts that searching for a user who does not exist in the database returns `False`.

4. **test_invalidInput Method**:
   - Asserts that calling `searchUser` with an invalid input type (non-string) raises a `TypeError`.

5. **test_invalidUserType Method**:
   - Asserts that searching for a user with a non-`TA` user type returns `False`.

## Edge Cases & Preconditions
- The test assumes that the `Admin` class has a method `searchUser` which takes a username as a string and returns a boolean indicating whether the user exists.
- The test checks various scenarios such as existing users, non-existing users, invalid input types, and users of different types.

## Result Synopsis
The code tests the `searchUser` method to ensure it correctly identifies the existence of users in the database. It verifies both positive and negative cases, including handling of invalid inputs.

## Docstring Draft
```python
"""This class contains unit tests for the searchUser method of the Admin class.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If any assertion fails.
"""
``````

## setUp  
``/Project/unit_tests/test_searchUser.py``  
```def setUp(self):
        self.ta1 = User.objects.create(username="bob", user_type="ta")                        
        self.ta2 = User.objects.create(username="pam", user_type="ta")
        self.skill = Skill.objects.create(owner=self.ta1, name="science")
        self.instructor = User.objects.create(username="alice", user_type="instructor")
        self.admin1 = Admin()```  

**Documentation:**
```python## Overview
This code sets up a test environment by creating various users and skills for testing purposes.

## Interface
### Signature
```python
def setUp(self):
```
### Parameters
| Name     | Type       | Purpose                  |
|----------|------------|--------------------------|
| `self`   | `unittest.TestCase` | The instance of the test case. |

## Inner Workings
- Creates a user with the username "bob" and type "ta" and assigns it to `self.ta1`.
- Creates another user with the username "pam" and type "ta" and assigns it to `self.ta2`.
- Creates a skill owned by `self.ta1` with the name "science" and assigns it to `self.skill`.
- Creates a user with the username "alice" and type "instructor" and assigns it to `self.instructor`.
- Initializes an instance of the `Admin` class and assigns it to `self.admin1`.

## Edge Cases & Preconditions
- The method assumes that Django's ORM (`User.objects.create`, `Skill.objects.create`) is available and functioning correctly.
- No explicit error handling is provided for potential failures during user creation.

## Result Synopsis
The method sets up the following:
- Two TA users: "bob" and "pam".
- A skill owned by one of the TAs named "science".
- An instructor user named "alice".
- An instance of the `Admin` class.
These objects can then be used in subsequent tests.

## Docstring Draft
```python
"""Sets up a test environment with users and skills for testing purposes.

Args:
    self (unittest.TestCase): The instance of the test case.

Returns:
    None

Raises:
    None
"""
``````

## test_userExists  
``/Project/unit_tests/test_searchUser.py``  
```def test_userExists(self):
        self.assertTrue(self.admin1.searchUser("bob"), msg='should have returned true since TA is in db')```  

**Documentation:**
```python## Overview
This code snippet tests the `searchUser` method to verify if it correctly identifies the existence of a user named "bob" in the database.

## Interface
- **Signature**: `test_userExists(self)`
- **Parameters**:
  | Name | Type | Purpose |
  |------|------|---------|
  | self | object | The instance of the test class. |

## Inner Workings
1. The method calls the `searchUser` method on an object named `admin1`, passing the string "bob" as the argument.
2. It asserts that the result of `admin1.searchUser("bob")` is `True`.
3. If the assertion fails, it raises an error with the message 'should have returned true since TA is in db'.

## Edge Cases & Preconditions
- **Precondition**: The user "bob" must exist in the database for the test to pass.
- **Edge Case**: If "bob" does not exist in the database, the method should return `False`, and this test will fail.

## Result Synopsis
The code tests whether the `searchUser` method returns `True` when a valid user name is provided.

## Docstring Draft
```python
"""Tests that searchUser correctly identifies the existence of a user.

Args:
    self (unittest.TestCase): The instance of the unittest TestCase class.

Returns:
    None

Raises:
    AssertionError: If the searchUser method does not return True for an existing user.
"""
``````

## test_noUser  
``/Project/unit_tests/test_searchUser.py``  
```def test_noUser(self):
        self.assertFalse(self.admin1.searchUser("joe"), msg='should have returned false since TA is not in db')```  

**Documentation:**
```python## Overview
This code snippet is a unit test method that checks whether the `searchUser` function of an object named `admin1` returns `False` when searching for a user "joe" who is not in the database.

## Interface
- **Signature**: `test_noUser(self)`
- **Parameters**:
  | Name | Type | Purpose |
  |------|------|---------|
  | self | TestClassInstance | The test class instance. |

## Inner Workings
1. The method calls the `searchUser` function of `admin1` with the argument `"joe"`.
2. It asserts that the result of `self.admin1.searchUser("joe")` is `False`.
3. If the assertion fails, it provides a message `'should have returned false since TA is not in db'`.

## Edge Cases & Preconditions
- The method assumes that there is an object `admin1` with a `searchUser` method.
- It does not handle any exceptions explicitly; if `searchUser` raises an exception, the test will fail.

## Result Synopsis
The code asserts that calling `searchUser` with `"joe"` returns `False`, indicating that "joe" is not found in the database as expected.

## Docstring Draft
```python
"""Tests that searchUser returns False when searching for a user who does not exist.

Args:
    self (TestClassInstance): The test class instance.

Raises:
    AssertionError: If searchUser does not return False.
"""
``````

## test_invalidInput  
``/Project/unit_tests/test_searchUser.py``  
```def test_invalidInput(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid search type"):
            self.admin1.searchUser(143)```  

**Documentation:**
```python## Overview
This code snippet is a unit test function designed to verify that the `searchUser` method of an admin object raises a `TypeError` when provided with an invalid input.

## Interface
- **Signature**: `test_invalidInput(self)`
- **Parameters**:
  | Name | Type | Purpose |
  |------|------|---------|
  | self | unittest.TestCase | The test case instance. |

## Inner Workings
1. The function uses the `with` statement to catch exceptions raised during the execution of the block.
2. Inside the block, it calls `self.admin1.searchUser(143)`.
3. It asserts that a `TypeError` is raised using `self.assertRaises`, with the message "should raise exception for invalid search type".

## Edge Cases & Preconditions
- The function assumes that the `searchUser` method should handle non-string inputs (like integers) and raise a `TypeError`.
- If the method does not correctly handle such cases, this test will fail.

## Result Synopsis
The function verifies that calling `searchUser` with a non-string input raises a `TypeError`.

## Docstring Draft
```python
"""Verifies that searchUser raises TypeError for invalid input.

Raises:
    AssertionError: When `searchUser` does not raise TypeError for an integer input.
"""
``````

## test_invalidUserType  
``/Project/unit_tests/test_searchUser.py``  
```def test_invalidUserType(self):
        self.assertFalse(self.admin1.searchUser("alice"), msg="should not find user with user_type not ta")```  

**Documentation:**
```python## Overview
This code snippet is a unit test function that checks whether the `searchUser` method of an object (presumably an admin) returns `False` when called with a user type that is not "ta".

## Interface
- **Signature**: `test_invalidUserType(self)`
- **Parameters**:
  | Name   | Type   | Purpose                     |
  |--------|--------|-----------------------------|
  | self   | object | The test case instance.       |

## Inner Workings
1. The function calls the `searchUser` method on an object named `admin1`, passing a user type string "alice" as the argument.
2. It asserts that the result of the `searchUser` call is `False`.
3. If the assertion fails, it raises an error with the message "should not find user with user_type not ta".

## Edge Cases & Preconditions
- The function assumes that the `admin1` object has a method called `searchUser`.
- It expects that passing a non-"ta" user type will result in `False` being returned.
- No additional preconditions or assumptions are made about the input or behavior of the `searchUser` method.

## Result Synopsis
The function tests whether the `searchUser` method returns `False` when called with an invalid user type ("alice"). If it does not, the test will fail.

## Docstring Draft
```python
"""Tests that searchUser returns False for a non-"ta" user type.

Args:
    self (unittest.TestCase): The test case instance.

Raises:
    AssertionError: If searchUser returns True for the user type "alice".
"""
``````

## TestCreateSection  
``/Project/unit_tests/test_createSection.py``  
```class TestCreateSection(TestCase):
    def setUp(self):
        self.admin = Admin()
        self.course1 = Course.objects.create(name="361", dateTime="2023-04-18 10:32:34.184712")
        self.section1 = Section.objects.create(sectionName="891", owner=self.course1)
        self.course2 = Course.objects.create(name="337", dateTime="2023-04-18 10:32:34.184712")

    def test_SectionExistsInDatabase(self):
        sections = list(Section.objects.filter(sectionName__exact="891"))
        self.assertEqual(sections, [self.section1], msg="Section not found in database")

    def test_createSectionBasic(self):
        self.assertEqual(self.admin.createSection("337", "101"), True, msg="createSection() error: Section creation failed")

    def test_duplicateSection(self):
        with self.assertRaises(ValueError, msg="Duplicate section, must raise error"):
            self.admin.createSection("891", "361")

    def test_invalidSectionName(self):
        with self.assertRaises(TypeError, msg="Invalid name, must raise error"):
            self.admin.createSection(12345, "361")

    def test_invalidCourse(self):
        with self.assertRaises(TypeError, msg="Invalid course name, must raise error"):
            self.admin.createSection("101", 12345)

    def test_courseNotPresent(self):
        with self.assertRaises(ValueError, msg="Invalid course (not in database), must raise error"):
            self.admin.createSection("101", "000")```  

**Documentation:**
```python## Overview
This code defines a test class `TestCreateSection` that extends `unittest.TestCase` to verify the functionality of section creation in a learning management system. It includes tests for basic section creation, handling duplicates, invalid inputs, and non-existent courses.

## Interface
### Signature
```python
class TestCreateSection(TestCase):
```

### Parameters
No parameters are explicitly defined at the class level. The `setUp` method initializes objects used across multiple test methods.

## Inner Workings
1. **Setup**: Initializes an admin user and two course objects with predefined attributes.
2. **Test Section Existence**: Verifies that a section exists in the database by querying for it using its name.
3. **Basic Section Creation**: Checks if creating a new section returns `True`.
4. **Duplicate Section Handling**: Ensures that attempting to create a duplicate section raises a `ValueError`.
5. **Invalid Section Name Handling**: Validates that passing an invalid section name (e.g., non-string) raises a `TypeError`.
6. **Invalid Course Handling**: Verifies that providing an invalid course ID or object type results in a `TypeError`.
7. **Course Not Present Handling**: Checks that attempting to create a section for a non-existent course raises a `ValueError`.

## Edge Cases & Preconditions
- Assumes that the admin user and courses are correctly initialized.
- Ensures that section names are strings and course IDs are integers.
- Verifies that sections and courses exist in the database before testing.

## Result Synopsis
The test class verifies various scenarios for creating sections, ensuring robust error handling and correct functionality.

## Docstring Draft
```python
"""Test cases for section creation in a learning management system.

This class contains multiple test methods to verify the behavior of creating sections,
including handling duplicates, invalid inputs, and non-existent courses.

Attributes:
    admin (Admin): An instance of the Admin class.
    course1 (Course): A Course object created before tests run.
    section1 (Section): A Section object associated with course1.
    course2 (Course): Another Course object for additional test cases.
"""
```

This Markdown-formatted explanation provides a comprehensive breakdown of the code, its purpose, and how it functions.```

## setUp  
``/Project/unit_tests/test_createSection.py``  
```def setUp(self):
        self.admin = Admin()
        self.course1 = Course.objects.create(name="361", dateTime="2023-04-18 10:32:34.184712")
        self.section1 = Section.objects.create(sectionName="891", owner=self.course1)
        self.course2 = Course.objects.create(name="337", dateTime="2023-04-18 10:32:34.184712")```  

**Documentation:**
```python## Overview
This code initializes the test environment for a section creation test by setting up an admin user, two courses, and one section associated with those courses.

## Interface
### Signature
```python
def setUp(self):
```

### Parameters
| Name       | Type   | Purpose                            |
|------------|--------|------------------------------------|
| self       | object | The test case instance.            |

## Inner Workings
1. **Create Admin User**: An `Admin` object is instantiated and assigned to `self.admin`.
2. **Create Courses**: Two `Course` objects are created:
   - `course1`: Named "361" with a specific date-time.
   - `course2`: Named "337" with the same date-time as `course1`.
3. **Create Section**: A `Section` object is created with the name "891" and associated with `self.course1`.

## Edge Cases & Preconditions
- Assumes that the database has the necessary models (`Admin`, `Course`, `Section`) defined.
- Assumes that the models are correctly set up to handle relationships between them (e.g., a section being linked to a course).
- Assumes that the date-time format used in creating courses is valid and recognized by the system.

## Result Synopsis
The function initializes the test environment by setting up an admin user, two courses, and one section. The result of this setup can be used to perform further tests related to section creation and management.

## Docstring Draft
```python
"""Sets up the test environment for section creation tests.

Initializes an admin user, creates two courses with specific details, and sets up a section associated with one of the courses.

Args:
    self (unittest.TestCase): The test case instance.
"""
```

Note: The docstring does not include parameters or return values because this function does not take any external parameters and does not explicitly return anything.```

## test_SectionExistsInDatabase  
``/Project/unit_tests/test_createSection.py``  
```def test_SectionExistsInDatabase(self):
        sections = list(Section.objects.filter(sectionName__exact="891"))
        self.assertEqual(sections, [self.section1], msg="Section not found in database")```  

**Documentation:**
```python## Overview
This code tests whether a section with the name "891" exists in the database and asserts that it matches the expected `section1` object.

## Interface
- **Signature**: `test_SectionExistsInDatabase(self)`
- **Parameters**:
  | Name     | Type   | Purpose                          |
  |----------|--------|----------------------------------|
  | self     |        | The test case instance.          |

## Inner Workings
1. **Query Execution**: The code executes a database query to find sections with the exact name "891" using `Section.objects.filter(sectionName__exact="891")`.
2. **Assertion**: The result of the query is compared against a list containing `self.section1`. If they match, the assertion passes; otherwise, it fails.

## Edge Cases & Preconditions
- **Precondition**: Assumes that `self.section1` is a valid section object with the name "891".
- **Failure Mode**: If no sections are found in the database or if the found sections do not match `self.section1`, the assertion will fail.
- **Error Handling**: No explicit error handling is shown; failures in assertions may raise an `AssertionError`.

## Result Synopsis
The code asserts that a section with the name "891" exists in the database and matches `self.section1`. If this condition is not met, the test will fail.

## Docstring Draft
```python
"""Test whether a section with the name '891' exists in the database and matches self.section1.

Args:
    self (unittest.TestCase): The test case instance.

Returns:
    None

Raises:
    AssertionError: If no matching section is found or if the found sections do not match self.section1.
"""
``````

## test_createSectionBasic  
``/Project/unit_tests/test_createSection.py``  
```def test_createSectionBasic(self):
        self.assertEqual(self.admin.createSection("337", "101"), True, msg="createSection() error: Section creation failed")```  

**Documentation:**
```python## Overview
This code snippet is a unit test for the `test_createSectionBasic` function within the `Project/unit_tests/test_createSection.py` file. The purpose of this test is to verify that the `createSection` method of an admin object successfully creates a section with specific parameters.

## Interface
### Signature
```python
def test_createSectionBasic(self):
```

### Parameters
| Name | Type | Purpose |
|------|------|---------|
| self | object | The instance of the class containing this method. |

## Inner Workings
1. The `test_createSectionBasic` method is called, which belongs to a class that presumably inherits from `unittest.TestCase`.
2. It uses the `assertEqual` method provided by `unittest.TestCase` to check if the result of calling `self.admin.createSection("337", "101")` is equal to `True`.
3. If the assertion fails, it raises an assertion error with the message "createSection() error: Section creation failed".

## Edge Cases & Preconditions
- The test assumes that there is an `admin` object available and that it has a method called `createSection` which accepts two parameters (`"337"` and `"101"`).
- The test does not handle any exceptions or errors explicitly. If the `createSection` method raises an exception, the test will fail.

## Result Synopsis
This code snippet tests whether the `createSection` method successfully creates a section with the provided parameters by checking if it returns `True`.

## Docstring Draft
```python
"""Tests the basic functionality of creating a section.

Args:
    self (unittest.TestCase): The instance of the test case class.

Raises:
    AssertionError: If the createSection() method does not return True.
"""
``````

## test_duplicateSection  
``/Project/unit_tests/test_createSection.py``  
```def test_duplicateSection(self):
        with self.assertRaises(ValueError, msg="Duplicate section, must raise error"):
            self.admin.createSection("891", "361")```  

**Documentation:**
```python## Overview
- The code is a unit test for the `createSection` method in an admin interface, ensuring that attempting to duplicate a section raises a `ValueError`.

## Interface
- **Signature**: `test_duplicateSection(self)`
- **Parameters**:
  | Name   | Type | Purpose                          |
  |--------|------|----------------------------------|
  | self   |      | Instance of the test class.      |

## Inner Workings
- The function tests the `createSection` method by attempting to create a section with an existing identifier.
- It uses `self.admin.createSection("891", "361")`, which is expected to raise a `ValueError`.
- The `with self.assertRaises(ValueError, msg="Duplicate section, must raise error"):` block is used to verify that the method raises a `ValueError` with the specified message.

## Edge Cases & Preconditions
- **Preconditions**: 
  - There must be an existing section with identifier `"891"`.
  - The test assumes that the `createSection` method will not allow duplicate identifiers and should raise a `ValueError` in such cases.
- **Potential Failure Modes**:
  - If the `createSection` method does not raise a `ValueError`, or if it raises a different error, the test will fail.
- **Assumptions**: 
  - The test expects that the environment is set up to recognize an existing section with identifier `"891"`.
  - The method `self.admin.createSection` should handle duplicate identifiers appropriately.

## Result Synopsis
- The function asserts that attempting to create a section with an existing identifier raises a `ValueError`, as expected.

## Docstring Draft
```python
"""Tests that attempting to create a section with an existing identifier raises a ValueError.

The test assumes that there is already a section with identifier "891".

Args:
    self (unittest.TestCase): The test case instance.

Raises:
    AssertionError: If the method does not raise a ValueError.
"""
``````

## test_invalidSectionName  
``/Project/unit_tests/test_createSection.py``  
```def test_invalidSectionName(self):
        with self.assertRaises(TypeError, msg="Invalid name, must raise error"):
            self.admin.createSection(12345, "361")```  

**Documentation:**
```python## Overview
This code is a unit test for the `createSection` method in an admin interface. It checks that calling this method with an invalid section name (specifically, a non-string value) raises a `TypeError`.

## Interface
- **Signature**: `test_invalidSectionName(self)`
- **Parameters**:
  | Name   | Type   | Purpose                     |
  |--------|--------|-----------------------------|
  | self   | object | The test case instance.       |

## Inner Workings
1. The test method uses the `with` statement to assert that a `TypeError` is raised when calling `self.admin.createSection(12345, "361")`.
2. The expected error message is specified as `"Invalid name, must raise error"`.

## Edge Cases & Preconditions
- **Preconditions**: The `createSection` method should be able to handle different types of section names.
- **Edge Case**: Passing a non-string value (`12345`) for the section name should trigger an exception because it is invalid.
- **Error Handling**: The test expects that the method raises a `TypeError`.

## Result Synopsis
The code tests the behavior of the `createSection` method when provided with an invalid section name. It verifies that the method correctly identifies this as an error and raises the expected `TypeError`.

## Docstring Draft
```python
"""Tests creating a section with an invalid section name.

This test ensures that calling createSection with a non-string value for the section name raises a TypeError.

Args:
    self (unittest.TestCase): The test case instance.

Raises:
    AssertionError: If a TypeError is not raised when providing a non-string value as the section name.
"""
``````

## test_invalidCourse  
``/Project/unit_tests/test_createSection.py``  
```def test_invalidCourse(self):
        with self.assertRaises(TypeError, msg="Invalid course name, must raise error"):
            self.admin.createSection("101", 12345)```  

**Documentation:**
```python## Overview
- This code snippet tests the `createSection` method of an admin object to ensure that it raises a `TypeError` when provided with invalid input for the course name.

## Interface
- **Signature**: 
  ```python
  def test_invalidCourse(self):
  ```
- **Parameters**:
  | Name   | Type   | Purpose                    |
  |--------|--------|------------------------------|
  | N/A    | N/A    | This is a method of a class, no parameters are explicitly defined in the signature. It uses `self` to reference the instance of the class and calls another method within that instance (`createSection`). |

## Inner Workings
- The method `test_invalidCourse` does not take any arguments.
- It uses the `assertRaises` context manager from Python's unittest framework to check if calling `self.admin.createSection("101", 12345)` raises a `TypeError`.
- If the expected error is raised, the test passes; otherwise, it fails.

## Edge Cases & Preconditions
- The method assumes that:
  - `self.admin` is an instance of a class that has a `createSection` method.
  - The `createSection` method should raise a `TypeError` when passed an invalid course name (a non-string value).
- If the `createSection` method does not raise an error or raises an unexpected error, the test will fail.

## Result Synopsis
- The code tests whether calling `createSection` with a string for the course name and an integer for the section ID raises a `TypeError`.
- It asserts that the expected exception is raised, indicating successful validation of the method's behavior under invalid input.

## Docstring Draft
```python
"""Tests that createSection raises TypeError when provided with non-string course name.

Raises:
    AssertionError: If createSection does not raise TypeError as expected.
"""
``````

## test_courseNotPresent  
``/Project/unit_tests/test_createSection.py``  
```def test_courseNotPresent(self):
        with self.assertRaises(ValueError, msg="Invalid course (not in database), must raise error"):
            self.admin.createSection("101", "000")```  

**Documentation:**
```python## Overview
This code tests that an error is raised when attempting to create a section for a course that is not present in the database.

## Interface
- **Signature**: `test_courseNotPresent(self)`
- **Parameters**:
  | Name | Type | Purpose |
  |------|------|---------|
  | self | object | The test case instance. |

## Inner Workings
- The method `test_courseNotPresent` is called on an instance of a test class that presumably contains an attribute `admin`, which has a method `createSection`.
- Inside the method, a context manager `with self.assertRaises(ValueError, msg="Invalid course (not in database), must raise error"):` is used to assert that calling `self.admin.createSection("101", "000")` raises a `ValueError`.
  - The expected message of the exception is checked against the provided message.

## Edge Cases & Preconditions
- The method assumes that there is no course with ID "101" in the database.
- If such a course exists, or if any other error occurs, the test will fail.

## Result Synopsis
The method asserts that attempting to create a section for a non-existent course raises a `ValueError` with a specific message.

## Docstring Draft
```python
"""Tests that an error is raised when attempting to create a section for a course not present in the database.

Raises:
    ValueError: When trying to create a section for a non-existent course, must raise this error.
"""
``````

## TestAddSkills  
``/Project/unit_tests/test_addSkills.py``  
```class TestAddSkills(TestCase):
    def setUp(self):
        self.ta= Ta()
        self.ta1 = User.objects.create(username="bob", password="bob", user_type="ta")                     
        self.ta2 = User.objects.create(username="pam", user_type="ta")
        self.admin = User.objects.create(username="suzie", password="bob", user_type="admin")
        self.skill = Skill.objects.create(owner=self.ta1, name="science")

    def test_Add(self):
        self.assertTrue(self.ta.addSkills("math", self.ta1.username), msg="skill should be added to list")
        found = list(Skill.objects.filter(name="math"))
        self.assertEquals(len(found), 1, msg="skill was not added to db")
        self.assertEquals(self.skill.owner, self.ta1, msg="should be a part of ta's skills now")

    def test_wrongUserType(self):
        self.assertFalse(self.ta.addSkills("math", self.admin.username), msg="admin type don't have skills")
        found = list(Skill.objects.filter(name="math"))
        self.assertEquals(len(found), 0, msg="skill should not be added to db")

    def tests_duplicateSkill(self):
        self.assertFalse(self.ta.addSkills("science", self.ta1.username), msg="duplicate skills should not be created")
        self.assertTrue(self.ta.addSkills("science", self.ta2.username), msg="other tas should be able to have same skill")```  

**Documentation:**
```python## Overview
This code defines a test class `TestAddSkills` that tests the `addSkills` method of a `Ta` object. It ensures that skills are correctly added or not based on user type and handles duplicates appropriately.

## Interface
- **Signature**: Not applicable as this is a test class.
- **Parameters**:
  | Name      | Type     | Purpose                            |
  |-----------|----------|------------------------------------|
  | self      |          | Instance of the test class.        |

## Inner Workings
1. The `setUp` method initializes necessary objects, including a `Ta` instance and various `User` instances with different roles.
2. The `test_Add` method tests adding a new skill to a user. It checks if the skill is added successfully and if it appears in the database.
3. The `test_wrongUserType` method verifies that an admin cannot add skills, ensuring proper role enforcement.
4. The `tests_duplicateSkill` method ensures that duplicate skills are not created for the same user but can be created for different users.

## Edge Cases & Preconditions
- Assumes that the `addSkills` method correctly handles user roles and skill duplication.
- Tests for successful addition of a new skill, failure when adding an existing skill, and denial of skill addition by an admin.

## Result Synopsis
The test class `TestAddSkills` ensures that skills are added only by appropriate users (non-admins), handled duplicates correctly, and do not affect other users' skill lists.

## Docstring Draft
```python
"""Tests the addSkills method of the Ta class to ensure correct handling of skill additions based on user roles and duplication.

Args:
    self (TestAddSkills): Instance of the test class.
"""
``````

## setUp  
``/Project/unit_tests/test_addSkills.py``  
```def setUp(self):
        self.ta= Ta()
        self.ta1 = User.objects.create(username="bob", password="bob", user_type="ta")                     
        self.ta2 = User.objects.create(username="pam", user_type="ta")
        self.admin = User.objects.create(username="suzie", password="bob", user_type="admin")
        self.skill = Skill.objects.create(owner=self.ta1, name="science")```  

**Documentation:**
```python## Overview
This code sets up test environment for the `addSkills` function. It creates necessary instances of `Ta`, `User`, and `Skill` objects to be used in subsequent tests.

## Interface
- **Signature**: `setUp(self)`
- **Parameters**: None

## Inner Workings
- The `setUp` method initializes a test environment by creating an instance of the `Ta` class and three instances of the `User` class (`ta1`, `ta2`, and `admin`). It also creates a single instance of the `Skill` class owned by `ta1`.
- Each user object is associated with specific attributes like username, password, and user type.
- The skill object is linked to `ta1`.

## Edge Cases & Preconditions
- Assumes that the database connection is working correctly and that Django ORM can create objects as expected.
- Potential failure modes include:
  - Database issues leading to object creation failures.
  - Existing users with the same username, which might cause exceptions.
- Error-handling logic is not explicitly shown in this code but is implicitly handled by Django's ORM. If an error occurs during object creation, it will raise an exception.

## Result Synopsis
This method prepares a test environment by creating necessary objects, making them available for use in subsequent tests.

## Docstring Draft
```python
"""Sets up the test environment.

Args:
    None

Returns:
    None

Raises:
    None
"""
``````

## test_Add  
``/Project/unit_tests/test_addSkills.py``  
```def test_Add(self):
        self.assertTrue(self.ta.addSkills("math", self.ta1.username), msg="skill should be added to list")
        found = list(Skill.objects.filter(name="math"))
        self.assertEquals(len(found), 1, msg="skill was not added to db")
        self.assertEquals(self.skill.owner, self.ta1, msg="should be a part of ta's skills now")```  

**Documentation:**
```python## Overview
This code is a unit test for the `addSkills` method in a hypothetical system that manages user skills.

## Interface
### Signature
```python
test_Add(self)
```
### Parameters
| Name | Type | Purpose |
|------|------|---------|
| self | object | The instance of the class containing this method. |

## Inner Workings
1. **Assertion of Skill Addition**: The method asserts that adding a skill named "math" to a user (`self.ta`) is successful by calling `self.ta.addSkills("math", self.ta1.username)`. It uses `assertTrue` to verify that the return value is `True`, indicating the skill was added.

2. **Database Verification**: After attempting to add the skill, it checks if the skill "math" exists in the database using Django's ORM (`Skill.objects.filter(name="math")`). It asserts that exactly one record is found, ensuring the skill was successfully saved to the database.

3. **Ownership Check**: The method also verifies that the added skill belongs to the user `self.ta1` by comparing the `owner` attribute of the retrieved skill with `self.ta1`.

## Edge Cases & Preconditions
- **Skill Addition Success**: Assumes that the `addSkills` method correctly adds a skill if it doesn't already exist.
- **Database Integrity**: Assumes that Django's ORM is functioning as expected to retrieve and store data in the database.
- **User Existence**: Assumes that `self.ta1` is a valid user instance with an existing username.

## Result Synopsis
The code verifies that adding a skill to a user results in the skill being successfully added both to the user's list of skills and to the database. It also confirms that the added skill belongs to the specified user.

## Docstring Draft
```python
"""Tests the addSkills method to ensure it adds a skill to the user's list and database correctly.

Args:
    self (object): The instance of the class containing this method.

Returns:
    None

Raises:
    AssertionError: If any of the assertions fail.
"""
``````

## test_wrongUserType  
``/Project/unit_tests/test_addSkills.py``  
```def test_wrongUserType(self):
        self.assertFalse(self.ta.addSkills("math", self.admin.username), msg="admin type don't have skills")
        found = list(Skill.objects.filter(name="math"))
        self.assertEquals(len(found), 0, msg="skill should not be added to db")```  

**Documentation:**
```python## Overview
The code is a unit test function designed to verify that attempting to add skills to the system by an admin user does not succeed and that the skill is not stored in the database.

## Interface
### Signature
```python
def test_wrongUserType(self)
```

### Parameters
| Name   | Type   | Purpose                          |
|--------|--------|----------------------------------|
| `self` | object | The instance of the test class.  |

## Inner Workings
- **Step 1**: Calls the method `addSkills` on the attribute `ta` (presumably an instance of a class responsible for managing skills) with the arguments `"math"` and `admin.username`. It asserts that this call returns `False`, indicating that the admin user type does not have the permission to add skills.
- **Step 2**: Queries the database using Django's ORM (`Skill.objects.filter(name="math")`) to find any skill objects with the name `"math"`.
- **Step 3**: Asserts that the length of the found skills list is `0`, indicating that no skill with the name `"math"` was added to the database.

## Edge Cases & Preconditions
- The function assumes that:
  - There exists a method `addSkills` in the class accessible via `self.ta`.
  - The admin user does not have permission to add skills.
- If an admin user tries to add a skill, it should fail and not result in any changes to the database.

## Result Synopsis
The function asserts that adding a skill as an admin fails and no changes are made to the database.

## Docstring Draft
```python
"""Verifies that attempting to add skills by an admin user does not succeed and the skill is not stored in the database.

Args:
    self (object): The instance of the test class.

Returns:
    None

Raises:
    AssertionError: If adding a skill as an admin succeeds or if a skill is added to the database.
"""
``````

## tests_duplicateSkill  
``/Project/unit_tests/test_addSkills.py``  
```def tests_duplicateSkill(self):
        self.assertFalse(self.ta.addSkills("science", self.ta1.username), msg="duplicate skills should not be created")
        self.assertTrue(self.ta.addSkills("science", self.ta2.username), msg="other tas should be able to have same skill")```  

**Documentation:**
```python## Overview
This code tests the functionality of adding duplicate skills to different team members (TAs). It checks if a TA can add a skill that another TA already has.

## Interface
- **Signature**: `tests_duplicateSkill(self)`
  - **Parameters**: None

## Inner Workings
1. The method `tests_duplicateSkill` is part of a test class.
2. It calls the `addSkills` method on an instance of `ta`, passing "science" as the skill and different usernames (`self.ta1.username` and `self.ta2.username`) to simulate adding skills for two different TAs.
3. It asserts that attempting to add the same skill ("science") to a TA that already has it returns `False`.
4. It asserts that adding the same skill to another TA successfully returns `True`.

## Edge Cases & Preconditions
- The method assumes that `self.ta.addSkills` can be called with a skill name and a username.
- It checks if adding duplicate skills for different TAs behaves as expected.
- The test implicitly relies on the `addSkills` method correctly handling duplicate entries.

## Result Synopsis
The code verifies that adding a duplicate skill to one TA returns `False`, while it allows another TA to add the same skill successfully, demonstrating correct behavior of the system under test.

## Docstring Draft
```python
"""Tests the functionality of adding duplicate skills to different TAs.

Asserts that attempting to add a duplicate skill for an existing TA returns False,
while other TAs can successfully add the same skill.
"""
``````

## TestHomepage  
``/Project/unit_tests/test_Course.py``  
```class TestHomepage(TestCase):
    def setUp(self):
        self.admin1 = Admin()
        self.user1 = User.objects.create(username="lameGuy000", password="Password1:)", name="Richard Smalls", email="lameguy@uwm.edu", phone="123-4567", address="1614 E North Ave. Milwaukee WI 53211")
        self.user2 = User.objects.create(username="c00lguy100", password="P@ssw0rd", name="Hugh Mungus", email="coolguy@uwm.edu", phone="867-5309", address="2100 E. Kenwood Blvd. Milwaukee WI 53211")

    def test_userInfoCorrect(self):
        myInfo = self.admin1.viewMyInfo("c00lguy100", "P@ssw0rd")
        self.assertEqual(myInfo.username, "c00lguy100", "user's username is not correct")
        self.assertEqual(myInfo.password, "P@ssw0rd", "user's password is not correct")
        self.assertEqual(myInfo.name, "Hugh Mungus", "user's name is not correct")
        self.assertEqual(myInfo.email, "coolguy@uwm.edu", "user's email is not correct")
        self.assertEqual(myInfo.address, "2100 E. Kenwood Blvd. Milwaukee WI 53211", "user's address is not correct")

    def test_invalidUsername(self):
        with self.assertRaises(TypeError, msg="should raise exception since username is not string"):
            self.admin1.viewMyInfo(1, "P@ssw0rd")

    def test_invalidPassword(self):
        with self.assertRaises(TypeError, msg="should raise exception since password is not string"):
            self.admin1.viewMyInfo("c00lguy100", 12)```  

**Documentation:**
```python## Overview
This code snippet defines a set of unit tests for the `viewMyInfo` method of an `Admin` class, using Django's testing framework. The tests verify that the method correctly retrieves and returns user information when provided with valid credentials.

## Interface
- **Signature**: Not explicitly defined as part of the given text.
- **Parameters**:
  | Name   | Type    | Purpose                |
  |--------|---------|------------------------|
  | `self` | `TestHomepage` | Reference to the current test instance. |

## Inner Workings
1. **Setup**: The `setUp` method initializes two user instances (`user1` and `user2`) for use in the tests.
2. **Valid User Test (`test_userInfoCorrect`)**:
   - Calls `admin1.viewMyInfo` with valid username and password.
   - Asserts that the returned user object's attributes (username, password, name, email, address) match the expected values.
3. **Invalid Username Test (`test_invalidUsername`)**:
   - Attempts to call `admin1.viewMyInfo` with a non-string username (integer).
   - Asserts that a `TypeError` is raised with the specified message.
4. **Invalid Password Test (`test_invalidPassword`)**:
   - Attempts to call `admin1.viewMyInfo` with a non-string password (integer).
   - Asserts that a `TypeError` is raised with the specified message.

## Edge Cases & Preconditions
- Assumes that the `Admin` class has a method named `viewMyInfo`.
- Assumes that the `User` model has attributes: `username`, `password`, `name`, `email`, and `address`.
- Ensures that `admin1` is an instance of the `Admin` class.
- Asserts that input parameters are strings.

## Result Synopsis
The tests verify that:
- The `viewMyInfo` method returns correct user information when provided with valid credentials.
- A `TypeError` is raised and caught when non-string types are passed as username or password.

## Docstring Draft
```python
"""Test cases for the viewMyInfo method of the Admin class.

Args:
    self (TestHomepage): The test instance.
"""
``````

## TestCreateCourse  
``/Project/unit_tests/test_Course.py``  
```class TestCreateCourse(TestCase):
    def setUp(self):
        self.admin1 = Admin()
        self.course1 = Course.objects.create(name="Intro CS", dateTime="2022-02-12 14:30:34")
        self.course2 = Course.objects.create(name="CS 2", dateTime="2022-02-12 14:30:34")


    def test_CourseInDb(self):
        course_list = list(Course.objects.filter(name__exact="CS 2"))
        self.assertEqual(course_list, [self.course2], msg='course should be in database')

    def test_courseExists(self):
        self.assertEqual(self.admin1.createCourse("Intro CS", "2022-02-12 14:30:34"), "Course already exists", msg='should have returned course already exists msg')

    def test_newCourse(self):
        self.assertEqual(self.admin1.createCourse("Data Structures", "2022-02-12 14:30:34"), "Course creation successful", msg='should have added course and returned success msg')

    def test_invalidCourse(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid name type"):
            self.admin1.createCourse(38432489238, 1430)

    def test_invalidTimeFormat(self):
        with self.assertRaises(ValueError, msg="should raise exception for invalid time type"):
            self.admin1.createCourse("Intro History", "cats")

    def test_invalidTimeType(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid time type"):
            self.admin1.createCourse("Intro History", 1413)```  

**Documentation:**
```python## Overview
The provided code defines a set of unit tests for the `createCourse` method within an `Admin` class. These tests validate the creation and existence checks of courses in a database, as well as handling errors related to invalid inputs.

## Interface
- **Signature**: 
  - Not applicable as these are methods within a class.
- **Parameters**:
  | Name    | Type     | Purpose                     |
  |---------|----------|-----------------------------|
  | `name`  | str      | The name of the course.       |
  | `dateTime`| str      | The start time of the course. |

## Inner Workings
- **test_CourseInDb**: 
  - Filters courses by name and checks if it matches the expected course (`self.course2`). It asserts that the filtered list contains only this course.
  
- **test_courseExists**:
  - Calls `createCourse` with a course name that already exists in the database. It expects to receive a message indicating that the course already exists.

- **test_newCourse**:
  - Attempts to create a new course and checks if it returns a success message.

- **test_invalidCourse**:
  - Attempts to create a course with an invalid `name` type (integer). It asserts that a `TypeError` is raised.

- **test_invalidTimeFormat**:
  - Attempts to create a course with an invalid `dateTime` format. It asserts that a `ValueError` is raised.

- **test_invalidTimeType**:
  - Attempts to create a course with an invalid `dateTime` type (integer). It asserts that a `TypeError` is raised.

## Edge Cases & Preconditions
- The tests assume the existence of at least one course (`self.course1`) in the database before running.
- Invalid inputs are checked for specific error types: `TypeError` for non-string `name` or `dateTime`, and `ValueError` for invalid time format.

## Result Synopsis
The tests ensure that courses can be created, retrieved, and exist checks correctly handle various scenarios, including successful course creation and error handling for invalid inputs.

## Docstring Draft
```python
"""Test methods for the createCourse method of the Admin class.

Tests validate the creation and existence checks of courses in a database,
as well as handling errors related to invalid inputs.

Args:
    name (str): The name of the course.
    dateTime (str): The start time of the course.

Returns:
    str: The result message from the createCourse method.

Raises:
    ValueError: When `dateTime` is not in a valid format.
    TypeError: When either `name` or `dateTime` is not a string.
"""
``````

## TestSearchCourse  
``/Project/unit_tests/test_Course.py``  
```class TestSearchCourse(TestCase):
    def setUp(self):
        self.admin1 = Admin()
        self.course1 = Course.objects.create(name="Intro CS", dateTime="2022-02-12 14:30:34.339504")
        self.course2 = Course.objects.create(name="CS 2", dateTime="2022-02-12 14:30:34.339504")

    def test_courseExists(self):
        self.assertTrue(self.admin1.searchCourse("Intro CS"), msg='should have returned true since course is in db')

    def test_noCourse(self):
        self.assertFalse(self.admin1.searchCourse("Geography"), msg='should have returned false since course is not in db')

    def test_invalidInput(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid search type"):
            self.admin1.searchCourse(143)```  

**Documentation:**
```python## Overview
This code defines a test class `TestSearchCourse` that tests the `searchCourse` method of an `Admin` class. It checks if courses exist in the database and handles cases where no courses match or invalid input is provided.

## Interface
- **Signature**: N/A (This is a class, not a function)
- **Parameters**: None

## Inner Workings
- The `setUp` method creates two `Course` objects in the database.
- The `test_courseExists` method asserts that searching for an existing course returns `True`.
- The `test_noCourse` method asserts that searching for a non-existing course returns `False`.
- The `test_invalidInput` method asserts that passing invalid input (e.g., an integer) to `searchCourse` raises a `TypeError`.

## Edge Cases & Preconditions
- Assumes the existence of an `Admin` class with a `searchCourse` method.
- Assumes the existence of a `Course` model with `name` and `dateTime` fields.
- The `searchCourse` method must return `True` for existing courses and `False` for non-existing courses.
- Passing invalid input to `searchCourse` should raise a `TypeError`.

## Result Synopsis
The tests check the functionality of the `searchCourse` method, ensuring it correctly identifies existing and non-existing courses and handles invalid input gracefully.

## Docstring Draft
```python
"""Tests the searchCourse method of the Admin class.

This class contains methods to test various scenarios when searching for courses.
"""

# No parameters

# No returns

# Raises:
    TypeError: When `searchCourse` is called with an invalid type (e.g., integer).
```

File path: Project/unit_tests/test_Course.py
Function/Class: TestSearchCourse```

## setUp  
``/Project/unit_tests/test_Course.py``  
```def setUp(self):
        self.admin1 = Admin()
        self.user1 = User.objects.create(username="lameGuy000", password="Password1:)", name="Richard Smalls", email="lameguy@uwm.edu", phone="123-4567", address="1614 E North Ave. Milwaukee WI 53211")
        self.user2 = User.objects.create(username="c00lguy100", password="P@ssw0rd", name="Hugh Mungus", email="coolguy@uwm.edu", phone="867-5309", address="2100 E. Kenwood Blvd. Milwaukee WI 53211")```  

**Documentation:**
```python## Overview
The `setUp` function in the `test_Course.py` file initializes test instances of an admin and two users for use in course-related tests.

## Interface
- **Signature**: `def setUp(self):`
- **Parameters**:
    - None

## Inner Workings
1. An instance of the `Admin` class is created and stored in `self.admin1`.
2. Two instances of the `User` model are created using Django's ORM (`User.objects.create`). Each user has a unique username, password, name, email, phone number, and address.

## Edge Cases & Preconditions
- Assumes that the `Admin` class can be instantiated without any arguments.
- Assumes that Django's ORM can create instances of the `User` model with the provided attributes.
- No explicit error handling is noted for potential failures during instance creation (e.g., if passwords don't meet complexity requirements).

## Result Synopsis
The function initializes and stores an admin and two users in the class instance variables, preparing them for use in subsequent tests.

## Docstring Draft
```python
"""Sets up the test environment by creating an admin user and two regular users.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If any of the user creation fails (e.g., due to password complexity).
"""
``````

## test_userInfoCorrect  
``/Project/unit_tests/test_Course.py``  
```def test_userInfoCorrect(self):
        myInfo = self.admin1.viewMyInfo("c00lguy100", "P@ssw0rd")
        self.assertEqual(myInfo.username, "c00lguy100", "user's username is not correct")
        self.assertEqual(myInfo.password, "P@ssw0rd", "user's password is not correct")
        self.assertEqual(myInfo.name, "Hugh Mungus", "user's name is not correct")
        self.assertEqual(myInfo.email, "coolguy@uwm.edu", "user's email is not correct")
        self.assertEqual(myInfo.address, "2100 E. Kenwood Blvd. Milwaukee WI 53211", "user's address is not correct")```  

**Documentation:**
```python## Overview
This code snippet is a unit test for verifying the correctness of user information retrieval from a system.

## Interface
- **Signature**: `test_userInfoCorrect(self)`
- **Parameters**:
  | Name    | Type     | Purpose                        |
  |---------|----------|----------------------------------|
  | `self`  | `unittest.TestCase` | The test case instance. |

## Inner Workings
The function `test_userInfoCorrect` performs the following steps:
1. Calls `self.admin1.viewMyInfo("c00lguy100", "P@ssw0rd")` to retrieve user information for the username `"c00lguy100"` with the password `"P@ssw0rd"`.
2. Uses assertions (`self.assertEqual`) to verify that:
   - The retrieved `myInfo.username` matches `"c00lguy100"`.
   - The retrieved `myInfo.password` matches `"P@ssw0rd"`.
   - The retrieved `myInfo.name` matches `"Hugh Mungus"`.
   - The retrieved `myInfo.email` matches `"coolguy@uwm.edu"`.
   - The retrieved `myInfo.address` matches `"2100 E. Kenwood Blvd. Milwaukee WI 53211"`.

## Edge Cases & Preconditions
- **Assumptions**: 
  - There exists a user with the username `"c00lguy100"` and password `"P@ssw0rd"`.
  - The `self.admin1` object has a method `viewMyInfo` that correctly retrieves user information.
  
- **Potential Failure Modes**:
  - If the user credentials are incorrect or the user does not exist, an error may be raised by `viewMyInfo`.

## Result Synopsis
The function asserts that the retrieved user information matches the expected values. If any assertion fails, it will raise an `AssertionError`.

## Docstring Draft
```python
"""Verifies the correctness of retrieving user information.

Args:
    self (unittest.TestCase): The test case instance.

Raises:
    AssertionError: If any of the assertions fail.
"""
``````

## test_invalidUsername  
``/Project/unit_tests/test_Course.py``  
```def test_invalidUsername(self):
        with self.assertRaises(TypeError, msg="should raise exception since username is not string"):
            self.admin1.viewMyInfo(1, "P@ssw0rd")```  

**Documentation:**
```python## Overview
- This function tests the behavior of `viewMyInfo` method when an invalid username (non-string) is provided.

## Interface
- **Signature**: `test_invalidUsername(self)`
- **Parameters**:
  | Name   | Type    | Purpose                               |
  |--------|---------|---------------------------------------|
  | self   | None    | The test case instance                |

## Inner Workings
- The function calls the `viewMyInfo` method of an object named `admin1`.
- It passes two arguments to `viewMyInfo`: a non-string value (integer `1`) and a string value (`"P@ssw0rd"`).
- The function is expected to raise a `TypeError` because the username should be a string.
- The `assertRaises` context manager checks if the `TypeError` is raised with the specified error message.

## Edge Cases & Preconditions
- **Assumption**: The method `viewMyInfo` expects a string as the username.
- **Potential Failure Modes**: If `viewMyInfo` does not raise an exception when a non-string username is provided, or if it raises an exception with a different message, the test will fail.
- **Error-Handling Logic**: The function asserts that `TypeError` should be raised.

## Result Synopsis
- The code checks whether `viewMyInfo` correctly handles a non-string username by raising a `TypeError`.

## Docstring Draft
```python
"""Tests that viewMyInfo raises TypeError when an invalid username (non-string) is provided.

Raises:
    AssertionError: If the TypeError with the expected message is not raised.
"""
``````

## test_invalidPassword  
``/Project/unit_tests/test_Course.py``  
```def test_invalidPassword(self):
        with self.assertRaises(TypeError, msg="should raise exception since password is not string"):
            self.admin1.viewMyInfo("c00lguy100", 12)```  

**Documentation:**
```python## Overview
This code snippet tests the `viewMyInfo` method of an admin object to ensure that it raises a `TypeError` when provided with a non-string password.

## Interface
- **Signature**: 
  ```python
  test_invalidPassword(self)
  ```
- **Parameters**:
  - None. The method does not take any parameters explicitly. It uses the context and setup provided by the class it belongs to (`self.admin1`).

## Inner Workings
1. The method `test_invalidPassword` is invoked.
2. It uses a `with` statement with `self.assertRaises(TypeError, msg="should raise exception since password is not string")`. This asserts that calling `viewMyInfo` on `self.admin1` with the arguments `"c00lguy100"` and `12` will raise a `TypeError`.
3. The method assumes that `viewMyInfo` should receive two parameters: a username (as a string) and a password (also as a string).
4. If a `TypeError` is not raised as expected, the test will fail.

## Edge Cases & Preconditions
- The assumption here is that the method `viewMyInfo` expects its password parameter to be a string.
- It does not explicitly check if the username parameter is a string before validating the password type.
- If `viewMyInfo` were designed differently and could handle non-string passwords, this test would not pass.

## Result Synopsis
The code tests whether the `viewMyInfo` method correctly raises a `TypeError` when it receives a non-string as the password argument.

## Docstring Draft
```python
"""Tests that viewMyInfo method raises TypeError when provided with a non-string password.

This ensures that the method enforces correct input types for passwords.

Args:
    self (unittest.TestCase): The test case instance.

Raises:
    AssertionError: If no TypeError is raised when calling viewMyInfo with a non-string password.
"""
``````

## setUp  
``/Project/unit_tests/test_Course.py``  
```def setUp(self):
        self.admin1 = Admin()
        self.course1 = Course.objects.create(name="Intro CS", dateTime="2022-02-12 14:30:34")
        self.course2 = Course.objects.create(name="CS 2", dateTime="2022-02-12 14:30:34")```  

**Documentation:**
```python## Overview
The `setUp` method initializes necessary objects for testing, specifically an admin user and two course instances.

## Interface
**Signature**: 
```python
def setUp(self):
```
**Parameters**:
| Name | Type | Purpose |
|------|------|---------|
| None | - | The function does not accept any parameters. |

## Inner Workings
- Creates an `Admin` instance and assigns it to `self.admin1`.
- Creates two `Course` instances using Django's ORM (`Course.objects.create`). Each course has a unique name but the same datetime.
  - The first course is named "Intro CS" with a datetime of "2022-02-12 14:30:34".
  - The second course is named "CS 2" with the same datetime.

## Edge Cases & Preconditions
- Assumes that Django ORM is properly configured and available.
- Assumes that `Admin` and `Course` models are defined and accessible within the test environment.
- Potential failure modes include:
  - If the Django ORM setup fails, creating instances will raise exceptions.
  - If the `Admin` or `Course` model definitions do not match the expected structure, errors will occur.

## Result Synopsis
The method sets up two course instances and an admin instance for use in subsequent test methods. No return value is explicitly mentioned as it is typically used within a testing framework to prepare state before each test run.

## Docstring Draft
```python
"""Initializes test objects for the Course tests.

This method creates necessary objects (an admin user and two course instances) for testing.
"""

# No parameters

Returns:
    None
``````

## test_CourseInDb  
``/Project/unit_tests/test_Course.py``  
```def test_CourseInDb(self):
        course_list = list(Course.objects.filter(name__exact="CS 2"))
        self.assertEqual(course_list, [self.course2], msg='course should be in database')```  

**Documentation:**
```python## Overview
This code tests whether a specific course is present in the database.

## Interface
- **Signature**: `def test_CourseInDb(self)`
- **Parameters**:
  | Name     | Type   | Purpose                          |
  |----------|--------|----------------------------------|
  | self     | object | The test case instance.          |

## Inner Workings
- Fetches a list of courses from the database where the name exactly matches "CS 2".
- Asserts that this list contains only one course, which is `self.course2`.

## Edge Cases & Preconditions
- Assumes that `self.course2` has been previously defined and is stored in the database with the name "CS 2".
- Potential failure mode if no courses match the name "CS 2", or if multiple courses match.
- Errors will be raised if `self.course2` does not exist in the database.

## Result Synopsis
The function asserts that there is exactly one course named "CS 2" in the database, which should be `self.course2`.

## Docstring Draft
```python
"""Tests whether a specific course is present in the database.

Args:
    self (unittest.TestCase): The test case instance.

Raises:
    AssertionError: If the assertion fails.
"""
``````

## test_courseExists  
``/Project/unit_tests/test_Course.py``  
```def test_courseExists(self):
        self.assertEqual(self.admin1.createCourse("Intro CS", "2022-02-12 14:30:34"), "Course already exists", msg='should have returned course already exists msg')```  

**Documentation:**
```python## Overview
This code tests the `createCourse` method of an admin object to ensure that it correctly handles the scenario where a course with the same name and start time already exists.

## Interface
- **Signature**: `test_courseExists(self)`
- **Parameters**:
  - `self`: The test case instance, which provides access to the class attributes and methods.

## Inner Workings
1. The method `test_courseExists` is called on an instance of a test case.
2. It uses the `createCourse` method from the `admin1` object with parameters `"Intro CS"` for the course name and `"2022-02-12 14:30:34"` for the start time.
3. The expected return value is the string `"Course already exists"`.
4. The `assertEqual` method is used to verify that the actual return value from `createCourse` matches the expected value.

## Edge Cases & Preconditions
- **Precondition**: The course with name `"Intro CS"` and start time `"2022-02-12 14:30:34"` should already exist in the system for this test to pass.
- **Edge Case**: If the course does not exist, the test will fail because it expects the method to return `"Course already exists"`.
- **Error Handling**: The `assertEqual` method will raise an assertion error if the actual return value from `createCourse` does not match the expected value.

## Result Synopsis
The code tests whether the `createCourse` method returns the correct message when attempting to create a course that already exists in the system.

## Docstring Draft
```python
"""Tests the behavior of the createCourse method when a course with the same name and start time already exists.

Args:
    self: The test case instance.

Raises:
    AssertionError: If the createCourse method does not return the expected message.
"""
``````

## test_newCourse  
``/Project/unit_tests/test_Course.py``  
```def test_newCourse(self):
        self.assertEqual(self.admin1.createCourse("Data Structures", "2022-02-12 14:30:34"), "Course creation successful", msg='should have added course and returned success msg')```  

**Documentation:**
```python## Overview
The `test_newCourse` function is a unit test method that checks whether the `createCourse` method of an admin object successfully creates a new course and returns an appropriate message.

## Interface
- **Signature**: `test_newCourse(self)`
- **Parameters**:
  - None

## Inner Workings
1. The function calls `self.admin1.createCourse("Data Structures", "2022-02-12 14:30:34")` with the course name "Data Structures" and a timestamp.
2. It asserts that the return value of this method call is equal to the string `"Course creation successful"` using `self.assertEqual`.
3. If the assertion passes, it means that the `createCourse` method successfully created the course and returned the expected message.

## Edge Cases & Preconditions
- The function assumes that the admin object (`self.admin1`) has a method `createCourse` that can be called with valid parameters.
- It also assumes that the `createCourse` method will correctly handle the creation of a new course and return the expected success message.
- If the `createCourse` method fails to create the course or returns an unexpected message, the test will fail.

## Result Synopsis
The function asserts that calling `self.admin1.createCourse("Data Structures", "2022-02-12 14:30:34")` returns `"Course creation successful"`, indicating that the new course was successfully created.

## Docstring Draft
```python
"""Test the createCourse method of an admin object to ensure it correctly creates a new course and returns the expected success message.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If the createCourse method does not return the expected success message.
"""
``````

## test_invalidCourse  
``/Project/unit_tests/test_Course.py``  
```def test_invalidCourse(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid name type"):
            self.admin1.createCourse(38432489238, 1430)```  

**Documentation:**
```python## Overview
This code tests whether the `createCourse` method raises a `TypeError` when an invalid type is provided as the course name.

## Interface
- **Signature**: `def test_invalidCourse(self)`
- **Parameters**:
    | Name     | Type   | Purpose                    |
    |----------|--------|----------------------------|
    | self     | object | The instance of the class. |

## Inner Workings
- The method uses a context manager (`with self.assertRaises(TypeError, msg="...")`) to assert that calling `self.admin1.createCourse(38432489238, 1430)` raises a `TypeError`.
    - The first argument to `assertRaises` specifies the expected exception type.
    - The second argument is an optional message for debugging if the assertion fails.

## Edge Cases & Preconditions
- **Assumptions**: 
    - The `admin1` object has a method `createCourse` that takes two parameters: `course_name` and `course_id`.
    - The `course_id` parameter is expected to be of an integer type.
- **Potential Failure Modes**:
    - If the method does not raise a `TypeError` when given non-string input for `course_name`, the test will fail.
- **Error-Handling Logic**: 
    - The test asserts that a `TypeError` is raised with the specified message, ensuring that the exception handling in the `createCourse` method works as expected.

## Result Synopsis
The function tests whether an exception is correctly raised when invalid input (non-string) is provided for the course name parameter. If successful, it confirms that the system appropriately handles such errors by raising a `TypeError`.

## Docstring Draft
```python
"""Tests that createCourse raises TypeError when given non-string input for course_name.

Raises:
    AssertionError: If createCourse does not raise TypeError for invalid name type.
"""
```
The provided test function `test_invalidCourse` checks if the `createCourse` method correctly handles an invalid input type by raising a `TypeError`. The docstring has been drafted to reflect this functionality and the expected error handling.```

## test_invalidTimeFormat  
``/Project/unit_tests/test_Course.py``  
```def test_invalidTimeFormat(self):
        with self.assertRaises(ValueError, msg="should raise exception for invalid time type"):
            self.admin1.createCourse("Intro History", "cats")```  

**Documentation:**
```python## Overview
This code snippet is a unit test method designed to verify that an exception is raised when an attempt is made to create a course with an invalid time format. It specifically tests the `createCourse` method of an admin object.

## Interface
- **Signature**: `test_invalidTimeFormat(self)`
- **Parameters**:
  | Name     | Type   | Purpose                                |
  |----------|--------|------------------------------------------|
  | self     |        | Reference to the current test instance |

## Inner Workings
- The method uses a context manager (`with`) to assert that a `ValueError` is raised when calling `self.admin1.createCourse("Intro History", "cats")`.
- The exception message is checked to ensure it contains the string `"should raise exception for invalid time type"`.

## Edge Cases & Preconditions
- **Assumptions**: The `createCourse` method in `admin1` should handle invalid time formats and raise a `ValueError` with a specific error message.
- **Potential Failure Modes**: If the `createCourse` method does not raise an exception for invalid time formats, or if the raised exception does not contain the expected message, the test will fail.
- **Error-Handling Logic**: The test uses `self.assertRaises` to verify that the correct exception is raised and with the correct message.

## Result Synopsis
The code tests that calling `createCourse` with invalid time format arguments raises a `ValueError` with a specific message.

## Docstring Draft
```python
"""Tests that an exception is raised when creating a course with an invalid time format.

Raises:
    AssertionError: If no exception is raised or if the wrong exception message is returned.
"""
``````

## test_invalidTimeType  
``/Project/unit_tests/test_Course.py``  
```def test_invalidTimeType(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid time type"):
            self.admin1.createCourse("Intro History", 1413)```  

**Documentation:**
```python## Overview
This code snippet is a unit test method for the `createCourse` function in an admin interface. It checks that calling the function with an invalid time type raises a `TypeError`.

## Interface
- **Signature**: `test_invalidTimeType(self)`
- **Parameters**:
  | Name     | Type   | Purpose                           |
  |----------|--------|-----------------------------------|
  | self     |        | The test case instance.           |

## Inner Workings
1. The method uses the `with` statement to catch an expected exception.
2. It asserts that a `TypeError` is raised when calling `self.admin1.createCourse("Intro History", 1413)`.
3. The message "should raise exception for invalid time type" is provided to describe what the test checks.

## Edge Cases & Preconditions
- The function assumes that `createCourse` should not accept an integer as a time type.
- It does not explicitly handle any other types of invalid inputs, focusing solely on integers.

## Result Synopsis
The method passes if a `TypeError` is raised with the specified message when calling `createCourse` with an integer instead of expected data. Otherwise, it fails.

## Docstring Draft
```python
"""Tests that createCourse raises TypeError for invalid time type.

Args:
    self: The test case instance.

Raises:
    AssertionError: If a TypeError is not raised with the correct message.
"""
``````

## setUp  
``/Project/unit_tests/test_Course.py``  
```def setUp(self):
        self.admin1 = Admin()
        self.course1 = Course.objects.create(name="Intro CS", dateTime="2022-02-12 14:30:34.339504")
        self.course2 = Course.objects.create(name="CS 2", dateTime="2022-02-12 14:30:34.339504")```  

**Documentation:**
```python## Overview
The `setUp` method is designed to prepare the test environment by creating instances of `Admin` and two `Course` objects.

## Interface
- **Signature**: `def setUp(self)`
- **Parameters**:
  | Name     | Type        | Purpose                         |
  |----------|-------------|-----------------------------------|
  | self     | instance    | Reference to the current test case object |

## Inner Workings
1. The method creates an instance of `Admin` and assigns it to `self.admin1`.
2. It creates two instances of `Course`, each with specific attributes (`name` and `dateTime`), and assigns them to `self.course1` and `self.course2` respectively.

## Edge Cases & Preconditions
- Assumes that the database is accessible and can be interacted with via Django's ORM.
- The method does not handle errors related to database operations (e.g., if the database connection fails).
- If a `Course` creation fails, it will raise an exception which must be handled by the test framework.

## Result Synopsis
This method sets up the necessary objects for further testing of methods that depend on these administrative and course data.

## Docstring Draft
```python
"""Sets up the test environment.

Prepares instances of `Admin` and two `Course` objects for further tests.

Args:
    self (object): Reference to the current test case object.

Raises:
    Any exceptions raised by database operations will be propagated.
"""
``````

## test_courseExists  
``/Project/unit_tests/test_Course.py``  
```def test_courseExists(self):
        self.assertTrue(self.admin1.searchCourse("Intro CS"), msg='should have returned true since course is in db')```  

**Documentation:**
```python## Overview
- This code snippet tests whether a specific course exists within a database using the `admin1` object's `searchCourse` method.

## Interface
### Signature
```python
def test_courseExists(self):
```
### Parameters
| Name | Type | Purpose |
|------|------|---------|
| self | Test case instance | Reference to the current test case. |

## Inner Workings
- The function `test_courseExists` is a method of a test case class.
- It uses the `admin1` object's `searchCourse` method to check if a course with the name "Intro CS" exists in the database.
- The `assertTrue` assertion checks whether the result from `searchCourse` is `True`, meaning the course exists.

## Edge Cases & Preconditions
- **Preconditions**: 
  - The `admin1` object must have a method `searchCourse` that returns `True` if the course exists and `False` otherwise.
  - The database must contain a record for the "Intro CS" course.
- **Assumptions**:
  - The `assertTrue` assertion assumes that the method call does not raise any exceptions.
- **Potential Failure Modes**:
  - If `searchCourse` returns `False`, the test will fail, indicating that the course does not exist in the database as expected.
  - If an exception is raised by `searchCourse`, it could cause the test to fail or be skipped.

## Result Synopsis
- The function asserts that the result of `admin1.searchCourse("Intro CS")` is `True`.
- If the assertion passes, the test indicates that the "Intro CS" course exists in the database as expected.
- If the assertion fails, the test will report an error indicating that the course does not exist.

## Docstring Draft
```python
"""Tests whether a specific course exists within the database.

Args:
    self (unittest.TestCase): The current test case instance.

Raises:
    AssertionError: If the "Intro CS" course does not exist in the database.
"""
``````

## test_noCourse  
``/Project/unit_tests/test_Course.py``  
```def test_noCourse(self):
        self.assertFalse(self.admin1.searchCourse("Geography"), msg='should have returned false since course is not in db')```  

**Documentation:**
```python## Overview
This code snippet defines a unit test method named `test_noCourse` within the context of testing an admin's ability to search for a non-existent course.

## Interface
- **Signature**: `def test_noCourse(self)`
  - **Parameters**:
    - None

## Inner Workings
1. The method calls `self.admin1.searchCourse("Geography")`, which is expected to return `False` if the course "Geography" does not exist in the database.
2. The method asserts that `self.assertFalse()` evaluates to `True` based on the result of `searchCourse`. If `searchCourse` returns `True` (indicating the course exists), this assertion will fail, and an error message 'should have returned false since course is not in db' will be displayed.

## Edge Cases & Preconditions
- The method assumes that `self.admin1.searchCourse` is a valid method that can search for courses in a database.
- It expects that there should be no "Geography" course in the database to pass this test, as otherwise, the assertion would fail.

## Result Synopsis
This code tests whether the `searchCourse` method correctly returns `False` when querying for a non-existent course. If it passes, it confirms that the method behaves as expected when dealing with absent data.

## Docstring Draft
```python
"""Tests that the searchCourse method returns False for a non-existent course.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If the searchCourse method does not return False for a non-existent course.
"""
``````

## test_invalidInput  
``/Project/unit_tests/test_Course.py``  
```def test_invalidInput(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid search type"):
            self.admin1.searchCourse(143)```  

**Documentation:**
```python## Overview
- This code snippet tests the `searchCourse` method of an `admin1` object to ensure it raises a `TypeError` when provided with an invalid search type.

## Interface
- **Signature**: `test_invalidInput(self)`
- **Parameters**:
  | Name | Type | Purpose |
  |------|------|---------|
  | self | unittest.TestCase | The test case instance. |

## Inner Workings
- The code sets up a test by calling the `searchCourse` method on an `admin1` object with an integer argument (`143`) as the search type.
- It uses the `assertRaises` context manager to verify that a `TypeError` is raised during this call.
- The context manager also provides a message stating what should happen if the exception is not raised.

## Edge Cases & Preconditions
- **Assumption**: The `searchCourse` method expects a specific data type for its search parameter, likely a string or another valid format.
- **Potential Failure Mode**: If the `searchCourse` method does not handle non-string arguments correctly, it will not raise the expected `TypeError`.
- **Error-Handling Logic**: The code checks that a `TypeError` is raised, indicating proper exception handling for invalid input.

## Result Synopsis
- The function tests that calling `searchCourse` with an integer argument raises a `TypeError`.

## Docstring Draft
```python
"""Tests that searchCourse method raises TypeError for invalid search type.

Raises:
    AssertionError: If a TypeError is not raised when providing an integer as the search type.
"""
``````

## TestAssignSection  
``/Project/unit_tests/test_assignSection.py``  
```class TestAssignSection(TestCase):
    def setUp(self):
        self.instructor= Instructor()
        self.INS = User.objects.create(username="userone", password="1234", name="userone",
                                         email="userone@example.com", phone="1234567890",
                                         address="123 Roadrage lane, Springfield, Illinois ", user_type="instructor")
        self.TA = User.objects.create(username="usertwo", password="4321", name="usertwo",
                                         email="usertwo@example.com", phone="0987654321",
                                         address="1325 Barrington Rd, Hoffman Estates, IL 60169", user_type="ta")
        self.course1 = Course.objects.create(name="courseone", dateTime="2023-05-15 10:00:00")
        self.section1 = Section.objects.create(sectionName="891", owner=self.course1, user_id=self.INS)

    def test_assignSection_validInput(self):
        self.instructor.assignSection("courseone", "891", "usertwo")
        assigned_section = Section.objects.get(sectionName__exact="891")
        self.assertEqual(assigned_section.user_id, self.TA, msg="Section not displaying assigned TA")

    def test_assignSection_invalidUser(self):
        with self.assertRaises(ValueError, msg="assignSection() failed to raise error for invalid user"):
            self.instructor.assignSection("courseone", "891", "userthree")

    def test_assignSection_invalidCourse(self):
        with self.assertRaises(ValueError, msg="assignSection() failed to raise error for invalid course"):
            self.instructor.assignSection("coursefive", "891", "usertwo")

    def test_assignSection_invalidSection(self):
        with self.assertRaises(ValueError, msg="assignSection() failed to raise error for invalid section"):
            self.instructor.assignSection("courseone", "111", "usertwo")

    def test_assignSection_userAlreadyAssigned(self):
        self.section1.user_id = self.TA
        self.section1.save()
        with self.assertRaises(ValueError, msg="assignSection() failed to raise error for user already assigned"):
            self.instructor.assignSection("courseone", "891", "usertwo")```  

**Documentation:**
```python## Overview
The provided code defines a test class `TestAssignSection` that tests the `assignSection` method of an `Instructor` object. This method is expected to assign a TA ( Teaching Assistant) to a specific course section.

## Interface
- **Signature**: 
  ```python
  class TestAssignSection(TestCase):
      def setUp(self): ...
      
      def test_assignSection_validInput(self): ...
      
      def test_assignSection_invalidUser(self): ...
      
      def test_assignSection_invalidCourse(self): ...
      
      def test_assignSection_invalidSection(self): ...
      
      def test_assignSection_userAlreadyAssigned(self): ...
  ```
- **Parameters**:
  - `self`: Refers to the instance of `TestAssignSection`.

## Inner Workings
- The `setUp` method initializes necessary objects (`Instructor`, `User`, `Course`, and `Section`) before each test.
  
- Each test method uses assertions to verify the behavior of `assignSection` under different scenarios:
  - **test_assignSection_validInput**: Checks if a TA is correctly assigned to a section with valid input.
  - **test_assignSection_invalidUser**: Verifies that an error is raised when attempting to assign a non-existent user.
  - **test_assignSection_invalidCourse**: Ensures an error is thrown for assigning a section to a non-existent course.
  - **test_assignSection_invalidSection**: Checks if an error occurs when trying to assign a TA to a non-existent section.
  - **test_assignSection_userAlreadyAssigned**: Verifies that an error is raised when attempting to re-assign a user to a section they are already in.

## Edge Cases & Preconditions
- The `setUp` method assumes the existence of users, courses, and sections with specific attributes (e.g., usernames, IDs).
- Errors are expected when using non-existent users, courses, or sections.
- An error is also expected if attempting to re-assign a user who is already in the section.

## Result Synopsis
The code tests various scenarios for assigning a TA to a course section and verifies that appropriate errors are raised when invalid inputs are provided. It confirms that an existing user can be correctly assigned to a section, and repeated assignments or attempts to assign non-existent entities result in exceptions being thrown.

## Docstring Draft
```python
"""Test class for the assignSection method of the Instructor class.

This class tests various scenarios for assigning a TA (Teaching Assistant) to a course section, including valid inputs and edge cases such as invalid users, courses, sections, and already assigned users.
"""
```

This Markdown-formatted explanation provides a comprehensive breakdown of the code's functionality, parameters, control flow, error handling, and expected outcomes.```

## setUp  
``/Project/unit_tests/test_assignSection.py``  
```def setUp(self):
        self.instructor= Instructor()
        self.INS = User.objects.create(username="userone", password="1234", name="userone",
                                         email="userone@example.com", phone="1234567890",
                                         address="123 Roadrage lane, Springfield, Illinois ", user_type="instructor")
        self.TA = User.objects.create(username="usertwo", password="4321", name="usertwo",
                                         email="usertwo@example.com", phone="0987654321",
                                         address="1325 Barrington Rd, Hoffman Estates, IL 60169", user_type="ta")
        self.course1 = Course.objects.create(name="courseone", dateTime="2023-05-15 10:00:00")
        self.section1 = Section.objects.create(sectionName="891", owner=self.course1, user_id=self.INS)```  

**Documentation:**
```python## Overview
This code sets up the initial test environment by creating an instructor and two users (a TA and a regular user), as well as a course and a section.

## Interface
### Signature
```python
def setUp(self):
```

### Parameters
| Name | Type | Purpose |
| --- | --- | --- |
| None |  | This method does not take any parameters. |

## Inner Workings
1. **Create an Instructor Object**: An instance of `Instructor` is created and stored in the `self.instructor` attribute.
2. **Create a User (Instructor)**: A user with type "instructor" is created using Django's ORM (`User.objects.create`). This user is stored in the `self.INS` attribute.
3. **Create a User (TA)**: Another user with type "ta" is created using Django's ORM and stored in the `self.TA` attribute.
4. **Create a Course**: A course named "courseone" is created and its date and time set to "2023-05-15 10:00:00". This course is stored in the `self.course1` attribute.
5. **Create a Section**: A section with name "891", owned by the previously created course, and associated with the instructor user is created using Django's ORM. This section is stored in the `self.section1` attribute.

## Edge Cases & Preconditions
- **Preconditions**:
  - Assumes that the `Instructor`, `User`, `Course`, and `Section` classes are correctly implemented and available.
  - Assumes that the database connection is properly set up and accessible.
- **Potential Failure Modes**:
  - If any of the ORM operations fail (e.g., due to database issues), an exception will be raised.
  - If the user types ("instructor" or "ta") are not recognized, the code may create a user with an invalid type.

## Result Synopsis
This method initializes the test environment by creating necessary objects for testing purposes. It sets up an instructor and two users (a TA and a regular user), as well as a course and a section. The created objects are stored in instance attributes (`self.instructor`, `self.INS`, `self.TA`, `self.course1`, `self.section1`) for use in subsequent test cases.

## Docstring Draft
```python
"""Sets up the initial test environment by creating necessary objects.

Args:
    None

Returns:
    None

Raises:
    None
"""
```

File path: Project/unit_tests/test_assignSection.py
Function/Class: setUp```

## test_assignSection_validInput  
``/Project/unit_tests/test_assignSection.py``  
```def test_assignSection_validInput(self):
        self.instructor.assignSection("courseone", "891", "usertwo")
        assigned_section = Section.objects.get(sectionName__exact="891")
        self.assertEqual(assigned_section.user_id, self.TA, msg="Section not displaying assigned TA")```  

**Documentation:**
```python## Overview
This code snippet tests the `assignSection` method of an instructor object to ensure that it correctly assigns a section to a user and retrieves the correct information from the database.

## Interface
- **Signature**: `test_assignSection_validInput(self)`
- **Parameters**:
  | Name     | Type   | Purpose                          |
  |----------|--------|----------------------------------|
  | self     | object | The instance of the test class. |

## Inner Workings
1. The method calls the `assignSection` method on an `instructor` object with the parameters `"courseone"`, `"891"`, and `"usertwo"`.
2. It then retrieves a `Section` object from the database using the `sectionName__exact="891"` lookup.
3. Finally, it asserts that the `user_id` of the retrieved section matches the expected `TA`.

## Edge Cases & Preconditions
- **Assumptions**: 
  - The `instructor.assignSection` method correctly assigns the section to the user.
  - There is a `Section` object in the database with `sectionName="891"`.
  - The `user_id` of the section matches the expected `TA`.

- **Potential Failure Modes**:
  - If there is no `Section` object with `sectionName="891"`, an exception will be raised.
  - If the `user_id` of the retrieved section does not match the expected `TA`, the assertion will fail.

- **Error Handling**: 
  - The code assumes that any exceptions raised during the assignment process are handled by the `assignSection` method.

## Result Synopsis
The function asserts that a section is correctly assigned to a user and retrieves the correct information from the database. If the assertions pass, the test passes; otherwise, it fails.

## Docstring Draft
```python
"""Tests the assignSection method with valid input to ensure proper section assignment and retrieval.

Args:
    self (unittest.TestCase): The instance of the test class.

Raises:
    AssertionError: If the section is not assigned correctly or if the retrieved user_id does not match the expected TA.
"""
``````

## test_assignSection_invalidUser  
``/Project/unit_tests/test_assignSection.py``  
```def test_assignSection_invalidUser(self):
        with self.assertRaises(ValueError, msg="assignSection() failed to raise error for invalid user"):
            self.instructor.assignSection("courseone", "891", "userthree")```  

**Documentation:**
```python## Overview
This code is a unit test method that checks if the `assignSection` function raises a `ValueError` when an invalid user is provided.

## Interface
- **Signature**: `test_assignSection_invalidUser(self)`
- **Parameters**:
  | Name     | Type   | Purpose                         |
  |----------|--------|-----------------------------------|
  | self     | object | The test case instance.           |

## Inner Workings
1. The test method uses the `with` statement to assert that a `ValueError` is raised when calling `self.instructor.assignSection("courseone", "891", "userthree")`.
2. If no exception is raised, the test will fail.

## Edge Cases & Preconditions
- Assumes that `assignSection` should raise a `ValueError` for an invalid user.
- No explicit error-handling logic to handle other potential exceptions or return values.

## Result Synopsis
The code asserts that calling `self.instructor.assignSection("courseone", "891", "userthree")` raises a `ValueError`.

## Docstring Draft
```python
"""Checks if the assignSection function raises a ValueError for an invalid user.

Raises:
    AssertionError: If the ValueError is not raised.
"""
``````

## test_assignSection_invalidCourse  
``/Project/unit_tests/test_assignSection.py``  
```def test_assignSection_invalidCourse(self):
        with self.assertRaises(ValueError, msg="assignSection() failed to raise error for invalid course"):
            self.instructor.assignSection("coursefive", "891", "usertwo")```  

**Documentation:**
```python## Overview
This code tests the `assignSection` method of an instructor object to ensure it raises a `ValueError` when attempting to assign a section to an invalid course.

## Interface
- **Signature**: 
  ```python
  def test_assignSection_invalidCourse(self)
  ```
- **Parameters**:
  | Name | Type | Purpose |
  |------|------|---------|
  | self | unittest.TestCase | The test case instance. |

## Inner Workings
1. The method `test_assignSection_invalidCourse` is called.
2. It asserts that when the `assignSection` method of an instructor object is invoked with parameters "coursefive", "891", and "usertwo", a `ValueError` is raised.
3. If the expected exception is not raised, the test will fail.

## Edge Cases & Preconditions
- **Assumptions**: 
  - The instructor object has a method `assignSection`.
  - The instructor object is capable of handling and raising exceptions.
- **Potential Failure Modes**:
  - The `assignSection` method might handle invalid courses differently than expected, causing the test to fail.
- **Error-Handling Logic**:
  - The test uses `self.assertRaises` to verify that a `ValueError` is raised.

## Result Synopsis
The code ensures that the `assignSection` method correctly raises a `ValueError` when an invalid course identifier is provided.

## Docstring Draft
```python
"""Test assigning a section with an invalid course identifier.

Args:
    self (unittest.TestCase): The test case instance.

Raises:
    AssertionError: If assignSection does not raise ValueError for invalid courses.
"""
``````

## test_assignSection_invalidSection  
``/Project/unit_tests/test_assignSection.py``  
```def test_assignSection_invalidSection(self):
        with self.assertRaises(ValueError, msg="assignSection() failed to raise error for invalid section"):
            self.instructor.assignSection("courseone", "111", "usertwo")```  

**Documentation:**
```python## Overview
This code tests the `assignSection` method of an instructor object to ensure it raises a `ValueError` when an invalid section is provided.

## Interface
### Signature
```python
def test_assignSection_invalidSection(self):
```

### Parameters
| Name | Type | Purpose |
|------|------|---------|
| None | None | This is a method of a class, so there are no parameters passed explicitly. The test is performed on an instance of the class that has been set up in advance with the necessary attributes and methods. |

## Inner Workings
- The method `test_assignSection_invalidSection` is part of a test case class.
- It asserts that calling the `assignSection` method of an instructor object with invalid parameters ("courseone", "111", "usertwo") raises a `ValueError`.
- The assertion is made using `self.assertRaises`, which checks if the expected exception (`ValueError`) is raised when the specified function is called.

## Edge Cases & Preconditions
- The test assumes that the instructor object has an `assignSection` method that can be invoked with the given parameters.
- It implicitly tests whether the `assignSection` method correctly handles invalid section identifiers by ensuring a `ValueError` is raised under these conditions.

## Result Synopsis
The code asserts that calling `self.instructor.assignSection("courseone", "111", "usertwo")` raises a `ValueError`, as expected when an invalid section is provided.

## Docstring Draft
```python
"""Tests the assignSection method to ensure it raises a ValueError for invalid sections.

Raises:
    AssertionError: If a ValueError is not raised when an invalid section is provided.
"""
``````

## test_assignSection_userAlreadyAssigned  
``/Project/unit_tests/test_assignSection.py``  
```def test_assignSection_userAlreadyAssigned(self):
        self.section1.user_id = self.TA
        self.section1.save()
        with self.assertRaises(ValueError, msg="assignSection() failed to raise error for user already assigned"):
            self.instructor.assignSection("courseone", "891", "usertwo")```  

**Documentation:**
```python## Overview
This code snippet is a unit test function that checks whether the `assignSection` method correctly raises a `ValueError` when attempting to assign a section to a user who is already assigned.

## Interface
- **Signature**: `test_assignSection_userAlreadyAssigned(self)`
- **Parameters**:
  | Name       | Type   | Purpose                       |
  |------------|--------|-------------------------------|
  | self       | object | The instance of the test class. |

## Inner Workings
1. The method sets up a scenario where a user (`self.TA`) is already assigned to a section (`self.section1`).
2. It saves this assignment to ensure it's persisted.
3. It attempts to assign the same section (`"891"`) to another user (`"usertwo"`), expecting the `assignSection` method to raise a `ValueError`.
4. The test checks if the `assignSection` method indeed raises a `ValueError` with the expected message.

## Edge Cases & Preconditions
- Assumes that:
  - `self.TA` is a valid user ID.
  - `self.section1` is a valid section instance and is already assigned to `self.TA`.
  - The `assignSection` method exists and is callable on the `instructor` object with the given parameters.
- Potential failure modes:
  - If the `assignSection` method does not raise an error when the user is already assigned, the test will fail.
  - If the error message raised by `assignSection` does not match the expected message, the test will fail.

## Result Synopsis
The function asserts that calling `self.instructor.assignSection("courseone", "891", "usertwo")` raises a `ValueError` with the message "assignSection() failed to raise error for user already assigned".

## Docstring Draft
```python
"""Checks that assignSection method raises ValueError when user is already assigned.

Args:
    self (object): The instance of the test class.

Raises:
    AssertionError: If assignSection does not raise a ValueError as expected.
"""
``````

## TestCreateAccount  
``/Project/unit_tests/test_create_delete.py``  
```class TestCreateAccount(TestCase):
    def setUp(self):
        self.admin_instance = Admin()
        self.account1 = User.objects.create(username="testuser1", password="testpass1", email="test1@example.com")
        self.account2 = User.objects.create(username="testuser2", password="testpass2", email="test2@example.com")

    def test_account_exists(self):
        self.assertFalse(self.admin_instance.create_account("testuser1", "testpass1", "test1@example.com"), msg='should have returned true since account is in db')

    def test_new_account(self):
        self.assertTrue(self.admin_instance.create_account("testuser3", "testpass3", "test3@example.com"), msg='should have added account and returned success msg')

    def test_invalid_username_type(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid username type"):
            self.admin_instance.create_account(38432489238, "testpass4", "test4@example.com")```  

**Documentation:**
```python## Overview
The `TestCreateAccount` class is designed to test the functionality of creating and verifying user accounts using an `Admin` instance.

## Interface
### Signature
```python
class TestCreateAccount(TestCase):
```
### Parameters
| Parameter | Type   | Purpose |
|-----------|--------|---------|
| None      |        | This is a class, not a function with parameters. |

## Inner Workings
- The `setUp` method initializes an `Admin` instance and creates two user accounts in the database.
- The `test_account_exists` method checks that attempting to create an account that already exists returns `False`.
- The `test_new_account` method verifies that creating a new, unique account returns `True`.
- The `test_invalid_username_type` method tests error handling by ensuring that passing an invalid username type (e.g., an integer) raises a `TypeError`.

## Edge Cases & Preconditions
- The test assumes the existence of an `Admin` class with a `create_account` method.
- It assumes the availability of a `User` model with `username`, `password`, and `email` fields in a Django-like ORM.
- The test checks for specific error messages when exceptions are raised.

## Result Synopsis
The code tests the creation and validation of user accounts. Successful account creation returns `True`, and attempting to create an existing account or using invalid data types raises appropriate errors.

## Docstring Draft
```python
"""
Tests the functionality of creating and verifying user accounts.

Args:
    None

Returns:
    None

Raises:
    None
"""
```

This Markdown-formatted explanation provides a clear overview, interface details, inner workings analysis, edge cases, result synopsis, and a draft docstring for the `TestCreateAccount` class.```

## TestDeleteAccount  
``/Project/unit_tests/test_create_delete.py``  
```class TestDeleteAccount(TestCase):
    def setUp(self):
        self.admin_instance = Admin()
        self.account1 = User.objects.create(username="testuser1", password="testpass1", email="test1@example.com")
        self.account2 = User.objects.create(username="testuser2", password="testpass2", email="test2@example.com")

    def test_account_exists(self):
        self.assertTrue(self.admin_instance.delete_account(self.account1.username), msg='should have returned true since account is in db')

    def test_no_account(self):
        self.assertFalse(self.admin_instance.delete_account('999'), msg='should have returned false since account is not in db')

    def test_invalid_input(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid input type"):
            self.admin_instance.delete_account(999)```  

**Documentation:**
```python## Overview
This code defines a test class `TestDeleteAccount` that tests the functionality of deleting accounts using an admin instance. It includes methods to set up test data and validate different scenarios, such as deleting existing accounts, attempting to delete non-existing accounts, and handling invalid input types.

## Interface
- **Signature**: `class TestDeleteAccount(TestCase)`
  - No parameters; it is a class-based test case.
  
- **Parameters**:
  | Name       | Type     | Purpose                     |
  |------------|----------|-----------------------------|
  | None       |          | Inherits from `TestCase`.   |

## Inner Workings
- The `setUp` method initializes an admin instance and creates two user accounts for testing.
- The `test_account_exists` method checks that deleting an existing account returns `True`.
- The `test_no_account` method verifies that attempting to delete a non-existing account returns `False`.
- The `test_invalid_input` method asserts that the function raises a `TypeError` when provided with invalid input (e.g., a non-string username).

## Edge Cases & Preconditions
- Assumes the existence of an `Admin` class with a `delete_account` method.
- Assumes the existence of a `User` model with methods to create users and query their existence.
- Handles cases where the account exists, does not exist, and has invalid input types.

## Result Synopsis
The code tests various scenarios for deleting accounts and ensures that the function behaves as expected under different conditions. It confirms correct functionality for both valid and invalid inputs.

## Docstring Draft
```python
"""
Tests methods for deleting accounts using an admin instance.
"""

class TestDeleteAccount(TestCase):
    def setUp(self):
        """Set up test environment with admin and user instances."""
        self.admin_instance = Admin()
        self.account1 = User.objects.create(username="testuser1", password="testpass1", email="test1@example.com")
        self.account2 = User.objects.create(username="testuser2", password="testpass2", email="test2@example.com")

    def test_account_exists(self):
        """Verify deletion of an existing account."""
        result = self.admin_instance.delete_account(self.account1.username)
        self.assertTrue(result, msg='should have returned true since account is in db')

    def test_no_account(self):
        """Verify attempt to delete a non-existing account."""
        result = self.admin_instance.delete_account('999')
        self.assertFalse(result, msg='should have returned false since account is not in db')

    def test_invalid_input(self):
        """Assert that function raises TypeError for invalid input type."""
        with self.assertRaises(TypeError, msg="should raise exception for invalid input type"):
            self.admin_instance.delete_account(999)
``````

## setUp  
``/Project/unit_tests/test_create_delete.py``  
```def setUp(self):
        self.admin_instance = Admin()
        self.account1 = User.objects.create(username="testuser1", password="testpass1", email="test1@example.com")
        self.account2 = User.objects.create(username="testuser2", password="testpass2", email="test2@example.com")```  

**Documentation:**
```python## Overview
The `setUp` function initializes the test environment by creating an instance of `Admin` and two user instances using Django's ORM.

## Interface
**Signature**: 
```python
def setUp(self):
```

**Parameters**:
| Name     | Type   | Purpose                                                                 |
|----------|--------|-------------------------------------------------------------------------|
| self     | object | The reference to the current test class instance.                       |

## Inner Workings
- An `Admin` instance is created and assigned to `self.admin_instance`.
- Two user instances are created using Django's ORM (`User.objects.create`). Each user has a unique username, password, and email.

## Edge Cases & Preconditions
- The function assumes that the database connection is available and properly configured.
- If the usernames "testuser1" and "testuser2" already exist in the database, creating them again will raise an error. This is not handled within the `setUp` function itself but should be managed by Django's ORM or appropriate test setup logic.

## Result Synopsis
The function initializes the test environment with an `Admin` instance and two user instances, which can be used for further testing in methods of the same class.

## Docstring Draft
```python
"""Sets up the test environment.

This method initializes the test environment by creating an instance of Admin 
and two user instances using Django's ORM.

Args:
    self (object): The reference to the current test class instance.

Returns:
    None

Raises:
    None
"""
``````

## test_account_exists  
``/Project/unit_tests/test_create_delete.py``  
```def test_account_exists(self):
        self.assertFalse(self.admin_instance.create_account("testuser1", "testpass1", "test1@example.com"), msg='should have returned true since account is in db')```  

**Documentation:**
```python## Overview
This code tests whether an account exists by attempting to create it and verifying that the operation returns `False` as expected.

## Interface
- **Signature**: `test_account_exists(self)`
- **Parameters**:
  | Name        | Type     | Purpose                 |
  |-------------|----------|-------------------------|
  | self        | Test     | Reference to the test instance |

## Inner Workings
1. The function calls `self.admin_instance.create_account` with three parameters: a username, a password, and an email.
2. It asserts that the return value of `create_account` is `False`, indicating that the account already exists in the database.

## Edge Cases & Preconditions
- **Precondition**: The test assumes that the account `"testuser1"` already exists in the database before running this test.
- **Failure Mode**: If the account does not exist, the test will fail because it expects `create_account` to return `False`.

## Result Synopsis
The code asserts that attempting to create an existing account returns `False`, indicating that the operation was successful.

## Docstring Draft
```python
"""Tests whether an account exists by attempting to create it and verifying that the operation returns False as expected.

Args:
    self (Test): Reference to the test instance.

Returns:
    None

Raises:
    AssertionError: If the account creation does not return False.
"""
``````

## test_new_account  
``/Project/unit_tests/test_create_delete.py``  
```def test_new_account(self):
        self.assertTrue(self.admin_instance.create_account("testuser3", "testpass3", "test3@example.com"), msg='should have added account and returned success msg')```  

**Documentation:**
```python## Overview
This code snippet is a unit test for creating a new user account. It verifies that the `create_account` method of an admin instance successfully creates a new account with the provided username, password, and email.

## Interface
- **Signature**: `test_new_account(self)`
- **Parameters**:
  | Name         | Type   | Purpose                            |
  |--------------|--------|------------------------------------|
  | `self`       | object | The test case instance.              |

## Inner Workings
- The test calls the `create_account` method on an admin instance (`self.admin_instance`) with three parameters: a username, a password, and an email address.
- It asserts that the result of the `create_account` call is `True`, which indicates that the account creation was successful.
- If the account creation is not successful, it raises an assertion error with the message "should have added account and returned success msg".

## Edge Cases & Preconditions
- **Assumptions**:
  - The admin instance (`self.admin_instance`) has a working `create_account` method.
  - The provided username, password, and email are valid and not already in use.
- **Potential Failure Modes**: 
  - If the account creation fails (i.e., the method returns something other than `True`), the test will fail.
- **Error Handling**: This code does not explicitly handle errors; it relies on assertions to catch any unexpected outcomes.

## Result Synopsis
This function asserts that an attempt to create a new user account using valid credentials results in a successful creation, indicated by the method returning `True`.

## Docstring Draft
```python
"""Tests creating a new user account.

Asserts that the `create_account` method of an admin instance successfully creates a new account with the provided username, password, and email.
Raises an assertion error if the account creation fails.

Args:
    self (unittest.TestCase): The test case instance.

Returns:
    None

Raises:
    AssertionError: If the account creation is not successful.
"""
``````

## test_invalid_username_type  
``/Project/unit_tests/test_create_delete.py``  
```def test_invalid_username_type(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid username type"):
            self.admin_instance.create_account(38432489238, "testpass4", "test4@example.com")```  

**Documentation:**
```python## Overview
This code is a unit test for the `create_account` method of an admin instance. It verifies that calling this method with an invalid username type (non-string) raises a `TypeError`.

## Interface
- **Signature**: `def test_invalid_username_type(self)`
- **Parameters**:
  - None

## Inner Workings
1. The test uses the `with self.assertRaises` context manager to ensure that the `create_account` method raises a `TypeError`.
2. It calls `self.admin_instance.create_account(38432489238, "testpass4", "test4@example.com")`, passing an integer as the username.

## Edge Cases & Preconditions
- The test assumes that the `admin_instance` object has a method named `create_account`.
- It expects the method to raise a `TypeError` when provided with a non-string username.
- If the method does not raise an exception or raises a different type of exception, the test will fail.

## Result Synopsis
The code asserts that calling `create_account` with an integer as the username raises a `TypeError`.

## Docstring Draft
```python
"""Test that creating an account with an invalid username type raises a TypeError.

This test checks the behavior of the create_account method when provided with a non-string username.
It is expected to raise a TypeError in such cases.
"""
``````

## setUp  
``/Project/unit_tests/test_create_delete.py``  
```def setUp(self):
        self.admin_instance = Admin()
        self.account1 = User.objects.create(username="testuser1", password="testpass1", email="test1@example.com")
        self.account2 = User.objects.create(username="testuser2", password="testpass2", email="test2@example.com")```  

**Documentation:**
```python## Overview
The `setUp` method initializes the test environment by creating an instance of `Admin` and two instances of `User`.

## Interface
- **Signature**: `def setUp(self)`
- **Parameters**:
  | Name     | Type       | Purpose                         |
  |----------|------------|---------------------------------|
  | `self`   | `unittest.TestCase` | The test case instance. |

## Inner Workings
1. Creates an instance of the `Admin` class and assigns it to `self.admin_instance`.
2. Creates two instances of the `User` model using Django's ORM:
   - The first user has the username "testuser1", password "testpass1", and email "test1@example.com".
   - The second user has the username "testuser2", password "testpass2", and email "test2@example.com".

## Edge Cases & Preconditions
- Assumes that Django's ORM is properly configured and accessible.
- Assumes that the `User` model exists in the database schema.

## Result Synopsis
The method sets up the test environment by creating necessary instances for further testing.

## Docstring Draft
```python
"""Sets up the test environment by creating an instance of Admin and two User instances.

Args:
    self (unittest.TestCase): The test case instance.

Returns:
    None

Raises:
    AssertionError: If Django ORM is not properly configured.
"""
``````

## test_account_exists  
``/Project/unit_tests/test_create_delete.py``  
```def test_account_exists(self):
        self.assertTrue(self.admin_instance.delete_account(self.account1.username), msg='should have returned true since account is in db')```  

**Documentation:**
```python## Overview
- The function `test_account_exists` verifies that the method `delete_account` of `self.admin_instance` correctly deletes an account from a database and returns `True`.

## Interface
- **Signature**: `test_account_exists(self)`
- **Parameters**:
  - `None`: This is a method, not a standalone function.

## Inner Workings
- The method calls `self.admin_instance.delete_account(self.account1.username)` to attempt the deletion of an account.
- It asserts that the result of this call is `True`, indicating that the account was successfully deleted.
- If the deletion fails and does not return `True`, the assertion will raise an `AssertionError`.

## Edge Cases & Preconditions
- **Preconditions**:
  - The account specified by `self.account1.username` must exist in the database before calling `delete_account`.
  - The `admin_instance` must have a method `delete_account` that correctly handles account deletion.
- **Edge Cases**:
  - If the account does not exist, the behavior of `delete_account` is not specified by the code snippet provided. It may raise an exception or return an unexpected value.

## Result Synopsis
- The function asserts that calling `self.admin_instance.delete_account(self.account1.username)` returns `True`, indicating successful deletion.

## Docstring Draft
```python
"""Tests if deleting an existing account returns True.

Args:
    None: This is a method, not a standalone function.

Raises:
    AssertionError: If the delete operation does not return True.
"""
``````

## test_no_account  
``/Project/unit_tests/test_create_delete.py``  
```def test_no_account(self):
        self.assertFalse(self.admin_instance.delete_account('999'), msg='should have returned false since account is not in db')```  

**Documentation:**
```python## Overview
The `test_no_account` function verifies that attempting to delete an account that does not exist in the database results in a `False` return value.

## Interface
- **Signature**: `def test_no_account(self)`
- **Parameters**:
  | Name         | Type   | Purpose                 |
  |--------------|--------|-------------------------|
  | self         | object | Reference to the current instance of the test case |

## Inner Workings
1. The function calls `self.admin_instance.delete_account('999')` with an account ID that is not present in the database.
2. It asserts that the result of this call is `False`, indicating that the account deletion was unsuccessful due to the non-existent account.

## Edge Cases & Preconditions
- **Assumptions**: The method `delete_account` is implemented and accessible via `self.admin_instance`.
- **Potential Failure Modes**: If `delete_account` raises an exception or if it does not handle missing accounts correctly, the test may fail.
- **Error Handling**: The function does not explicitly handle errors; instead, it relies on the assertion to catch any unexpected behavior.

## Result Synopsis
The function asserts that deleting a non-existent account returns `False`.

## Docstring Draft
```python
"""Verifies that attempting to delete a non-existent account results in False.

Args:
    self (object): Reference to the current instance of the test case.

Returns:
    None

Raises:
    AssertionError: If the deletion of a non-existent account does not return False.
"""
``````

## test_invalid_input  
``/Project/unit_tests/test_create_delete.py``  
```def test_invalid_input(self):
        with self.assertRaises(TypeError, msg="should raise exception for invalid input type"):
            self.admin_instance.delete_account(999)```  

**Documentation:**
```python## Overview
This code snippet is a unit test method to verify that the `delete_account` function raises an appropriate exception when provided with invalid input.

## Interface
- **Signature**: `test_invalid_input(self)`
- **Parameters**:
  | Name    | Type   | Purpose                 |
  |---------|--------|-------------------------|
  | self    | object | Reference to the test case instance |

## Inner Workings
- The method uses the `with` statement along with `self.assertRaises(TypeError, msg="should raise exception for invalid input type")` to assert that a `TypeError` is raised when calling `self.admin_instance.delete_account(999)`.
- It passes an integer value (`999`) as an argument to the `delete_account` method, which is expected to trigger the exception.

## Edge Cases & Preconditions
- **Assumptions**: The `delete_account` method should raise a `TypeError` when provided with non-string input.
- **Potential Failure Modes**: If the `delete_account` method does not handle invalid input types correctly, it may either succeed (not raising an exception) or raise a different type of exception.
- **Error-Handling Logic**: The test checks for the correct exception type to ensure proper error handling.

## Result Synopsis
The code confirms that calling `self.admin_instance.delete_account(999)` raises a `TypeError`, as expected, indicating that the function correctly handles invalid input types.

## Docstring Draft
```python
"""Verifies that the delete_account method raises a TypeError when provided with invalid input type.

Args:
    self (unittest.TestCase): Reference to the test case instance.

Raises:
    ValueError: When an unexpected exception is raised during the test.
"""
``````
