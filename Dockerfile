FROM tiangolo/uvicorn-gunicorn-fastapi 

RUN pip install pydantic
RUN pip install sqlalchemy