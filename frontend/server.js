const path = require("path");
const fs = require("fs");

const express = require("express");
const serveStatic = require("serve-static");

const app = express();

//here we are configuring dist to serve app files
app.use("/", serveStatic(path.join(__dirname, "/dist")));

// this * route is to serve project on different page routes except root `/`
app.get(/.*/, function(req, res) {
  res.sendFile(path.join(__dirname, "/dist/index.html"));
});

const port = 8080;
app.listen(port, () => {
  if (process.env.DYNO) {
    console.log("Running on Heroku!");
    fs.openSync("/tmp/app-initialized", "w");
  }
});
console.log(`Server is listening on port: ${port}`);
