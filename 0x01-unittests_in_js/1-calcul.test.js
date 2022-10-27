const assert = require("assert");
const calculateNumber = require('./1-calcul.js');


describe("calculateNumber", function() {
  it("checks add", function() {
    assert.equal(calculateNumber('SUM', 13, 56), 69);
    assert.equal(calculateNumber('SUM', 12.6, 56.3), 69);
  });

  it("checks subtract", function() {
    assert.equal(calculateNumber('SUBTRACT', -13, -56), 43);
    assert.equal(calculateNumber('SUBTRACT', -12.6, -56.3), 43);
  });

  it("checks divide", function() {
    assert.equal(calculateNumber('DIVIDE', -10, 2), -5);
    assert.equal(calculateNumber('DIVIDE', -9.7, 2.1), -5);
    assert.equal(calculateNumber('DIVIDE', -9.7, 0), 'Error');
  });
});