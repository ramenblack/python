import random

def diceroll():
	random.seed()
	global d1,d2,sum
	d1 = random.randint(1,6)
	d2 = random.randint(1,6)
	sum = (d1+d2)

if __name__ == "__main__":
	global cash,bet
	playing=True
	cash=1000
	print('You have ',cash,'dollars!')
	while playing==True:
		while True:
			try:
				bet=int(input('How much you wanna bet playa?: $'))
				if bet>cash:
					raise ValueError
				break
			except:
				print("don't bet money you don't have, punk kid!")
		bet=int(bet)
		diceroll()
		print('dice d1 = ',d1,'dice d2 = ',d2,'sum is ',sum)
		if(sum==7 or sum==11):
			cash=cash+bet
			print('You WIN and now have ',cash,' dollars.')
		elif(sum==2 or sum==3 or sum==12):
			cash=cash-bet
			print ('You HECKIN LOST and now have ',cash,' dollars.')
		else:
			print ('Your POINT is ',sum,'. You must now roll ',sum,'before you roll a 7 in order to add to your $',cash,' cash.')
			point=sum
			while(sum!=7):
				diceroll()
				print('you rolled a ',sum)
				if (sum==point):
					cash=cash+bet
					print('YEAH BUDDY! You WIN and now have ',cash,'dollars.')
					break
			else:
				cash=cash-bet
				print('You LOST and now have ',cash,' dollars.')
			if cash==0:
				print('Looks like you are out of money. Pay up boi')
				playing=False
			else:
				test_playing=input('Care to play again? ')
				if test_playing=='yeet' or test_playing=='y' or test_playing=='papa bless' or test_playing=='yes':
					pass
				else:
					playing=False
