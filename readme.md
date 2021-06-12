[![codecov](https://codecov.io/gh/asherif123/pet-shop/branch/main/graph/badge.svg?token=EKX4AJ04S3)](https://codecov.io/gh/asherif123/pet-shop)

# Pet Shop API using Django & DRF

## Running Steps
- First create a virtual env  
```python3.8 -m venv venv```
- Activate the venv  
```source venv/bin/activate```
- Install the project requirements  
```pip install -r requirements.txt```
- Export your secret key  
```export SECRET_KEY=YOURSECRETKEY```
- Migrate the database  
```python manage.py migrate```
- Run the tests  
```python manage.py test```
- Run the server  
```python manage.py runserver```  
- And finally, import [Pet Shop.postman_collection.json](Pet%20Shop.postman_collection.json) into Postman to try the APIS!