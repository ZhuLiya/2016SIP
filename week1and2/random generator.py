import random

print('MENU')
print(' ')
adj=['funny','best','sour','spicy','sweet','salty','sunny','creamy','special','curry']
color=['green','blue','purple','black','silver','golden','white','yellow','red','platinum']
food=['rice','beef','pork','chicken','eggs','noodles','soup','tofu','shrimp','salmon']
number=['1.','2.','3.','4.','5.','6.','7.','8.','9.','10.']

def menu(d,k,r,s):
    for i in range(10):
        ra=random.randint(0,9)
        rc=random.randint(0,9)
        rf=random.randint(0,9)
        print(d[i]+k[ra]+' '+r[rc]+' '+s[rf])
menu(number,adj,color,food)

print('')
print(' ')
print('Band Name')
print(' ')
art=['The','A','My','His','Her','Your','One']
ad=['Screaming','Crazy','Sexy','Raining','Long','Tasty','Nineth']
noun=['Pyramid','Unicorn','Kungfu','Colon','Hair','Toilet','Stone']

def li(art,ad,noun):
    for i in range(7):
        r1=random.randint(0,6)
        r2=random.randint(0,6)
        r3=random.randint(0,6)
        print(art[r1]+' '+ad[r2]+' '+noun[r3])

li(art,ad,noun)

print(' ')
print(' ')
print('Haiku')
print(' ')
po=["Staring at the sun","It's now or never ","Where do you belong",
    'An old silent pond','Into the chestnut','Everything I smell',
    'Through the cold winter','As the wind does blow','Falling to the ground','Out of the water']
pl=["That is always the question",'A frog jumps into the pond','A worm digs silently',
    'What I thought were faces','Swaying in the evening sun','A broken signboard banging',
    'I watch a leaf settle down','For someone to shelter me','The sleeping child; on the porch','Look out and give me room there']

def ya(v,x,l):
    for i in range(7):
        r1=random.randint(0,9)
        r2=random.randint(0,9)
        r3=random.randint(0,9)
        print(v[r1])
        print(x[r2])
        print(l[r3])
        print('  ')
ya(po,pl,po)





















    
