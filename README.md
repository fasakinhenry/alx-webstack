# **JOBSTRAIGHT**

![alx-jobstraight](https://github.com/user-attachments/assets/20f5adb1-dda3-44ed-9323-265261b08cb8)

## **Description**
This web application enables potential clients to connect with professional service providers in various fields. Whether you need a plumber to fix your kitchen sink, a mechanic to service your car, or a dry cleaner to take care of your laundry, our platform makes it easy to find and hire the right professionals—all in one place.

Built using Django, the app offers a seamless platform where users can browse service providers, view their profiles, and request services. Service providers can create profiles, showcase their skills, and accept or decline client requests.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)
- [Contributing](#contributing)
- [Tech-Stack](#tech-stack)
- [Challenges-Faced](#challenges-faced)
- [Lessons-Learned](#lessons-learned)
- [Feedback](#feedback)
- [Authors](#authors)

## Installation
Follow the steps below to install and set up the JobStraight web app on your local machine.

### Pre-requisites
Ensure you have the following installed:

- ```Python``` (version 3.8 or later)

- ```Git```

- ```pip``` (Python package manager)

- ```virtualenv``` (for isolated environments)

### Step 1: Clone the Project Repository
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

## Usage

    1. Clients: Register an account and browse service providers.

    2. Service Providers: Create a profile and offer services.

    3. Search: Use filters to find the right provider for your needs.

    4. Book Services: Send requests and manage bookings.

    5. Messaging: Communicate securely within the platform.

## Features

- User authentication and authorization

- Profile management for clients and providers

- Service listing and booking system

- Search and filter functionality

- Secure in-app messaging

- Admin panel for management

## License

This project is licensed under the [MIT](https://github.com/fasakinhenry/alx-webstack/blob/main/LICENSE) license.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/fasakinhenry/alx-webstack/blob/main/LICENSE)

## Contributing

We welcome contributions! Kindly follow these steps to contribute:

    a. Fork the repository.

    b. Create a new feature branch: git checkout -b feature-name.

    c. Commit your changes: git commit -m 'Add new feature'.

    d. Push to your branch: git push origin feature-name.

    e. Submit a pull request.

For major changes, please open an issue first to discuss what you would like to change.

## Tech-Stack

**Client:** JavaScript, Bootstrap

**Server:** Python, Django

## Challenges-Faced

- Learning Django: We had to learn django quickly using tutorials and django documentations.

- Fixing bugs: Being new to Django, the team faced many errors but solved them through research and pain-staking debugging.

- Time management: We struggled to meet deadlines but improved by setting clear goals and working in smaller tasks.

- Team coordination: The team faced challenges working together but used regular meetings to stay aligned.

## Lessons-Learned

- We learned the basics of Django and how to build web applications with it.

- We improved our understanding of how backend and frontend technologies work together.

- Teamwork and communication are very important when working on a project.

## Feedback

For Feedback or Support, please email us at kennetho.onu@gmail.com.

## Authors

[![Obi](https://img.shields.io/badge/obi-009?style=for-the-badge&logo=ko-fi&logoColor=blue)](https://github.com/obithelight)
[![Henry](https://img.shields.io/badge/henry-500?style=for-the-badge&logo=ko-fi&logoColor=red)](https://github.com/fasakinhenry)
[![Tobijah](https://img.shields.io/badge/tobijah-054?style=for-the-badge&logo=ko-fi&logoColor=yellow)](https://github.com/rallmac)
[![Ayo](https://img.shields.io/badge/odunayo-010?style=for-the-badge&logo=ko-fi&logoColor=green)](https://https://github.com/Stringpappy)
