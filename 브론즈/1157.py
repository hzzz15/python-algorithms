word = input().strip().upper()
unique = list(set(word))
count_list = [word.count(char) for char in unique]

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    print(unique[count_list.index(max(count_list))])
