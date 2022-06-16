#include <iostream>

using namespace std;

//  Utility function to find
int factorial(int terms)
{
    int res = 1;
    for (int i = 2; i <= terms; i++)
        res *= i;
    return res;
}

// Function with for loop that returns value of 1/1! + 1/2! + .. + 1/n!
double sum(int terms)
{
    double sum = 0;
    for (int i = 1; i <= terms; i++)
        sum += 1.0 / factorial(i);
    return sum;
}

//main funtion that calls the functions and takes input of number of terms from the user
int main()
{
    int terms = 0;
    cout << "Enter the number of terms: ";
	cin >> terms;
    cout << sum(terms);
    return 0;
}