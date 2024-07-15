import random


secret_number= random.randint(1,6)
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    #try:
      guess = int(input("Guess the secret Number:  "))
    #except:ValueError
      if guess > 6:
        print('guess a number less than 7')
      guess_limit += 1

      if  guess != secret_number:
           print('You guess wrong Idiot:')
           guess_count += 1
      else:
           print('You guess right Goodluck')
           break


else:
    print('try again later')
