const app = require('./server');
const request = require('supertest');

test('GET / returns correct greeting', async () => {
  const response = await request(app).get('/');
  expect(response.status).toBe(200);
  expect(response.text).toContain('Hello from multi-stage Docker build!');
});

test('GET /info returns correct info', async () => {
  const response = await request(app).get('/info');
  expect(response.status).toBe(200);
  expect(response.body).toHaveProperty('app', 'three-stage-demo');
  expect(response.body).toHaveProperty('stages');
  expect(response.body.stages).toHaveLength(3);
});