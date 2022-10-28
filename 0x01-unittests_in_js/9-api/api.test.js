const { expect } = require('chai');
const request = require('request');

describe('app', () => {
  it('app test - GET /', (done) => {
    request('http://localhost:7865/', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('app test - GET /cart/id', (done) => {
    request('http://localhost:7865/cart/1', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    })
  });

  it('app test - GET /cart/id - bad id', (done) => {
    request('http://localhost:7865/cart/no', (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    })
  })
});
