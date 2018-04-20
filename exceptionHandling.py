# ------------------------------
# error and exceptions handling

# try
# except 
# finally

try:
	f = open('file.txt', 'r')
	f.write('toto')
	#io.UnsupportedOperation: not writable
except:
	print("Error: could not write the file")
else:
	print("file written successfully")
	f.close()
	