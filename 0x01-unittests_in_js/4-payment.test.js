const utils = require('./utils');
const chai = require("chai");
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');

const expect = chai.expect;

describe('sendPaymentRequestToApi', () => {
  it("checks sendPayment with a stub & spy", function() {
    const stubCheck = sinon.stub(utils, 'calculateNumber').returns(10);
    const spyCheck = sinon.spy(console, 'log');
    sendPaymentRequestToApi(5, 5);
    expect(spyCheck.calledWith('The total is: 10')).to.be.true;
    spyCheck.restore();
    stubCheck.restore();
  });
})