const chai = require("chai");
const sinon = require('sinon');
const getPaymentTokenFromAPI = require('./6-payment_token');

const expect = chai.expect;

describe('payment_token async test', () => {
  it("should return True", (done) => {
    getPaymentTokenFromAPI(true).then((res) => {
      expect(res.data).to.equal('Successful response from the API');
      done();
    });
  });
});
