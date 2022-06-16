// First name Last name
// Date

#include<iostream>
using namespace std;
int main()
{
    int numerator, denominator;
    cout<<"Enter the numerator: ";
    cin>>numerator;
    cout<<"Enter the denominator: ";
    cin>>denominator;

    if (numerator < denominator){
        cout << numerator + "/" + denominator + "is a proper fraction"
    }
    else{
        int mix = numerator / denominator;
        int remainder = numerator % denominator;
        if (remainder == 0){
            int whole = numerator / denominator;
            cout<< numerator + " / " + denominator + " is an improper fraction and it can be reduced to " + whole;
        }
        else{
            cout<< numerator +  "/" + denominator + "is an improper fraction and its mixed fraction is " + mix + "+" + remainder + denominator;
        }
    }
    return 0;
}