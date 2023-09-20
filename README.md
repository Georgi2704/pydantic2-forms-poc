# pydantic2-forms-poc

This project runs on Python 3.10

1.Install the required packages
```bash
 pip install -r requirements.txt
```

2. Run the webserver
```bash
 ./start.sh dev
```

Docs are found on 
http://127.0.0.1:8080/v1/docs/

Test form on
http://localhost:8080/v1/forms/minimal_example_form


Test 510 FormNotCompleteError:
```json
[
  {
    "first_name": "Georgi",
    "last_name": "Manev",
    "text": "Hallo allemaal",
    "choice": "Option A",
    "email": "abc@xxx.com",
    "maybe_a_number": 2
  },
]
```


Test 201 Created:
```json
[
  {
    "first_name": "Georgi",
    "last_name": "Manev",
    "text": "Hallo allemaal",
    "choice": "Option A",
    "email": "abc@xxx.com",
    "maybe_a_number": 2
  },
  {
    "age": 33
  }
]
```