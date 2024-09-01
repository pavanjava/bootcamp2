FROM python:3.10-bookworm

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./.env /code/.env
COPY ./app /code/app
COPY ./core /code/core

CMD ["fastapi", "run", "app/main.py", "--port", "8002"]