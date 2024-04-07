FROM node:20

WORKDIR /srv

COPY package*.json ./

RUN npm install

WORKDIR /srv/src

COPY src/ .

EXPOSE 3000

WORKDIR /srv/dist

COPY dist/ .

WORKDIR /srv

CMD ["node", "/srv/dist/app.js"]

