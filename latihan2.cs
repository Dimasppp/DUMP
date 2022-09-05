// See https://aka.ms/new-console-template for more informationusing System;

using System.IO.Pipes;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        class Person
        {
            public string Name;
            public string Alamat;
            public string JenisKelamin;
            public string Profesi;
            public string TglLahir;
            public int JumlahKendaraan;

            public Person(string Name, string Alamat, string JenisKelamin, string Profesi, string TglLahir, int JumlahKendaraan)
            {
                this.Name = Name;
                this.Alamat = Alamat;
                this.JenisKelamin = JenisKelamin;
                this.Profesi = Profesi;
                this.TglLahir = TglLahir;
                this.JumlahKendaraan = JumlahKendaraan;
            }
        }
        public static void Main(string[] args)
        {
            Person one = new Person("Naziel Ilham", "Jakarta", "Laki-laki", "Penyanyi", "16 Sep 1981", 3);
            Console.WriteLine("Nama Lengkap : " + one.Name);
            Console.WriteLine("Alamat : " + one.Alamat);
            Console.WriteLine("Jenis Kelamin : " + one.JenisKelamin);
            Console.WriteLine("Profesi : " + one.Profesi);
            Console.WriteLine("Tanggal Lahir : " + one.TglLahir);
            Console.WriteLine("Jumlah Kendaraan : " + one.JumlahKendaraan);
            Console.WriteLine(" ");
            
            Person two = new Person("Chelsea Islan", "Jakarta", "Perempuan", "Aktris Film", "2 Juni 1995", 1);
            Console.WriteLine("Nama Lengkap : " + two.Name);
            Console.WriteLine("Alamat : " + two.Alamat);
            Console.WriteLine("Jenis Kelamin : " + two.JenisKelamin);
            Console.WriteLine("Profesi : " + two.Profesi);
            Console.WriteLine("Tanggal Lahir : " + two.TglLahir);
            Console.WriteLine("Jumlah Kendaraan : " + two.JumlahKendaraan);
            Console.WriteLine(" ");

            Person three = new Person("Iqbaal Ramadhan", "Jakarta", "Laki-laki", "Aktor Film", "28 Des 1999", 2);
            Console.WriteLine("Nama Lengkap : " + three.Name);
            Console.WriteLine("Alamat : " + three.Alamat);
            Console.WriteLine("Jenis Kelamin : " + three.JenisKelamin);
            Console.WriteLine("Profesi : " + three.Profesi);
            Console.WriteLine("Tanggal Lahir : " + three.TglLahir);
            Console.WriteLine("Jumlah Kendaraan : " + three.JumlahKendaraan);
            Console.WriteLine(" ");
        }


    }
}