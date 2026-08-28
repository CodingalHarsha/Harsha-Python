Word = input("Enter any word : ")

Letter = input("Enter which letter you want to check the occurence for : ")

i = 0
count = 0

while i < len(Word):
    if Word[i] == Letter:
        count = count + 1
    i = i +1

print("Total number of times", Letter, "occured in this", Word, "is : ",count )