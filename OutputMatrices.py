class OutputMatrices:
	def writeTotal(self, stringlabel, total):
		outFile = open("OutFile.txt","a")

		print(stringlabel, total)
		outFile.write(stringlabel + str(total) + "\n")

		outFile.close()


	def write1DmatrixReal(self, stringlabel, matrix=[], leftlabels=[]):
		outFile = open("OutFile.txt","a")

		# print title
		print(stringlabel)
		outFile.write(stringlabel+'\n')

		# print leftlabels and contents
		for i in range(len(matrix)):
			print(leftlabels[i], end=" ")
			print("%.4f" % matrix[i])
			outFile.write(leftlabels[i] + " " + "%.4f" % matrix[i] + '\n')

		outFile.close()


	def write2DmatrixReal(self, stringlabel, matrix=[], leftlabels=[], toplabels=[]):
		outFile = open("OutFile.txt","a")

		# print title
		print(stringlabel)
		outFile.write(stringlabel+'\n')

		# print toplabels
		for i in range(len(toplabels)):
			print ("%6s" % toplabels[i], end=" ")
			outFile.write(str("%6s" % toplabels[i]) + " ")
		print()
		outFile.write('\n')

		# print leftlabels and contents
		leftlabelsIndex=0
		for row in matrix:
			print(leftlabels[leftlabelsIndex], end=" ")
			outFile.write(str(leftlabels[leftlabelsIndex]) + " ")
			for col in row:
				print("%.4f" % col, end=" ")
				outFile.write(str("%.4f" % col) + " ")
			print()
			outFile.write('\n')
			leftlabelsIndex=leftlabelsIndex+1

		outFile.close()


	def write2DmatrixInt(self, stringlabel, matrix=[], leftlabels=[], toplabels=[]):
		outFile = open("OutFile.txt","a")

		# print title
		print(stringlabel)
		outFile.write(stringlabel+'\n')

		# print toplabels
		for i in range(len(toplabels)):
			print ("%3s" % (toplabels[i]), end=" ")
			outFile.write(str("%3s" % toplabels[i]) + " ")
		print()
		outFile.write('\n')

		# print leftlabels and contents
		leftlabelsIndex=0
		for row in matrix:
			print("%3s" % leftlabels[leftlabelsIndex], end=" ")
			outFile.write(str("%3s" % leftlabels[leftlabelsIndex]) + " ")
			for col in row:
				print("%3s" % col, end=" ")
				outFile.write(str("%3s" % col) + " ")
			print()
			outFile.write('\n')
			leftlabelsIndex=leftlabelsIndex+1

		outFile.close()