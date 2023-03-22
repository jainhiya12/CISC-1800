# Hiya Jain
# Lab 06: Scrabble Score Tracker
# CISC 1800 - Introduction to Computer Programming

letter_score = {
  'A': 1, 'B': 3, 'C': 3, 'D': 2,'E': 1, 'F': 4, 'G': 2, 'H': 4,'I': 1, 'J': 8, 'K': 5, 'L': 1,'M': 3, 'N': 1, 'O': 1, 'P': 3,'Q': 10, 'R': 1, 'S': 1, 'T': 1,'U': 1, 'V': 4, 'W': 4, 'X': 8,'Y': 4, 'Z': 10}

def score_word(word):
  score = 0
  for ch in word:
    letter_value = letter_score[ch.upper()]
    score += letter_value
  return score

def add_players():
  print ("Welcome to theScrabble Score Calculator!\n")
  player_scores = {}
  player_counter = 1
  while True:
    if player_counter == 1:
      player_name = input("Enter your name: ")
      player_scores[player_name] = 0
      player_counter += 1
    
    player_name = input("Enter the name of another player: ")
    if player_name == ":s":
      break
    else:
      player_scores[player_name] = 0
      player_counter += 1
  return player_scores

def play_game():
  player_scores = add_players()
  print("Current scores: ", player_scores)
  counter = 0
  keys = list(player_scores.keys())
  while True:
    if counter >= len(keys):
      print("Current scores: ", player_scores)
      counter = 0

      current_word = input(f"{keys[counter]}, please enter a word: ")

      if current_word == ":q":
        break
      else:
        player_scores[keys[counter]] += score_word(current_word)
        counter += 1
    return player_scores

def main ():
  final_scores = play_game()
  print(f"Final scores: {final_scores}")
main ()
  
  
        
      
      

    
  
  
  
