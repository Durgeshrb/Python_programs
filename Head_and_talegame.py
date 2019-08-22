while True:
  x=int(input('press 1 for head and 2 for tale'))
  import random
  no2 = random.randint(1, 2)
  if no2==1 and x==1:
   print('its a head you win')
  elif no2==2 and x==2:
   print('its a tale you wun ')
  elif no2==1 and x!=1:
   print('ohh its head you lose')
  else:
   print('ohh its tale you los
