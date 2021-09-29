const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  describe('Sum integers', function() {
    it('should be able to add and return 4', function() {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });
  });
});

describe('calculate sum', function() {
  describe('Sum integers', function() {
    it('should be able to round and return 5', function() {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  });
});

describe('sum numbers', function() {
  describe('Sum integers', function() {
    it('should be able to round and return 5', function() {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });
  });
});

describe('round numbers', function() {
  describe('Sum integers', function() {
    it('should be able to add, round and return 6', function() {
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
  });
});
