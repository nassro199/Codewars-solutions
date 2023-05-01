#include <stdbool.h>
#include <math.h>

bool is_square(int n) {
    // Negative numbers are not squares
    if (n < 0) {
        return false;
    }

    // Compute the square root and round it to an integer
    int root = sqrt(n);
    
    // Check if the squared root times itself is equal to n
    return root * root == n;
}