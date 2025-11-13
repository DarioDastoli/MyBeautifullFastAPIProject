# F1Bot Project

## Overview
F1Bot is a FastAPI application designed for user authentication and management. It provides a set of APIs for user login, token generation, and role management, allowing for secure access to resources based on user roles.
During the development of this project, my main objective was to explore and implement FastAPI’s functionalities. For simplicity, some files include more content than necessary and could be refactored to manage, for instance, configurations in a more structured manner.

## Project Structure
```
F1Bot
├── app
│   ├── routers
│   │   ├── login.py          # User authentication and management routes
│   │   └── README.md         # Documentation for router functionalities
│   ├── db.py                 # Database connection and session management
│   ├── models.py             # Data models for the application
│   ├── schemas.py            # Pydantic schemas for data validation
│   └── main.py               # Entry point of the application
└── README.md                 # Overall documentation for the F1Bot project
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd F1Bot
   ```

2. **Install dependencies**:
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the FastAPI application using:
   ```
   uvicorn app.main:app --reload
   ```

## Usage
- Access the API documentation at `http://127.0.0.1:8000/docs` to explore the available endpoints and their functionalities.
- The main functionalities include:
  - User registration and management
  - User login and token generation
  - Role-based access control
