function validatePIN (pin) {
    // Check if the pin is either 4 or 6 digits and contains only digits
    return /^(\d{4}|\d{6})$/.test(pin);
  }