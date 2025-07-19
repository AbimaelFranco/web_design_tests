using System;
class Calculator
{
    public static void Main()
    {
        Console.WriteLine("Welcome to the calculator program!");

        while (true)
        {
            Console.WriteLine("Select an operation: +, -, *, /");

            string operation = Console.ReadLine();

            Console.Write("Enter your first number:");
            string firstnumber = Console.ReadLine();
            Console.Write("Enter your second number:");
            string secondnumber = Console.ReadLine();

            double num1 = double.Parse(firstnumber);
            double num2 = double.Parse(secondnumber);

            if (operation == "+")
            {
                double result = add(num1, num2);
                Console.WriteLine($"The result of {num1} + {num2} is {result}");
            }
            else if (operation == "-")
            {
                double result = subtract(num1, num2);
                Console.WriteLine($"The result of {num1} - {num2} is {result}");
            }
            else if (operation == "*")
            {
                double result = multiply(num1, num2);
                Console.WriteLine($"The result of {num1} * {num2} is {result}");
            }
            else if (operation == "/")
            {
                if (num2 != 0)
                {
                    double result = divide(num1, num2);
                    Console.WriteLine($"The result of {num1} / {num2} is {result}");
                }
                else
                {
                    Console.WriteLine("Error: Division by zero is not allowed.");
                }
            }
            else
            {
                Console.WriteLine("Invalid operation selected.");
            }

            Console.WriteLine("Do you want to perform another calculation? (Y/N)");
            string continueCalculation = Console.ReadLine();
            if (continueCalculation.ToLower() != "y")
            {
                break;
            }
        }
    }

    // Methods for basic arithmetic operations
    public static double add(double x, double y)
    {
        return x + y;
    }

    public static double subtract(double x, double y)
    {
        return x - y;
    }

    public static double multiply(double x, double y)
    {
        return x * y;
    }

    public static double divide(double x, double y)
    {
        if (y == 0)
        {
            throw new DivideByZeroException("Cannot divide by zero.");
        }
        return x / y;
    }
}