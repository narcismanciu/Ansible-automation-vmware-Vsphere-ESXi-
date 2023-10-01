'''22.Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

Extra:

Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each category of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.

dict1 = {}
f = open('names.txt','r')
for line in f.read().splitlines():
    if line not in dict1.keys():
        dict1[line]=1
    else:
        dict1[line]=dict1[line]+1
print(dict1)

f.close()


counter_dict = {}
with open('Training_01.txt') as f:
	line = f.readline()
	while line:
		line = line[3:-26]
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)
'''


'''
23.Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)

a = open('prime_numbers.txt','r')
b = open('happy_numbers.txt','r')

mylist1 = []
mylist2 = []
for number1 in a.read().splitlines():
    mylist1.append(number1)
for number2 in b.read().splitlines():
    mylist2.append(number2)

c = [item for item in mylist1 if item in mylist2]

print(c)
a.close()
b.close()

'''

'''
24.This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.


size = input('Input the size of the board: ')

def board(i):
    for line in range (int(i)):
        print(' ___ '*int(i))
        print('|    '*(int(i)+1))
    print(' ___ '*int(i))
     

board(size)

'''

'''

print('Hello')