text = input()
text = text.lower()

word_list = ["sand", "water", "fish", "sun"]
counter = 0

for word in word_list:
    if word in text:
        word_count_txt = text.count(word)
        counter += word_count_txt

print(counter)