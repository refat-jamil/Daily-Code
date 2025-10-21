# Python strings are sequences of characters used to 
# store and manipulate text data. 

message = 'Hello world'

print(message)

# message = 'Bobby's World'   #SyntaxError
#print(message)

message = 'Bobby\'s World'  

print(message)


message = 'Hello world'

print(len(message))
print(message[0])
print(message[4])
# print(message[11]) #IndexError: string index out of range
print(message[0:5])
print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('w'))
print(message.find('world'))
print(message.find('x'))
print(message.replace('world', 'universe'))


frist_word = 'Hello'
second_word = 'World'

message = frist_word + ' ' + second_word

print(message)

f_message = f'{frist_word}, {second_word}'
print(f_message)

