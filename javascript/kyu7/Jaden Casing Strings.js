String.prototype.toJadenCase = function () {
    return this.split(' ').map(word => {
      return word.charAt(0).toUpperCase() + word.slice(1);
    }).join(' ');
  };
  
  // Example usage:
  const str = "How can mirrors be real if our eyes aren't real";
  console.log(str.toJadenCase()); // Output: "How Can Mirrors Be Real If Our Eyes Aren't Real"