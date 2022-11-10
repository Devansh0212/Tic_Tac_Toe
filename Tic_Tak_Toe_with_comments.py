
def Tic_tac_toe():                                                # Defining tic_tac_toe function for the game
  list=["_","_","_","_","_","_","_","_","_"]                      # Making a list for storing positions of the players respectively
  t=1                                                             # 't' is a variable whose value is assigned to 1
  print("Hello! Welcome to Devansh's Tic Tac Toe game! ", )       # Game described for user to understand the rules and play accordingly
  print("Rules of the Game:  ")
  print("Game is for two Players only,Player 1 and Player 2 are represented by 'O' and 'X' respectfully ")
  print("Taking input from the players for their respective turns in the marked spaces in a 3*3 grid.")
  print("To win the game:") 
  print("Player cannot enter a position which is entered before. ")
  print("The player who is successfull in placing three of their 'O' or 'X' first in any of these possibilities(horizontal,vertical or diagonal row wins the game ")
  print("Else if they fail to do so the match would be a draw or tie")
  print("I hope you have a great time playing the game *_* ")
  print ("This is the position guide for the game.")             # Position guide for the user  if user is not sure what number to enter for position of their respective 'O' or 'X'
  print (" 1 2 3 ")
  print (" 4 5 6 ")
  print (" 7 8 9 ")
  
  for i in range(9):                                            # Initializing for loop in range of 9
      if t%2 == 0:                                              # When t is divided by 2 and the remainder is equal to zero ,it would pass the if statement
        pos=int(input("Enter your position for 'X' please => "))
        list[pos-1] = 'X'
        
      else :
        pos=int(input("Enter your position for 'O' please => "))# When t is divided by 2 and the remainder is not equal to zero ,it would pass the elif statement
        list[pos-1] = 'O'
     
      
      print("After",t,"=> ")                                    # Printing t for players to know how many turns they have played
      print(list[0],list[1],list[2])
      print(list[3],list[4],list[5])
      print(list[6],list[7],list[8])
      
      t=t+1                                                     # t is increasing by 1 in range of 9(for loop)
  
      if list[0] == list[1] and list[1] == list[2] and list[0] == 'O':   # (For player 1 which is 'O'in the game to win this is one of the possibility by which player 1 can win the game)(If player 1 manages to position 'O' in 0,1,and 2. ) 
        print("Player 1 wins :) ")  # Printing to inform the players that the game has ended and player 1 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[0] == list[3] and list[3] == list[6] and list[0] == 'O': #(If player 1 manages to position 'O' in 0,3,and 6 )
        print("Player 1 wins :) ")  # Printing to inform the players that the game has ended and player 1 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[0] == list[4] and list[4] == list[8] and list[0] == 'O': #(If player 1 manages to position 'O' in 1,4,and 8 )
        print("Player 1 wins :) ")  # Printing to inform the players that the game has ended and player 1 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[1] == list[4] and list[4] == list[7] and list[1] == 'O': #(If player 1 manages to position 'O' in 1,4,and 7 )
        print("Player 1 wins :) ")  # Printing to inform the players that the game has ended and player 1 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[2] == list[5] and list[5] == list[8] and list[2] == 'O': #(If player 1 manages to position 'O' in 2,5,and 8 )
        print("Player 1 wins :) ")  # Printing to inform the players that the game has ended and player 1 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[2] == list[4] and list[4] == list[6] and list[2] == 'O': #(If player 1 manages to position 'O' in 2,4,and 6 )
        print("Player 1 wins :) ") # Printing to inform the players that the game has ended and player 1 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[3] == list[4] and list[4] == list[5] and list[3] == 'O': #(If player 1 manages to position 'O' in 3,4,and 5 )
        print("Player 1 wins :) ") # Printing to inform the players that the game has ended and player 1 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[6] == list[7] and list[7] == list[8] and list[6] == 'O': #(If player 1 manages to position 'O' in 6,7,and 8 )
        print("Player 1 wins :) ")  # Printing to inform the players that the game has ended and player 1 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[0] == list[1] and list[1] == list[2] and list[0] == 'X': #(If player 2 manages to position 'X' in 0,1,and 2 )
        print("Player 2 wins :) ")  # Printing to inform the players that the game has ended and player 2 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[0] == list[3] and list[3] == list[6] and list[0] == 'X':#(If player 2 manages to position 'X' in 0,3,and 6 )
        print("Player 2 wins :) ")   # Printing to inform the players that the game has ended and player 2 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[0] == list[4] and list[4] == list[8] and list[0] == 'X':#(If player 2 manages to position 'X' in 0,4,and 8 )
        print("Player 2 wins :) ")   # Printing to inform the players that the game has ended and player 2 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[1] == list[4] and list[4] == list[7] and list[1] == 'X':#(If player 2 manages to position 'X' in 1,4,and 7 )
        print("Player 2 wins :) ")   # Printing to inform the players that the game has ended and player 2 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[2] == list[5] and list[5] == list[8] and list[2] == 'X':#(If player 2 manages to position 'X' in 2,5,and 8 )
        print("Player 2 wins :) ")   # Printing to inform the players that the game has ended and player 2 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[2] == list[4] and list[4] == list[6] and list[2] == 'X':#(If player 2 manages to position 'X' in 2,4,and 6 )
        print("Player 2 wins :) ")  # Printing to inform the players that the game has ended and player 2 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[3] == list[4] and list[4] == list[5] and list[3] == 'X':#(If player 2 manages to position 'X' in 3,4,and 5 )
        print("Player 2 wins :) ")   # Printing to inform the players that the game has ended and player 2 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
      elif list[6] == list[7] and list[7] == list[8] and list[6] == 'X':#(If player 2 manages to position 'X' in 6,7,and 8 )
        print("Player 2 wins :) ")   # Printing to inform the players that the game has ended and player 2 has won the game
        t=15
        break # Breaking out of the loop as the outcome has been decided and the game has ended
  
  if t==10:                                     # If statement for draw condition
    print("It's a draw :| ")                    # Printing to inform the players that the game is DRAW
    print("To play again run the code again.")  # If player wants to play again player needs to run the code again
    print("Thank You.")
    return True                                 
Tic_tac_toe()                                   # Calling the function 
