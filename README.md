# simple-rest-fastapi
SIMPLE REST API

## Description

Base FastAPI project for applying general RestAPI Application cases.

## Installation

1- clone the repo to your working directory

```bash
git clone https://github.com/naderelhadedy/simple-rest-fastapi.git
```

2- go to the project root directory

```bash
cd simple-rest-fastapi
```

3- create new environment

```bash
python -m venv venv
```

4- activate environment

```bash
.\venv\Scripts\activate
```

> this command is compatible with windows only.

5- install project dependencies

```bash
pip install -r requirements.txt
```


## Setup

1- start project services

```bash
docker-compose up
```

2- start the server

```bash
uvicorn app.main:app --reload
```

3- go to swagger `http://localhost:8000/docs` to try any endpoint

