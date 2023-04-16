### GOBIZNIZ THE BUZZ

## Setup ENV
1. Run 
```
virtualenv env
```
2. Install PIP Package
```
pip install -r requirements.txt
```

## Alembic Command
1. Initialize
```
alembic init alembic
```
2. auto write migration base on changes
```
alembic revision --autogenerate -m "Your migration message"
```
manual write migration
```
alembic revision -m "Your migration message" 
```
3. migrate the file
```
alembic upgrade head
```
