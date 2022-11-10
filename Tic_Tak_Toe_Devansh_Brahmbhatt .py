def Tic_tac_toe():
  list=["_","_","_","_","_","_","_","_","_"]
  t=1
  print("Hello! Welcome to Devansh's Tic Tac Toe game! ", )
  
  print("Rules: Game for 2 Players,Player 1 and Player 2 are represented by 'X' and 'O' respectfully "
        "taking their respective turns in the marked spaces in a 3*3 grid. The player who is successfull in placing "
        "three of their 'X' or 'O'(Whichever they get) in a horizontal, vertical, or diagonal row wins,if they fail to do so the match would be a draw or tie")
  print ("This is the position guide for the game.")
  print (" 1 2 3 ")
  print (" 4 5 6 ")
  print (" 7 8 9 ")
  
  for i in range (9):  
      if t%2 == 0:
        pos=int(input("Enter your position for 'X' please => "))
        list[pos-1]='X'
        
      else:
        pos=int(input("Enter your position for 'O' please => "))
        list[pos-1] = 'O'
        
      
    
      print("After",t,"=> ")
      print(list[0],list[1],list[2])
      print(list[3],list[4],list[5])
      print(list[6],list[7],list[8])
      
      t=t+1 
  
      if list[0] == list[1] and list[1] == list[2] and list[0] == 'O':
        print("Player 1 wins :) ")  
        t=15
        break
      elif list[0] == list[3] and list[3] == list[6] and list[0] == 'O':
        print("Player 1 wins :) ")  
        t=15
        break
      elif list[0] == list[4] and list[4] == list[8] and list[0] == 'O':
        print("Player 1 wins :) ")  
        t=15
        break
      elif list[1] == list[4] and list[4] == list[7] and list[1] == 'O':
        print("Player 1 wins :) ")  
        t=15
        break
      elif list[2] == list[5] and list[5] == list[8] and list[2] == 'O':
        print("Player 1 wins :) ")  
        t=15
        break
      elif list[2] == list[4] and list[4] == list[6] and list[2] == 'O':
        print("Player 1 wins :) ") 
        t=15
        break
      elif list[3] == list[4] and list[4] == list[5] and list[3] == 'O':
        print("Player 1 wins :) ") 
        t=15
        break
      elif list[6] == list[7] and list[7] == list[8] and list[6] == 'O':
        print("Player 1 wins :) ")  
        t=15
        break
      elif list[0] == list[1] and list[1] == list[2] and list[0] == 'X':
        print("Player 2 wins :) ")  
        t=15
        break
      elif list[0] == list[3] and list[3] == list[6] and list[0] == 'X':
        print("Player 2 wins :) ")  
        t=15
        break
      elif list[0] == list[4] and list[4] == list[8] and list[0] == 'X':
        print("Player 2 wins :) ")  
        t=15
        break
      elif list[1] == list[4] and list[4] == list[7] and list[1] == 'X':
        print("Player 2 wins :) ")  
        t=15
        break
      elif list[2] == list[5] and list[5] == list[8] and list[2] == 'X':
        print("Player 2 wins :) ")  
        t=15
        break
      elif list[2] == list[4] and list[4] == list[6] and list[2] == 'X':
        print("Player 2 wins :) ") 
        t=15
        break
      elif list[3] == list[4] and list[4] == list[5] and list[3] == 'X':
        print("Player 2 wins :) ")  
        t=15
        break
      elif list[6] == list[7] and list[7] == list[8] and list[6] == 'X':
        print("Player 2 wins :) ")  
        t=15
        break
  
  if t==10:
    print("It's a draw :| ")
    print("To play again run the code again.")
    print("Thank You.")
    return True
Tic_tac_toe()