function calculateNumber(type, a, b) {
  roundA = Math.round(a);
  roundB = Math.round(b);

  if (type === 'SUM') {
    return roundA + roundB;
  }

  if (type === 'SUBTRACT') {  
    return roundA - roundB;
  }

  if (type === 'DIVIDE') {
    if (roundB === 0 ) {
      return ("Error");
    }
    else {
      return roundA / roundB;
    }
  }
}
module.exports = calculateNumber;
