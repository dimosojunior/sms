from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db.models import Q
import datetime
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import letter
#from reportlab.lib.pagesizes import landscape
#from reportlab.platypus import Image
import os
from django.conf import settings
from django.http import HttpResponse
#from django.template.loader import get_template
#from xhtml2pdf import pisa
#from django.contrib.staticfiles import finders
import calendar
from calendar import HTMLCalendar
from DimosoApp.models import *
from django.db.models import Sum, Max, Min, Avg
from DimosoApp.forms import *
#from hitcount.views import HitCountDetailView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
import csv
from django.db.models.query import QuerySet


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


#SEND EMAIL AND SMS

from twilio.rest import Client
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
def base(request):
	return render(request, "DimosoApp/base.html")

@login_required(login_url='signin')
def home(request):
	activities = Activities.objects.all()

	context = {
		"activities":activities,
	}

	return render(request, 'DimosoApp/home.html',context)







#STUDENTS  VIEWS
@login_required(login_url='signin')
def students(request):
	students = RegisterStudents.objects.all()

	context = {
		"students":students,
	}

	return render(request, 'Students/students.html',context)

@login_required(login_url='signin')
def all_students(request):
	students = RegisterStudents.objects.all().order_by('-id')
	form = StudentsSearchForm(request.POST or None)
	if request.method =="POST":
		students = RegisterStudents.objects.filter(last_name__icontains=form['last_name'].value())

	context = {
		"students":students,
		"form": form,
	}
	
	return render(request, 'Students/all_students.html', context) 

@login_required(login_url='signin')
def search_student_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(last_name__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    student = RegisterStudents.objects.filter(search)
    mylist= []
    mylist += [x.last_name for x in student]
    return JsonResponse(mylist, safe=False)


@login_required(login_url='signin')
def add_student(request):
	form = AddStudentForm()
	regno= request.POST.get('regno')
	first_name= request.POST.get('first_name')
	middle_name= request.POST.get('middle_name')
	last_name= request.POST.get('last_name')
	email= request.POST.get('email')
	phone= request.POST.get('phone')


	x= RegisterStudents.objects.filter(regno=regno)
	y= RegisterStudents.objects.filter(email=email)
	z= RegisterStudents.objects.filter(phone=phone)
	if request.method == "POST":
		if x.exists():
			messages.info(request,f"Failed!, Registration number {regno} for {first_name} {middle_name} {last_name} already exists, You can't add student twice")
			return redirect('add_student')
		elif y.exists():
			messages.info(request,f"Failed!, Email {email} already exists, You can't add students with the same emails")
			return redirect('add_student')
		elif z.exists():
			messages.info(request,f"Failed!, Phone number {phone} already exists, You can't add students with the same phone numbers")
			return redirect('add_student')
		form=AddStudentForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,f"{first_name} {middle_name} {last_name} was added Successfully")
			return redirect('add_student')

	context = {
		"form":form,

	}
	
	return render(request, 'Students/add_student.html', context)

@login_required(login_url='signin')
def update_student(request,id):
	x = RegisterStudents.objects.get(id=id)
	form = UpdateStudentForm(instance=x)
	regno= request.POST.get('regno')
	first_name= request.POST.get('first_name')
	middle_name= request.POST.get('middle_name')
	last_name= request.POST.get('last_name')
	if request.method == "POST":
		form=UpdateStudentForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			messages.success(request,f"{first_name} {middle_name} {last_name} was updated Successfully")
			return redirect('all_students')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'Students/update_student.html', context)

@login_required(login_url='signin')
def delete_student(request,id):
	x = RegisterStudents.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"{x.first_name} {x.middle_name} {x.last_name} was deleted Successfully")
		return redirect('all_students')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'Students/delete_student.html', context)




#MWISHO WA STUDENTS VIEWS




















#SUBJECTS


@login_required(login_url='signin')
def subjects(request):
	subjects = Subjects.objects.all()

	context = {
		"subjects":subjects,
	}

	return render(request, 'Subjects/subjects.html',context)



@login_required(login_url='signin')
def add_student_marks(request):
	form = AddStudentMarksForm()
	#regno= request.POST.get('regno')
	#first_name= request.POST.get('first_name')
	if request.method == "POST":
		form=AddStudentMarksForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,f"marks was added Successfully")
			return redirect('add_student_marks')

	context = {
		"form":form,

	}
	
	return render(request, 'Subjects/add_student_marks.html', context)

@login_required(login_url='signin')
def view_subject_marks(request,id):
	marks = Marks.objects.get(id=id)

	#HIZI NI KWA AJILI YA KUCHANGE PAGE TO EXCEL FILE
	form = SearchStudentMarksForm(request.POST or None)
	

	context = {
		"marks":marks,
		"form":form,
	}

	return render(request, 'Subjects/view_subject_marks.html',context)






#PHYSICS SUBJECTS VIEWS
@login_required(login_url='signin')
def physics_subject_marks(request):
	marks = Marks.objects.filter(subjects__subject_name__contains="PHYSICS").order_by('-Average')

	#HIZI NI KWA AJILI YA KUCHANGE PAGE TO EXCEL FILE
	form = SearchStudentMarksForm(request.POST or None)

	if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['content-Disposition'] = 'attachment; filename="Physics Students Marks.csv"'
			writer = csv.writer(response)
			writer.writerow(['FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'GENDER','SUBJECT', 'TEST1','TEST2','TEST3','TEST4','TEST5','MID-TERM', 'ANNUAL','AVERAGE'])
			instance = marks
			for x in marks:
				writer.writerow([x.registerstudents.first_name,x.registerstudents.middle_name,x.registerstudents.last_name,x.registerstudents.gender,x.subjects.subject_name,x.Test1,x.Test2,x.Test3,x.Test4,x.Test5,x.MidTerm,x.Term, x.Average])
			return response

	#MWISHO HAPA
	

	context = {
		"marks":marks,
		"form":form,
	}

	return render(request, 'PHYSICS/physics_subject_marks.html',context)
@login_required(login_url='signin')
def search_physics_subject_marks(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(registerstudents__last_name__icontains=query)|Q(registerstudents__first_name__icontains=query)|Q(registerstudents__middle_name__icontains=query)
        results=Marks.objects.filter(mysearch, subjects__subject_name__contains="PHYSICS")
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'PHYSICS/search_physics_subject_marks.html',context)




@login_required(login_url='signin')
def update_physics_subject_marks(request,id):
	x = Marks.objects.get(id=id)
	form = UpdateStudentMarksForm(instance=x)
	
	if request.method == "POST":
		form=UpdateStudentMarksForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			messages.success(request,f"Marks was updated Successfully")
			return redirect('physics_subject_marks')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'PHYSICS/update_physics_subject_marks.html', context)

@login_required(login_url='signin')
def delete_physics_subject_marks(request,id):
	x = Marks.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"Marks was deleted Successfully")
		return redirect('physics_subject_marks')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'PHYSICS/delete_physics_subject_marks.html', context)







#CHEMISTRY SUBJECTS VIEWS
@login_required(login_url='signin')
def chemistry_subject_marks(request):
	marks = Marks.objects.filter(subjects__subject_name__contains="CHEMISTRY").order_by('-Average')

	#HIZI NI KWA AJILI YA KUCHANGE PAGE TO EXCEL FILE
	form = SearchStudentMarksForm(request.POST or None)

	if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['content-Disposition'] = 'attachment; filename="Chemistry Students Marks.csv"'
			writer = csv.writer(response)
			writer.writerow(['FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'GENDER','SUBJECT', 'TEST1','TEST2','TEST3','TEST4','TEST5','MID-TERM', 'ANNUAL','AVERAGE'])
			instance = marks
			for x in marks:
				writer.writerow([x.registerstudents.first_name,x.registerstudents.middle_name,x.registerstudents.last_name,x.registerstudents.gender,x.subjects.subject_name,x.Test1,x.Test2,x.Test3,x.Test4,x.Test5,x.MidTerm,x.Term, x.Average])
			return response

	#MWISHO HAPA
	

	context = {
		"marks":marks,
		"form":form,
	}

	return render(request, 'CHEMISTRY/chemistry_subject_marks.html',context)
@login_required(login_url='signin')
def search_chemistry_subject_marks(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(registerstudents__last_name__icontains=query)|Q(registerstudents__first_name__icontains=query)|Q(registerstudents__middle_name__icontains=query)
        results=Marks.objects.filter(mysearch, subjects__subject_name__contains="CHEMISTRY")
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'CHEMISTRY/search_chemistry_subject_marks.html',context)





@login_required(login_url='signin')
def update_chemistry_subject_marks(request,id):
	x = Marks.objects.get(id=id)
	form = UpdateStudentMarksForm(instance=x)
	
	if request.method == "POST":
		form=UpdateStudentMarksForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			messages.success(request,f"Marks was updated Successfully")
			return redirect('chemistry_subject_marks')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'CHEMISTRY/update_chemistry_subject_marks.html', context)

@login_required(login_url='signin')
def delete_chemistry_subject_marks(request,id):
	x = Marks.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"Marks was deleted Successfully")
		return redirect('chemistry_subject_marks')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'CHEMISTRY/delete_chemistry_subject_marks.html', context)









#BIOLOGY SUBJECTS VIEWS
@login_required(login_url='signin')
def biology_subject_marks(request):
	marks = Marks.objects.filter(subjects__subject_name__contains="BIOLOGY").order_by('-Average')

	#HIZI NI KWA AJILI YA KUCHANGE PAGE TO EXCEL FILE
	form = SearchStudentMarksForm(request.POST or None)

	if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['content-Disposition'] = 'attachment; filename="Biology Students Marks.csv"'
			writer = csv.writer(response)
			writer.writerow(['FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'GENDER','SUBJECT', 'TEST1','TEST2','TEST3','TEST4','TEST5','MID-TERM', 'ANNUAL','AVERAGE'])
			instance = marks
			for x in marks:
				writer.writerow([x.registerstudents.first_name,x.registerstudents.middle_name,x.registerstudents.last_name,x.registerstudents.gender,x.subjects.subject_name,x.Test1,x.Test2,x.Test3,x.Test4,x.Test5,x.MidTerm,x.Term, x.Average])
			return response

	#MWISHO HAPA
	

	context = {
		"marks":marks,
		"form":form,
	}

	return render(request, 'BIOLOGY/biology_subject_marks.html',context)




@login_required(login_url='signin')
def search_biology_subject_marks(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(registerstudents__last_name__icontains=query)|Q(registerstudents__first_name__icontains=query)|Q(registerstudents__middle_name__icontains=query)
        results=Marks.objects.filter(mysearch, subjects__subject_name__contains="BIOLOGY")
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'BIOLOGY/search_biology_subject_marks.html',context)




@login_required(login_url='signin')
def update_biology_subject_marks(request,id):
	x = Marks.objects.get(id=id)
	form = UpdateStudentMarksForm(instance=x)
	
	if request.method == "POST":
		form=UpdateStudentMarksForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			messages.success(request,f"Marks was updated Successfully")
			return redirect('biology_subject_marks')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'BIOLOGY/update_biology_subject_marks.html', context)

@login_required(login_url='signin')
def delete_biology_subject_marks(request,id):
	x = Marks.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"Marks was deleted Successfully")
		return redirect('biology_subject_marks')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'BIOLOGY/delete_biology_subject_marks.html', context)





#ENGLISH SUBJECTS VIEWS
@login_required(login_url='signin')
def english_subject_marks(request):
	marks = Marks.objects.filter(subjects__subject_name__contains="ENGLISH").order_by('-Average')

	#HIZI NI KWA AJILI YA KUCHANGE PAGE TO EXCEL FILE
	form = SearchStudentMarksForm(request.POST or None)

	if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['content-Disposition'] = 'attachment; filename="English Students Marks.csv"'
			writer = csv.writer(response)
			writer.writerow(['FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'GENDER','SUBJECT', 'TEST1','TEST2','TEST3','TEST4','TEST5','MID-TERM', 'ANNUAL','AVERAGE'])
			instance = marks
			for x in marks:
				writer.writerow([x.registerstudents.first_name,x.registerstudents.middle_name,x.registerstudents.last_name,x.registerstudents.gender,x.subjects.subject_name,x.Test1,x.Test2,x.Test3,x.Test4,x.Test5,x.MidTerm,x.Term, x.Average])
			return response

	#MWISHO HAPA
	

	context = {
		"marks":marks,
		"form":form,
	}

	return render(request, 'ENGLISH/english_subject_marks.html',context)




@login_required(login_url='signin')
def search_english_subject_marks(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(registerstudents__last_name__icontains=query)|Q(registerstudents__first_name__icontains=query)|Q(registerstudents__middle_name__icontains=query)
        results=Marks.objects.filter(mysearch, subjects__subject_name__contains="ENGLISH")
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'ENGLISH/search_english_subject_marks.html',context)




@login_required(login_url='signin')
def update_english_subject_marks(request,id):
	x = Marks.objects.get(id=id)
	form = UpdateStudentMarksForm(instance=x)
	
	if request.method == "POST":
		form=UpdateStudentMarksForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			messages.success(request,f"Marks was updated Successfully")
			return redirect('english_subject_marks')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'ENGLISH/update_english_subject_marks.html', context)

@login_required(login_url='signin')
def delete_english_subject_marks(request,id):
	x = Marks.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"Marks was deleted Successfully")
		return redirect('english_subject_marks')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'ENGLISH/delete_english_subject_marks.html', context)


#HISTORY SUBJECTS VIEWS
@login_required(login_url='signin')
def history_subject_marks(request):
	marks = Marks.objects.filter(subjects__subject_name__contains="HISTORY").order_by('-Average')

	#HIZI NI KWA AJILI YA KUCHANGE PAGE TO EXCEL FILE
	form = SearchStudentMarksForm(request.POST or None)

	if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['content-Disposition'] = 'attachment; filename="History Students Marks.csv"'
			writer = csv.writer(response)
			writer.writerow(['FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'GENDER','SUBJECT', 'TEST1','TEST2','TEST3','TEST4','TEST5','MID-TERM', 'ANNUAL','AVERAGE'])
			instance = marks
			for x in marks:
				writer.writerow([x.registerstudents.first_name,x.registerstudents.middle_name,x.registerstudents.last_name,x.registerstudents.gender,x.subjects.subject_name,x.Test1,x.Test2,x.Test3,x.Test4,x.Test5,x.MidTerm,x.Term, x.Average])
			return response

	#MWISHO HAPA
	

	context = {
		"marks":marks,
		"form":form,
	}

	return render(request, 'HISTORY/history_subject_marks.html',context)




@login_required(login_url='signin')
def search_history_subject_marks(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(registerstudents__last_name__icontains=query)|Q(registerstudents__first_name__icontains=query)|Q(registerstudents__middle_name__icontains=query)
        results=Marks.objects.filter(mysearch, subjects__subject_name__contains="HISTORY")
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'HISTORY/search_history_subject_marks.html',context)




@login_required(login_url='signin')
def update_history_subject_marks(request,id):
	x = Marks.objects.get(id=id)
	form = UpdateStudentMarksForm(instance=x)
	
	if request.method == "POST":
		form=UpdateStudentMarksForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			messages.success(request,f"Marks was updated Successfully")
			return redirect('history_subject_marks')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'HISTORY/update_history_subject_marks.html', context)

@login_required(login_url='signin')
def delete_history_subject_marks(request,id):
	x = Marks.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"Marks was deleted Successfully")
		return redirect('history_subject_marks')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'HISTORY/delete_history_subject_marks.html', context)





#KISWAHILI SUBJECTS VIEWS
@login_required(login_url='signin')
def kiswahili_subject_marks(request):
	marks = Marks.objects.filter(subjects__subject_name__contains="KISWAHILI").order_by('-Average')

	#HIZI NI KWA AJILI YA KUCHANGE PAGE TO EXCEL FILE
	form = SearchStudentMarksForm(request.POST or None)

	if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['content-Disposition'] = 'attachment; filename="Kiswahili Students Marks.csv"'
			writer = csv.writer(response)
			writer.writerow(['FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'GENDER','SUBJECT', 'TEST1','TEST2','TEST3','TEST4','TEST5','MID-TERM', 'ANNUAL','AVERAGE'])
			instance = marks
			for x in marks:
				writer.writerow([x.registerstudents.first_name,x.registerstudents.middle_name,x.registerstudents.last_name,x.registerstudents.gender,x.subjects.subject_name,x.Test1,x.Test2,x.Test3,x.Test4,x.Test5,x.MidTerm,x.Term, x.Average])
			return response

	#MWISHO HAPA
	

	context = {
		"marks":marks,
		"form":form,
	}

	return render(request, 'KISWAHILI/kiswahili_subject_marks.html',context)




@login_required(login_url='signin')
def search_kiswahili_subject_marks(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(registerstudents__last_name__icontains=query)|Q(registerstudents__first_name__icontains=query)|Q(registerstudents__middle_name__icontains=query)
        results=Marks.objects.filter(mysearch, subjects__subject_name__contains="KISWAHILI")
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'KISWAHILI/search_kiswahili_subject_marks.html',context)




@login_required(login_url='signin')
def update_kiswahili_subject_marks(request,id):
	x = Marks.objects.get(id=id)
	form = UpdateStudentMarksForm(instance=x)
	
	if request.method == "POST":
		form=UpdateStudentMarksForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			messages.success(request,f"Marks was updated Successfully")
			return redirect('kiswahili_subject_marks')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'KISWAHILI/update_kiswahili_subject_marks.html', context)

@login_required(login_url='signin')
def delete_kiswahili_subject_marks(request,id):
	x = Marks.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"Marks was deleted Successfully")
		return redirect('kiswahili_subject_marks')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'KISWAHILI/delete_kiswahili_subject_marks.html', context)



#CIVICS SUBJECTS VIEWS
@login_required(login_url='signin')
def civics_subject_marks(request):
	marks = Marks.objects.filter(subjects__subject_name__contains="CIVICS").order_by('-Average')

	#HIZI NI KWA AJILI YA KUCHANGE PAGE TO EXCEL FILE
	form = SearchStudentMarksForm(request.POST or None)

	if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['content-Disposition'] = 'attachment; filename="Civics Students Marks.csv"'
			writer = csv.writer(response)
			writer.writerow(['FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'GENDER','SUBJECT', 'TEST1','TEST2','TEST3','TEST4','TEST5','MID-TERM', 'ANNUAL','AVERAGE'])
			instance = marks
			for x in marks:
				writer.writerow([x.registerstudents.first_name,x.registerstudents.middle_name,x.registerstudents.last_name,x.registerstudents.gender,x.subjects.subject_name,x.Test1,x.Test2,x.Test3,x.Test4,x.Test5,x.MidTerm,x.Term, x.Average])
			return response

	#MWISHO HAPA
	

	context = {
		"marks":marks,
		"form":form,
	}

	return render(request, 'CIVICS/civics_subject_marks.html',context)




@login_required(login_url='signin')
def search_civics_subject_marks(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(registerstudents__last_name__icontains=query)|Q(registerstudents__first_name__icontains=query)|Q(registerstudents__middle_name__icontains=query)
        results=Marks.objects.filter(mysearch, subjects__subject_name__contains="CIVICS")
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'CIVICS/search_civics_subject_marks.html',context)




@login_required(login_url='signin')
def update_civics_subject_marks(request,id):
	x = Marks.objects.get(id=id)
	form = UpdateStudentMarksForm(instance=x)
	
	if request.method == "POST":
		form=UpdateStudentMarksForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			messages.success(request,f"Marks was updated Successfully")
			return redirect('civics_subject_marks')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'CIVICS/update_civics_subject_marks.html', context)

@login_required(login_url='signin')
def delete_civics_subject_marks(request,id):
	x = Marks.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"Marks was deleted Successfully")
		return redirect('civics_subject_marks')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'CIVICS/delete_civics_subject_marks.html', context)


#GEOGRAPHY SUBJECTS VIEWS
@login_required(login_url='signin')
def geography_subject_marks(request):
	marks = Marks.objects.filter(subjects__subject_name__contains="GEOGRAPHY").order_by('-Average')

	#HIZI NI KWA AJILI YA KUCHANGE PAGE TO EXCEL FILE
	form = SearchStudentMarksForm(request.POST or None)

	if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['content-Disposition'] = 'attachment; filename="Geography Students Marks.csv"'
			writer = csv.writer(response)
			writer.writerow(['FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'GENDER','SUBJECT', 'TEST1','TEST2','TEST3','TEST4','TEST5','MID-TERM', 'ANNUAL','AVERAGE'])
			instance = marks
			for x in marks:
				writer.writerow([x.registerstudents.first_name,x.registerstudents.middle_name,x.registerstudents.last_name,x.registerstudents.gender,x.subjects.subject_name,x.Test1,x.Test2,x.Test3,x.Test4,x.Test5,x.MidTerm,x.Term, x.Average])
			return response

	#MWISHO HAPA
	

	context = {
		"marks":marks,
		"form":form,
	}

	return render(request, 'GEOGRAPHY/geography_subject_marks.html',context)




@login_required(login_url='signin')
def search_geography_subject_marks(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(registerstudents__last_name__icontains=query)|Q(registerstudents__first_name__icontains=query)|Q(registerstudents__middle_name__icontains=query)
        results=Marks.objects.filter(mysearch, subjects__subject_name__contains="GEOGRAPHY")
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'GEOGRAPHY/search_geography_subject_marks.html',context)




@login_required(login_url='signin')
def update_geography_subject_marks(request,id):
	x = Marks.objects.get(id=id)
	form = UpdateStudentMarksForm(instance=x)
	
	if request.method == "POST":
		form=UpdateStudentMarksForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			messages.success(request,f"Marks was updated Successfully")
			return redirect('geography_subject_marks')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'GEOGRAPHY/update_geography_subject_marks.html', context)

@login_required(login_url='signin')
def delete_geography_subject_marks(request,id):
	x = Marks.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"Marks was deleted Successfully")
		return redirect('geography_subject_marks')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'GEOGRAPHY/delete_geography_subject_marks.html', context)






#MATHEMATICS SUBJECTS VIEWS
@login_required(login_url='signin')
def mathematics_subject_marks(request):
	marks = Marks.objects.filter(subjects__subject_name__contains="MATHEMATICS").order_by('-Average')

	#HIZI NI KWA AJILI YA KUCHANGE PAGE TO EXCEL FILE
	form = SearchStudentMarksForm(request.POST or None)

	if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['content-Disposition'] = 'attachment; filename="Mathematics Students Marks.csv"'
			writer = csv.writer(response)
			writer.writerow(['FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'GENDER','SUBJECT', 'TEST1','TEST2','TEST3','TEST4','TEST5','MID-TERM', 'ANNUAL','AVERAGE'])
			instance = marks
			for x in marks:
				writer.writerow([x.registerstudents.first_name,x.registerstudents.middle_name,x.registerstudents.last_name,x.registerstudents.gender,x.subjects.subject_name,x.Test1,x.Test2,x.Test3,x.Test4,x.Test5,x.MidTerm,x.Term, x.Average])
			return response

	#MWISHO HAPA
	

	context = {
		"marks":marks,
		"form":form,
	}

	return render(request, 'MATHEMATICS/mathematics_subject_marks.html',context)




@login_required(login_url='signin')
def search_mathematics_subject_marks(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(registerstudents__last_name__icontains=query)|Q(registerstudents__first_name__icontains=query)|Q(registerstudents__middle_name__icontains=query)
        results=Marks.objects.filter(mysearch, subjects__subject_name__contains="MATHEMATICS")
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'MATHEMATICS/search_mathematics_subject_marks.html',context)




@login_required(login_url='signin')
def update_mathematics_subject_marks(request,id):
	x = Marks.objects.get(id=id)
	form = UpdateStudentMarksForm(instance=x)
	
	if request.method == "POST":
		form=UpdateStudentMarksForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			messages.success(request,f"Marks was updated Successfully")
			return redirect('mathematics_subject_marks')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'MATHEMATICS/update_mathematics_subject_marks.html', context)

@login_required(login_url='signin')
def delete_mathematics_subject_marks(request,id):
	x = Marks.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"Marks was deleted Successfully")
		return redirect('mathematics_subject_marks')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'MATHEMATICS/delete_mathematics_subject_marks.html', context)
#MWISHO WA SUBJECTS VIEWS














#VIEWS ZA ADD MORE OTHER SUBJECTS

@login_required(login_url='signin')
def add_more_subjects(request):
	form = AddMoreSubjectsForm()
	subject_name= request.POST.get('subject_name')
	
	if request.method == "POST":
		form=AddMoreSubjectsForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,f"{subject_name} subject was added Successfully")
			return redirect('add_more_subjects')

	context = {
		"form":form,

	}
	
	return render(request, 'Subjects/add_more_subjects.html', context)



@login_required(login_url='signin')
def update_more_subjects(request,id):
	x = Subjects.objects.get(id=id)
	form = UpdateMoreSubjectsForm(instance=x)
	
	if request.method == "POST":
		form=UpdateMoreSubjectsForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			messages.success(request,f"{x.subject_name} was updated Successfully")
			return redirect('subjects')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'Subjects/update_more_subjects.html', context)

@login_required(login_url='signin')
def delete_more_subjects(request,id):
	x = Subjects.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"{x.subject_name} was deleted Successfully")
		return redirect('subjects')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'Subjects/delete_more_subjects.html', context)




#MWISHO WA ADD MORE SUBJECTS












#GENERAL RESULTS VIEWS


@login_required(login_url='signin')
def add_general_results(request):
	form = AddGeneralResultsForm()
	#registerstudents__last_name__icontains
	students= request.POST.get('students')
	x= GeneralResults.objects.filter(students=students)
	
	
	if request.method == "POST":
		
		if x.exists():
			messages.info(request,f"Failed!, Students already exists, You can't add student twice")
			return redirect('add_general_results')

		form=AddGeneralResultsForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,f"Results  were added Successfully")
			return redirect('add_general_results')

	context = {
		"form":form,

	}
	
	return render(request, 'GeneralResults/add_general_results.html', context)


@login_required(login_url='signin')
def update_general_results(request,id):
	x= GeneralResults.objects.get(id=id)
	form = UpdateGeneralResultsForm(instance=x)
	
	
	
	if request.method == "POST":
		

		form=UpdateGeneralResultsForm(request.POST or None, files=request.FILES,instance=x)
		if form.is_valid():
			form.save()
			messages.success(request,f"{x.students.first_name} {x.students.middle_name} {x.students.last_name} Results  were Updated Successfully")
			return redirect('students_general_results')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'GeneralResults/update_general_results.html', context)


@login_required(login_url='signin')
def delete_general_results(request,id):
	x = GeneralResults.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"{x.students.first_name} {x.students.middle_name} {x.students.last_name} Results were deleted Successfully")
		return redirect('students_general_results')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'GeneralResults/delete_general_results.html', context)


@login_required(login_url='signin')
def search_general_results(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(students__last_name__icontains=query)|Q(students__first_name__icontains=query)|Q(students__middle_name__icontains=query)
        results=GeneralResults.objects.filter(mysearch)
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'GeneralResults/search_general_results.html',context)



#CODES ZA KUPRINT GENERAL RESULTS ZINAANZIA HAPA
def print_students_general_results(request):
    
    
	querySet = GeneralResults.objects.all().order_by('-student_average')
	top_ten = GeneralResults.objects.all().order_by('-student_average')[ :10]
	last_ten = GeneralResults.objects.all().order_by('student_average')[ :10]

	physics_sum = GeneralResults.objects.all().aggregate(sum=Sum('physics'))
	chemistry_sum = GeneralResults.objects.all().aggregate(sum=Sum('chemistry'))
	biology_sum = GeneralResults.objects.all().aggregate(sum=Sum('biology'))
	english_sum = GeneralResults.objects.all().aggregate(sum=Sum('english'))
	civics_sum = GeneralResults.objects.all().aggregate(sum=Sum('civics'))
	history_sum = GeneralResults.objects.all().aggregate(sum=Sum('history'))
	geography_sum = GeneralResults.objects.all().aggregate(sum=Sum('geography'))
	kiswahili_sum = GeneralResults.objects.all().aggregate(sum=Sum('kiswahili'))
	mathematics_sum = GeneralResults.objects.all().aggregate(sum=Sum('mathematics'))


	physics_average = GeneralResults.objects.all().aggregate(avg=Avg('physics'))
	chemistry_average = GeneralResults.objects.all().aggregate(avg=Avg('chemistry'))
	biology_average = GeneralResults.objects.all().aggregate(avg=Avg('biology'))
	english_average = GeneralResults.objects.all().aggregate(avg=Avg('english'))
	civics_average = GeneralResults.objects.all().aggregate(avg=Avg('civics'))
	history_average = GeneralResults.objects.all().aggregate(avg=Avg('history'))
	geography_average = GeneralResults.objects.all().aggregate(avg=Avg('geography'))
	kiswahili_average = GeneralResults.objects.all().aggregate(avg=Avg('kiswahili'))
	mathematics_average = GeneralResults.objects.all().aggregate(avg=Avg('mathematics'))


	physics_max = GeneralResults.objects.all().aggregate(max=Max('physics'))
	chemistry_max = GeneralResults.objects.all().aggregate(max=Max('chemistry'))
	biology_max = GeneralResults.objects.all().aggregate(max=Max('biology'))
	english_max = GeneralResults.objects.all().aggregate(max=Max('english'))
	civics_max = GeneralResults.objects.all().aggregate(max=Max('civics'))
	history_max = GeneralResults.objects.all().aggregate(max=Max('history'))
	geography_max = GeneralResults.objects.all().aggregate(max=Max('geography'))
	kiswahili_max = GeneralResults.objects.all().aggregate(max=Max('kiswahili'))
	mathematics_max = GeneralResults.objects.all().aggregate(max=Max('mathematics'))


	physics_min = GeneralResults.objects.all().aggregate(min=Min('physics'))
	chemistry_min = GeneralResults.objects.all().aggregate(min=Min('chemistry'))
	biology_min = GeneralResults.objects.all().aggregate(min=Min('biology'))
	english_min = GeneralResults.objects.all().aggregate(min=Min('english'))
	civics_min = GeneralResults.objects.all().aggregate(min=Min('civics'))
	history_min = GeneralResults.objects.all().aggregate(min=Min('history'))
	geography_min = GeneralResults.objects.all().aggregate(min=Min('geography'))
	kiswahili_min = GeneralResults.objects.all().aggregate(min=Min('kiswahili'))
	mathematics_min = GeneralResults.objects.all().aggregate(min=Min('mathematics'))
	template_path = 'GeneralResults/print_general_results.html'
    #querySet = KawaidaDozi.objects.get(id=id)
	context = {
	    "querySet": querySet,
	    "top_ten":top_ten,
		"last_ten":last_ten,

		"physics_sum":physics_sum,
		"chemistry_sum":chemistry_sum,
		"biology_sum":biology_sum,
		"civics_sum":civics_sum,
		"history_sum":history_sum,
		"mathematics_sum":mathematics_sum,
		"kiswahili_sum":kiswahili_sum,
		"english_sum":english_sum,
		"geography_sum":geography_sum,


		"physics_average":physics_average,
		"chemistry_average":chemistry_average,
		"biology_average":biology_average,
		"civics_average":civics_average,
		"history_average":history_average,
		"mathematics_average":mathematics_average,
		"kiswahili_average":kiswahili_average,
		"english_average":english_average,
		"geography_average":geography_average,


		"physics_max":physics_max,
		"chemistry_max":chemistry_max,
		"biology_max":biology_max,
		"civics_max":civics_max,
		"history_max":history_max,
		"mathematics_max":mathematics_max,
		"kiswahili_max":kiswahili_max,
		"english_max":english_max,
		"geography_max":geography_max,


		"physics_min":physics_min,
		"chemistry_min":chemistry_min,
		"biology_min":biology_min,
		"civics_min":civics_min,
		"history_min":history_min,
		"mathematics_min":mathematics_min,
		"kiswahili_min":kiswahili_min,
		"english_min":english_min,
		"geography_min":geography_min,


	}
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="GeneralResults.pdf"'
	#if you want to download before opening it
	#response['Content-Disposition'] = 'attachment; filename="report.pdf"'
	template = get_template(template_path)
	html = template.render(context)

	pisa_status= pisa.CreatePDF(
	    html, dest=response)
	if pisa_status.err:
	    return HttpResponse('we had some errors <pre>' + html + '</pre>')
	return response



@login_required(login_url='signin')
def students_general_results(request):
	results = GeneralResults.objects.all().order_by('-student_average')
	top_ten = GeneralResults.objects.all().order_by('-student_average')[ :10]
	last_ten = GeneralResults.objects.all().order_by('student_average')[ :10]

	physics_sum = GeneralResults.objects.all().aggregate(sum=Sum('physics'))
	chemistry_sum = GeneralResults.objects.all().aggregate(sum=Sum('chemistry'))
	biology_sum = GeneralResults.objects.all().aggregate(sum=Sum('biology'))
	english_sum = GeneralResults.objects.all().aggregate(sum=Sum('english'))
	civics_sum = GeneralResults.objects.all().aggregate(sum=Sum('civics'))
	history_sum = GeneralResults.objects.all().aggregate(sum=Sum('history'))
	geography_sum = GeneralResults.objects.all().aggregate(sum=Sum('geography'))
	kiswahili_sum = GeneralResults.objects.all().aggregate(sum=Sum('kiswahili'))
	mathematics_sum = GeneralResults.objects.all().aggregate(sum=Sum('mathematics'))


	physics_average = GeneralResults.objects.all().aggregate(avg=Avg('physics'))
	chemistry_average = GeneralResults.objects.all().aggregate(avg=Avg('chemistry'))
	biology_average = GeneralResults.objects.all().aggregate(avg=Avg('biology'))
	english_average = GeneralResults.objects.all().aggregate(avg=Avg('english'))
	civics_average = GeneralResults.objects.all().aggregate(avg=Avg('civics'))
	history_average = GeneralResults.objects.all().aggregate(avg=Avg('history'))
	geography_average = GeneralResults.objects.all().aggregate(avg=Avg('geography'))
	kiswahili_average = GeneralResults.objects.all().aggregate(avg=Avg('kiswahili'))
	mathematics_average = GeneralResults.objects.all().aggregate(avg=Avg('mathematics'))


	physics_max = GeneralResults.objects.all().aggregate(max=Max('physics'))
	chemistry_max = GeneralResults.objects.all().aggregate(max=Max('chemistry'))
	biology_max = GeneralResults.objects.all().aggregate(max=Max('biology'))
	english_max = GeneralResults.objects.all().aggregate(max=Max('english'))
	civics_max = GeneralResults.objects.all().aggregate(max=Max('civics'))
	history_max = GeneralResults.objects.all().aggregate(max=Max('history'))
	geography_max = GeneralResults.objects.all().aggregate(max=Max('geography'))
	kiswahili_max = GeneralResults.objects.all().aggregate(max=Max('kiswahili'))
	mathematics_max = GeneralResults.objects.all().aggregate(max=Max('mathematics'))


	physics_min = GeneralResults.objects.all().aggregate(min=Min('physics'))
	chemistry_min = GeneralResults.objects.all().aggregate(min=Min('chemistry'))
	biology_min = GeneralResults.objects.all().aggregate(min=Min('biology'))
	english_min = GeneralResults.objects.all().aggregate(min=Min('english'))
	civics_min = GeneralResults.objects.all().aggregate(min=Min('civics'))
	history_min = GeneralResults.objects.all().aggregate(min=Min('history'))
	geography_min = GeneralResults.objects.all().aggregate(min=Min('geography'))
	kiswahili_min = GeneralResults.objects.all().aggregate(min=Min('kiswahili'))
	mathematics_min = GeneralResults.objects.all().aggregate(min=Min('mathematics'))

	#HIZI NI KWA AJILI YA KUCHANGE PAGE TO EXCEL FILE
	form = ChangeGeneralResultsPageToExcelForm(request.POST or None)

	if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['content-Disposition'] = 'attachment; filename="General Students Results.csv"'
			writer = csv.writer(response)
			writer.writerow(['FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'GENDER','PHYSICS', 'CHEMISTRY','BIOLOGY','ENGLISH','MATHEMATICS','HISTORY','KISWAHILI', 'CIVICS','GEOGRAPHY','TOTAL','AVERAGE','POINT','GRADE'])
			instance = results
			for x in results:
				writer.writerow([x.students.first_name,x.students.middle_name,x.students.last_name,x.students.gender,x.physics,x.chemistry,x.biology,x.english,x.mathematics,x.history,x.kiswahili,x.civics, x.geography,x.student_total,x.student_average,x.student_point,x.student_grade])
			return response

	#MWISHO HAPA
	

	context = {
		"results":results,
		"top_ten":top_ten,
		"last_ten":last_ten,

		"physics_sum":physics_sum,
		"chemistry_sum":chemistry_sum,
		"biology_sum":biology_sum,
		"civics_sum":civics_sum,
		"history_sum":history_sum,
		"mathematics_sum":mathematics_sum,
		"kiswahili_sum":kiswahili_sum,
		"english_sum":english_sum,
		"geography_sum":geography_sum,


		"physics_average":physics_average,
		"chemistry_average":chemistry_average,
		"biology_average":biology_average,
		"civics_average":civics_average,
		"history_average":history_average,
		"mathematics_average":mathematics_average,
		"kiswahili_average":kiswahili_average,
		"english_average":english_average,
		"geography_average":geography_average,


		"physics_max":physics_max,
		"chemistry_max":chemistry_max,
		"biology_max":biology_max,
		"civics_max":civics_max,
		"history_max":history_max,
		"mathematics_max":mathematics_max,
		"kiswahili_max":kiswahili_max,
		"english_max":english_max,
		"geography_max":geography_max,


		"physics_min":physics_min,
		"chemistry_min":chemistry_min,
		"biology_min":biology_min,
		"civics_min":civics_min,
		"history_min":history_min,
		"mathematics_min":mathematics_min,
		"kiswahili_min":kiswahili_min,
		"english_min":english_min,
		"geography_min":geography_min,


		"form":form,
	}

	return render(request, 'GeneralResults/students_general_results.html',context)



















#IMPORTANT INFORMATIONS

@login_required(login_url='signin')
def add_important_informations(request):
	form = AddImportantInformationsForm()
	#registerstudents__last_name__icontains
	students= request.POST.get('students')
	x= ImportantInformations.objects.filter(students=students)
	
	
	if request.method == "POST":
		
		if x.exists():
			messages.info(request,f"Failed!, Students already exists, You can't add student twice")
			return redirect('add_important_informations')

		form=AddImportantInformationsForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,f"Informations  were added Successfully")
			return redirect('add_important_informations')

	context = {
		"form":form,

	}
	
	return render(request, 'ImportantInformations/add_important_informations.html', context)


def important_informations(request):
	informations = ImportantInformations.objects.all()

	#HIZI NI KWA AJILI YA KUCHANGE PAGE TO EXCEL FILE
	form = ChangeImportantInformationsPageToExcelForm(request.POST or None)

	if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['content-Disposition'] = 'attachment; filename="Important Students Informations.csv"'
			writer = csv.writer(response)
			writer.writerow(['FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'GENDER','TABIA', 'ANADAIWA'])
			instance = informations
			for x in informations:
				writer.writerow([x.students.first_name,x.students.middle_name,x.students.last_name,x.students.gender,x.habit,x.debt])
			return response

	#MWISHO HAPA
	

	context = {
		"informations":informations,
		"form":form,
	}

	return render(request, 'ImportantInformations/important_informations.html',context)



@login_required(login_url='signin')
def update_important_informations(request,id):
	x= ImportantInformations.objects.get(id=id)
	form = UpdateImportantInformationsForm(instance=x)
	
	
	
	if request.method == "POST":
		

		form=UpdateImportantInformationsForm(request.POST or None, files=request.FILES,instance=x)
		if form.is_valid():
			form.save()
			messages.success(request,f"{x.students.first_name} {x.students.middle_name} {x.students.last_name} Informations  were Updated Successfully")
			return redirect('important_informations')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'ImportantInformations/update_important_informations.html', context)


@login_required(login_url='signin')
def delete_important_informations(request,id):
	x = ImportantInformations.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"{x.students.first_name} {x.students.middle_name} {x.students.last_name} Informations were deleted Successfully")
		return redirect('important_informations')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'ImportantInformations/delete_important_informations.html', context)


@login_required(login_url='signin')
def view_important_informations(request,id):
	x = ImportantInformations.objects.get(id=id)

	
	context = {
		
		"x":x,

	}
	
	return render(request, 'ImportantInformations/view_important_informations.html', context)



@login_required(login_url='signin')
def search_important_informations(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(students__last_name__icontains=query)|Q(students__first_name__icontains=query)|Q(students__middle_name__icontains=query)
        results=ImportantInformations.objects.filter(mysearch)
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'ImportantInformations/search_important_informations.html',context)










#SEND EMAIL AND SMS VIEWS
def add_send_sms_and_email(request):
	form = SendSmsEmailForm()
	students= request.POST.get('students')
	x= SendSmsEmail.objects.filter(students=students)
	if request.method == 'POST':
		if x.exists():
			messages.info(request,f"Failed!, You can't send sms or email twice to the same student")
			return redirect('add_send_sms_and_email')
		form = SendSmsEmailForm(request.POST)
		if form.is_valid():
			form.save()


			#HIZI NIKWA AJILI YA KUTUMA EMAIL KWA MZAZI

			to = request.POST.get('email')
			name = request.POST.get('students')
			phone = request.POST.get('phone')
			
			send_through_email = request.POST.get('send_through_email')
			send_through_text = request.POST.get('send_through_text')
			
						
			html_content = render_to_string(
				"SendSmsEmail/send_sms_email_template.html",
				{
				'title':'Students Report System ', 
				'name':name,
				'phone':phone,
				'send_through_email':send_through_email,
				"send_through_text":send_through_text
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"Students Report System",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)

			
		#context={
			#"title":'send email'
		#}

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST.get('name')
			phone = request.POST.get('phone')
			send_through_email = request.POST.get('send_through_email')
			send_through_text = request.POST.get('send_through_text')

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "88165b7478ba4628ad0dcd8a6593922d"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=send_through_text,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			
			messages.success(request,f"Email sent successfully to {to} and message sent successfully to {phone}")
			return redirect('add_send_sms_and_email')
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			
	return render(request, 'SendSmsEmail/add_send_sms_and_email.html', {"form":form})



def all_sms_email_sent_students(request):
	sms = SendSmsEmail.objects.all()

	#HIZI NI KWA AJILI YA KUCHANGE PAGE TO EXCEL FILE
	form = ChangeSendSmsEmailPageToExcelForm(request.POST or None)

	if form['export_to_CSV'].value() == True:
			response = HttpResponse(content_type='text/csv')
			response['content-Disposition'] = 'attachment; filename="Send Sms ana Email Students.csv"'
			writer = csv.writer(response)
			writer.writerow(['FIRST NAME', 'MIDDLE NAME', 'LAST NAME', 'GENDER','EMAIL', 'PHONE','MESSAGE','DATE & TIME'])
			instance = sms
			for x in sms:
				writer.writerow([x.students.first_name,x.students.middle_name,x.students.last_name,x.students.gender,x.email,x.phone,x.send_through_text,x.post_date])
			return response

	#MWISHO HAPA
	

	context = {
		"sms":sms,
		"form":form,
	}

	return render(request, 'SendSmsEmail/all_sms_email_sent_students.html',context)


def update_send_sms_and_email(request,id=id):
	
	x=SendSmsEmail.objects.get(id=id)
	form = UpdateSendSmsEmailForm(instance=x)
	
	if request.method == 'POST':
		
		form = UpdateSendSmsEmailForm(request.POST,instance=x)
		if form.is_valid():
			form.save()


			#HIZI NIKWA AJILI YA KUTUMA EMAIL KWA MZAZI

			to = request.POST.get('email')
			name = request.POST.get('students')
			phone = request.POST.get('phone')
			
			send_through_email = request.POST.get('send_through_email')
			send_through_text = request.POST.get('send_through_text')
			
						
			html_content = render_to_string(
				"SendSmsEmail/send_sms_email_template.html",
				{
				'title':'Students Report System ', 
				'name':name,
				'phone':phone,
				'send_through_email':send_through_email,
				"send_through_text":send_through_text
				
				
				
				})
			text_content = strip_tags(html_content)
			email = EmailMultiAlternatives(
			"Students Report System",
			#content
			text_content,
			#from email
			settings.EMAIL_HOST_USER,
			[to]


			)
			email.attach_alternative(html_content,"text/html")
			email.send(fail_silently=True)

			
		#context={
			#"title":'send email'
		#}

			#HIZI NI KWA AJILI YA KUTUMA SMS KWA MZAZI
			name = request.POST.get('name')
			phone = request.POST.get('phone')
			send_through_email = request.POST.get('send_through_email')
			send_through_text = request.POST.get('send_through_text')

			account_sid = "AC8d65d3310f680df6905c512df6690afb"
			auth_token = "88165b7478ba4628ad0dcd8a6593922d"
			client = Client(account_sid, auth_token)
			message = client.messages \
						.create(
							body=send_through_text,
							from_='+17692248509',
							#to='+255628431507'
							to =phone
									)
			print("message sent successfully")
			
			messages.success(request,f"Email sent successfully to {to} and message sent successfully to {phone}")
			return redirect('add_send_sms_and_email')
			#sendsms()

			#ZINAISHIA HAPA HIZO ZA KUTUMA SMS

			
	return render(request, 'SendSmsEmail/update_send_sms_and_email.html', {"form":form})



@login_required(login_url='signin')
def delete_sms_email_sent_students(request,id):
	x = SendSmsEmail.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"{x.students.first_name} {x.students.middle_name} {x.students.last_name} Informations were deleted Successfully")
		return redirect('all_sms_email_sent_students')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'SendSmsEmail/delete_sms_email_sent_students.html', context)


@login_required(login_url='signin')
def view_sms_email_sent_students(request,id):
	x = SendSmsEmail.objects.get(id=id)

	
	context = {
		
		"x":x,

	}
	
	return render(request, 'SendSmsEmail/view_sms_email_sent_students.html', context)



@login_required(login_url='signin')
def search_sms_email_sent_students(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(students__last_name__icontains=query)|Q(students__first_name__icontains=query)|Q(students__middle_name__icontains=query)
        results=SendSmsEmail.objects.filter(mysearch)
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'SendSmsEmail/search_sms_email_sent_students.html',context)














#PANGILIA ALAMA
def alama(request):
	alama = PangiliaAlama.objects.all()

	context = {
		"alama":alama,
		
	}

	return render(request, 'PangiliaAlama/alama.html',context)

@login_required(login_url='signin')
def add_pangilia_alama(request):
	form = PangiliaAlamaForm()
	
	
	
	if request.method == "POST":
		
		

		form=PangiliaAlamaForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,f"Added Successfully")
			return redirect('alama')

	context = {
		"form":form,

	}
	
	return render(request, 'PangiliaAlama/add_pangilia_alama.html', context)











#OTHER SYSTEMS MADE BY ME
@login_required(login_url='signin')
def other_systems_made_by_me(request):
	

	return render(request, 'OtherSystems/other_systems_made_by_me.html')



#HOW TO USE THIS SYSTEM
@login_required(login_url='signin')
def how_to_use_this_system(request):
	

	return render(request, 'HowToUseSystem/how_to_use_this_system.html')













#INDIVIDUAL RESULTS
@login_required(login_url='signin')
def add_individual_results(request):
	form = AddIndividualResultsForm()
	#registerstudents__last_name__icontains
	students= request.POST.get('students')
	x= IndividualResults.objects.filter(students=students)
	
	
	if request.method == "POST":
		
		if x.exists():
			messages.info(request,f"Failed!, Students already exists, You can't add student results twice")
			return redirect('add_individual_results')

		form=AddIndividualResultsForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,f"Student Results  were added Successfully")
			return redirect('add_individual_results')

	context = {
		"form":form,

	}
	
	return render(request, 'IndividualResults/add_individual_results.html', context)



@login_required(login_url='signin')
def all_individual_results(request):
	results = IndividualResults.objects.all()

	context = {
		"results":results,
	}

	return render(request, 'IndividualResults/all_individual_results.html',context)




@login_required(login_url='signin')
def search_individual_results(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(students__students__last_name__icontains=query)|Q(students__students__first_name__icontains=query)|Q(students__students__middle_name__icontains=query)
        results=IndividualResults.objects.filter(mysearch)
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'IndividualResults/search_individual_results.html',context)




@login_required(login_url='signin')
def view_individual_results(request,id):
	x = IndividualResults.objects.get(id=id)

	context = {
		"x":x,
	}

	return render(request, 'IndividualResults/view_individual_results.html',context)

@login_required(login_url='signin')
def update_individual_results(request,id):
	x= IndividualResults.objects.get(id=id)
	form = AddIndividualResultsForm(instance=x)
	#registerstudents__last_name__icontains
	
	
	
	
	if request.method == "POST":

		form=AddIndividualResultsForm(request.POST or None, files=request.FILES, instance=x)
		if form.is_valid():
			form.save()
			messages.success(request,f"{x.students.students.first_name} {x.students.students.middle_name} {x.students.students.last_name} Results  were Updated Successfully")
			return redirect('all_individual_results')

	context = {
		"form":form,
		"x":x,

	}
	
	return render(request, 'IndividualResults/update_individual_results.html', context)

@login_required(login_url='signin')
def delete_individual_results(request,id):
	x = IndividualResults.objects.get(id=id)

	if request.method == "POST":
		
		x.delete()
		messages.success(request,f"{x.students.students.first_name} {x.students.students.middle_name} {x.students.students.last_name} Results were deleted Successfully")
		return redirect('all_individual_results')
	

	context = {
		
		"x":x,

	}
	
	return render(request, 'IndividualResults/delete_individual_results.html', context)




#CODES ZA KUPRINT INDIVIDUAL RESULTS ZINAANZIA HAPA
def print_individual_results(request):
    
    
	results = IndividualResults.objects.all()
	
	template_path = 'IndividualResults/print_individual_results.html'
    #results = KawaidaDozi.objects.get(id=id)
	context = {
	    "results": results,
	    


	}
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="GeneralResults.pdf"'
	#if you want to download before opening it
	#response['Content-Disposition'] = 'attachment; filename="report.pdf"'
	template = get_template(template_path)
	html = template.render(context)

	pisa_status= pisa.CreatePDF(
	    html, dest=response)
	if pisa_status.err:
	    return HttpResponse('we had some errors <pre>' + html + '</pre>')
	return response