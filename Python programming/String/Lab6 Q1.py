#Write a Python program to count the occurrences of each word in a
#given sentence
#string = “To change the overall look of your document. To change the look
#available in the gallery”
str= input("Enter a string :")
ch=input("Enter char")
count=0
for i in str:
    if i==ch:
        count+=1
print("Char occurance : ", count)

word = input("Enter a word :")

str1 = str.split()
count=0
for w in str1:
    if w== word:
        count+=1
print("Occurance of words :",count)

