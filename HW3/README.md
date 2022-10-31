# Group Members
---
* Nick Terrell | terrelln19@students.ecu.edu
* Cameron Sabiston | sabistonc20@students.ecu.edu
---
## Quick Start
### Local Test Setup
Clone the repo and *CD* to the repo location for *HW3* then install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 main.py
```

Open your web browser and navigate to:
```
127.0.0.1:5000/api/update_basket_a
```
You should see a prompt that says "Success"

Next navigate to:
```
127.0.0.1:5000/api/unique
```
This should return a table which includes all of the unique fruits.
