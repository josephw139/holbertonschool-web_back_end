const express = require('express');

const app = express();

app.listen(7865);

app.on('listening', function () {
  console.log('API available on localhost port 7865');
});

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

module.exports = app;
