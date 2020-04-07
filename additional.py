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