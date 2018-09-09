import operator
word_count_map = {}

lines = open('dreams_copy.txt', 'r').readlines()
for line in lines:
    words = line.split()
    for word in words:
        if not word in word_count_map:
            word_count_map[word] = 0
        word_count_map[word] += 1

#print out the top 50 words used
sorted_map = list(reversed(sorted(word_count_map.items(), key=operator.itemgetter(1))))
for i in range(50):
    print(sorted_map[i])
