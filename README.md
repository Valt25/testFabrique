# Test for Fabrique
## How to run
`docker build -t testFabrique .`

`docker run -p 8000:8000 --name testFabrique testFabrique`

To add superuser:

`docker exec -it testFabrique bash`

`python manage.py createsuperuser --username <username>

## TODO

Part about getting list of passed reviews was left undone.

## Possibilities

Every param pass as a first level property of JSON object. E.g. params of (propertyA, propertyB) means api expect `{"propertyA":"value", "propertyB": "value"}`

Question type, gets one of the possible values(text, select, checkbox)

| Title                  | UrlPath          | Method | Params                                   |
|------------------------|------------------|--------|------------------------------------------|
| Login                  | /login/          | POST   | username, password                       |
| Create review          | /reviews/        | POST   | title, description, start_date, end_date |
| Update Review          | /reviews/*id*/   | PUT    | title, description, start_date           |
| Delete Review          | /reviews/*id*/   | DElETE |                                          |
| Create Question        | /questions/      | POST   | review_id, text, type                    |
| Update Question        | /questions/*id*/ | PUT    | text, type                               |
| Delete Question        | /questions/*id*/ | DELETE |                                          |
| List of active Reviews | /reviews/active/ | GET    |                                          |
| Create Answer          | /reviews/answer/ | POST   | answer_text, question_id                 |
|                        |                  |        |                                          |