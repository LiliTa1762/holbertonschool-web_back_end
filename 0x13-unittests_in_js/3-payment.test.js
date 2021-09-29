const sinon = require('sinon');
let { expect } = require('chai');

const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('Using spies', function() {
  it('should have the same result', function() {
    const UtilSpy = sinon.spy(Utils, 'calculateNumber');
    const ConsoleSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20)

    expect(UtilSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(ConsoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;

    UtilSpy.restore();
    ConsoleSpy.restore();
  });
});
