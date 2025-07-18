# Flask vs FastAPI
---

## What is Flask?
**Flask** is a lightweight web framework written in Python. 
It helps you create APIs and web applications quickly.

Flask is perfect for:
- Creating REST APIs
- Prototyping
- Building microservices

---

## Installation 
### 1. Create Environment 
```bash
conda create -n flask_env python=3.11 -y
conda activate flask_env
```

### 2. Install Flask
```bash
pip install Flask
```

### 3. Run Flask App
```bash
set FLASK_APP=main.py          
flask run
```

- Runs at: http://127.0.0.1:5000

---

##  Example Flask Code

```python
from flask import Flask, request, jsonify

app = Flask(__name__)
name = None

@app.route('/post', methods=['POST'])
def post_name():
    global name
    name = request.json.get('name')
    return jsonify({"message": f"Saved: {name}"})

@app.route('/get', methods=['GET'])
def get_name():
    return jsonify({"name": name or "No name saved"})

if __name__ == '__main__':
    app.run(debug=True)

    
```

---

## Using Postman
1. Open Postman
2. Select **POST**
3. Enter URL `http://127.0.0.1:5000/post`
4. In **Body → raw → JSON**:
```json
{
  "name": "Bharath"
}
```
5. Click **Send**

Use **GET** for `/users` and just hit Send.

---
# FastAPI

## What is FastAPI?
*pFastAPIpp** is a modern, high-performance Python web framework for building APIs quickly, with automatic data validation and documentation.


FastAPI is perfect for:

- Creating RESTful APIs
- Microservices and production-ready systems
- High-performance async apps

----
## Installation (Ubuntu / Windows using Conda)
### 1. Create Environment
```bash
conda create -n fastapi_env python=3.11 -y
conda activate fastapi_env
```
### 2. Install FastAPI and Uvicorn
```bash
pip install fastapi uvicorn
```
### 3. Run FastAPI App

 ### uvicorn main:app --reload
- Runs at: http://127.0.0.1:8000

---

##  Example Fastapi Code

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model
class Message(BaseModel):
    text: str

# In-memory store
saved_message = ""

# POST method
@app.post("/save")
def save_message(msg: Message):
    global saved_message
    saved_message = msg.text
    return {"message": "Message saved!"}

# GET method
@app.get("/read")
def read_message():
    return {"saved_message": saved_message}

```

---
## APIs, HTTP Methods in flask and fastapi
---
### What is an API? 
API stands for Application Programming Interface. 
It lets two software components talk to each other.

-Client (Frontend, Mobile App) → makes request
-Server (Flask API) → returns response in JSON format
### What is a Header and a Body in HTTP?
### Headers
- Key-value pairs sent with HTTP request or response
- Examples:
 - Content-Type: application/json
 - Authorization: Bearer <token>
 - Accept-Language: en
-Used to pass metadata and control the behavior of the request/response.

----
## Body
-Actual payload/data sent with POST or PUT requests

-Common formats: JSON, form-data
```bash
{
  "username": "admin",
  "password": "1234"
}
```
## URL Structure

---
```bash
https://api.example.com/v1/users?id=123
|-----| |-------------| |------|
 Scheme     Host         Path
                        └── Resource (Endpoint)

```
---     

### Parts of a URL

- Scheme: http / https
- Host: Domain or IP
- Path: API route (e.g. /v1/users)
- Query String: After ?, key-value pairs (e.g. ?id=123)


---
## HTTP GET vs POST
```bash

Feature                 GET	                              POST
Purpose	                Retrieve data	                    Submit or send data
Params	                Sent via URL query	              Sent via request body
Body	                 Not supported	JSON / form-data   supported
Example	                /users?id=123	                    /login with { "user": "x" }
```

---
## flask vs fastapi
---
### Performance

flask   :Good for medium-sized applications but slow for complex applications.

fastapi :Faster and better than Flask.

---
### Use Case

flask   :Web applications

fastapi :APIs

---
### HTTP Methods

flask   :@app.route(“/”, methods = [“GET”])
@app.route(“/”, methods = [“POST”])

fastapi : @app.get(“/”)
@app.post(“/”)

---

### Data Validation

flask    :No validation support.

fastaapi :In-built data validation.

---

### Error Message Display

flask   :Displayed in HTML format

fastapi :Displayed in JSON format


# GitHub Markdown Cheatsheet

## Headings
# H1
## H2
### H3
#### H4
##### H5
###### H6

## Bold and Italics
**This text is bold**  
*This text is italic*  
***This text is bold and italic***

## Lists

### Unordered List
- Item One
- Item Two
  - Subitem A
  - Subitem B

### Ordered List
1. First Item
2. Second Item
3. Third Item

## Links
[GitHub Homepage](https://github.com)

## Images
![Sample Image](https://via.placeholder.com/150)

## Code Examples

### Inline Code
Here is some `inline code` in a sentence.

### Code Block
```python
def hello_world():
    print("Hello, World!")
```

## Blockquote
> This is a blockquote for highlighting important text.

## Horizontal Line

---

## Tables

| Syntax | Description |
|---------|-------------|
| Header | Title |
| Paragraph | Text |

## Task Lists

- [ ] Task not completed
- [x] Task completed

## Strikethrough

~~This text is struck through~~

## tabels

Feature                 GET	                              POST
Purpose	                Retrieve data	                    Submit or send data
Params	                Sent via URL query	              Sent via request body
Body	                 Not supported	JSON / form-data   supported
Example	                /users?id=123	                    /login with { "user": "x" }



