from src.IA_UNO_basics import IA_UNO_basics
import random

class IA_UNO(IA_UNO_basics):    
    
    def applying_action_card(self,card):
        if(card[0][0] == 'X'): # BLOQUEIO
            self.block_card_action()
    
        elif(card[0][0] == 'R'): # REVERSO
            self.reverse_card_action()
         
        elif(card[0][0] == '+'): #SOMA DOIS 
            for card in self.take_two_cards_action():
                self.players.get_player_by_index(self.INDEX_WHO_IS_PLAYING+1).me_player.take_a_new_card(card)

        elif(card[0][0] == 'W'): #SOMA QUATRO
            for card in self.take_four_cards_action():
                self.players.get_player_by_index(self.INDEX_WHO_IS_PLAYING+1).me_player.take_a_new_card(card)
       
        elif(card[0][0] == 'C'): # ESCOLHA A COR
            self.CURRENTLY_CARD = self.uno_deck.uno(card[0],self.choose_a_new_color_card_action())
        
        #numbers cards action
        elif(card[0][0] == '0'): #can change hands with other person
            self.zero_action_card()
        elif(card[0][0] == '9'): #bater na mesa
            pass
            
      #  if(card[0][0] == '7' or self.STILL_A_ROUND_OF_7): #silence
        #    if(card[0][0] == '7'):
         #       self.STILL_A_ROUND_OF_7 = True
          #      self.seven_count = 1
           # self.seven_action_card()
            #self.seven_count +=1
            
            #if(self.seven_count == len(self.players)):
             #   self.STILL_A_ROUND_OF_7 = False
    
    def block_card_action(self):
        self.INDEX_WHO_IS_PLAYING += 1
    
    def reverse_card_action(self):
        ##getting the last player's position on vetor
        currently_player_name = self.players.vetor[self.INDEX_WHO_IS_PLAYING%4].me_player.name.split()
        currently_player_number = int(currently_player_name[1])
        
        ##reversing vetor
        self.players.vetor.reverse()
        
        #updating vector by currently player index
        self.INDEX_WHO_IS_PLAYING = self.players.get_vector_of_numbers().index(currently_player_number)
        
        #for ia_player in self.players.vetor:
         #   name = ia_player.me_player.name.split()
          #  if int(name[1]) == currently_player_number:
           #     self.INDEX_WHO_IS_PLAYING = i
            #i+=1

    def take_two_cards_action(self):
        if len(self.uno_deck.cards) < 2:
            self.refuel_deck()
        
        new_two_cards = [self.take_new_card_from_deck() for i in range(0,2)]
        return new_two_cards
    
    def take_four_cards_action(self):
        if len(self.uno_deck.cards) < 4:
            self.refuel_deck()

        new_four_cards = [self.take_new_card_from_deck() for i in range(0,4)]
        return new_four_cards
    
    def choose_a_new_color_card_action(self):
        new_color = random.sample(self.uno_deck.colors,1)
        return new_color[0]
    
    def seven_action_card(self):
        probability_of_saying_something = 20
        
        result = random.randint(1,101)
        
        if result <= probability_of_saying_something: #someone said something
            who_said = random.sample(self.players.vetor,1)
            new_card = self.take_new_card_from_deck()
            who_said[0].draw_from_deck(new_card) #puxa uma carta
            print("Someone falou no 7!")       
        
    def zero_action_card(self):
        q_cards_of_others_players = []
        player_q_cards = len(self.players.vetor[self.INDEX_WHO_IS_PLAYING%4].me_player.my_cards)
        
        for i in range(0, len(self.players)):
            q_cards_of_others_players.append(self.players.get_player_by_index(i))
        
        good_for_exchange = [ i  for i in q_cards_of_others_players if len(i.me_player.my_cards) < player_q_cards]

        if len(good_for_exchange) != 0:
            prob = random.randint(1,101)
            if prob >= 40: #60% de probabilidade de trocar
                #exchange!
                change_hand_with = random.sample(good_for_exchange,1)
                aux = change_hand_with[0].me_player.my_cards

                change_hand_with[0].me_player.my_cards = self.players.get_player_by_index(self.INDEX_WHO_IS_PLAYING%4).me_player.my_cards
                self.players.vetor[self.INDEX_WHO_IS_PLAYING%4].me_player.my_cards = aux

        else:
            #o jogador consegue ver as cartas do outro
            pass
                        