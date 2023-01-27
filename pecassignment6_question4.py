word = input("enter a word : ")
def reverse(word):
    if len(word) ==0:
        return word
    else:
        return reverse(word[1:]) + word[0]
print(reverse(word))
s = word.replace(" ","")
b = reverse(word).replace(" ","")
if s == b:
    print("YES")
else:
    print("NO")


