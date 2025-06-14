This a project to create a simple web application APIs using Python.
# Divain
This project is a simple web application that provides APIs for managing a Stock of items.
It is built using Python and FASTAPI, and it uses Postgres as the database.
# Features
- this project provides APIs for managing a Stock of items.
- It allows you to get full stock of items.
- It allows you to update an items stock movement and stores the history
- It allows you to get the history of an item stock movement.

# packages needed
- fastapi
- uvicorn
- psycopg2
- sqlalchemy
- pydantic

## 🚀 Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: psycopg2 (or SQLAlchemy if using ORM)
- **Testing**: TestClient

Sample Endpoints 
    Method	    Endpoint	                Description
-   GET	    /stocks	                        List all stock items
-   POST	/stocks_movement	            Update stock quantity
-   GET	/stocks_movement_history	    Get stock movement history

# Installation      
1. Clone the repository:
   ```bash
   git clone
    