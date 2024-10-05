# FROM python:3.12-slim-buster

# RUN apt update -y && apt install awscli -y
# WORKDIR /app

# COPY ./app
# RUN pip install -r requirements.txt

# CMD ["python3", "main.py"]

# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set environment variables
ENV FLASK_APP=flask_app/main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Expose port 5000 for the Flask app to run on
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run"]

# For Streamlit (optional)
# CMD ["streamlit", "run", "src/webapp/streamlit_app.py", "--server.port=8501", "--server.enableCORS=false"]
