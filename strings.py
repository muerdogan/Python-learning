#strings ;

#whatever text #will return with a syntax error

'whatever text' #string
"whatever text" #string
"317" #string
317 #NOT string

"Mr. Brown's jacket"
'Mr. Brown\'s jacket' #escape string


#strings with variables ;

first_name = "Jack"
last_name = "Brown"

first_name + last_name #will return with "JackBrown"

first_name + "Brown" #returns with "JackBrown"

first_name + first_name + first_name #JackJackJack
first_name*3 #JackJackJack

"Jack" + last_name + "got" + "a" + "jacket" #JackBrowngotajacket


#more about strings 

name = "Jack Brown"

print(name) #Jack Brown

name[0] #index returns for "J" first letter from left to right

name[7] #index returns for "o" 8th letter left to right

name[-3] #index returns for "o" 3rd letter from right to left

name[3:10] #index returns right to left between 4th to 10th letter : ck Brown 

name[:7] #index start beginning left to right to 8th letter : Jack Bro

name[2:] #index starts from right to left 3rd : ck Brown

len(name) #returns for character count : 10

len("python") #6
