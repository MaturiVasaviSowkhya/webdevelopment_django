from django.urls import path
from thirdapp import views

urlpatterns =[
	path('demo1/',views.demo1),
	path('home1/',views.home1,name='home1'),
	path('addstudent/',views.addstudent,name='addstudent'),
	path('details1/',views.details1,name='details1'),
	path('update1/<int:id>/',views.update1,name='update1'),
	path('delete1/<int:id>/',views.delete1,name='delete1'),
	
	]

