function calculateNumber(type, a, b) {
  if (type === 'SUM') {
    roundA = Math.round(a);
    roundB = Math.round(b);
  
    return roundA + roundB;
  }

  if (type === 'SUBTRACT') {
    roundA = Math.round(a);
    roundB = Math.round(b);
  
    return roundA - roundB;
  }

  if (type === 'DIVIDE') {
    roundA = Math.round(a);
    roundB = Math.round(b);

    if (roundB === 0 ) {
      return ("Error");
    }
    else {
      return roundA / roundB;
    }
  }
}
module.exports = calculateNumber;
