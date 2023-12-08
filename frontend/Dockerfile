
FROM node:14-alpine


WORKDIR /usr/src/app


COPY package*.json ./


RUN npm install


COPY . .


EXPOSE 3000


ENV DOCTORS_SERVICE_URL http://localhost:9090
ENV APPOINTMENTS_SERVICE_URL http://localhost:6060


CMD ["node", "app.js"]
