from PIL import Image
im = Image.open("puppy.jpg")
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)
data =im.getdata()
data_list = list(data)
new_pic=[]

for i in range(len(data_list)):
    RED=data_list[i][0]
    GREEN=data_list[i][1]
    BLUE=data_list[i][2]
    if RED+GREEN+BLUE<=182:
        RED=0
        GREEN=51
        BLUE=76
    if 182<RED+GREEN+BLUE<=364:
        RED=217
        GREEN=26
        BLUE=33
    if 364<RED+GREEN+BLUE<=546:
        RED=112
        GREEN=26
        BLUE=33
    if RED+GREEN+BLUE>546:
        RED=252
        GREEN=227
        BLUE=166
        

im.putdata(data)
im.rotate(360).show()   
