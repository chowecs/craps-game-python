from random import randint

print('CRAPS rule:')
print('There are two dice, if the sum of dice in first round are 7 or 11, you win.')
print('If the sum of the dice in first round are 2, 3 or 12, you lose.')
print('Otherwise, keep rolling. If the sum of the dice equals to the first result, you win. If it is equal to 7, you lose.')

money = 1000
while money > 0:
    print('your assets: ',money)
    play = True
    while True:
        bet = int(input('Please enter your bet: '))
        if 0 < bet <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('The sum of 2 dice are: ', first)
    if first == 7 or first == 11:
        print('You win!')
        money += bet*2
        play = False
    elif first == 2 or first == 3 or first == 12:
        print('You lose...')
        money -= bet
        play = False
    while play:
        res = randint(1, 6) + randint(1, 6)
        print('The sum of 2 dice are: ', res)
        if res == first:
            print('You win!')
            money += bet*2
            play = False
        elif res == 7:
            print('You lose...')
            money -= bet
            play = False

print('You have no money to play now...')