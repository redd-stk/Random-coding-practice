#include <iostream> 

#include <string> 

using namespace std; 


int main() 

{ 

// Declare a named constant for array size here 

const int MAX_AVERAGES = 8; 


// Declare array here 0.299

double averages[MAX_AVERAGES]; 


// Use this integer variable as your loop index 

int loopIndex; 


// Use this variable to store the batting average input by user 

double battingAverage; 


// Use these variables to store the minimim and maximum values 

double min, max; 


// Use these variables to store the total and the average 

double total, average; 


// Write a loop to get batting averages from user and assign to array 

for(loopIndex = 0; loopIndex < MAX_AVERAGES; loopIndex++) 

{ 

cout << "Enter a batting average: "; 

cin >> battingAverage; 

// Assign value to array 

averages[loopIndex] = battingAverage; 

} 

// Assign the first element in the array to be the minimum and the maximum 

min = averages[0]; 

max = averages[0]; 

// Start out your total with the value of the first element in the array 

total = averages[0]; 

// Write a loop here to access array values starting with averages[1] 

for(loopIndex = 1; loopIndex < MAX_AVERAGES; loopIndex++) 

{ 

// Within the loop test for minimum and maximum batting averages. 

if(averages[loopIndex] < min) 

min = averages[loopIndex]; 

if(averages[loopIndex] > max) 

max = averages[loopIndex]; 

// Also accumulate a total of all batting averages 

total += averages[loopIndex]; 

} 



// Calculate the average of the 8 batting averages 

average = total / MAX_AVERAGES; 


// Print the batting averages stored in the averages array 

for(loopIndex = 0; loopIndex < MAX_AVERAGES; loopIndex++) 

{ 

cout << "averages[" << loopIndex << "] is: " << averages[loopIndex] << endl; 

} 

// Print the maximum batting average, minimum batting average, and average batting average 

cout << "Minimum batting average is " << min << endl; 

cout << "Maximum batting average is " << max << endl; 

cout << "Average batting average is " << average << endl; 

return 0; 

} 
