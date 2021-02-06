from django.shortcuts import render
from django.http import HttpResponse
from formsapp.forms import StudentForm
# Create your views here.
def demo(request):
	return HttpResponse('iam from formsapp')

def reg(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		form.save()
		return HttpResponse('Data Inserted using Forms...')
	form = StudentForm()
	return render(request,'formsapp/reg.html', {'form':form})