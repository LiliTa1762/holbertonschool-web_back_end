const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  describe('Sum integers', function() {
    it('should be able to add and return 4', function() {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });
  });

  describe('Sum and round integers', function() {
    it('should be able to round and return 5', function() {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  });

  describe('Sum and round int to 5', function() {
    it('should be able to round and return 5', function() {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });
  });

  describe('Sum and round numbers', function() {
    it('should be able to add, round and return 6', function() {
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
  });
})
