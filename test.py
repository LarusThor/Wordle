word_dict = {'steinar': 3, 'lárus': 4, 'sævar': 2}

# for name, score in word_dict.items():
    
#     print(min(score))

word_dict = sorted(word_dict.items(), key=lambda x: x[1])

print(word_dict)

