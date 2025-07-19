using System.Collections.Generic;

// Array
/// <summary>
/// In C# arrays are used to store multiple values of the same type.
/// They are fixed in size and can be accessed using an index.
/// Arrays can be created in two ways: as an object or using an initializer.
/// </summary>

// Creacion como objeto
int[] numeros = new int[3];

numeros[0] = 10;
numeros[1] = 20;
numeros[2] = 30;

// Creacion como inicializador
int[] nums = { 10, 20, 30 };

string[] nombres = { "Juan", "Ana", "Pedro" };


// Lists
/// <summary>/// In C#, lists are dynamic arrays that can grow and shrink in size.
/// They are part of the System.Collections.Generic namespace and provide more flexibility than arrays.
/// Lists can be created using the List<T> class, where T is the type of elements in the list.
/// </summary>

/// using System.Collections.Generic;
List<string> frutas = new List<string>();
frutas.Add("Manzana");
frutas.Add("Banana");
frutas.Add("Naranja");

// Accessing elements in a list
string primeraFruta = frutas[0]; // "Manzana"
// Iterating through a list
foreach (string fruta in frutas)
{
    Console.WriteLine(fruta);
}
// Removing an element from a list
frutas.Remove("Banana");
// Counting elements in a list
frutas.Count; // 2
// Checking if a list contains an element
frutas.Contains("Naranja"); // true
// Inserting an element at a specific index
frutas.Insert(1, "Fresa"); // Inserts "Fresa" at index 1
// Clearing all elements from a list
frutas.Clear(); // Removes all elements from the list

// Sorting a list
frutas.Sort(); // Sorts the list in ascending order
// Reversing a list
frutas.Reverse(); // Reverses the order of elements in the list
// Converting a list to an array
string[] frutasArray = frutas.ToArray(); // Converts the list to an array
// Finding an element in a list
int index = frutas.IndexOf("Naranja"); // Returns the index of "Naranja"


// Dictionary
/// <summary>
/// In C#, dictionaries are collections of key-value pairs.
/// They are part of the System.Collections.Generic namespace and provide a way to store data in a way that allows for fast lookups.
/// Dictionaries can be created using the Dictionary<TKey, TValue> class, where TKey is the type of keys and TValue is the type of values.
/// </summary>

/// using System.Collections.Generic;
Dictionary<string, int> edades = new Dictionary<string, int>();
edades.Add("Juan", 30);
edades.Add("Ana", 25);
edades.Add("Pedro", 35);
// Accessing values in a dictionary
int edadJuan = edades["Juan"]; // 30
// Iterating through a dictionary
foreach (KeyValuePair<string, int> par in edades)
{
    Console.WriteLine($"{par.Key}: {par.Value}");
}
// Checking if a key exists in a dictionary
bool existeAna = edades.ContainsKey("Ana"); // true
// Removing a key-value pair from a dictionary
edades.Remove("Pedro"); // Removes the key "Pedro" and its value
// Counting key-value pairs in a dictionary
int cantidad = edades.Count; // 2
// Clearing all key-value pairs from a dictionary
edades.Clear(); // Removes all key-value pairs from the dictionary
// Getting all keys from a dictionary
ICollection<string> claves = edades.Keys; // Returns a collection of keys
// Getting all values from a dictionary
ICollection<int> valores = edades.Values; // Returns a collection of values