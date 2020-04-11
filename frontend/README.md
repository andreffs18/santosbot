# Frontend App

VueJS app that serves a "slack-alike" interface to showcase "Gustavo Santos" bot functionality.

## Install 

This project has a `Dockerfile` which allows you to run this with [docker](https://docs.docker.com/get-docker/):

```shell script
# Build and run project, on port 8080
~/santosbot/frontend $ docker build --build-arg VUE_APP_API_URL=http://localhost:8888 -t frontend:latest .
~/santosbot/frontend $ docker run --rm -it -v $(PWD):/app -v /app/node_modules -p 8080:8080 frontend:latest 
```

## Usage

This Vue App has the 3 commands that come with the default settings, + one more command to serve this app using an simple [express.js](https://expressjs.com/) server.

- `npm run serve`: for development use only, compiles and hot-reloads are enabled.
- `npm run dist`: build project on **/dist/** folder all minified static files ready to deploy.
- `npm run lint`: runs eslint (pretty plugin) on all vue files and fixes accordingly.
- `npm run start`: runs express.js server which used all static file in **/dist/** folder.


### Environment Variables

The only variable that we need to setup to make the "Slack alike" app work is the `VUE_APP_API_URL`. 
This one is configured when we build the docker image and is passed as a build argument (```--build-arg```).

This variable is used to request quotes on the Backend API, for that you must have it running on a separate shell. 


### Project Structure

All app components can be found on **/frontend/src/components** directory and its organized the following way:

![](https://i.imgur.com/UJPRbU0.png)
