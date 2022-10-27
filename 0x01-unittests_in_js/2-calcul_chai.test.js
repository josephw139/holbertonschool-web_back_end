const assert = require("assert");
const calculateNumber = require('./2-calcul_chai.js');
const chai = require("chai");

const expect = chai.expect;

describe("calculateNumber", function() {
  it("checks add", function() {
    expect(calculateNumber('SUM', 13, 56)).to.equal(69);
    expect(calculateNumber('SUM', 12.6, 56.3)).to.equal(69);
  });

  it("checks subtract", function() {
    expect(calculateNumber('SUBTRACT', -13, -56)).to.equal(43);
    expect(calculateNumber('SUBTRACT', -12.6, -56.3)).to.equal(43);
  });

  it("checks divide", function() {
    expect(calculateNumber('DIVIDE', -10, 2)).to.equal(-5);
    expect(calculateNumber('DIVIDE', -9.7, 2.1)).to.equal(-5);
    expect(calculateNumber('DIVIDE', -9.7, 0)).to.equal('Error');
  });
});