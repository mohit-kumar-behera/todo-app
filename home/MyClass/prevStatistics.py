import math

class previousStatistics:
	def __init__(self,allTask):
		self.allTask = allTask

	def previousTasks(self):
		return self.allTask

	def overallTaskStatus(self):
		self.allTaskPercentage = 0
		self.overalltaskStatus = 0
		self.overallTask = 0
		for task in self.allTask:
			self.overalltaskStatus += task.taskStatus()
			self.overallTask += task.totalTask()
		if self.overallTask > 0:
			self.allTaskPercentage = math.ceil((self.overalltaskStatus/self.overallTask)*100)
		return self.allTaskPercentage

