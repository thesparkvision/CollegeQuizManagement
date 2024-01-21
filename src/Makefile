# Define the Python interpreter
include .env

PYTHON = python3

# Set up the virtual environment and install dependencies
setup:
	$(PYTHON) -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

# Create a Docker container for PostgreSQL
create_db_image:
	docker run --rm -d --name postgres -e POSTGRES_USER=$(USER) -e POSTGRES_PASSWORD=$(PASSWORD) -p 5432:5432 postgres
	sleep 3
	docker exec -it postgres psql -U myuser -c 'CREATE DATABASE $(DB_NAME);'
	
# Run Alembic to apply database migrations
update_db:
	alembic upgrade head

# Start the FastAPI server using uvicorn
start_server:
	uvicorn main:app --reload