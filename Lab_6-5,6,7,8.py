
#*** You must write a comment for every chunk of code you write from now on along with your author tag***

#Create a Python file named lab_6-5
#Create a program that will take a list (of numbers) of any length and return the highest and lowest value in the list. If the list does not have at least 2 unique numbers, return the string: “error: list does not meet specifications”)
#hint: test the program on lists of 0,1,2 + lengths, as well as lists that do and do not meet specifications! 
def hilo(list):
    i = 1
    re = [list[0],list[0]]
    while i < len(list):
        if list[i] > re[0]:
            re[0] = list[i]
        if list[i] < re[1]:
            re[1] = list[i]    
        i += 1    
    return re if len(list) >= 2 else "error: list does not meet specifications"   

print(hilo([1,2,3,4,5]))
print(hilo([1]))
print(hilo([5,6,7,8]))
#________________________________________________________________________________
#Create a Python file named lab_6-6

#Create a program that asks a user to input 5 unique words.
#Construct a list of the 5 input values, in the order that the user gave them.
#Have the program display a list where each index corresponds to the length of the word given by the user at the corresponding index.
#You may assume accurate input values. NO LOOPS
def six():
    list = [input("please give word:"),input("please give word:"),input("please give word:"),input("please give word:"),input("please give word:")]
    print(str(len(list[0]))+" "+str(len(list[1]))+" "+str(len(list[2]))+""+str(len(list[3]))+" "+str(len(list[4])))
six()
#_________________________________________________________________________________
#Create a Python file named lab_6-7
#Create a program that asks a user to input 3 numeric values
#Construct a list of the 3 input values, in the order that the user gave them.
#Have the program display a list with each of the values as integers that have been doubled 
#You may assume accurate input values.
def seven():
    print(str(int(input("please give number"))*2)+" "+str(int(input("please give number"))*2)+" "+str(int(input("please give number"))*2))
seven()

#_________________________________________________________________________________
#Create a Python file named lab_6-8
#Create a program that asks a user to input 3 numeric values
#Construct a list of the 3 input values, in the order that the user gave them.
#Have the program display the string “even” if all numbers in the list are even.
#Have the program display the string “odd” if all numbers in the list are odd.
#Have the program display the string “mixed” if the numbers in the list are both even and odd.
#You may assume accurate input values. You may NOT use a loop. 
def evenodd():
    list = [int(input("please give number:")),int(input("please give number:")),int(input("please give number:"))]
    print("even" if list[0]/2 == int(list[0]/2) and list[1]/2 == int(list[1]/2) and list[2]/2 == int(list[2]/2) else "odd" if list[0]/2 != int(list[0]/2) and list[1]/2 != int(list[1]/2) and list[2]/2 != int(list[2]/2) else "mixed")
evenodd()