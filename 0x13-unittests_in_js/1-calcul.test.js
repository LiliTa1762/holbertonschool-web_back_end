const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  describe('type of math, return a round integer', function() {
    it('should be able to add and return 6', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
  });
});

describe('calculateNumber', function() {
  describe('Subtract integers', function() {
    it('should be able to subtract and return -4', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
  });
});

describe('calculateNumber', function() {
  describe('Divide integers', function() {
    it('should be able to divide and return 0.2', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
  });
});

describe('calculateNumber', function() {
  describe('Error', function() {
    it('should be able to divide and return Error', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
  });
});
