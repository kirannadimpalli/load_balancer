# Load Balancer

## Overview
This project demonstrates how to build an HTTP load balancer using Flask.

## Setup

### Create and Activate Virtual Environment
To create a virtual environment and activate it:

```sh
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate # On Unix or MacOS
```

### Build Docker Image

```sh
docker build -t server .
docker-compose up -d
docker-compose down
```
### Running Tests

```sh
python -m pytest test_files
make run_tests
```

