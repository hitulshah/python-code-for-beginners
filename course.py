fruit = 'banana'
# print(fruit[2])
# print(len(fruit))

#index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(index, letter)
#     index = index + 1

#for x in range(0, len(fruit)):
    #letter = fruit[x]
   # print(x, letter)
    #x = x + 1

# count = 0    
# for letter in fruit:
#     if letter == 'a' :
#         count = count + 1
# print(count)

# x = input('Enter the letter:')
# if x in fruit :
#     print('True')
# else :
#     print('false')


# x = 'hituls18@gmail.com'
# atpos = x.find('@')
# sppos = x.find('.')
# host = x[atpos + 1 : sppos]
# print(host)

text = "X-DSPAM-Confidence:    0.8475"
x = text.find('0')
y = text[x:]
z = float(y)
print(z)