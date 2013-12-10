

def encode(src):

	dict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', \
			11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', \
			21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z', 26:'a', 27:'b', 28:'c', 29:'d', 30:'e', \
			31:'f', 32:'g', 33:'h', 34:'i', 35:'j', 36:'k', 37:'l', 38:'m', 39:'n', 40:'o', \
			41:'p', 42:'q', 43:'r', 44:'s', 45:'t', 46:'u', 47:'v', 48:'w', 49:'x', 50:'y', \
			51:'z', 52:'0', 53:'1', 54:'2', 55:'3', 56:'4', 57:'5', 58:'6', 59:'7', 60:'8', \
			61:'9', 62:'+', 63:'/'}


	paddingZero = {1:'0', 2:'00', 3:'000', 4:'0000', 5:'00000', 6:'000000', 7:'0000000', 8:'00000000'}
	paddingTail = {8:'0000', 16:'00'}
	paddingEqual = {8:'==', 16:'='}

	sin = ''
	for c in src:
		value = bin(ord(c))
		temp = value[2:]
		n = 8 - len(temp)
		if n != 0:
			temp = paddingZero[n] + temp
		sin = sin + temp
	
	output = ''
	n = len(sin) % 24
	sin += paddingTail[n]
	
	for i in range(6, len(sin) + 1, 6):
		output += dict[int(sin[i - 6:i], 2)]
	output += paddingEqual[n]

	return output

def decode(src):

	#ZWFzdXJlLg==
	dict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, \
			'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, \
			'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25, 'a':26, 'b':27, 'c':28, 'd':29, 'e':30, \
			'f':31, 'g':32, 'h':33, 'i':34, 'j':35, 'k':36, 'l':37, 'm':38, 'n':39, 'o':40, \
			'p':41, 'q':42, 'r':43, 's':44, 't':45, 'u':46, 'v':47, 'w':48, 'x':49, 'y':50, \
			'z':51, '0':52, '1':53, '2':54, '3':55, '4':56, '5':57, '6':58, '7':59, '8':60, \
			'9':61, '+':62, '/':63}
	
	paddingZero = {1:'0', 2:'00', 3:'000', 4:'0000', 5:'00000', 6:'000000'}
	delPaddingTail = {2:4, 1:2}
	
	n = 0
	if src[len(src) - 1] == '=':
		n += 1
		if src[len(src) - 2] == '=':
			n += 1
	
	str = ''
	temp = src[:len(src) - n]
	for c in temp:
		value = (bin(dict[c]))[2:]
		c = 6 - len(value)
		if c != 0:
			value =  paddingZero[c] + value
		str += value
	str = str[:len(str) - delPaddingTail[n]]

	output = ''
	for i in range(8, len(str) + 1, 8):
		output += chr(int(str[i - 8:i], 2))
	
	return output

if __name__ == "__main__":
	print(encode("easure."))
	print(decode("ZWFzdXJlLg=="))

	#str = encode("你好吗！")
	#print(str)
	#print(decode(str))










