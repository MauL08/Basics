loop = int(input())
suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
card_value = [int(x) for x in input().split()]
for i in card_value:
    suit_value = i/13
    rank_value = i%13
    suit_value = int(suit_value)
    rank_value = int(rank_value)
    print(ranks[rank_value]+'-'+'of'+'-'+suits[suit_value]+' ')
