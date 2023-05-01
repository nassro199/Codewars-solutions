// This function takes in a 10x10 array representing a Battleship game board and returns true if the board is valid, false otherwise
function validateBattlefield(field) {
    // Define a function 'hit' which returns 0 if the given row and column are out of bounds, otherwise it returns the value in the given cell
    var hit = (row, col) => (row < 0 || col < 0 || row > 9 || col > 9) ? 0 : field[row][col];
    
    // Initialize an array 'ships' to keep track of the number of ships of each size (0, 1, 2, 3, and 4) on the board
    // Initialize variables 'row' and 'col' to 0 to loop through each cell in the board
    for (var ships = [10,0,0,0,0], row = 0; row < 10; row++) {
      for (var col = 0; col < 10; col++) {
        // If the current cell contains a ship (has a value of 1):
        if ( hit(row,col) ) {
          // Check if the ship is touching a corner of another ship
          if ( hit(row-1, col-1) || hit(row-1, col+1) ) return false;
          // Check if the ship is touching the side of another ship
          if ( hit(row-1, col  ) && hit(row  , col-1) ) return false;
          // Check if the ship is longer than 4 cells
          if ( ( field[row][col] += hit(row-1, col) + hit(row, col-1) ) > 4 ) return false;
          // Increment the counter for the size of the ship
          ships[field[row][col]]++;
          // Decrement the counter for the previous size of the ship
          ships[field[row][col] - 1]--;
        }
      }
    }
    // Check if there are the correct number of ships of each size (0, 1, 2, 3, and 4) on the board
    return [0,4,3,2,1].every((s,i) => s == ships[i]);
  }
  