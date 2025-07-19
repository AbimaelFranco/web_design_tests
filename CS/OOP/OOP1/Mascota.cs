public class Mascota
{
    public string Dueno;
    public string Raza;
    public int Edad;

    public Mascota(string dueno, string raza, int edad)
    {
        Dueno = dueno;
        Raza = raza;
        Edad = edad;
    }

    public void Saludar()
    {
        Console.WriteLine($"El {Raza} de {Dueno} te dice Hola");
    }

}