FROM node:14

WORKDIR /app

COPY server.js .

COPY package.json .

RUN npm ci --only=production

EXPOSE 3000

CMD ["node","server.js"]
