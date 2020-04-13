FROM node:lts-alpine

WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./
# install project dependencies
RUN npm install
# copy project files and folders to the current working directory
COPY src/ ./src
COPY public/ ./public
COPY server.js vue.config.js babel.config.js ./

# Setup environments
ARG VUE_APP_API_URL
ENV VUE_APP_API_URL $VUE_APP_API_URL

# build app for production with minification
RUN npm run build

# Start server
CMD npm run start
