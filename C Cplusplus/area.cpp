#include <iostream>
using namespace std;

int main() {
	
    int bases[5] = {1, 2, 3, 4, 5};
    int heights[5];
    int areas[5];

//Taking height values as input from user
    int i; // Variable for access heights array index

    for (i = 0; i < 5; i++) {
      // Reading User Input heights value Based on index
        cout << "Enter the value for height in position " << i << " : ";
        cin >> heights[i];
    }

// Calculating areas from bases and heights arrays for values with same indexes
    for (int i=0; i < 5; i++) {
        areas[i] =  0.5 * bases[i] * heights[i]; //calculates the area for the specific similar indices only
        cout<< "The area for base and height at index " << i << " is " << areas[i] << endl ;
    }

//printing the areas generated from the base and height arrays


}