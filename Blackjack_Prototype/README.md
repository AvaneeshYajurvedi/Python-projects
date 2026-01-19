# Project Description

Blackjack Prototype is a minimal implementation of the classic casino card game Blackjack.

Both the user and the computer are dealt two cards at the start. The user can choose to draw one additional card, while the computer follows standard dealer rules.

The game automatically:

Adjusts the value of an Ace (11 → 1) if the hand exceeds 21

Detects Blackjack

Determines win, loss, or draw conditions

This is a prototype, meaning:

One round per execution

No betting system

No replay loop

Focused purely on logic, not UI

## Blackjack Rules (As Implemented in This Code)

### Card Values

Number cards (2–9) → Face value

10, Jack, Queen, King → 10

Ace → 11 (automatically changes to 1 if total exceeds 21)

### Initial Deal

User receives 2 random cards

Computer receives 2 random cards

Total hand values are calculated immediately

### Blackjack Check

If User gets a Blackjack (Ace + 10) → User wins instantly

If Computer gets a Blackjack → User loses instantly

### User Turn

User is asked:

Do You Want To Draw Another Card? (Y/N)

If Yes:

One card is added

If total = 21 → User wins

If total > 21 → User loses (Bust)

If No:

Turn passes to the computer

### Computer Turn (Dealer Logic)

Computer draws cards until total ≥ 17

Outcomes:

Total = 21 → Computer wins

Total > 21 → User wins

Otherwise → Compare hands

## Final Comparison

Higher total (≤ 21) wins

Equal totals → Draw

## Key Features

Automatic Ace value adjustment

Dealer logic based on real Blackjack rules

Clear win/loss conditions

Clean separation of logic using functions

## Technologies Used

Python 3

Built-in random module

## How to Run

python blackjack.py

Make sure Python 3 is installed on your system.

## Future Improvements

Game loop (play multiple rounds)

Betting system

Multiple hits for the user

Hidden dealer card

Score tracking

GUI or terminal-based card visuals

## Disclaimer

This project is a learning prototype, not a full casino-grade Blackjack implementation.
