class InputSeq:
	def __init__(self):
		self.sequences=[];
		self.numRows=0
		self.numCols=0
		self.cols=["col"]
		self.readSequences()


	def readSequences(self):
		filename=input("Enter file name: ")
		seqFile=open(filename)

		# store aa into 2D array
		for line in seqFile:
			seqstr=line.rstrip()
			seqlist=seqstr.split(",")
			self.numCols=len(seqlist) # count numCols
			self.sequences.append(seqlist)
		self.numRows=len(self.sequences) # count numRows

		# create cols list
		for i in range(self.numCols):
			self.cols.append(i)

		# print
		self.writeSequences()


	def writeSequences(self):
		outFile = open("OutFile.txt","a")

		rowcount=1 # leftlabels
		# print leftlabels
		for row in self.sequences:
			print("%2s" % rowcount, end=" ")
			outFile.write(str("%2s" % rowcount) + " ")

			# print contents
			for col in row:
				print("%2s" % col, end=" ")
				outFile.write(str("%2s" % col) + " ")
			print()
			outFile.write('\n')
			rowcount=rowcount+1
