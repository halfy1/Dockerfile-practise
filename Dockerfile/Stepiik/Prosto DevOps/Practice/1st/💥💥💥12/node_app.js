const express = require("express");
const app = express();
const port = process.env.PORT || 8080;

app.get("/", (req, res) => {
  res.send("Hello from Node.js!");
});

app.listen(port, () => {
  console.log(`Node app listening on port ${port}`);
});