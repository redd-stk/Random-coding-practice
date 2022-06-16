#include <stdio.h>

void main()
{
    int buffer[10] = {0}, averageOver = 0, total = 0, oldIndex = 0, numsEntered = 0, timesPassed = 0, avrOverOutput = 0; // Declarations
    int *p = buffer; //I've replaced the buffer array with a pointer p which I will now use in all instances where buffer is referenced
    double average = 0.0;                                                                                                // Declaration
    printf("Enter the number of values to be averaged over (N): ");                                                      // Prompt user to enter a value that will be used to determine what values will be averaged over
    scanf("%d", &averageOver);                                                                                           // Get integer input and save the value to the averageOver variable
    while (1)
    {
        printf("Enter a value: ");              // Prompt the user to enter a value
        scanf("%d", & p[numsEntered % 10]); // Get element at index i in the "buffer" array as an integer. **Buffer has been replaced with pointer p here
        // numsEntered++;                     // Increment the amount of numbers entered by the user
        printf("Buffer Contents: ");
        for (int loop = 0; loop < 10; loop++) // Prints array elements horizontally
            printf("%d\t", p[loop]);     // Output a tab element followed by the value at index "loop" in "buffer". **Buffer is also replaced with p here
        printf("\n");                         // Output a newline

        total += p[numsEntered % 10]; //Adds the most recent number to the array. **p has been used to point to the buffer array

        if ((numsEntered) < averageOver)
        {
            avrOverOutput = numsEntered + 1;
        }
        else
        {
            oldIndex = ((numsEntered - averageOver) % 10);
            total -= p[oldIndex++];  //**p has also replaced buffer here
            avrOverOutput = averageOver;
        }
        average = ((float)total / avrOverOutput);
        printf("\nNumber of values entered: %d  Average Over: %d  Average: %.2f %s", (numsEntered++), avrOverOutput, (float)average, "\n");
    }
}