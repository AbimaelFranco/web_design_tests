// DataTypes and Variables
int userAge = 0;
string userName = "Alex";
bool state = true;

// Console input and output
Console.WriteLine("Welcome to the program!");
Console.Write("Enter your name: ");
string name = Console.ReadLine();

Console.Write("Enter your age: ");
string inputAge = Console.ReadLine();
int age = int.Parse(inputAge);

Console.WriteLine($"Hello {name}, you are {age} years old.");

// Conditional statements if
if (age < 18)
{
    Console.WriteLine("You are a minor.");
    Console.WriteLine($"To be an adult you need {18 - age} more years");
}
else
{
    Console.WriteLine("You are an adult.");
}

// Loop for
Console.WriteLine("Your life was looking like this:");
for (int i = 0; i <= age; i++)
{
    Console.WriteLine($"You had {i} years old");
}