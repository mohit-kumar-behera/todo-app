from django.db import models
from django.utils import timezone
import math

class taskCreate(models.Model):
	taskDate = models.DateField(auto_now_add = True,unique = True)

	def taskStatus(self):
		#percentage of completed task
		completeCount = 0 #default value
		tasklist = self.tasklist_set.all()
		for task in tasklist:
			if task.isComplete:
				completeCount += 1
		return completeCount

	def totalTask(self):
		#Total number of tasks
		tasklist = self.tasklist_set.all()
		return len(tasklist)

	def taskPercentage(self):
		taskCompletePercent = 0 #default value
		completedTask = self.taskStatus()
		totalTask = self.totalTask()
		if totalTask > 0:
			taskCompletePercent = math.ceil((completedTask/totalTask)*100)
		return taskCompletePercent
	
	def __str__(self):
		return "task #"+str(self.id)+" @ "+str(self.taskDate)

	class Meta:
		verbose_name_plural = 'Create Task'



class taskList(models.Model):
	task = models.ForeignKey(taskCreate,on_delete = models.CASCADE)
	taskDescription = models.TextField(blank = False,null = False)
	taskTime = models.TimeField(auto_now_add = False,default = timezone.localtime(),blank = True,null = True)
	isComplete = models.BooleanField(default = False)

	def __str__(self):
		return "@ "+str(self.task.taskDate)+" - "+self.taskDescription[:40]

	class Meta:
		ordering = ['taskTime']
