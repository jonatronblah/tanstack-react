FROM node:20.14.0-bookworm as build

RUN npm update -g npm

RUN npm update -g yarn

WORKDIR /usr/src/app

COPY app-client/package.json app-client/yarn.lock ./
RUN yarn install

FROM build as dev

CMD yarn dev --host

FROM build as prod

CMD yarn build