FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -yq nodejs build-essential
RUN npm install -g yarn

COPY . /code/
WORKDIR /code/

RUN pip install pipenv
RUN pipenv install --system

WORKDIR /code/client
RUN yarn
RUN yarn dev

EXPOSE 8000