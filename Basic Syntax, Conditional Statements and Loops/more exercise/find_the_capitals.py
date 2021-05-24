# word = input()
# new_list = []
# for letter in word:
#     if letter.isupper():
#         new = word.index(letter)
#         new_list.append(new)
# print(new_list)

# version one - short
word = input()
new = [index for index in range(len(word)) if word[index].isupper()]
print(new)


# version 2
word = input()
new_list = []
for index in range(len(word)):
    if word[index].isupper():
        new_list.append(index)
print(new_list)