class ConwayLife {

  public static int[][] getGeneration(int[][] cells, int generations) {

    if ( generations < 1)  
        return cropped(cells);
        
    int [][] resized = new int [cells.length+2][cells[0].length+2]; 
      
    for (int i = 0; i < cells.length; i++)
        for (int j = 0; j < cells[i].length; j++)
            resized[i+1][j+1] = cells[i][j];            
      
      
    int [][] nextgen = new int [cells.length+2][cells[0].length+2];  
    int cell = 0, weight = 0, x = 0, y = 0, endx = 0, endy = 0;
    boolean searchabove = false, searchbelow = false, searchleft = false, searchright = false;
    
    for (int i = 0; i < resized.length; i++){
      if (i-1 >= 0) searchabove = true; else searchabove = false;
      if (i + 1 < resized.length) searchbelow = true; else searchbelow = false;
        
      for (int j = 0; j < resized[i].length; j++){
        
        cell = resized[i][j];
        if (j-1 >= 0) searchleft = true; else searchleft = false;
        if (j+1 < resized[i].length) searchright = true; else searchright = false;

        weight = 0;
        if (searchabove) x = i - 1; else x = i;
        if (searchbelow) endx = i + 1; else endx = i;
        if (searchleft) y = j - 1; else y = j;
        if (searchright) endy = j + 1; else endy = j;

        for (;x <= endx; x++)
            for (int p = y; p <= endy; p++)  
                weight += resized[x][p];
            
        weight -= cell;  

        if (cell == 1 && (weight < 2 || weight > 3))
          nextgen[i][j] = 0;
        else if (cell == 0 && weight == 3)
          nextgen[i][j] = 1;
        else
          nextgen[i][j] = cell;
      }
    }
    nextgen = cropped(nextgen); 
    return  getGeneration(nextgen, generations-1); 
  }
    
  public static int [][] cropped(int [][] cells){
  
      int leftmost = cells[0].length, rightmost = 0, uppermost = cells.length, lowermost =0;
      for (int i = 0; i < cells.length; i++)
          for (int j = 0; j < cells[i].length; j++)
              if (cells[i][j] == 1){
                  if (i < uppermost)
                      uppermost = i;
                  if (i > lowermost)
                      lowermost = i;
                  if (j < leftmost)
                      leftmost = j;
                  if (j > rightmost)
                      rightmost = j;
              }
        
      int [][] cropped = new int [lowermost - uppermost + 1][rightmost-leftmost+1];  
      for (int i = uppermost; i <= lowermost; i++)
          for (int j = leftmost; j <= rightmost; j++)
              cropped[i - uppermost][j-leftmost] = cells[i][j];
      return cropped;
  }
  
}