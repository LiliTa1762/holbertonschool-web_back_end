const chai = require('chai');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  describe('type of math, return a round integer', function() {
    it('should be able to add and return 7', function() {
      chai.expect(calculateNumber('SUM', 2, 4)).to.equal(6);
    });
  });
});

describe('calculateNumber', function() {
  describe('Subtract integers', function() {
    it('should be able to subtract and return -4', function() {
      chai.expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
  });
});

describe('calculateNumber', function() {
  describe('Divide integers', function() {
    it('should be able to divide and return 0.2', function() {
      chai.expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });
  });
});

describe('calculateNumber', function() {
  describe('Error', function() {
    it('should be able to divide and return Error', function() {
      chai.expect(calculateNumber('DIVIDE', 3.4, 0)).to.equal('Error');
    });
  });
});
