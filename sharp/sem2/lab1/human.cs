//*my first class for introduction to OOP in C#
using System;	


//namespace program {
	public class Human {
		private int age; 
		private int heigth;
		private int weight;
		private int thougthspos = 0; //used for navigation through "thougths" array
		static private int population = 0;

		protected string name;	
		
		private string job;
		private string[] thougths = new string[10];

		private	Random rnd = new Random();
	
		public static int getPopulation { //property, which allows acces to private "population" field
			get {return population;}
		}
	
		
		public string getThougths { //PROPERTY
			get { 					//PROPERTY METHOD
				string AllThougths = "";
				for(int i = thougths.Length - 1; i >= 0; i--) {
					AllThougths += thougths[i] + "\n";
				}
				return AllThougths;
			}
		}
		

		public int this[string i] { //INDEX
			get {
				switch (i) { 
					case "Heigth": 
						return heigth;
					case "Weight": 
						return weight;
					case "Age": 
						return age;
					default: 
						Console.Write("bad index input"); //bad input warning 
						return 0;
				}
			}		
		}
	

		public string rename { //rename property
			set {
				name = value;
			}
		}
	
		
		public string this[int i] { // overload of index
			get	{
				return thougths[i]; 
			}
		}		
		
		
		public Human(int newAge, int newHeigth, int newWeight, string newName, string newJob = "unemployed") { // constructor		
			string errorMessage = "";

			if (newAge < 0) {  //exception handling
				errorMessage = errorMessage + "invalid age " + age;
			}
			if (newHeigth <= 0) {
				errorMessage = errorMessage + "invalid heigth " + heigth;
			}
			if (newWeight <= 0) {
				errorMessage = errorMessage + "invalid weight " + weight;
			}
			if (errorMessage != "") {
				throw new Exception("bad input " + errorMessage);
			}

			age = newAge;
			heigth = newHeigth; 
			weight = newWeight;
			name = newName;
			job = newJob;			
			population++;
		}
		
		
		public void ShowParams() {
			Console.Write(" Age - {0}\n Heigth - {1}\n Weight - {2}\n Name - {3}\n Job - {4}\n",age, heigth, weight, name, job);
		}

		
		public void Tell(string input) { //thoughts array input
			if (thougthspos < 10) {
				thougths[thougthspos] += input;
				thougthspos++;
			}
			
			else {
				Console.WriteLine("ERROR! Thougths array overload!"); //protection from array overflow
				return;
			}

		}
	
		
		public string Ask() { //.Ask method overload	
			return thougths[rnd.Next(0, thougthspos + 2)];
		}
		
		
		public string Ask(int answer){ //thoughts array output
			return thougths[answer];
		}
	
	}
//}
	
//	class Program {
	/*	static int Main() {
			Console.Write("Population:");
			Console.WriteLine(Human.getPopulation);
			
			Human Anisimov = new Human (60, 160, 70, "Vladimir", "Mathematician"); 
			Console.Write("Population:");
			Console.WriteLine(Human.getPopulation);
			
			Human Vasya = new Human (47, 170, 60, "Vasya"); 			
			Console.Write("Population:");
			Console.WriteLine(Human.getPopulation);
			
			Console.Write("Anisimov's params\n");
			Anisimov.ShowParams();
			Console.Write("Vasya's params\n");
			Vasya.ShowParams();	// used to demonstrate unintialized field usage

			Anisimov.Tell("2 + 2 = 4!");
			Anisimov.Tell("Smoking is bad!");
			Anisimov.Tell("dx/dy = ???");
			Anisimov.Tell("We all live in hell!");
			Anisimov.Tell("All humans are mortal...");
			Anisimov.Tell("Some random math stuff!");	
			Anisimov.Tell("Circulation of vector field!!!");		
			Anisimov.Tell("3x^3 + const = ???");
			Anisimov.Tell("Could I pass Turing Test?");
			Anisimov.Tell(Console.ReadLine()); 
		
			Anisimov.Tell("Circulation of vector field!!!"); //protection from array overflow demonstration
			Anisimov.Tell("3x^3 + const = ???");
			Anisimov.Tell("Could I pass Turing Test?"); 
			
			Console.WriteLine("getThougths demonstration:\n");
			Console.WriteLine(Anisimov.getThougths);
			
			Console.WriteLine("Method, overload & index demonstration:\n");
			Console.WriteLine(Anisimov[5]);			//Index demonstration
			Console.Write(Anisimov.Ask(8) + "\n");  //.Ask method demonstration
			Console.Write(Anisimov.Ask() + "\n");	//.Ask method overload demonstration	

			Console.WriteLine(Anisimov["Weight"]); //index overload demonstration
			Console.WriteLine(Anisimov["Heigth"]);
			Console.WriteLine(Anisimov["Age"]);
			
			Anisimov.rename = "Pyotr"; //rename property demonstraion
						
			Anisimov.ShowParams();

			return 0;
		}
	}*/
//}
