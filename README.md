# FastAPI
All about FastAPI, basic setup, code, ML model api

FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints. It's quickly gained popularity due to its speed, ease of use, and a rich set of built-in features.

# Why FastAPI?
FastAPI excels in several areas, making it a compelling choice for API development:

Speed (Performance): FastAPI is incredibly fast, rivaling Node.js and Go. This is primarily due to its foundation on Starlette (for the web parts) and Pydantic (for data validation and serialization), both of which are highly optimized for asynchronous operations.

Fast to Code & Fewer Bugs: It leverages Python's type hints to provide excellent editor support (autocompletion, type checking), which significantly speeds up development and reduces human errors. You write less boilerplate code and spend less time debugging.

Automatic Interactive Documentation: One of its standout features is the automatic generation of interactive API documentation (using OpenAPI, formerly Swagger UI, and ReDoc). This means you get a user-friendly interface to explore and test your API endpoints directly in the browser, without any extra effort.

Data Validation and Serialization: FastAPI uses Pydantic for robust data validation and serialization. You define your data models using standard Python types, and FastAPI automatically validates incoming request data, provides clear error messages for invalid input, and handles the conversion of data between Python types and JSON.

Asynchronous Support: It fully embraces Python's async/await keywords, making it ideal for handling I/O-bound tasks and building highly concurrent and scalable applications (e.g., real-time applications, WebSockets).

Dependency Injection: FastAPI has a powerful and easy-to-use dependency injection system, which promotes modular, testable, and maintainable code. You can easily inject dependencies like database connections, authentication logic, and more.

Standards-Based: It's built on and fully compatible with open standards for APIs like OpenAPI and JSON Schema, which fosters interoperability and allows for automatic client code generation in various languages.

Security Features: FastAPI includes built-in support for security features like OAuth2 and JWT, and automatically validates request data to mitigate common vulnerabilities.

# How FastAPI Works
At its core, FastAPI takes advantage of:

Starlette: A lightweight ASGI (Asynchronous Server Gateway Interface) framework that provides the core web functionalities, including routing, middleware, and WebSockets.

Pydantic: A data validation and settings management library that uses Python type annotations to define data schemas.
When you define an API endpoint in FastAPI, you use Python type hints for function parameters and return values. FastAPI then uses Pydantic to:

Validate incoming request data: It automatically checks if the data received matches the types and structures you've defined.

Convert data: It converts incoming data from the network (e.g., JSON) into Python data types and vice-versa for responses.

Generate documentation: It uses the type information to automatically create the OpenAPI specification, which powers the interactive documentation.

# Environment Setup and Execution Commands:
Install Python 3.12
/Users/binod/Documents/Binod/fastapi-study

(base) Binods-MBP:fastapi-study binod$ python3 -m venv fastapi-demo
(base) Binods-MBP:fastapi-study binod$ source fastapi-demo/bin/activate
(fastapi-demo) (base) Binods-MBP:fastapi-study binod$ pwd

> pip install fastapi 
> pip show fastapi 
> pip install unicorn 
> uvicorn --version
Create main.py
How to run:
>  uvicorn main:app --reload

