#include <iostream>

using namespace std;

int menu()
{
    int n;

    cout << "\n------Welcome to Martin's Simple Calculator------\n";
    cout << "\n\n------Menu------\n";
    cout << "1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n";
    cout << "Please enter a number from above: ";
    cin >> n;

    while (n < 0 || n > 5)
    {
        cout << "You have entered an invalid number.... Please re-enter your number\n";
        cout << "Please enter a number from above: ";
        cin >> n;
    }
}

int Add(int x, int y)
{
    return x + y;
}

int Subtract(int x, int y)
{
    return x - y;
}

int Multiply(int x, int y)
{
    return x * y;
}

float Divide(int x, int y)
{
    if (y != 0)
        return (float)x / y;

    return 0;
}

int Modulus(int x, int y)
{
    return x % y;
}

int main()
{
    char choice = 'y';
    
    while (choice == 'y')
    {
        int n = menu();
        int x, y;
        cout << "Please enter your first number: ";
        cin >> x;
        cout << "Please enter your second number: ";
        cin >> y;

        switch (n)
        {
        case 1:
            cout << "Result = " << Add(x, y);
            break;
        case 2:
            cout << "Result = " << Subtract(x, y);
            break;
        case 3:
            cout << "Result = " << Multiply(x, y);
            break;
        case 4:
            cout << "Result = " << Divide(x, y);
            break;
        case 5:
            cout << "Result = " << Modulus(x, y);
            break;
        }

        cout << "\nDo you want to continue(y/n): ";
        cin >> choice;
        
    }
    cout << "Have a nice Day";
    return 0;
}