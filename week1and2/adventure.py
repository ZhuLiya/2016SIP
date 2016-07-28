print('Today, you weak up, but you find that you are not at your home. '
	'There are two doors. One on the left has a picture of a cat on it, and the other one on the right has a picture of a boy on it.')

print('START')

input1=input('Do you want to open the door on the left or the door on the right?(type left or right)')
while (input1!="left"and input1!="right"):
	print('ERROR')
	input1=input('Do you want to open the door on the left or the door on the right?(type left or right)')
if input1=="left":
	print('there is a boat, and there is a big cat that can talk.')
	input2=input('After two days, there is no food. Do you want to eat the cat or go to find food?(type eat or find)')
	while (input2!='eat'and input2!='find'):
		print('ERROR')
		input2=input('After two days, there is no food. Do you want to eat the cat or go to find food?(type eat or find)')
	if input2=="eat":
		print('GAME OVER. You die because of illness.')
	elif input2=="find":
		print('Yeah! You find a little bit food.')
		input3=input('Do you want to share food with the cat that talk with you on the boat for two days, or eat all food by yourself?(type share or myself)')
		while (input3!='share'and input3!='myself'):
			print('ERROR')
			input3=input('Do you want to share food with the cat that talk with you on the boat for two days, or eat all food by yourself?(type share or myself)')	
		if input3=="share":
			print('GAME OVER! Yeah! You are survive! There is a helicopter and they save you and the cat!')
		elif input3=="myself":
			print('GAME OVER. You die because sharks beat you.')

elif input1=="right":
	print('there is a airplane, and there is a boy.')
	
	input4=input('You go on a vacation with the boy on a cruise ship. However,'
			' a storm comes, the ship is broken, and you have slilpped into a coma by that time,'
			' when you weak up, the boy and you are on a uninhabited island.'
			' There is a chance to leave by yourself.'
			'Do you want to leave or stay?(type leave or stay)')
	while (input4!='leave'and input4!="stay"):
		print('ERROR')
		input4=input('You go on a vacation with the boy on a cruise ship. However,'
			' a storm comes, the ship is broken, and you have slilpped into a coma by that time,'
			' when you weak up, the boy and you are on a uninhabited island.'
			' There is a chance to leave by yourself.'
			'Do you want to leave or stay?(type leave or stay)')
	if input4=="leave":
		print('GAME OVER. You die because a tiger beat you.')
	elif input4=="stay":
		print('You choose stay, but there is a problem, you do not have any food.')
		
		input5=input('Do you want to eat the boy or go to find food?(type eat or find)')
		while(input5!='eat'and input5!='find'):
			print('ERROR')
			input5=input('Do you want to eat the boy or go to find food?(type eat or find)')
		if input5=='eat':
			print("GAME OVER. You die because the boy kill you.")
		elif input5=='find':
			print('Yeah! You find a little bit food.')
			input7=('Do you want to share with the boy or eat by yourself?(type share or myself)')
			while (input7!='share'and input7!='myself'):
				print('ERROR')
				input7=('Do you want to share with the boy or eat by yourself?(type share or myself)')
			if input7=="share":
				print('GAME OVER! Yeah! You are survive! A helicopter comes and find you!')
			elif input7=="myself":
				print('GAME OVER. You die because the food is poisonous.') 