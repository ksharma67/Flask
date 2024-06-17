# Deploying a Dockerized Flask Application

This repository contains a Dockerized Flask application that uses an ARM-compatible base image for Python.

## Prerequisites

Before you begin, ensure you have the following installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)

## Getting Started

### Clone the Repository

First, clone this repository to your local machine:
```bash
git clone https://github.com/ksharma67/Flask
cd flask_app
```

### Build the Docker Image

To build the Docker image for the Flask application, run the following command:
```bash
docker build -t flask-app .
```

### Run the Docker Container

Once the Docker image is built, you can run a Docker container with the following command:
```bash
docker run -p 8080:8080 flask-app
```

This command maps port 8080 of the Docker container to port 8080 of your local machine. You can replace 8080:8080 with any other port if needed.

### Accessing the Application
After running the container, you can access the Flask application at http://localhost:8080 in your web browser.
