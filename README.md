# TODOs REST API
This is a TODOs list application using a Django REST Framework application. 

## Getting Started
To use/run for this application API, you will need to have the Python3 and Django framework installed on your mechine. You may cloned this project and navigate to the project directory and run the following command to install the required packages: 

```python
pip install -r requirements.txt
```

Next, run the following command to start the development server: 

```python
python manage.py runserver
```

And now you can make requests to the API via **`http//localhost:8000'**.
<br /><br />

## API Endpoints
There will be **CRUD** endpoints available: 
<br /><br />

### Get '/todos/'
Get a list of all the TODOs list items. 

Response body: 
```json
{
    "data": [
        {
            "id": 1,
            "name": "Django exercise",
            "description": "Coming soon  exam for django",
            "due_date": "2023-03-16T18:00:00Z",
            "status": "done",
            "priority": "yes",
            "category": "WORK"
        },
        {
            "id": 2,
            "name": "Grocery Shopping",
            "description": "To buy vege, meat & rice",
            "due_date": "2023-03-03T18:00:00Z",
            "status": "todo",
            "priority": "yes",
            "category": "SHOPPING"
        }
    ],
        "message": "POST to /todos with 'name', 'description', 'due_date', 'status'(todo/in_progress/done), 'priority'(yes/no), 'category'(WORK/PERSONAL/SHOPPING/OTHER)."
}
```
For the Get query, it also support **Sort** and **Filter** features.
<br /><br />

### Filtering and Sorting
You can filter the TODOs list items using the following parameters:

- **`'status'`**: Filter by status, possible values are **`'todo'`**, **`'in_progress'`**, and **`'done'`**.
- **`'category'`**: Filter by category, possible values are **`'WORK'`**, **`'PERSONAL'`**, **`'SHOPPING'`**, and **`'OTHER'`**.
- **`'priority'`**: Filter by priority, possible values are **`'yes'`** and **`'no'`**.
- **`'name'`**: Filter by name.
- **`'due_date_before'`**: Filter by due date before a specified date (YYYY-MM-DD).
- **`'due_date_after'`**: Filter by due date after a specified date (YYYY-MM-DD).
- **`'Example filter'`**: ?status=todo&category=WORK&sort_by=due_date

You can sort the TODOs list items using the **`'sort_by'`** parameter. You can sort by one or more fields. Prefix a field with '-' to sort in descending order.

Example sort: **`'?sort_by=name,-priority'`**
<br /><br />

### Post '/todos/'

Create a new TODO item using below request body api format. 

Request body:

```json
{
    "name": "string",
    "description": "string",
    "due_date": "YYYY-MM-DD",
    "status": "todo|in_progress|done",
    "priority": "yes|no",
    "category": "WORK|PERSONAL|SHOPPING|OTHER"
}
```
<br /><br />
### GET /todos/:id

Get a single Todo item with the specified **`id`**.
Reponse body: 
```json
{
    "data": [
        {
            "id": 2,
            "name": "Grocery Shopping",
            "description": "To buy vege, meat & rice",
            "due_date": "2023-03-03T18:00:00Z",
            "status": "todo",
            "priority": "yes",
            "category": "SHOPPING"
        }
    ],
    "message": "POST to /todos with 'name', 'description', 'due_date', 'status'(todo/in_progress/done), 'priority'(yes/no), 'category'(WORK/PERSONAL/SHOPPING/OTHER)."
}
```
<br /><br />
### PUT /todos/:id

Update a single Todo item with the specified **`id`** & allow fields to update the **`'name'`**, **`'description'`**, **`'due_date'`**, **`'status'`**, **`'priority'`**, and **`'category'`**.
Request body: 
``` json
{
  "name": "Updated Todo"
}
```

Response body: 
```json
        {
            "id": 2,
            "name": "Updated Todo",
            "description": "To buy vege, meat & rice",
            "due_date": "2023-03-03T18:00:00Z",
            "status": "todo",
            "priority": "yes",
            "category": "SHOPPING"
        }
```

<br /><br />
### DELETE /todos/:id

Delete a single Todo item with the specified **`id`**. No request body needed for **`DELETE`** request.

<br /><br />
## Authentication 

In this TODOs Rest application project, I have also implemented the authentication. This API requires Token authentication. To authenticate, include an **`'Authorization'`** header with the value **`'Token <your_token>'`**.

To get an authentication token, send a POST request to the **`'/api-token-auth/'`** URL with your username and password in the request body:

```bash
POST /api-token-auth/
{
"username": "your_username",
"password": "your_password"
}
```
I have created a sample superuser at this application, so you may use the sample super user to input the "username" and "password"
```json
"username": "admin"
"password": "admin"
```

The server will respond with a JSON object containing the authentication token:
```bash
{
"token": "your_token"
}
```
<br /><br />
## Testing 

To run tests for the Todo app, navigate to the root directory of the project in your terminal and run the following command:
```bash
    python manage.py test
```

This will run all the tests in the **'tests.py'** file located in the todo app directory.

Currently, there is only one test case included, **'TodoModelTestCase'**, which tests the Todo model's properties such as name, description, due date, status, priority, and category. You can add more test cases as needed to ensure the functionality of the app.

If all tests pass, you should see a message similar to the following:

```bash
Ran 1 test in 0.001s

OK
```