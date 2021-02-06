from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def sample(request):
	return HttpResponse("<h1>Welcome to django session</h1>")




def centerexample(request):
	return HttpResponse("<center> <h1>Welcome Sowbhanu</h1> </center> ")


def taskfun(request):
	return HttpResponse("<center><h1>django session</h1></center><br><br><h2> this is sowbhanu<h2><br> ")


def integervalueex(request,num):
	return HttpResponse("1235.......%d"%num)


def stringvalueex(request,name):
	return HttpResponse("Sowbhanu......."+name)

def example(request,name,num):
	return HttpResponse("Sowbhanu"+name+"Age="+str(num))

def samplehtmlex(request):
	return render(request,'Student/Sample.html')


def  htmlexcss(request):
	return render(request,'Student/demo.html')

def  htmlex(request):
	return render(request,'Student/External.html')

def  boostrapex(request):
	return render(request,'Student/boostrap.html')
	
def vijayaclg(request):
	return render(request,'Student/Vijayacollege.html')

def VITWCollege(request):
	if request.method == 'POST':
		fname=request.POST.get('First Name')
		lname=request.POST.get('Last Name')
		rollno=request.POST.get('rno')
		uname=request.POST.get('User Name')
		email=request.POST.get('email')
		password=request.POST.get('pswd')
		cpassword=request.POST.get('password')
		phoneno=request.POST.get('Phone Number')

		#return HttpResponse("success")
		return render(request,'Student/details.html',{'fname':fname,'lname':lname,'rollno':rollno,'uname':uname,'email':email,'password':password,'cpassword':cpassword,'phoneno':phoneno})
	return render(request,'Student/VITWclg.html')



def details(request):
	return render(request,'Student/details.html')





