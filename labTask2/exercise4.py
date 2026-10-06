#4no.
txt=input("Enter a name:")
char=0
vowel=0
spaces=0
for i in txt:
    char+=1
    if i=="aeiou":
        vowel+=1
    if i==" ":
        spaces+=1

print("No of char:",char)
print("No of vowel:",vowel)
print("No of spaces:",spaces)

