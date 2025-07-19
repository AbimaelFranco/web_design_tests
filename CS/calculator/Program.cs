Console.WriteLine("Welcome to the calculator program!");
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
    double result = num1 + num2;
    Console.WriteLine($"The result of {num1} + {num2} is {result}");
}
else if (operation == "-")
{
    double result = num1 - num2;
    Console.WriteLine($"The result of {num1} - {num2} is {result}");
}
else if (operation == "*")
{
    double result = num1 * num2;
    Console.WriteLine($"The result of {num1} * {num2} is {result}");
}
else if (operation == "/")
{
    if (num2 != 0)
    {
        double result = num1 / num2;
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