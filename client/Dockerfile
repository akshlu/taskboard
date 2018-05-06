FROM node:9.11.1-alpine

RUN npm install -g yarn

RUN mkdir /code

ADD package.json yarn.lock /code/
RUN yarn
ADD . /code/
WORKDIR /code/client