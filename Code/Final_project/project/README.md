# Tic Tac Toe
#### Video Demo: https://youtu.be/3RcTUpqyGzA
#### Description:
My program allows the users to play Tic Tac Toe. Tic Tac Toe is a game where 2 players take turns to put an “X” or an “O” in a grid of nine spaces. Whoever gets 3 in a row (horizontally, vertically or diagonally) is the winner.The program will be written in Python. This project is inspired by the Mario problem set I did in week 1. The program's aim is to entertain programmers while they take a break from doing their project.

When the user first runs the code, the layout of the grid will be printed in the terminal. The numbers on the layout correspond to the number the space is allocated to. You can place the "X" or "O" on the grid by using the numbers key on your keyboard. The space at the top left or the grid is allocated with the number 1. The rest of the spaces are allocated with a number incrementing by 1 from left to right, top to bottom. 2 players will be required to play the game. Each player will take turns placing an “X” or “O” in the grid. The person that starts first will be using “X” and the second player will use “O”. When a player wins, the program will congratulate the winner. When they tie the program will print “it's a draw!”

I choose to use python as it is straightforward and more compact. This will save on space as the program has to be downloaded to the users files. Python is also a native language to Linux. For users using a Linux OS, they can simply run the program straight from the OS's Terminal. For Windows, the Command Prompt can also comprehend python. Users can simply open the file through Command Prompt and the program will run automatically. This works very similarly with OSx (Apple).

The way I implemented the program is mainly by using functions. Then I made a while loop to loop through the functions. The functions include print_board(), print_layout(), player_move(icon), is_victory(icon) and is_draw(). These functions help to organise everything and improve readability. Having functions also allows me to narrow the problem to a certain function rather than having to debug the whole program.

The function of print_board() is to print the grid which the users will play on. This is done by first having a list of 9 " ". After that the " " are arranged in a 3 by 3 order in between "|". This will create an illustration of a 3 by 3 grid.

The function of print_layout() is very similar, instead of printing " ", they are substituted with numbers. This number is like the position of the space where users can use to tell the program where to put the "X" or "O".

The function player_move(icon) will take either an "X" or "O" as input and ask the user where to place "X" or "O". The program also checks if the place the user asked for is available.

The function is_victory(icon) will take either an "X" or "O" as an input. It checks if either "X" or "O" have achieved 3 in a row. If there is a 3 in a row, the function returns true otherwise it returns false.

Lastly, the function is_draw() checks if there are any spaces left to be occupied. If there is no spaces left we can assume that the game is a tie if we run is_victory(icon) before that and it returns false.

Hope you will enjoy the game!