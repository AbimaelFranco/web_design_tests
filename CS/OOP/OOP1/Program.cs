class Program
{
    static void Main()
    {
        Persona Alex = new Persona("Alexander", 24);
        Alex.Saludar();

        Mascota PerroAlex = new Mascota(Alex.Nombre, "perro", 2);
        PerroAlex.Saludar();
    }
}