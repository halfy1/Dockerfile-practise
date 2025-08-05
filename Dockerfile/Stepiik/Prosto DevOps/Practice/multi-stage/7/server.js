const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Hello from multi-stage Docker build!');
});

app.get('/info', (req, res) => {
  res.json({
    app: 'three-stage-demo',
    stages: ['deps', 'test', 'production'],
    environment: process.env.NODE_ENV || 'development'
  });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app; // для тестов