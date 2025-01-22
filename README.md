# **JobStraight**
JobStraight is a web application that connects clients with service providers, making it easier to find and hire skilled professionals.

## **Description**
This web application enables potential clients to connect with professional service providers in various fields. Whether you need a plumber to fix your kitchen sink, a mechanic to service your car, or a dry cleaner to take care of your laundry, our platform makes it easy to find and hire the right professionals—all in one place.

Built using Django, the app offers a seamless platform where users can browse service providers, view their profiles, and request services. Service providers can create profiles, showcase their skills, and accept or decline client requests.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)
- [Contributing](#contributing)

## Installation
Follow the steps below to install and set up the JobStraight web app on your local machine.

### Pre-requisites
Ensure you have the following installed:

- ```Python``` (version 3.8 or later)

- ```Git```

- ```pip``` (Python package manager)

- ```virtualenv``` (for isolated environments)

### Step 1: Clone the Repository
```bash
    git clone https://github.com/fasakinhenry/alx-webstack.git
```

Change into the project directory:
```
    cd alx-webstack
```

### Step 2: Create and Activate a Virtual Environment
It's a good practice to install Django inside a virtual environment to isolate dependencies.

1.  Create a virtual environment
```bash
    python3 -m venv myenv
```
2.  Activate the virtual environment
-   Linux/macOS:
```bash
    source myenv/bin/activate
```
-   Windows:
```bash
    myenv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
    pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a .env file in the project's root directory and add the required variables:
```bash
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=sqlite:///db.sqlite3
```

### Step 5: Apply Database Migrations
```bash
    python3 manage.py migrate
```

### Step 6: Create a Superuser
```bash
    python3 manage.py createsuperuser
```

### Step 7: Collect Static Files
```bash
    python3 manage.py collectstatic --noinput
```

### Step 8: Run the Development Server
```bash
    python3 manage.py runserver
```
The project will be accessible at ```http://127.0.0.1:8000/```

### Step 9: Deactivate Virtual Environment
```bash
    deactivate
```
