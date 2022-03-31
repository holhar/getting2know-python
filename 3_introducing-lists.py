# 3 Instroducing Lists

# 3.1 List Basics

# 3-1 Names:
from operator import inv


names = ['Ben', 'Daniel', 'Alex']
print(names[0])
print(names[1])
print(names[-1])

# 3-2 Greetings:
print('Hello ' + names[0])
print('Hello ' + names[1])
print('Hello ' + names[-1])

# 3-3 Your Own List:
transportation = ['bicycle', 'tain', 'my feet']
print("I love to travel with " + transportation[-1] + ", it's simply the best way")

# 3.2 Changing, Adding, and Removing Elements

# 3-4 Guest List:
invitations = names
print('Hi ' + invitations[0] + ", would you like to join for dinner?")
print('Hi ' + invitations[1] + ", would you like to join for dinner?")
print('Hi ' + invitations[2] + ", would you like to join for dinner?")

# 3-5 Changing Guest List:
print(invitations[-1] + " can not make it")
invitations[-1] = 'Louis'
print("Hi " + invitations[0] + ", would you like to join for dinner?")
print("Hi " + invitations[1] + ", would you like to join for dinner?")
print("Hi " + invitations[2] + ", would you like to join for dinner?")

# 3-6 More Guests:
print("Hey, I got a bigger table! I'll invite more people...")
invitations.insert(0, 'Marc')
invitations.insert(2, 'Phil')
invitations.append('Frida')
print("Hi " + invitations[0] + ", would you like to join for dinner?")
print("Hi " + invitations[1] + ", would you like to join for dinner?")
print("Hi " + invitations[2] + ", would you like to join for dinner?")
print("Hi " + invitations[3] + ", would you like to join for dinner?")
print("Hi " + invitations[4] + ", would you like to join for dinner?")
print("Hi " + invitations[5] + ", would you like to join for dinner?")

# 3-7 Shrinking Guest List:
print("Oh no! The bigger dinner table hasn't arrived. I can only invite two people... :-(")
invitation = invitations.pop()
print("Sorry " + invitation + " I have to uninvite you")
invitation = invitations.pop()
print("Sorry " + invitation + " I have to uninvite you")
invitation = invitations.pop()
print("Sorry " + invitation + " I have to uninvite you")
invitation = invitations.pop()
print("Sorry " + invitation + " I have to uninvite you")

print("Hi " + invitations[0] + ", dinner time is still going on")
print("Hi " + invitations[1] + ", dinner time is still going on")

del(invitations)

# 3.3 Organizing a list

# 3-8 Seeing the World:
placesToVisit = ['Japan', 'Fiji', 'New Zealand', 'Greece', 'Columbia']
print(placesToVisit)
print(sorted(placesToVisit))
print(placesToVisit)
placesToVisit.reverse()
print(placesToVisit)
placesToVisit.sort()
print(placesToVisit)

# 3-9 Dinner Guests:
print('There are ' + len(placesToVisit) + ' items in the placesToVisit array')

# 3-10 Every Function:
# Maybe later...

# 3.4 Avoiding Index Errors When Working with Lists

# 3-11 Intentional Error:
names[100]