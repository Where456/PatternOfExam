# A simple REST-based Flask application to work with the database

This tutorial provides a description and instructions for using a simple REST application on Flask that provides database functionality. The application allows you to perform read, add, update and delete operations on data.

## Routes and domains
### 1. Getting all data
Method: GET
URL: http://localhost:10001/notes

Description: Gets all data from the database.

Example response:
![img.png](static/img.png)
---
### 2. Adding new data
Method: POST
URL: http://localhost:10001/add

Description: Adds new data to the database.

Request body: JSON object with a text field to specify the title and content of the note.

Example request:
![img_2.png](static/img_2.png)
---
### 3. Changing data
Method: PUT
URL: http://localhost:10001/notes/{id}

Description: Changes the data in the database for the specified id.

Request body: JSON object with title and content fields to specify the new title and content of the note.

Example request:
![img_3.png](static/img_3.png)
---
### 4. Deleting data
Method: DELETE
URL: http://localhost:10001/delete/{id}

Description: Deletes data from the database for the specified id.

Example request:
![img_5.png](static/img_5.png)