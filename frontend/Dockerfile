# build stage
FROM node:lts-alpine as build-stage
# make the 'app' folder the current working directory
WORKDIR /app
# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./
# install project dependencies
RUN npm install
# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .
# build app for production with minification
# RUN npm run build

# install simple http server for serving static content
# RUN npm install -g http-server
# make the 'app' folder the current working directory
EXPOSE 8080
CMD ["npm", "run", "serve"]
# CMD [ "http-server", "dist" ]

# production stage
#FROM nginx:stable-alpine as production-stage
#COPY --from=build-stage /app/dist /usr/share/nginx/html
#EXPOSE 8080
#CMD ["nginx", "-g", "daemon off;"]