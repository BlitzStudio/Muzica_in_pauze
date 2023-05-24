FROM node:latest

WORKDIR app

COPY package*.json ./

RUN npm install

ENV HOST=0.0.0.0
ENV PORT=8000
EXPOSE 8000

COPY . .

CMD [ "node","index.js" ]
