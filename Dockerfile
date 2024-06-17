# Use an ARM-compatible base image for Python
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies
RUN apt-get update

# Copy and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables
ENV PORT 8080
ENV HOST 0.0.0.0

# Specify the command to run your application
CMD ["python", "app.py"]