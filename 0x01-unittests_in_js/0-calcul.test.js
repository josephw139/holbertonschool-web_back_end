const assert = require("assert");
const calculateNumber = require('./0-calcul.js');


describe("calculateNumber", function() {
  it("checks equality - positive", function() {
    assert.equal(calculateNumber(13, 56), 69);
    assert.equal(calculateNumber(12.6, 56.3), 69);
  });

  it("checks equality - negative", function() {
    assert.equal(calculateNumber(-13, -56), -69);
    assert.equal(calculateNumber(-12.6, -56.3), -69);
  });
});