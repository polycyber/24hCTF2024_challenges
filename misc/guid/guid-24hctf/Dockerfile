FROM node:20

WORKDIR /app


COPY *.json ./

RUN npm install

WORKDIR /app/src

COPY src/ .

EXPOSE 4200

CMD ["npm", "start"]
