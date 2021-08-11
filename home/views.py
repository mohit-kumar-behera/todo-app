from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.utils import timezone
from django.urls import reverse
from .models import taskCreate,taskList
import datetime
import math

from .MyClass import prevStatistics as PS

def home(request):
	try:
		todayTask = taskCreate.objects.get(taskDate = datetime.datetime.now())
	except taskCreate.DoesNotExist:
		context = {'todayTask':False}
		return render(request,'home/home.html',context)
	todayTaskList = todayTask.tasklist_set.order_by('taskTime')
	context = {'todayTask':todayTask,'tasks':todayTaskList}
	try:
		error_message = request.session['error_message']
	except:
		pass
	else:
		context['error_message'] = error_message
		del request.session['error_message']
	if 'addTaskSubmit' in request.POST:
		print("Add task form is submitted")
		taskDescription = request.POST.get('taskDescription')
		if not request.POST.get('taskTime'):
			taskTime = None
		else:
			taskTime = request.POST.get('taskTime')	
			#Cannot store the time that has passed
			taskTime__obj = datetime.datetime.strptime(taskTime,'%H:%M').time()
			nowTime__obj = datetime.datetime.now().time()
			if taskTime__obj < nowTime__obj:
				print("Impossible event happened")
				context['error_message'] = "You can assign tasks only to the future events."
				return render(request,'home/home.html',context)
		todayTask.tasklist_set.create(taskDescription=taskDescription,taskTime=taskTime)
	return render(request,'home/home.html',context)


def toggleTask(request):
	if request.GET:
		#print("Came inside toggle task function")
		data = {'successfull':True}
		taskId = request.GET.get('taskId')
		getTask = taskList.objects.get(id=taskId)
		getTask.isComplete = not(getTask.isComplete) #toggle the previous condition of task
		getTask.save()
		data['isComplete'] = getTask.isComplete
		return JsonResponse(data)
	else:
		#print("Something went wrong")
		data = {'successfull':False}
		return JsonResponse(data)

def createTask(request):
	try:
		createTask = taskCreate.objects.create()
	except:
		request.session['error_message'] = 'You have already created a task for today.'
		return HttpResponseRedirect(reverse("home:home"))
	else:
		getAllTask = taskCreate.objects.all()
		if len(getAllTask) > 7:
			getAllTask.first().delete()
		return HttpResponseRedirect(reverse("home:home"))



def statistics(request):
	context = {}
	ps = PS.previousStatistics(allTask = taskCreate.objects.all())
	overallTaskCompletePercent = ps.overallTaskStatus()
	PreviousFewTasks = ps.previousTasks()
	context['overallTaskCompletePercent'] = overallTaskCompletePercent
	context['PreviousFewTasks'] = PreviousFewTasks
	try:
		todayTask = taskCreate.objects.get(taskDate = datetime.datetime.now())
	except taskCreate.DoesNotExist:
		context['todayTask'] = False
		return render(request,'home/statistic.html',context)
	taskCompletePercentage = todayTask.taskPercentage()

	context['todayTask'] = todayTask
	context['taskCompletePercentage'] = taskCompletePercentage
	return render(request,'home/statistic.html',context)



'''
Task creating and listing tasks -- finish
apply the same in frontend -- finish
apply the frontend to todayTaskStatus -- 
delete the task after 24 hours
	Logic to it:
		taskPublishedDate > timezone.localtime() + datetime.timedelta(days=1)
'''
