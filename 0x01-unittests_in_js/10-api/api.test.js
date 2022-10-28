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
      expect(body).to.equal('Payment methods for cart 1');
      done();
    })
  });

  it('app test - GET /cart/id - bad id', (done) => {
    request('http://localhost:7865/cart/no', (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('app test - GET /available_payments', (done) => {
    request('http://localhost:7865/available_payments', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal({"payment_methods":{"credit_cards":true,"paypal":false}})
      done();
    });
  });

  it('app test - POST /login', (done) => {
    request({method: 'POST', url: 'http://localhost:7865/login',
        json: { userName: 'Betty' }
      }, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });
});
