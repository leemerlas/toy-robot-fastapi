# toy-robot-fastapi

#### A sample RPC server that accepts REST procedures and returns relevent JSON data

## Local setup
### 1. Create a Python virtual environment
In the root directory of the project, run the following command:

```
python -m venv venv
```

After the virtual environment is created, activate it by running: <br>
- <strong>Windows</strong>

```
.\venv\Scripts\activate
```
- <strong>Linux\macOS</strong>
```
source venv/bin/activate
```

### 2. Install required libraries

After activating the virtual environment, the next step is to install the libraries needed by running:

```
pip install -r requirements.txt
```

### 3. Running the application

Since FastAPI was used, it can be run via two ways:

1. Using the `uvicorn` command

```
uvicorn app.main:app --reload
```

2. Using the `fastapi run` command:

```
# Navigate to the app directory first since that's where main.py is located
cd app
fastapi dev main.py
```

### 4. Running unit tests

To run the unit tests, use the `pytest` command:
```
pytest tests\test_robot.py
```