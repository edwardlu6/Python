# Edward Lu, January 28th, CSCI-UA.0002-003, EdwardLu_assign1_part2.py
# user can enter the three names here
name1 = input("enter name #1:") #enter name1
name2 = input("enter name #2:") #enter name2
name3 = input("enter name #3:") #enter name3
# the following codes allow the names to be displayed in every possible order in different formats
print("Please enter name #1:",name1) #To print out the name #1
print("Please enter name #2:",name2 ) #To print out the name #2
print("Please enter name #3:",name3) #To print out the name #3
print() #print out a line break
print("Here are your names in every possible order:","\n"+"--------------------------------------------") #The following codes print out the names in every possible order 
print() #print out a line break
print("1.",name1+",", name2+",", name3) #print out the first format
print() #print out a line break
print("2.","**"+name1+"** **"+name3+"** **"+name2+"**") #print out the second format
print() #print out a line break
print("3.",name2+"-"+name1+"-"+name3) #print out the third format
print() #print out a line break
print("4.",name2,"\n"+name3,"\n"+name1) #print out the fourth format
print() #print out a line break
print("5.", name3,"\n","  "+name2+"!","\n","  "+name1)#print out the fifth format
print() #print out a line break
print("6.","---"+name3,"\n","  "+"------"+name1,"\n","  "+"---------"+name2) #print out the sixth format
