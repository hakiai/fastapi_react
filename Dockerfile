FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y git

COPY ./backend /backend
COPY ./frontend/build /frontend/build
WORKDIR /backend

RUN pip install --upgrade pip \
    && pip install pipenv \
    && pipenv sync

ENV PORT=8000

CMD ["pipenv", "run", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0"]
