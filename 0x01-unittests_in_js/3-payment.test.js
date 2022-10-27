const utils = require('./utils');
const chai = require("chai");
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');

const expect = chai.expect;

describe('sendPaymentRequestToApi', () => {
  it("checks sendPayment", function() {
    const spyCheck = sinon.spy(utils, "calculateNumber");
    sendPaymentRequestToApi(5, 5);
    expect(spyCheck.calledWith('SUM', 5, 5)).to.be.true;
    spyCheck.restore();
  });
})