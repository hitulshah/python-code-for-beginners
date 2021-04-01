#fibonacci sequence
# term = int(input('Enter terms:'))
# n1 = 0
# n2 = 1
# if term <= 0 :
#     print('Please enter valid term')
# elif term == 1 :
#     print(n1)
# else :
#     for i in range(term) :
#         print(n1)
#         x = n1 + n2
#         n1 = n2
#         n2 = x

#list and files examples        
# fname = input("Enter file name: ")
# fh = open(fname)
# count = 0
# for line in fh:
#     if not line.startswith('From'):
#         continue
#     if line.startswith('From:'):
#         continue
#     else:
#         line = line.split()
#         line = line[1]
#         print(line)
#     count += 1
# print("There were",count,"lines in the file with From as the first word")

#fname = raw_input("Enter file name: ")
# fh = open(fname)
# lst = list()                       # list for the desired output
# for line in fh:                    # to read every line of file romeo.txt
#     word= line.rstrip().split()    # to eliminate the unwanted blanks and turn the line into a list of words
#     for element in word:           # check every element in word    
#         if element in lst:         # if element is repeated
#             continue               # do nothing
#         else :                     # else if element is not in the list
#             lst.append(element)    # append     
# lst.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
# print lst                          # print the list
        