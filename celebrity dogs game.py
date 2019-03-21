#celebrity dogs game

#define global variables
all_cards = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','aa','ab','ac','ad']
p_cat = ''
c_cat = ''
p_cat_val = ''
c_cat_val = ''
winner=""

#import modules
import random

def clear():#function to clear screen
      for i in range(0,100):
            print("\n")

def menu(): #quick start
      menu_choice = raw_input("Play Game\nQuit\n>>> ")
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
      p_cat = ''
      c_cat = ''
      p_cat_val = ''
      c_cat_val = ''
      winner=""
      winner="player"
      possible_cards = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]#define number of cards that can be used
      cards_tbp = int(raw_input("\nHow many cards would you like to be played?\nThis includes you and the CPU\nThe number must be above 4, but below 30, and only an even number.\n>>>\t"))#ask for input and convert it into an integer
      print("You have selected to play " +str(cards_tbp) +" cards.\n")#print how many cards are selected
      selection = raw_input("Is this ok?\n>>>[Y\N] ")
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
                  a_exercise = random.randint(1,5) #randomly select variables
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
                  if cards_tbp <= 5: #check if number of cards is valid
                        print("Error! Cards selected is too low or not even. Returning to card selection...\n")
                        game()
                  elif cards_tbp >= 29:
                        print("Error! Cards selected is too high or not even. Returning to card selection...\n")
                        game()
                  elif cards_tbp == 6 or 8 or 10 or 12 or 14 or 16 or 18 or 20 or 22 or 24 or 26 or 28:
                        allocated_cards = []
                        player_cards = []
                        computer_cards = []
                        while len(player_cards) != (cards_tbp/2): #while the player has less than half of all cards played this game, do
                              random_card = random.choice(all_cards)
                              if random_card not in allocated_cards: #if the random card is not already being used, do
                                    player_cards.append(random_card) #give to player
                                    allocated_cards.append(random_card) #set as already being used
                        print("Your cards are:")#tell the player what cards they have
                        for cards in range(len(player_cards)-1): #repeat for the amount of cards that the player has
                              if player_cards[cards] == 'a': #tell the player the name of the cards they have
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
                        print("\n")
                        while len(computer_cards) != (cards_tbp/2): #while the computer has less cards than half the amount of cards being played this game, do
                              random_card = random.choice(all_cards)
                              if random_card not in allocated_cards: #if the random card is not already being used, do
                                    computer_cards.append(random_card) #give to computer
                                    allocated_cards.append(random_card) #set as already being used
                        while len(player_cards) != 0:
                              print("\nYour card is:")#tell the player what their card is.
                              if player_cards[len(player_cards)-1] == 'a':#if card == __ , do
                                    p_card_selected = 'a' #set active player card
                                    print("\nAnnie the Afgan Hound")#print name
                                    print("Intelligence =\t" +str(a_intelligence))#print intelligence
                                    print("Exercise =\t" +str(a_exercise))#print exercise
                                    print("Friendliness =\t" +str(a_friendliness))#print friendliness
                                    print("Drool =\t" +str(a_drool)) #print drool, do all this for other cards, up to 'ad'
                              elif player_cards[len(player_cards)-1] == 'b':
                                    p_card_selected = 'b'
                                    print("\nBertie the Boxer")
                                    print("Intelligence =\t" +str(b_intelligence))
                                    print("Exercise =\t" +str(b_exercise))
                                    print("Friendliness =\t" +str(b_friendliness))
                                    print("Drool =\t" +str(b_drool))
                              elif player_cards[len(player_cards)-1] == 'c':
                                    p_card_selected = 'c'
                                    print("\nBetty the Borzoi")
                                    print("Intelligence =\t" +str(c_intelligence))
                                    print("Exercise =\t" +str(c_exercise))
                                    print("Friendliness =\t" +str(c_friendliness))
                                    print("Drool =\t" +str(c_drool))
                              elif player_cards[len(player_cards)-1] == 'd':
                                    p_card_selected = 'd'
                                    print("\nCharlie the Chihuahua")
                                    print("Intelligence =\t" +str(d_intelligence))
                                    print("Exercise =\t" +str(d_exercise))
                                    print("Friendliness =\t" +str(d_friendliness))
                                    print("Drool =\t" +str(d_drool))
                              elif player_cards[len(player_cards)-1] == 'e':
                                    p_card_selected = 'e'
                                    print("\nChaz the Cockerspaniel")
                                    print("Intelligence =\t" +str(e_intelligence))
                                    print("Exercise =\t" +str(e_exercise))
                                    print("Friendliness =\t" +str(e_friendliness))
                                    print("Drool =\t" +str(e_drool))
                              elif player_cards[len(player_cards)-1] == 'f':
                                    p_card_selected = 'f'
                                    print("\nDonald the Dalmation")
                                    print("Intelligence =\t" +str(f_intelligence))
                                    print("Exercise =\t" +str(f_exercise))
                                    print("Friendliness =\t" +str(f_friendliness))
                                    print("Drool =\t" +str(f_drool))
                              elif player_cards[len(player_cards)-1] == 'g':
                                    p_card_selected = 'g'
                                    print("\nAlfie the Affenpinscher")
                                    print("Intelligence =\t" +str(g_intelligence))
                                    print("Exercise =\t" +str(g_exercise))
                                    print("Friendliness =\t" +str(g_friendliness))
                                    print("Drool =\t" +str(g_drool))
                              elif player_cards[len(player_cards)-1] == 'h':
                                    p_card_selected = 'h'
                                    print("\nAlbert the Alaskan Klee Kai")
                                    print("Intelligence =\t" +str(h_intelligence))
                                    print("Exercise =\t" +str(h_exercise))
                                    print("Friendliness =\t" +str(h_friendliness))
                                    print("Drool =\t" +str(h_drool))
                              elif player_cards[len(player_cards)-1] == 'i':
                                    p_card_selected = 'i'
                                    print("\nBernie the Black and Tan Coonhound")
                                    print("Intelligence =\t" +str(i_intelligence))
                                    print("Exercise =\t" +str(i_exercise))
                                    print("Friendliness =\t" +str(i_friendliness))
                                    print("Drool =\t" +str(i_drool))
                              elif player_cards[len(player_cards)-1] == 'j':
                                    p_card_selected = 'j'
                                    print("\nChloe the Chinese Shar-Pei")
                                    print("Intelligence =\t" +str(j_intelligence))
                                    print("Exercise =\t" +str(j_exercise))
                                    print("Friendliness =\t" +str(j_friendliness))
                                    print("Drool =\t" +str(j_drool))
                              elif player_cards[len(player_cards)-1] == 'k':
                                    p_card_selected = 'k'
                                    print("\nElizabeth the English Toy Spaniel")
                                    print("Intelligence =\t" +str(k_intelligence))
                                    print("Exercise =\t" +str(k_exercise))
                                    print("Friendliness =\t" +str(k_friendliness))
                                    print("Drool =\t" +str(k_drool))
                              elif player_cards[len(player_cards)-1] == 'l':
                                    p_card_selected = 'l'
                                    print("\nJake the Japanese Chin")
                                    print("Intelligence =\t" +str(l_intelligence))
                                    print("Exercise =\t" +str(l_exercise))
                                    print("Friendliness =\t" +str(l_friendliness))
                                    print("Drool =\t" +str(l_drool))
                              elif player_cards[len(player_cards)-1] == 'm':
                                    p_card_selected = 'm'
                                    print("\nKaty the Korean Jindo Dog")
                                    print("Intelligence =\t" +str(m_intelligence))
                                    print("Exercise =\t" +str(m_exercise))
                                    print("Friendliness =\t" +str(m_friendliness))
                                    print("Drool =\t" +str(m_drool))
                              elif player_cards[len(player_cards)-1] == 'n':
                                    p_card_selected = 'n'
                                    print("\nKaapro the Kooikerhondje")
                                    print("Intelligence =\t" +str(n_intelligence))
                                    print("Exercise =\t" +str(n_exercise))
                                    print("Friendliness =\t" +str(n_friendliness))
                                    print("Drool =\t" +str(n_drool))
                              elif player_cards[len(player_cards)-1] == 'o':
                                    p_card_selected = 'o'
                                    print("\nKa the Komondor")
                                    print("Intelligence =\t" +str(o_intelligence))
                                    print("Exercise =\t" +str(o_exercise))
                                    print("Friendliness =\t" +str(o_friendliness))
                                    print("Drool =\t" +str(o_drool))
                              elif player_cards[len(player_cards)-1] == 'p':
                                    p_card_selected = 'p'
                                    print("\nMatt the Mutt")
                                    print("Intelligence =\t" +str(p_intelligence))
                                    print("Exercise =\t" +str(p_exercise))
                                    print("Friendliness =\t" +str(p_friendliness))
                                    print("Drool =\t" +str(p_drool))
                              elif player_cards[len(player_cards)-1] == 'q':
                                    p_card_selected = 'q'
                                    print("\nNancy the Norfolk Terrier")
                                    print("Intelligence =\t" +str(q_intelligence))
                                    print("Exercise =\t" +str(q_exercise))
                                    print("Friendliness =\t" +str(q_friendliness))
                                    print("Drool =\t" +str(q_drool))
                              elif player_cards[len(player_cards)-1] == 'r':
                                    p_card_selected = 'r'
                                    print("\nNoelle the Norwich Terrier")
                                    print("Intelligence =\t" +str(r_intelligence))
                                    print("Exercise =\t" +str(r_exercise))
                                    print("Friendliness =\t" +str(r_friendliness))
                                    print("Drool =\t" +str(r_drool))
                              elif player_cards[len(player_cards)-1] == 's':
                                    p_card_selected = 's'
                                    print("\nNatasha the Nova Scotia Tolling Retriever")
                                    print("Intelligence =\t" +str(s_intelligence))
                                    print("Exercise =\t" +str(s_exercise))
                                    print("Friendliness =\t" +str(s_friendliness))
                                    print("Drool =\t" +str(s_drool))
                              elif player_cards[len(player_cards)-1] == 't':
                                    p_card_selected = 't'
                                    print("\nStacy the Staffordshire Bull Terrier")
                                    print("Intelligence =\t" +str(t_intelligence))
                                    print("Exercise =\t" +str(t_exercise))
                                    print("Friendliness =\t" +str(t_friendliness))
                                    print("Drool =\t" +str(t_drool))
                              elif player_cards[len(player_cards)-1] == 'u':
                                    p_card_selected = 'u'
                                    print("\nBrenda the Bull Dog")
                                    print("Intelligence =\t" +str(u_intelligence))
                                    print("Exercise =\t" +str(u_exercise))
                                    print("Friendliness =\t" +str(u_friendliness))
                                    print("Drool =\t" +str(u_drool))
                              elif player_cards[len(player_cards)-1] == 'v':
                                    p_card_selected = 'v'
                                    print("\nDarcy the Dogo Argentino")
                                    print("Intelligence =\t" +str(v_intelligence))
                                    print("Exercise =\t" +str(v_exercise))
                                    print("Friendliness =\t" +str(v_friendliness))
                                    print("Drool =\t" +str(v_drool))
                              elif player_cards[len(player_cards)-1] == 'w':
                                    p_card_selected = 'w'
                                    print("\nGlenda the German Shorthaired Pointer")
                                    print("Intelligence =\t" +str(w_intelligence))
                                    print("Exercise =\t" +str(w_exercise))
                                    print("Friendliness =\t" +str(w_friendliness))
                                    print("Drool =\t" +str(w_drool))
                              elif player_cards[len(player_cards)-1] == 'x':
                                    p_card_selected = 'x'
                                    print("\nHerbet the Havanese")
                                    print("Intelligence =\t" +str(x_intelligence))
                                    print("Exercise =\t" +str(x_exercise))
                                    print("Friendliness =\t" +str(x_friendliness))
                                    print("Drool =\t" +str(x_drool))
                              elif player_cards[len(player_cards)-1] == 'y':
                                    p_card_selected = 'y'
                                    print("\nPeter the Pekingese")
                                    print("Intelligence =\t" +str(y_intelligence))
                                    print("Exercise =\t" +str(y_exercise))
                                    print("Friendliness =\t" +str(y_friendliness))
                                    print("Drool =\t" +str(y_drool))
                              elif player_cards[len(player_cards)-1] == 'z':
                                    p_card_selected = 'z'
                                    print("\nPerkie the Plott")
                                    print("Intelligence =\t" +str(z_intelligence))
                                    print("Exercise =\t" +str(z_exercise))
                                    print("Friendliness =\t" +str(z_friendliness))
                                    print("Drool =\t" +str(z_drool))
                              elif player_cards[len(player_cards)-1] == 'aa':
                                    p_card_selected = 'aa'
                                    print("\nPoppy the Puli")
                                    print("Intelligence =\t" +str(aa_intelligence))
                                    print("Exercise =\t" +str(aa_exercise))
                                    print("Friendliness =\t" +str(aa_friendliness))
                                    print("Drool =\t" +str(aa_drool))
                              elif player_cards[len(player_cards)-1] == 'ab':
                                    p_card_selected = 'ab'
                                    print("\nXenophon the Xoloitzcuintli")
                                    print("Intelligence =\t" +str(ab_intelligence))
                                    print("Exercise =\t" +str(ab_exercise))
                                    print("Friendliness =\t" +str(ab_friendliness))
                                    print("Drool =\t" +str(ab_drool))
                              elif player_cards[len(player_cards)-1] == 'ac':
                                    p_card_selected = 'ac'
                                    print("\nYork the Yorkipoo")
                                    print("Intelligence =\t" +str(ac_intelligence))
                                    print("Exercise =\t" +str(ac_exercise))
                                    print("Friendliness =\t" +str(ac_friendliness))
                                    print("Drool =\t" +str(ac_drool))
                              elif player_cards[len(player_cards)-1] == 'ad':
                                    p_card_selected = 'ad'
                                    print("\nSan the Samoyed")
                                    print("Intelligence =\t" +str(ad_intelligence))
                                    print("Exercise =\t" +str(ad_exercise))
                                    print("Friendliness =\t" +str(ad_friendliness))
                                    print("Drool =\t" +str(ad_drool))
                              print("")
                              p_cat = ''
                              if winner == "player":
                                    while p_cat != 'intelligence' or 'exercise' or 'friendliness' or 'drool':
                                          p_cat = raw_input("\nWhat category would you like to use?\n>>> ") #Ask what category the player would like to use
                                          p_cat = p_cat.lower() #set p_cat to all lower-case
                                          if p_cat == 'intelligence': # if p_cat is 'drool', do
                                                print("Ok")
                                                c_cat = 'Intelligence'
                                          elif p_cat == 'exercise': #if p_cat is 'exercise', do
                                                print("Ok")
                                                c_cat = 'Excercise'
                                                break
                                          elif p_cat == 'friendliness': #if p_cat is 'friendliness', do
                                                print("Ok")
                                                c_cat = 'Friendliness'
                                                break
                                          elif p_cat == 'drool': #if p_cat is 'drool', do
                                                print("Ok")
                                                c_cat = 'Drool'
                                                break
                                          else: #if p_cat is none, do, and repeat loop
                                                print("")#error
                                                
                              elif winner == "computer":
                                    all_categories = ['Intelligence', 'Exercise', 'Friendliness', 'Drool']
                                    c_cat = random.choice(all_categories)
                                    if c_cat == 'Intelligence':
                                          p_cat = 'intelligence'
                                    elif c_cat == 'Exercise':
                                          p_cat = 'exercise'
                                    elif c_cat == 'Friendliness':
                                          p_cat = 'friendliness'
                                    elif c_cat == 'Drool':
                                          p_cat = 'drool'
                                    else:
                                          print("Error")
                              else:
                                    print("Error")
                              if True:
                                    if p_cat == 'intelligence':#set p_cat_val to the correct value for the selected category
                                          if player_cards[len(player_cards)-1] == 'a':
                                                p_cat_val = a_intelligence
                                          elif player_cards[len(player_cards)-1] == 'b':
                                                p_cat_val = b_intelligence
                                          elif player_cards[len(player_cards)-1] == 'c':
                                                p_cat_val = c_intelligence
                                          elif player_cards[len(player_cards)-1] == 'd':
                                                p_cat_val = d_intelligence
                                          elif player_cards[len(player_cards)-1] == 'e':
                                                p_cat_val = e_intelligence
                                          elif player_cards[len(player_cards)-1] == 'f':
                                                p_cat_val = f_intelligence
                                          elif player_cards[len(player_cards)-1] == 'g':
                                                p_cat_val = g_intelligence
                                          elif player_cards[len(player_cards)-1] == 'h':
                                                p_cat_val = h_intelligence
                                          elif player_cards[len(player_cards)-1] == 'i':
                                                p_cat_val = i_intelligence
                                          elif player_cards[len(player_cards)-1] == 'j':
                                                p_cat_val = j_intelligence
                                          elif player_cards[len(player_cards)-1] == 'k':
                                                p_cat_val = k_intelligence
                                          elif player_cards[len(player_cards)-1] == 'l':
                                                p_cat_val = l_intelligence
                                          elif player_cards[len(player_cards)-1] == 'm':
                                                p_cat_val = m_intelligence
                                          elif player_cards[len(player_cards)-1] == 'n':
                                                p_cat_val = n_intelligence
                                          elif player_cards[len(player_cards)-1] == 'o':
                                                p_cat_val = o_intelligence
                                          elif player_cards[len(player_cards)-1] == 'p':
                                                p_cat_val = p_intelligence
                                          elif player_cards[len(player_cards)-1] == 'q':
                                                p_cat_val = q_intelligence
                                          elif player_cards[len(player_cards)-1] == 'r':
                                                p_cat_val = r_intelligence
                                          elif player_cards[len(player_cards)-1] == 's':
                                                p_cat_val = s_intelligence
                                          elif player_cards[len(player_cards)-1] == 't':
                                                p_cat_val = t_intelligence
                                          elif player_cards[len(player_cards)-1] == 'u':
                                                p_cat_val = u_intelligence
                                          elif player_cards[len(player_cards)-1] == 'v':
                                                p_cat_val = v_intelligence
                                          elif player_cards[len(player_cards)-1] == 'w':
                                                p_cat_val = w_intelligence
                                          elif player_cards[len(player_cards)-1] == 'x':
                                                p_cat_val = x_intelligence
                                          elif player_cards[len(player_cards)-1] == 'y':
                                                p_cat_val = y_intelligence
                                          elif player_cards[len(player_cards)-1] == 'z':
                                                p_cat_val = z_intelligence
                                          elif player_cards[len(player_cards)-1] == 'aa':
                                                p_cat_val = aa_intelligence
                                          elif player_cards[len(player_cards)-1] == 'ab':
                                                p_cat_val = ab_intelligence
                                          elif player_cards[len(player_cards)-1] == 'ac':
                                                p_cat_val = ac_intelligence
                                          elif player_cards[len(player_cards)-1] == 'ad':
                                                p_cat_val = ad_intelligence
                                          else:
                                                print("Error")
                                    elif p_cat == 'exercise':
                                          if player_cards[len(player_cards)-1] == 'a':
                                                p_cat_val = a_exercise
                                          elif player_cards[len(player_cards)-1] == 'b':
                                                p_cat_val = b_exercise
                                          elif player_cards[len(player_cards)-1] == 'c':
                                                p_cat_val = c_exercise
                                          elif player_cards[len(player_cards)-1] == 'd':
                                                p_cat_val = d_exercise
                                          elif player_cards[len(player_cards)-1] == 'e':
                                                p_cat_val = e_exercise
                                          elif player_cards[len(player_cards)-1] == 'f':
                                                p_cat_val = f_exercise
                                          elif player_cards[len(player_cards)-1] == 'g':
                                                p_cat_val = g_exercise
                                          elif player_cards[len(player_cards)-1] == 'h':
                                                p_cat_val = h_exercise
                                          elif player_cards[len(player_cards)-1] == 'i':
                                                p_cat_val = i_exercise
                                          elif player_cards[len(player_cards)-1] == 'j':
                                                p_cat_val = j_exercise
                                          elif player_cards[len(player_cards)-1] == 'k':
                                                p_cat_val = k_exercise
                                          elif player_cards[len(player_cards)-1] == 'l':
                                                p_cat_val = l_exercise
                                          elif player_cards[len(player_cards)-1] == 'm':
                                                p_cat_val = m_exercise
                                          elif player_cards[len(player_cards)-1] == 'n':
                                                p_cat_val = n_exercise
                                          elif player_cards[len(player_cards)-1] == 'o':
                                                p_cat_val = o_exercise
                                          elif player_cards[len(player_cards)-1] == 'p':
                                                p_cat_val = p_exercise
                                          elif player_cards[len(player_cards)-1] == 'q':
                                                p_cat_val = q_exercise
                                          elif player_cards[len(player_cards)-1] == 'r':
                                                p_cat_val = r_exercise
                                          elif player_cards[len(player_cards)-1] == 's':
                                                p_cat_val = s_exercise
                                          elif player_cards[len(player_cards)-1] == 't':
                                                p_cat_val = t_exercise
                                          elif player_cards[len(player_cards)-1] == 'u':
                                                p_cat_val = u_exercise
                                          elif player_cards[len(player_cards)-1] == 'v':
                                                p_cat_val = v_exercise
                                          elif player_cards[len(player_cards)-1] == 'w':
                                                p_cat_val = w_exercise
                                          elif player_cards[len(player_cards)-1] == 'x':
                                                p_cat_val = x_exercise
                                          elif player_cards[len(player_cards)-1] == 'y':
                                                p_cat_val = y_exercise
                                          elif player_cards[len(player_cards)-1] == 'z':
                                                p_cat_val = z_exercise
                                          elif player_cards[len(player_cards)-1] == 'aa':
                                                p_cat_val = aa_exercise
                                          elif player_cards[len(player_cards)-1] == 'ab':
                                                p_cat_val = ab_exercise
                                          elif player_cards[len(player_cards)-1] == 'ac':
                                                p_cat_val = ac_exercise
                                          elif player_cards[len(player_cards)-1] == 'ad':
                                                p_cat_val = ad_exercise
                                          else:
                                                print("")#error
                                    elif p_cat == 'friendliness':
                                          if player_cards[len(player_cards)-1] == 'a':
                                                p_cat_val = a_friendliness
                                          elif player_cards[len(player_cards)-1] == 'b':
                                                p_cat_val = b_friendliness
                                          elif player_cards[len(player_cards)-1] == 'c':
                                                p_cat_val = c_friendliness
                                          elif player_cards[len(player_cards)-1] == 'd':
                                                p_cat_val = d_friendliness
                                          elif player_cards[len(player_cards)-1] == 'e':
                                                p_cat_val = e_friendliness
                                          elif player_cards[len(player_cards)-1] == 'f':
                                                p_cat_val = f_friendliness
                                          elif player_cards[len(player_cards)-1] == 'g':
                                                p_cat_val = g_friendliness
                                          elif player_cards[len(player_cards)-1] == 'h':
                                                p_cat_val = h_friendliness
                                          elif player_cards[len(player_cards)-1] == 'i':
                                                p_cat_val = i_friendliness
                                          elif player_cards[len(player_cards)-1] == 'j':
                                                p_cat_val = j_friendliness
                                          elif player_cards[len(player_cards)-1] == 'k':
                                                p_cat_val = k_friendliness
                                          elif player_cards[len(player_cards)-1] == 'l':
                                                p_cat_val = l_friendliness
                                          elif player_cards[len(player_cards)-1] == 'm':
                                                p_cat_val = m_friendliness
                                          elif player_cards[len(player_cards)-1] == 'n':
                                                p_cat_val = n_friendliness
                                          elif player_cards[len(player_cards)-1] == 'o':
                                                p_cat_val = o_friendliness
                                          elif player_cards[len(player_cards)-1] == 'p':
                                                p_cat_val = p_friendliness
                                          elif player_cards[len(player_cards)-1] == 'q':
                                                p_cat_val = q_friendliness
                                          elif player_cards[len(player_cards)-1] == 'r':
                                                p_cat_val = r_friendliness
                                          elif player_cards[len(player_cards)-1] == 's':
                                                p_cat_val = s_friendliness
                                          elif player_cards[len(player_cards)-1] == 't':
                                                p_cat_val = t_friendliness
                                          elif player_cards[len(player_cards)-1] == 'u':
                                                p_cat_val = u_friendliness
                                          elif player_cards[len(player_cards)-1] == 'v':
                                                p_cat_val = v_friendliness
                                          elif player_cards[len(player_cards)-1] == 'w':
                                                p_cat_val = w_friendliness
                                          elif player_cards[len(player_cards)-1] == 'x':
                                                p_cat_val = x_friendliness
                                          elif player_cards[len(player_cards)-1] == 'y':
                                                p_cat_val = y_friendliness
                                          elif player_cards[len(player_cards)-1] == 'z':
                                                p_cat_val = z_friendliness
                                          elif player_cards[len(player_cards)-1] == 'aa':
                                                p_cat_val = aa_friendliness
                                          elif player_cards[len(player_cards)-1] == 'ab':
                                                p_cat_val = ab_friendliness
                                          elif player_cards[len(player_cards)-1] == 'ac':
                                                p_cat_val = ac_friendliness
                                          elif player_cards[len(player_cards)-1] == 'ad':
                                                p_cat_val = ad_friendliness
                                          else:
                                                print("Error")
                                    elif p_cat == 'drool':
                                          if player_cards[len(player_cards)-1] == 'a':
                                                p_cat_val = a_drool
                                          elif player_cards[len(player_cards)-1] == 'b':
                                                p_cat_val = b_drool
                                          elif player_cards[len(player_cards)-1] == 'c':
                                                p_cat_val = c_drool
                                          elif player_cards[len(player_cards)-1] == 'd':
                                                p_cat_val = d_drool
                                          elif player_cards[len(player_cards)-1] == 'e':
                                                p_cat_val = e_drool
                                          elif player_cards[len(player_cards)-1] == 'f':
                                                p_cat_val = f_drool
                                          elif player_cards[len(player_cards)-1] == 'g':
                                                p_cat_val = g_drool
                                          elif player_cards[len(player_cards)-1] == 'h':
                                                p_cat_val = h_drool
                                          elif player_cards[len(player_cards)-1] == 'i':
                                                p_cat_val = i_drool
                                          elif player_cards[len(player_cards)-1] == 'j':
                                                p_cat_val = j_drool
                                          elif player_cards[len(player_cards)-1] == 'k':
                                                p_cat_val = k_drool
                                          elif player_cards[len(player_cards)-1] == 'l':
                                                p_cat_val = l_drool
                                          elif player_cards[len(player_cards)-1] == 'm':
                                                p_cat_val = m_drool
                                          elif player_cards[len(player_cards)-1] == 'n':
                                                p_cat_val = n_drool
                                          elif player_cards[len(player_cards)-1] == 'o':
                                                p_cat_val = o_drool
                                          elif player_cards[len(player_cards)-1] == 'p':
                                                p_cat_val = p_drool
                                          elif player_cards[len(player_cards)-1] == 'q':
                                                p_cat_val = q_drool
                                          elif player_cards[len(player_cards)-1] == 'r':
                                                p_cat_val = r_drool
                                          elif player_cards[len(player_cards)-1] == 's':
                                                p_cat_val = s_drool
                                          elif player_cards[len(player_cards)-1] == 't':
                                                p_cat_val = t_drool
                                          elif player_cards[len(player_cards)-1] == 'u':
                                                p_cat_val = u_drool
                                          elif player_cards[len(player_cards)-1] == 'v':
                                                p_cat_val = v_drool
                                          elif player_cards[len(player_cards)-1] == 'w':
                                                p_cat_val = w_drool
                                          elif player_cards[len(player_cards)-1] == 'x':
                                                p_cat_val = x_drool
                                          elif player_cards[len(player_cards)-1] == 'y':
                                                p_cat_val = y_drool
                                          elif player_cards[len(player_cards)-1] == 'z':
                                                p_cat_val = z_drool
                                          elif player_cards[len(player_cards)-1] == 'aa':
                                                p_cat_val = aa_drool
                                          elif player_cards[len(player_cards)-1] == 'ab':
                                                p_cat_val = ab_drool
                                          elif player_cards[len(player_cards)-1] == 'ac':
                                                p_cat_val = ac_drool
                                          elif player_cards[len(player_cards)-1] == 'ad':
                                                p_cat_val = ad_drool
                                          else:
                                                print("Error")
                                    else:
                                          print("Error!")
                                    if c_cat == "Intelligence":
                                          if computer_cards[len(computer_cards)-1] == 'a':
                                                c_cat_val = a_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'b':
                                                c_cat_val = b_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'c':
                                                c_cat_val = c_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'd':
                                                c_cat_val = d_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'e':
                                                c_cat_val = e_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'f':
                                                c_cat_val = f_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'g':
                                                c_cat_val = g_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'h':
                                                c_cat_val = h_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'i':
                                                c_cat_val = i_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'j':
                                                c_cat_val = j_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'k':
                                                c_cat_val = k_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'l':
                                                c_cat_val = l_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'm':
                                                c_cat_val = m_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'n':
                                                c_cat_val = n_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'o':
                                                c_cat_val = o_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'p':
                                                c_cat_val = p_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'q':
                                                c_cat_val = q_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'r':
                                                c_cat_val = r_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 's':
                                                c_cat_val = s_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 't':
                                                c_cat_val = t_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'u':
                                                c_cat_val = u_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'v':
                                                c_cat_val = v_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'w':
                                                c_cat_val = w_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'x':
                                                c_cat_val = x_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'y':
                                                c_cat_val = y_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'z':
                                                c_cat_val = z_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'aa':
                                                c_cat_val = aa_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'ab':
                                                c_cat_val = ab_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'ac':
                                                c_cat_val = ac_intelligence
                                          elif computer_cards[len(computer_cards)-1] == 'ad':
                                                c_cat_val = ad_intelligence
                                          else:
                                                print("Error")
                                    elif c_cat == 'Exercise':
                                          if computer_cards[len(computer_cards)-1] == 'a':
                                                c_cat_val = a_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'b':
                                                c_cat_val = b_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'c':
                                                c_cat_val = c_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'd':
                                                c_cat_val = d_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'e':
                                                c_cat_val = e_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'f':
                                                c_cat_val = f_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'g':
                                                c_cat_val = g_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'h':
                                                c_cat_val = h_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'i':
                                                c_cat_val = i_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'j':
                                                c_cat_val = j_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'k':
                                                c_cat_val = k_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'l':
                                                c_cat_val = l_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'm':
                                                c_cat_val = m_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'n':
                                                c_cat_val = n_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'o':
                                                c_cat_val = o_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'p':
                                                c_cat_val = p_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'q':
                                                c_cat_val = q_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'r':
                                                c_cat_val = r_exercise
                                          elif computer_cards[len(computer_cards)-1] == 's':
                                                c_cat_val = s_exercise
                                          elif computer_cards[len(computer_cards)-1] == 't':
                                                c_cat_val = t_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'u':
                                                c_cat_val = u_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'v':
                                                c_cat_val = v_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'w':
                                                c_cat_val = w_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'x':
                                                c_cat_val = x_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'y':
                                                c_cat_val = y_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'z':
                                                c_cat_val = z_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'aa':
                                                c_cat_val = aa_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'ab':
                                                c_cat_val = ab_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'ac':
                                                c_cat_val = ac_exercise
                                          elif computer_cards[len(computer_cards)-1] == 'ad':
                                                c_cat_val = ad_exercise
                                          else:
                                                print("")
                                    elif c_cat == 'Friendliness':
                                          if computer_cards[len(computer_cards)-1] == 'a':
                                                c_cat_val = a_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'b':
                                                c_cat_val = b_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'c':
                                                c_cat_val = c_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'd':
                                                c_cat_val = d_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'e':
                                                c_cat_val = e_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'f':
                                                c_cat_val = f_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'g':
                                                c_cat_val = g_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'h':
                                                c_cat_val = h_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'i':
                                                c_cat_val = i_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'j':
                                                c_cat_val = j_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'k':
                                                c_cat_val = k_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'l':
                                                c_cat_val = l_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'm':
                                                c_cat_val = m_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'n':
                                                c_cat_val = n_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'o':
                                                c_cat_val = o_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'p':
                                                c_cat_val = p_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'q':
                                                c_cat_val = q_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'r':
                                                c_cat_val = r_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 's':
                                                c_cat_val = s_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 't':
                                                c_cat_val = t_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'u':
                                                c_cat_val = u_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'v':
                                                c_cat_val = v_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'w':
                                                c_cat_val = w_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'x':
                                                c_cat_val = x_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'y':
                                                c_cat_val = y_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'z':
                                                c_cat_val = z_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'aa':
                                                c_cat_val = aa_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'ab':
                                                c_cat_val = ab_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'ac':
                                                c_cat_val = ac_friendliness
                                          elif computer_cards[len(computer_cards)-1] == 'ad':
                                                c_cat_val = ad_friendliness
                                          else:
                                                print("Error")
                                    elif c_cat == 'Drool':
                                          if computer_cards[len(computer_cards)-1] == 'a':
                                                c_cat_val = a_drool
                                          elif computer_cards[len(computer_cards)-1] == 'b':
                                                c_cat_val = b_drool
                                          elif computer_cards[len(computer_cards)-1] == 'c':
                                                c_cat_val = c_drool
                                          elif computer_cards[len(computer_cards)-1] == 'd':
                                                c_cat_val = d_drool
                                          elif computer_cards[len(computer_cards)-1] == 'e':
                                                c_cat_val = e_drool
                                          elif computer_cards[len(computer_cards)-1] == 'f':
                                                c_cat_val = f_drool
                                          elif computer_cards[len(computer_cards)-1] == 'g':
                                                c_cat_val = g_drool
                                          elif computer_cards[len(computer_cards)-1] == 'h':
                                                c_cat_val = h_drool
                                          elif computer_cards[len(computer_cards)-1] == 'i':
                                                c_cat_val = i_drool
                                          elif computer_cards[len(computer_cards)-1] == 'j':
                                                c_cat_val = j_drool
                                          elif computer_cards[len(computer_cards)-1] == 'k':
                                                c_cat_val = k_drool
                                          elif computer_cards[len(computer_cards)-1] == 'l':
                                                c_cat_val = l_drool
                                          elif computer_cards[len(computer_cards)-1] == 'm':
                                                c_cat_val = m_drool
                                          elif computer_cards[len(computer_cards)-1] == 'n':
                                                c_cat_val = n_drool
                                          elif computer_cards[len(computer_cards)-1] == 'o':
                                                c_cat_val = o_drool
                                          elif computer_cards[len(computer_cards)-1] == 'p':
                                                c_cat_val = p_drool
                                          elif computer_cards[len(computer_cards)-1] == 'q':
                                                c_cat_val = q_drool
                                          elif computer_cards[len(computer_cards)-1] == 'r':
                                                c_cat_val = r_drool
                                          elif computer_cards[len(computer_cards)-1] == 's':
                                                c_cat_val = s_drool
                                          elif computer_cards[len(computer_cards)-1] == 't':
                                                c_cat_val = t_drool
                                          elif computer_cards[len(computer_cards)-1] == 'u':
                                                c_cat_val = u_drool
                                          elif computer_cards[len(computer_cards)-1] == 'v':
                                                c_cat_val = v_drool
                                          elif computer_cards[len(computer_cards)-1] == 'w':
                                                c_cat_val = w_drool
                                          elif computer_cards[len(computer_cards)-1] == 'x':
                                                c_cat_val = x_drool
                                          elif computer_cards[len(computer_cards)-1] == 'y':
                                                c_cat_val = y_drool
                                          elif computer_cards[len(computer_cards)-1] == 'z':
                                                c_cat_val = z_drool
                                          elif computer_cards[len(computer_cards)-1] == 'aa':
                                                c_cat_val = aa_drool
                                          elif computer_cards[len(computer_cards)-1] == 'ab':
                                                c_cat_val = ab_drool
                                          elif computer_cards[len(computer_cards)-1] == 'ac':
                                                c_cat_val = ac_drool
                                          elif computer_cards[len(computer_cards)-1] == 'ad':
                                                c_cat_val = ad_drool
                                          else:
                                                print("Error")
                                    else:
                                          print("Error!")
                              if p_cat == 'intelligence':
                                    if p_cat_val > c_cat_val:
                                          print("You had a higher score than the computer!\nYou won!")
                                          card_tbm = computer_cards[len(computer_cards)-1]
                                          computer_cards.pop(len(computer_cards)-1)
                                          player_cards.append(card_tbm)
                                          
                                          card_tbm = player_cards[len(player_cards)-1]
                                          player_cards.pop(len(player_cards)-1)
                                          player_cards.append(card_tbm)
                                          
                                          winner="player"
                                    elif p_cat_val == c_cat_val:
                                          print("You and the computer drew.\nYou get the cards.")
                                          card_tbm = computer_cards[len(computer_cards)-1]
                                          computer_cards.pop(len(computer_cards)-1)
                                          player_cards.append(card_tbm)
                                          
                                          card_tbm = player_cards[len(player_cards)-1]
                                          player_cards.pop(len(player_cards)-1)
                                          player_cards.append(card_tbm)
                                          
                                          winner="player"
                                    else:
                                          print("The computer had a higher score than you.\nThe computer won.")
                                          card_tbm = player_cards[len(player_cards)-1]
                                          player_cards.pop(len(player_cards)-1)
                                          computer_cards.append(card_tbm)

                                          card_tbm = computer_cards[len(computer_cards)-1]
                                          computer_cards.pop(len(computer_cards)-1)
                                          computer_cards.append(card_tbm)

                                          winner="computer"
                              elif p_cat == 'exercise':
                                    if p_cat_val > c_cat_val:
                                          print("You had a higher score than the computer!\nYou won!")
                                          card_tbm = computer_cards[len(computer_cards)-1]
                                          computer_cards.pop(len(computer_cards)-1)
                                          player_cards.append(card_tbm)

                                          card_tbm = player_cards[len(player_cards)-1]
                                          player_cards.pop(len(player_cards)-1)
                                          player_cards.append(card_tbm)

                                          winner="player"
                                    elif p_cat_val == c_cat_val:
                                          print("You and the computer drew.\nYou get the cards.")
                                          card_tbm = computer_cards[len(computer_cards)-1]
                                          computer_cards.pop(len(computer_cards)-1)
                                          player_cards.append(card_tbm)

                                          card_tbm = player_cards[len(player_cards)-1]
                                          player_cards.pop(len(player_cards)-1)
                                          player_cards.append(card_tbm)
                                          
                                          winner="player"
                                    else:
                                          print("The computer had a higher score than you.\nThe computer won.")
                                          card_tbm = player_cards[len(player_cards)-1]
                                          player_cards.pop(len(player_cards)-1)
                                          computer_cards.append(card_tbm)

                                          card_tbm = computer_cards[len(computer_cards)-1]
                                          computer_cards.pop(len(computer_cards)-1)
                                          computer_cards.append(card_tbm)
                                          
                                          winner="computer"
                              elif p_cat == 'friendliness':
                                    if p_cat_val > c_cat_val:
                                          print("You had a higher score than the computer!\nYou won!")
                                          card_tbm = computer_cards[len(computer_cards)-1]
                                          computer_cards.pop(len(computer_cards)-1)
                                          player_cards.append(card_tbm)

                                          card_tbm = player_cards[len(player_cards)-1]
                                          player_cards.pop(len(player_cards)-1)
                                          player_cards.append(card_tbm)

                                          winner="player"
                                    elif p_cat_val == c_cat_val:
                                          print("You and the computer drew.\nYou get the cards.")
                                          card_tbm = computer_cards[len(computer_cards)-1]
                                          computer_cards.pop(len(computer_cards)-1)
                                          player_cards.append(card_tbm)

                                          card_tbm = player_cards[len(player_cards)-1]
                                          player_cards.pop(len(player_cards)-1)
                                          player_cards.append(card_tbm)

                                          winner="player"
                                    else:
                                          print("The computer had a higher score than you.\nThe computer won.")
                                          card_tbm = player_cards[len(player_cards)-1]
                                          player_cards.pop(len(player_cards)-1)
                                          computer_cards.append(card_tbm)

                                          card_tbm = computer_cards[len(computer_cards)-1]
                                          computer_cards.pop(len(computer_cards)-1)
                                          computer_cards.append(card_tbm)

                                          winner="computer"
                              elif p_cat == 'drool':
                                    if p_cat_val < c_cat_val:
                                          print("You had a lower score than the computer!\nYou won!")
                                          card_tbm = computer_cards[len(computer_cards)-1]
                                          computer_cards.pop(len(computer_cards)-1)
                                          player_cards.append(card_tbm)

                                          card_tbm = player_cards[len(player_cards)-1]
                                          player_cards.pop(len(player_cards)-1)
                                          player_cards.append(card_tbm)

                                          winner="player"
                                    elif p_cat_val == c_cat_val:
                                          print("You and the computer drew.\nYou get the cards.")
                                          card_tbm = computer_cards[len(computer_cards)-1]
                                          computer_cards.pop(len(computer_cards)-1)
                                          player_cards.append(card_tbm)

                                          card_tbm = player_cards[len(player_cards)-1]
                                          player_cards.pop(len(player_cards)-1)
                                          player_cards.append(card_tbm)

                                          winner="player"
                                    else:
                                          print("The computer had a lower score than you.\nThe computer won.")
                                          card_tbm = player_cards[len(player_cards)-1]
                                          player_cards.pop(len(player_cards)-1)
                                          computer_cards.append(card_tbm)

                                          card_tbm = computer_cards[len(computer_cards)-1]
                                          computer_cards.pop(len(computer_cards)-1)
                                          computer_cards.append(card_tbm)

                                          winner="computer"
                              else:
                                    print("Fatal Error!")

                              if len(player_cards) == cards_tbp or len(computer_cards) == int('0'):
                                    print("Well done, you won!")
                              elif len(player_cards) == int('0') or len(computer_cards) == cards_tbp:
                                    print("Bad luck, you lost.")
                              else:
                                    print("") #Do literally nothing
                  else:
                        print("Unknown Error! Retrurning to card selection.")
                        game()#return to card selection
      else:
              print("Error with selected number of cards. Returning to card selection.")
              game()#return to card selection

def finish():
      if len(player_cards) == 0:
            print("Bad luck, you lost.")
      elif len(computer_cards) == 0:
            print("Well done, you won!")
      elif len(computer_cards) and len(player_cards) != 0:
            print("Error")
            

menu()#start the menu function
