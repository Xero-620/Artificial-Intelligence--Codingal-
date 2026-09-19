import random

def get_user_choice():
    while True:
        choice = input("Enter Rock, Paper, or Scissors (or 'quit' to exit): ").strip().capitalize()
        if choice in ['Rock', 'Paper', 'Scissors', 'Quit']:
            return choice
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")

def get_ai_choice(player_history):
    # Strategy: Counter the player's most frequent move.
    # Fallback to random choice if there isn't enough history.
    if not player_history:
        return random.choice(['Rock', 'Paper', 'Scissors'])
    
    # Count occurrences of player choices
    rock_count = player_history.count('Rock')
    paper_count = player_history.count('Paper')
    scissors_count = player_history.count('Scissors')
    
    # Predict player's most likely move
    if rock_count >= paper_count and rock_count >= scissors_count:
        predicted_move = 'Rock'
    elif paper_count >= rock_count and paper_count >= scissors_count:
        predicted_move = 'Paper'
    else:
        predicted_move = 'Scissors'
        
    # Choose counter move to the predicted move
    counters = {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}
    return counters[predicted_move]

def determine_winner(player, ai):
    if player == ai:
        return "Tie"
    
    winning_combos = {
        'Rock': 'Scissors',
        'Paper': 'Rock',
        'Scissors': 'Paper'
    }
    
    if winning_combos[player] == ai:
        return "Player"
    return "AI"

def play_game():
    player_history = []
    scores = {'Player': 0, 'AI': 0, 'Ties': 0}
    
    print("=== Rock Paper Scissors vs AI ===")
    
    while True:
        player_choice = get_user_choice()
        if player_choice == 'Quit':
            print("\nThanks for playing!")
            break
            
        ai_choice = get_ai_choice(player_history)
        player_history.append(player_choice)
        
        print(f"You chose: {player_choice}")
        print(f"AI chose:  {ai_choice}")
        
        result = determine_winner(player_choice, ai_choice)
        
        if result == "Tie":
            print("Outcome: It's a tie!")
            scores['Ties'] += 1
        elif result == "Player":
            print("Outcome: You win!")
            scores['Player'] += 1
        else:
            print("Outcome: AI wins!")
            scores['AI'] += 1
            
        print(f"Score - You: {scores['Player']} | AI: {scores['AI']} | Ties: {scores['Ties']}\n")

if __name__ == "__main__":
    play_game()