const express = require("express"); // Import the express module
const fs = require("fs"); // Import the fs module
const path = require("path"); // Import the path module

const app = express(); // Create an express app
const port = 3000; // Set the port

// Handle an HTTP GET request to the '/' endpoint
app.get("/", (req, res) => {
  const filePath = path.join(__dirname, 'index.html');
  res.sendFile(filePath);
});

app.get("/images", (req, res) => {
  fs.readdir("outputs", (err, files) => {
    if (err) {
      // Handle error if the directory cannot be read
      console.log(err);
      res.sendStatus(500);
    } else {
      // Send the list of image file names as a JSON response
      res.json(files);
    }
  });
});

// Handle an HTTP GET request to the '/outputs/*' endpoint
app.get("/outputs/:file", (req, res) => {
  const filePath = path.join(__dirname, 'outputs', req.params.file);
  res.sendFile(filePath);
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
