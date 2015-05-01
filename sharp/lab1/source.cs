// simple 15 console game - my first C# program

using System;

class Program {
	
	static int jcoord; // current 
	static int icoord; // empty space coordinates	

	static ConsoleKeyInfo move; // button, pressed by player
	
	static int [,] board = new int[4, 4] { {1, 0, 2, 7}, {4, 5, 6, 3}, {8, 9, 15, 11}, {12, 13, 14, 10} }; // Creates gameboard,
																										    // 0 indicates an empty space
	static void getcoord() { // this method finds out current coordinates of 0 			
	 
		for (int i = 0; i < 4; ++i) {
           	for (int j = 0; j < 4; ++j) {
               	if (board[i,j] == 0) {
					icoord = i;
                    jcoord = j; 
					break;
				}
			}
		}	
	}
	
	public static void swap() {	// this method is used to put the selected token at the empty space

		int temp;
			
		move = Console.ReadKey();

		try {	//exception will occur, when player tries to move 0 out of gameboard

			if (move.Key == ConsoleKey.LeftArrow) {
				temp = board[icoord, jcoord];		
				board[icoord, jcoord] = board[icoord, jcoord - 1]; 
				board[icoord, jcoord - 1] = temp;	
				}	

			else if (move.Key == ConsoleKey.RightArrow) {
        		temp = board[icoord, jcoord];
        		board[icoord, jcoord] = board[icoord, jcoord + 1];
        		board[icoord, jcoord + 1] = temp;
				}

			else if	(move.Key == ConsoleKey.UpArrow) {
        		temp = board[icoord, jcoord];
        		board[icoord, jcoord] = board[icoord - 1, jcoord];
        		board[icoord - 1, jcoord] = temp;
			}
	
			else if (move.Key == ConsoleKey.DownArrow) {
        		temp = board[icoord, jcoord];
        		board[icoord, jcoord] = board[icoord + 1, jcoord];
        		board[icoord + 1, jcoord] = temp;
				}	
		}	
		
		catch (IndexOutOfRangeException) { 
			return;
			}	
		}	
	
	static bool victorycheck() {	// this method checks if this array's elements are in order 	
									//if they are - player wins
		int j = 0;
		int i = 0;

		for (i = 0; i < 3; i++) {                    	
			if (i > 2) {
				if (board[i,j] > board[i - 1, j + 3]) {
				return false;
				}
			}
				for (j = 0; j < 3; j++) {
				if (board[i,j] > board[i, j + 1]) {
                    return false;
					}
				else {
					continue;
				}			
			}	
		}	
	return true;
	}	

	static void show() { 	// this method displays gameboard
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {	       
				Console.Write("{0,3}",board[i,j]);					
			}    				
				Console.Write('\n');
		}
	}

	static void Main() {
		
			Console.WriteLine();
			
			while(move.Key != ConsoleKey.Escape) {		

				victorycheck();       		
	
				Console.Write("Welcome to the 15 game!\n");
				show();
        	
				getcoord();
			
				Console.WriteLine();
        		Console.Write("Make your move!\n");
				Console.Write("Use arrow keys to move 0 token, and escape key to exit");
	        	Console.Write('\n');
    	    	Console.Write("0 token can't leave gameboard!\n");
       			Console.Write('\n');
       				
				swap();
				Console.Clear();
					
				if (victorycheck() == true) {
					Console.Write("Victory!");
					break;
				}
		}
	return;
	}
}

	
