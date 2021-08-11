Sentencce = []
user_sentence = input("enter your sentence")
for i in range(len(user_sentence)):
    Sentencce.append(user_sentence[i])

number_of_words = Sentencce.count(" ")

a = number_of_words + 1
print("there are",a ,"words in your sentence")
