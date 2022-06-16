#include<iostream>
using namespace std;
int main()
{
    int num1,denom1,rem,denom2;
    cout<<"Enter the numerator ";
    cin>>num1;
    cout<<"Enter the denominator ";
    cin>>denom1;
    rem=num1%denom1;
    num1=(num1-rem)/denom1;
    cout<<"Mixed Fraction = "<<num1<<" "<<rem<<"/"<<denom1;
    return 0;
}