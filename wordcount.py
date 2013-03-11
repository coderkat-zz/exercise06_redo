from sys import argv 

script, filename = argv

f = open(filename)

text = f.read()

new_text = text.lower()

newer_text = new_text.replace("!", " ")
text_1 = newer_text.replace("?", " ")
text_2 = text_1.replace(".", " ")
text_final = text_2.replace(",", " ")

# et cetera (or write a function that DOES THIS CRAP)

words = text_final.split()

word_dict = {} 

#when the word appears, count 1
#the count is the value in the dictionary for that word
word_value = 0

for word in words:
	word_dict.setdefault(word, word_value)
	occurs = word_dict[word]
	word_dict[word] = occurs + 1

'''
for key, value in word_dict.iteritems():	
        print "Key == %r, value == %r" % (key, value)
'''

# pull apart the dict into 2 lists
val_list = []
key_list = []

for key, value in word_dict.iteritems():
	key_list = word_dict.keys()
	val_list.append(value) 

# zip lists together to manipulate by value
toop_list = zip(val_list, key_list)


for value, key in sorted(toop_list):
	print "Frequency == %r, key == %r" % (value, key)

