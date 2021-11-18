FROM python:3.7

# python setup
RUN python3 -m pip install --upgrade pip
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /cognite/app/
WORKDIR /cognite/app/
RUN poetry install

EXPOSE 4180
CMD poetry run python3 -m src.app
