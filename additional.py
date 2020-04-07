import re
import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def get_ending(filename):
	filename = filename[::-1]
	ending = filename[:filename.index('.')+1]
	ending = ending[::-1]
	return ending

'''def create_links(text, start_s):
	#indexes = [m.start() for m in re.finditer(start_s, s)]
	try:
		index = text.index(start_s)
		s = text[:index]
		link = text[index:text[index+1:].index(' ')+len(s)]
		s += f'<a href="{link}">{link}</a>'
		s += text[text.index(link)+len(link):]
		return create_links(s, start_s)
	except ValueError:
		return text'''
