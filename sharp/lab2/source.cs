using System;
using System.Globalization;
using System.Text;

class Program {

	static void printmonth(string CultureName) {
		CultureInfo cul = new CultureInfo(CultureName);
		DateTime date = new DateTime();
		
		for(int i = 0; i < 12; i++) {
			Console.WriteLine(date.ToString("MMMM", cul));
			date = date.AddMonths(1);	
		}
	}


	static string reverse(string input) {
		char[] array = input.ToCharArray();
															
		string[] strarray = new string[10];
	
		StringBuilder sb = new StringBuilder("", 300);	
	
		int counter = 0;
		
		for (int i = 0; i < array.Length; i++) {
			strarray[counter] += array[i];
			if (array[i] == ' ') {
				counter++;
			}
		}	
			
		for (int current = counter; current >= 0; --current) {
			string trim_current = strarray[current].Trim();
			if (current == counter) {
				sb.Append(trim_current);		
			}
			else {
				sb.Append(" ").Append(trim_current);}	
			}
		
		string reversed = sb.ToString();
		return reversed;
	}
	

	static string nextletter(string input) {
		char[] array;
		char[] vowels = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'};
		
		StringBuilder sb = new StringBuilder("", 300);	
		
		array = input.ToCharArray();		
		
		for(int i = array.Length - 2; i >= 0; i--) {
			for(int j = 0; j < vowels.Length; j++) { 
				if(array[i]	== vowels[j]) {
					if (array[i + 1] == 'z') {
						array[i + 1] = 'a';
					} 
					else {
						array[i + 1]++;					
					}
				}
			}	
		}	
		
		for(int i = 0; i < array.Length; i++) {
			sb.Append(array[i]);
		}
		string output = sb.ToString();
		return output;
	}
	

	static int Main() {
		
		string input;
		int choice;

		input = Console.ReadLine();		
		choice = Console.Read();		

		switch (choice) {
			case '1':
				printmonth(input);
				break;				
			case '2':
				Console.Write(nextletter(input));
				break;
			case '3':
				Console.Write(reverse(input));
				break;
			}
		return 0;
	}
}
