from InputSeq import *
from OutputMatrices import *
import math

class MakeBLOSUM:
	def __init__(self):
		self.seqIn = InputSeq()
		self.seq = self.seqIn.sequences
		self.colNums = self.seqIn.numCols
		self.colList = self.seqIn.cols
		self.aaList = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
		self.aaNums = len(self.aaList)
		self.aaSubFreq = [[0 for c in range(self.colNums)] for r in range(self.seqIn.numRows)]
		self.aaSubRate = [[0 for c in range(self.aaNums)] for r in range(self.aaNums)]
		self.aaSubProb = [[0.0 for c in range(self.aaNums)] for r in range(self.aaNums)]
		self.aaColsTotal = [0 for r in range(self.aaNums)]
		self.aaMargProb = [0.0 for r in range(self.aaNums)]
		self.aaExpSubRate = [[0.0 for c in range(self.aaNums)] for r in range(self.aaNums)]
		self.aaOddsRatio = [[0.0 for c in range(self.aaNums)] for r in range(self.aaNums)]
		self.aaLogOddsRatio = [[0.0 for c in range(self.aaNums)] for r in range(self.aaNums)]


	def countInCols(self):	
		# count aa frequency in cols	
		for r in range(self.seqIn.numRows):
			for c in range(self.colNums):
				for n in range(self.aaNums):
					if(self.seq[r][c]==self.aaList[n]):
						self.aaSubFreq[n][c]=self.aaSubFreq[n][c]+1
		
		# print
		OutputMatrices().write2DmatrixInt("\nAA Count in Columns", self.aaSubFreq, self.aaList, self.colList)


	def countSubProb(self):
		#count substitutions rate
		totalI = 0
		for i1 in range(self.aaNums):
			for i2 in range(i1+1):
				for c in range (self.colNums): 
					if i1==i2:
						self.aaSubRate[i1][i2] = int(self.aaSubRate[i1][i2]+(self.aaSubFreq[i1][c]*(self.aaSubFreq[i1][c]-1))/2)
					else:
						self.aaSubRate[i1][i2] = int(self.aaSubRate[i1][i2]+(self.aaSubFreq[i1][c])*(self.aaSubFreq[i2][c]))

		for i1 in range(0,self.aaNums):
			for i2 in range(0,i1+1):
				totalI = totalI + self.aaSubRate[i1][i2]

		# print
		aaListTop = self.aaList.copy()
		aaListTop.insert(0, ' ')
		
		OutputMatrices().write2DmatrixInt("\nAA Counted Substitutions Rate", self.aaSubRate, self.aaList, aaListTop)
		OutputMatrices().writeTotal("Total substitutions count = ", totalI)

		# count observed substitutions rate
		totalD = float(totalI)
		for i1 in range (0,self.aaNums):
			for i2 in range (0,i1+1):
				self.aaSubProb[i1][i2] = self.aaSubRate[i1][i2]/totalD

		#print
		OutputMatrices().write2DmatrixReal("\nAA Observed Subtitutions Rate", self.aaSubProb, self.aaList, self.aaList)


	def countMargProb(self):
		# count grand total
		aaGrandTotal=0
		for i1 in range(self.aaNums):
			for i2 in range(self.colNums):
				self.aaColsTotal[i1] = self.aaColsTotal[i1] + self.aaSubFreq[i1][i2]
			aaGrandTotal = aaGrandTotal + self.aaColsTotal[i1]

		# count marginal prob
		dbaaGrandTotal = float(aaGrandTotal)
		for i in range(self.aaNums):
			self.aaMargProb[i] = self.aaColsTotal[i]/dbaaGrandTotal;

		# print 
		OutputMatrices().writeTotal("\nGrand Total = ", aaGrandTotal)
		OutputMatrices().write1DmatrixReal("AA Marginal Probabilities", self.aaMargProb, self.aaList)


	def countExpSubRate(self):
		# count expected subst rate
		for i1 in range(self.aaNums):
			for i2 in range(i1+1):
				if i1==i2:
					self.aaExpSubRate[i1][i2] = self.aaMargProb[i1] * self.aaMargProb[i2]
				else:
					self.aaExpSubRate[i1][i2] = 2 * self.aaMargProb[i1] * self.aaMargProb[i2]

		# print 
		OutputMatrices().write2DmatrixReal("\nAA Expected Substitutions Rate", self.aaExpSubRate, self.aaList, self.aaList)


	def countOddsRatio(self):
		# count odds ratio
		for i1 in range(self.aaNums):
			for i2 in range(i1+1):
				if self.aaExpSubRate[i1][i2]!=0:
					self.aaOddsRatio[i1][i2] = self.aaSubProb[i1][i2] / self.aaExpSubRate[i1][i2]

		# print 
		OutputMatrices().write2DmatrixReal("\nAA Odds Ratio", self.aaOddsRatio, self.aaList, self.aaList)


	def countLogOddsRatio(self):
		# count log odds ratio
		for i1 in range(self.aaNums):
			for i2 in range(i1+1):
				if self.aaOddsRatio[i1][i2]!=0:
					self.aaLogOddsRatio[i1][i2] = 2 * (math.log(self.aaOddsRatio[i1][i2])) / math.log(2)
				else:
					self.aaLogOddsRatio[i1][i2] = -9.9900

		# print
		OutputMatrices().write2DmatrixReal("\nAA Log Odds Ratio", self.aaOddsRatio, self.aaList, self.aaList)


m = MakeBLOSUM()
m.countInCols()
m.countSubProb()
m.countMargProb()
m.countExpSubRate()
m.countOddsRatio()
m.countLogOddsRatio()