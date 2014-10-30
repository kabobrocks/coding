'''Opens a file called enable1.txt for reading'''
my_file = open("enable1.txt", "r")
results = []

#reads the file and searches for all words beginning with 'at', adds them to a list
for line in my_file:
    if line[:2] == "at":
        results.append(line.rstrip('\n'))
my_file.close()

results.sort(key=len)

#prints the ten shortest results
for i in range(10):
    print(results[i].replace(results[i][:2], "@") + ' : ' + results[i])

print('')
#prints the ten longest results
for i in range(10):	
    print(results[len(results)-i-1].replace(results[len(results)-i-1][:2], "@") + ' : ' + results[len(results)-i-1])

