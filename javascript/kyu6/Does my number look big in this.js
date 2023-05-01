function narcissistic(value) {
    const digits = value.toString().split('');
    const n = digits.length;
    const sum = digits.reduce((acc, digit) => acc + Math.pow(parseInt(digit), n), 0);
    return sum === value;
  }