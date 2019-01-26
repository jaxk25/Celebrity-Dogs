#celebrity dogs game

#import modules
import random

def clear():#function to clear screen
      for i in range(0,100):
            print("\n")

def menu(): #quick start
      menu_choice = raw_input("Play Game\nQuit\n>>>\t")
      menu_choice = menu_choice.lower()#set characters in menu_choice to all lower case
      if menu_choice == 'play game':
            game()#start game function
      elif menu_choice == 'quit':
            print("\nThank you for playing")
            raw_input("Press RETURN to exit")#when RETURN pressed, end program
      else:
            print("\nError\n")#if neither result is entered, return an error and use the menu function
            menu()

def game():#main game
      possible_cards = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]#define number of cards that can be used
      cards_tbp = int(raw_input("\nHow many cards would you like to be played?\nThis includes you and the CPU\nThe number must be above 4, but below 30, and only an even number.\n>>>\t"))#ask for input and convert it into an integer
      print("You have selected to play " +str(cards_tbp) +" cards.\n")#print how many cards are selected
      selection = raw_input("Is this ok?\n>>>[Y\N] \t")
      selection = selection.lower()#set selection variable to all lower case
      if selection == 'y':
            print("\nOk.\n")#continue
      elif selection == 'n':
            print("\nOk.\n Returning to selection.\n")
            game()#choose again
      else:
            print("\nError\n")
            game() #error with selection, choose again
      if cards_tbp in possible_cards:#if player's selection is valid in possible_cards, do
            f=open("dogs.txt", "r")#open dogs.txt in read mode
            if f.mode == 'r': #if opened correctly in read mode, do
                  contents = f.read() #set contents value to what is in the dogs.txt file
                  a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,ab,ac,ad = contents.split("', '")#split contents into separate variables where there is a "', '"
                  a_exercise = random.randint(1,5)
                  b_exercise = random.randint(1,5)
                  c_exercise = random.randint(1,5)
                  d_exercise = random.randint(1,5)
                  e_exercise = random.randint(1,5)
                  f_exercise = random.randint(1,5)
                  g_exercise = random.randint(1,5)
                  h_exercise = random.randint(1,5)
                  i_exercise = random.randint(1,5)
                  j_exercise = random.randint(1,5)
                  k_exercise = random.randint(1,5)
                  l_exercise = random.randint(1,5)
                  m_exercise = random.randint(1,5)
                  n_exercise = random.randint(1,5)
                  o_exercise = random.randint(1,5)
                  p_exercise = random.randint(1,5)
                  q_exercise = random.randint(1,5)
                  r_exercise = random.randint(1,5)
                  s_exercise = random.randint(1,5)
                  t_exercise = random.randint(1,5)
                  u_exercise = random.randint(1,5)
                  v_exercise = random.randint(1,5)
                  w_exercise = random.randint(1,5)
                  x_exercise = random.randint(1,5)
                  y_exercise = random.randint(1,5)
                  z_exercise = random.randint(1,5)
                  aa_exercise = random.randint(1,5)
                  ab_exercise = random.randint(1,5)
                  ac_exercise = random.randint(1,5)
                  ad_exercise = random.randint(1,5)
                  a_intelligence = random.randint(1,100)
                  b_intelligence = random.randint(1,100)
                  c_intelligence = random.randint(1,100)
                  d_intelligence = random.randint(1,100)
                  e_intelligence = random.randint(1,100)
                  f_intelligence = random.randint(1,100)
                  g_intelligence = random.randint(1,100)
                  h_intelligence = random.randint(1,100)
                  i_intelligence = random.randint(1,100)
                  j_intelligence = random.randint(1,100)
                  k_intelligence = random.randint(1,100)
                  l_intelligence = random.randint(1,100)
                  m_intelligence = random.randint(1,100)
                  n_intelligence = random.randint(1,100)
                  o_intelligence = random.randint(1,100)
                  p_intelligence = random.randint(1,100)
                  q_intelligence = random.randint(1,100)
                  r_intelligence = random.randint(1,100)
                  s_intelligence = random.randint(1,100)
                  t_intelligence = random.randint(1,100)
                  u_intelligence = random.randint(1,100)
                  v_intelligence = random.randint(1,100)
                  w_intelligence = random.randint(1,100)
                  x_intelligence = random.randint(1,100)
                  y_intelligence = random.randint(1,100)
                  z_intelligence = random.randint(1,100)
                  aa_intelligence = random.randint(1,100)
                  ab_intelligence = random.randint(1,100)
                  ac_intelligence = random.randint(1,100)
                  ad_intelligence = random.randint(1,100)
                  a_friendliness = random.randint(1,10)
                  b_friendliness = random.randint(1,10)
                  c_friendliness = random.randint(1,10)
                  d_friendliness = random.randint(1,10)
                  e_friendliness = random.randint(1,10)
                  f_friendliness = random.randint(1,10)
                  g_friendliness = random.randint(1,10)
                  h_friendliness = random.randint(1,10)
                  i_friendliness = random.randint(1,10)
                  j_friendliness = random.randint(1,10)
                  k_friendliness = random.randint(1,10)
                  l_friendliness = random.randint(1,10)
                  m_friendliness = random.randint(1,10)
                  n_friendliness = random.randint(1,10)
                  o_friendliness = random.randint(1,10)
                  p_friendliness = random.randint(1,10)
                  q_friendliness = random.randint(1,10)
                  r_friendliness = random.randint(1,10)
                  s_friendliness = random.randint(1,10)
                  t_friendliness = random.randint(1,10)
                  u_friendliness = random.randint(1,10)
                  v_friendliness = random.randint(1,10)
                  w_friendliness = random.randint(1,10)
                  x_friendliness = random.randint(1,10)
                  y_friendliness = random.randint(1,10)
                  z_friendliness = random.randint(1,10)
                  aa_friendliness = random.randint(1,10)
                  ab_friendliness = random.randint(1,10)
                  ac_friendliness = random.randint(1,10)
                  ad_friendliness = random.randint(1,10)
                  a_drool = random.randint(1,10)
                  b_drool = random.randint(1,10)
                  c_drool = random.randint(1,10)
                  d_drool = random.randint(1,10)
                  e_drool = random.randint(1,10)
                  f_drool = random.randint(1,10)
                  g_drool = random.randint(1,10)
                  h_drool = random.randint(1,10)
                  i_drool = random.randint(1,10)
                  j_drool = random.randint(1,10)
                  k_drool = random.randint(1,10)
                  l_drool = random.randint(1,10)
                  m_drool = random.randint(1,10)
                  n_drool = random.randint(1,10)
                  o_drool = random.randint(1,10)
                  p_drool = random.randint(1,10)
                  q_drool = random.randint(1,10)
                  r_drool = random.randint(1,10)
                  s_drool = random.randint(1,10)
                  t_drool = random.randint(1,10)
                  u_drool = random.randint(1,10)
                  v_drool = random.randint(1,10)
                  w_drool = random.randint(1,10)
                  x_drool = random.randint(1,10)
                  y_drool = random.randint(1,10)
                  z_drool = random.randint(1,10)
                  aa_drool = random.randint(1,10)
                  ab_drool = random.randint(1,10)
                  ac_drool = random.randint(1,10)
                  ad_drool = random.randint(1,10)
                  if cards_tbp <= 5:
                        print("Error! Cards selected is too low or not even. Returning to card selection...\n")
                        game()
                  elif cards_tbp >= 29:
                        print("Error! Cards selected is too high or not even. Returning to card selection...\n")
                        game()
                  elif cards_tbp == 6 or 8 or 10 or 12 or 14 or 16 or 18 or 20 or 22 or 24 or 26 or 28:
                        allocated_cards = []
                        player_cards = []
                        computer_cards = []
                        for i in range(0,cards_tbp/2):
                              random_card = random.randint(1,30)
                              if random_card == 1:
                                    random_card = 'a'
                              elif random_card == 2:
                                    random_card = 'b'
                              elif random_card == 3:
                                    random_card = 'c'
                              elif random_card == 4:
                                    random_card = 'd'
                              elif random_card == 5:
                                    random_card = 'e'
                              elif random_card == 6:
                                    random_card = 'f'
                              elif random_card == 7:
                                    random_card = 'g'
                              elif random_card == 8:
                                    random_card = 'h'
                              elif random_card == 9:
                                    random_card = 'i'
                              elif random_card == 10:
                                    random_card = 'j'
                              elif random_card == 11:
                                    random_card = 'k'
                              elif random_card == 12:
                                    random_card = 'l'
                              elif random_card == 13:
                                    random_card = 'm'
                              elif random_card == 14:
                                    random_card = 'n'
                              elif random_card == 15:
                                    random_card = 'o'
                              elif random_card == 16:
                                    random_card = 'p'
                              elif random_card == 17:
                                    random_card = 'q'
                              elif random_card == 18:
                                    random_card = 'r'
                              elif random_card == 19:
                                    random_card = 's'
                              elif random_card == 20:
                                    random_card = 't'
                              elif random_card == 21:
                                    random_card = 'u'
                              elif random_card == 22:
                                    random_card = 'v'
                              elif random_card == 23:
                                    random_card = 'w'
                              elif random_card == 24:
                                    random_card = 'x'
                              elif random_card == 25:
                                    random_card = 'y'
                              elif random_card == 26:
                                    random_card = 'z'
                              elif random_card == 27:
                                    random_card = 'aa'
                              elif random_card == 28:
                                    random_card = 'ab'
                              elif random_card == 29:
                                    random_card = 'ac'
                              elif random_card == 30:
                                    random_card = 'ad'
                              else:
                                    print("Unknown Error! Returing to card selection.")
                              if random_card not in allocated_cards:
								player_cards.append(random_card)
								allocated_cards.append(random_card)
                        print("Your cards are:")
                        for cards in range(0, len(player_cards)):
							if player_cards[cards] == 'a':
								print("\n\tAnnie the Afgan Hound")
							elif player_cards[cards] == 'b':
								print("\n\tBertie the Boxer")
							elif player_cards[cards] == 'c':
								print("\n\tBetty the Borzoi")
							elif player_cards[cards] == 'd':
								print("\n\tCharlie the Chihuahua")
							elif player_cards[cards] == 'e':
								print("\n\tChaz the Cockerspaniel")
							elif player_cards[cards] == 'f':
								print("\n\tDonald the Dalmation")
							elif player_cards[cards] == 'g':
								print("\n\tAlfie the Affenpinscher")
							elif player_cards[cards] == 'h':
								print("\n\tAlbert the Alaskan Klee Kai")
							elif player_cards[cards] == 'i':
								print("\n\tBernie the Black and Tan Coonhound")
							elif player_cards[cards] == 'j':
								print("\n\tChloe the Chinese Shar-Pei")
							elif player_cards[cards] == 'k':
								print("\n\tElizabeth the English Toy Spaniel")
							elif player_cards[cards] == 'l':
								print("\n\tJake the Japanese Chin")
							elif player_cards[cards] == 'm':
								print("\n\tKaty the Korean Jindo Dog")
							elif player_cards[cards] == 'n':
								print("\n\tKaapro the Kooikerhondje")
							elif player_cards[cards] == 'o':
								print("\n\tKa the Komondor")
							elif player_cards[cards] == 'p':
								print("\n\tMatt the Mutt")
							elif player_cards[cards] == 'q':
								print("\n\tNancy the Norfolk Terrier")
							elif player_cards[cards] == 'r':
								print("\n\tNoelle the Norwich Terrier")
							elif player_cards[cards] == 's':
								print("\n\tNatasha the Nova Scotia Tolling Retriever")
							elif player_cards[cards] == 't':
								print("\n\tStacy the Staffordshire Bull Terrier")
							elif player_cards[cards] == 'u':
								print("\n\tBrenda the Bull Dog")
							elif player_cards[cards] == 'v':
								print("\n\tDarcy the Dogo Argentino")
							elif player_cards[cards] == 'w':
								print("\n\tGlenda the German Shorthaired Pointer")
							elif player_cards[cards] == 'x':
								print("\n\tHerbet the Havanese")
							elif player_cards[cards] == 'y':
								print("\n\tPeter the Pekingese")
							elif player_cards[cards] == 'z':
								print("\n\tPerkie the Plott")
							elif player_cards[cards] == 'aa':
								print("\n\tPoppy the Puli")
							elif player_cards[cards] == 'ab':
								print("\n\tXenophon the Xoloitzcuintli")
							elif player_cards[cards] == 'ac':
								print("\n\tYork the Yorkipoo")
							elif player_cards[cards] == 'ad':
								print("\n\tSan the Samoyed")
							else:
								print("Error! Retruning to card selection")
								game()
                                    
                  else:
                        print("Unknown Error! Retrurning to card selection.")
                        game()
      else:
		  print("Error with selected number of cards. Returning to card selection.")
		  game()
		  
menu()#start the menu function
