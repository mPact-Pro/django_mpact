# Development stage
FROM python:3.10-slim as development

# Install development dependencies (e.g., debuggers, linters)
RUN pip install --upgrade pip
RUN pip install --no-cache-dir debugpy

# Copy and install dependencies
COPY requirements.txt /usr/src/app/
# Copy the whole project for development purposes
COPY . /usr/src/app/

ARG SECRET_KEY
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT

# Set up the working directory
WORKDIR /usr/src/app

RUN pip install -r requirements.txt
# Collect static files
RUN python manage.py collectstatic --no-input

# Optionally, clean up any unnecessary files to reduce image size
RUN find . -name "*.pyc" -exec rm -f {} +
RUN find . -type d -name "__pycache__" -exec rm -rf {} +

CMD ["python", "manage.py", "runserver"]