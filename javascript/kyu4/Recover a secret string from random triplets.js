var recoverSecret = function(triplets) {
  // create a map of letters and their dependencies
  var dependencies = {};
  for (var i = 0; i < triplets.length; i++) {
    var triplet = triplets[i];
    for (var j = 0; j < 3; j++) {
      var letter = triplet[j];
      if (!dependencies[letter]) {
        dependencies[letter] = new Set();
      }
      for (var k = j + 1; k < 3; k++) {
        dependencies[letter].add(triplet[k]);
      }
    }
  }
  
  // use a modified version of Kahn's algorithm to determine the order of letters
  var incomingEdges = {};
  for (var letter in dependencies) {
    incomingEdges[letter] = 0;
  }
  for (var letter in dependencies) {
    for (var dep of dependencies[letter]) {
      incomingEdges[dep]++;
    }
  }
  var queue = [];
  var order = "";
  for (var letter in incomingEdges) {
    if (incomingEdges[letter] === 0) {
      queue.push(letter);
    }
  }
  while (queue.length > 0) {
    var letter = queue.shift();
    order += letter;
    if (dependencies[letter]) {
      for (var dep of dependencies[letter]) {
        incomingEdges[dep]--;
        if (incomingEdges[dep] === 0) {
          queue.push(dep);
        }
      }
    }
  }
  
  return order;
};
