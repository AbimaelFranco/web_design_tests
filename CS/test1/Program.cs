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