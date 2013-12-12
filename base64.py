

code = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encodeBase64(src, encode="utf-8"):
	
	global code

	paddingTail = {0:'', 8:'0000', 16:'00'}
	paddingEqual = {0:'', 8:'==', 16:'='}

	src = src.encode(encode)
	sin = ''
	for c in src:
		sin += bin(c)[2:].zfill(8)
	n = len(sin) % 24
	sin += paddingTail[n]

	output = ''
	for i in range(6, len(sin) + 1, 6):
		output += code[int(sin[i - 6:i], 2)]
	output += paddingEqual[n]

	return output


def decodeBase64(src, encode="utf-8"):

	global code
	delPaddingTail = {0:0, 2:4, 1:2}

	value = ''
	n = src.count('=')
	sin = src[:len(src) - n]
	for c in sin:
		value += bin(code.find(c))[2:].zfill(6)
	value = value[:len(value) - delPaddingTail[n]]

	middle = []
	for i in range(8, len(value) + 1, 8):
		middle.append(int(value[i-8:i], 2))
	output = bytes(middle).decode(encoding=encode)

	return output

	

