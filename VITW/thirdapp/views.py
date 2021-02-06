from django.shortcuts import render,redirect
from django.http import HttpResponse
from thirdapp.models import Student

# Create your views here.
def demo1(request):
	return HttpResponse('From Third App ....')

def home1(request):
	return render(request,'thirdapp/home.html')


def addstudent(request):
	return render(request,'thirdapp/create.html')

def addstudent(request):
	if request.method == 'POST':
		fn = request.POST.get('fname')
		ln = request.POST.get('lname')
		n = request.POST.get('username')
		r = request.POST.get('rollno')
		e = request.POST.get('Email')
		m = request.POST.get('mobile')
		g = request.POST.get('gender')
		a = request.POST.get('age')
		Student.objects.create(fname=fn,lname=ln,name=n,rnum=r,email=e,mobile=m,gender=g,age=a)
		return HttpResponse('Record Inserted Succesfully')
	return render(request,'thirdapp/create.html')

def details1(request):
	info=Student.objects.all()
	context={'info':info}
	return render(request,'thirdapp/details1.html',context)


def update1(request,id):
	data = Student.objects.get(id=id)
	if request.method == 'POST':
		data.fname = request.POST['fname']
		data.lname = request.POST['lname']
		data.name = request.POST['name']
		data.rnum = request.POST['rollno']
		data.email = request.POST['email']
		data.mobile = request.POST['mobile']
		#data.gender = request.POST['gender']
		data.age = request.POST['age']
		data.save();
		return redirect('/details1')
	return render(request,'thirdapp/update.html',{'data':data})



def delete1(request,id):
	obj = Student.objects.get(id=id)
	if request.method == 'POST':
		obj.delete()
		return redirect('details1')
	return render(request,'thirdapp/delete.html',{'obj':obj})


