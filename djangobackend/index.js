const functions = require("firebase-functions");
const { exec } = require("child_process");

exports.djangoBackend = functions.https.onRequest((req, res) => {
  exec("python manage.py runserver 0.0.0.0:8000", (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      res.status(500).send(`Server error: ${error}`);
      return;
    }
    res.status(200).send(stdout);
  });
});
