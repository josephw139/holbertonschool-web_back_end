const utils = require('./utils');
const chai = require("chai");
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');

const expect = chai.expect;

describe('sendPaymentRequestToApi', () => {
  let spyCheck;
  beforeEach(() => {
    spyCheck = sinon.spy(console, 'log');
  });
  afterEach(() => {
    spyCheck.restore();
  })

  it("checks sendPayment with a stub, spy, hook", function() {
    sendPaymentRequestToApi(100, 20);
    expect(spyCheck.calledWith('The total is: 120')).to.be.true;
    expect(spyCheck.calledOnce).to.be.true;
  });

  it("checks sendPayment with a stub, spy, hook", function() {
    sendPaymentRequestToApi(10, 10);
    expect(spyCheck.calledWith('The total is: 20')).to.be.true;
    expect(spyCheck.calledOnce).to.be.true;
  });
})