#Open a file to read
#Print all words in a dictionary file that has one word per line

#open file named "dictionary.txt" for reading ('r') 
data_file = open ("dictionary.txt", 'r')

# iterate through the file one line at a time
#for line_str in data_file:
#	print (line_str)

def clean_word (word) : 
	"""Return word in lowercase stripped of whitespace."""
	return word.strip().lower ()

def get_vowels_in_word (word) :
	"""Return vowels in string word include repeats."""
	vowel_str="aeiou"
	vowels_in_word=""
	for char in word:
		if char in vowel_str: 
			vowels_in_word += char
	return vowels_in_word

# main program
print ("Find words containing vowels 'aeiou' in that order :")
for word in data_file:		# for each word in the file
	word = clean_word (word) #clean the word
	if len (word) <= 3:		# if word is too small, skip it
		continue
	vowel_str= get_vowels_in_word (word)
	print(vowel_str)
	if vowel_str == 'aeiou': #get vowels in order
		print (word)		#check if you hv exactly all vowels in order
