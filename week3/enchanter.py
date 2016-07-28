#attr: gender, power type, eye color, hair color and skin color
#methods: create and destroy

class enchanter(): 
	def __init__(self, gender, powertype, eyecolor, haircolor, skincolor):
		self.gender=gender
		self.powertype=powertype
		self.eyecolor=eyecolor
		self.haircolor=haircolor
		self.skincolor=skincolor
		self.pronoun='They'

	def pronoun(self):
		if (self.gender=='female'):
			return self.pronoun == 'she'
		elif (self.gender=='male'):
			return self.pronoun =='he'
		else:
			return self.pronoun

	def create(self, obj):
		print('A '+self.gender +' enchanter with '+self.eyecolor+' eyes, '+self.haircolor+' hairs and '+
			self.skincolor + ' skin use '+self.powertype+' to create '+obj+'. '+self.pronoun+' is fantansitic!')

	def destroy(self, asd):
		print('A '+self.gender +' enchanter with '+self.eyecolor+' eyes, '+self.haircolor+' hairs, and '+
			self.skincolor + ' skin use '+self.powertype+' to destroy '+asd+'. '+self.pronoun+' is fantansitic!')

liya = enchanter('female', 'ice', 'grey', 'blue', 'white')
liya.create('cat')