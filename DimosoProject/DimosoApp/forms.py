from DimosoApp.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class AddStudentForm(forms.ModelForm):
	image=forms.ImageField(
		required=False,

		widget = forms.FileInput(attrs={'id':'image'})

	)
	regno=forms.IntegerField(
	    
		widget = forms.NumberInput(attrs={'placeholder':'Student Registration Number'})

	)
	first_name=forms.CharField(
	    
		widget = forms.TextInput(attrs={'placeholder':'Student First Name'})

	)
	middle_name=forms.CharField(
	    
		widget = forms.TextInput(attrs={'placeholder':'Student Middle Name'})

	)
	last_name=forms.CharField(
	    
		widget = forms.TextInput(attrs={'placeholder':'Student Last Name'})

	) 
	email=forms.EmailField(
	    
		widget = forms.TextInput(attrs={'placeholder':'Student Parents Email'})

	)
	phone=forms.CharField(
	    
		widget = forms.TextInput(attrs={'placeholder':'Student Parents Phone'})

	)  
	
 
	
	
	class Meta:
		model = RegisterStudents
		fields =['regno','first_name','middle_name','last_name','email', 'phone','gender','image']


class UpdateStudentForm(forms.ModelForm):
	image=forms.ImageField(
		required=False,

		widget = forms.FileInput(attrs={'id':'image'})

	)
	regno=forms.IntegerField(
	    
		widget = forms.NumberInput(attrs={'placeholder':'Student Registration Number'})

	)
	first_name=forms.CharField(
	    
		widget = forms.TextInput(attrs={'placeholder':'Student First Name'})

	)
	middle_name=forms.CharField(
	    
		widget = forms.TextInput(attrs={'placeholder':'Student Middle Name'})

	)
	last_name=forms.CharField(
	    
		widget = forms.TextInput(attrs={'placeholder':'Student Last Name'})

	) 
	email=forms.EmailField(
	    
		widget = forms.TextInput(attrs={'placeholder':'Student Parents Email'})

	)
	phone=forms.CharField(
	    
		widget = forms.TextInput(attrs={'placeholder':'Student Parents Phone'})

	)  
	
 
	
	
	class Meta:
		model = RegisterStudents
		fields =['regno','first_name','middle_name','last_name','email', 'phone','gender','image']



class StudentsSearchForm(forms.ModelForm):
	
	last_name = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'lastname', 'placeholder' : 'Enter Student Last Name'})

	)
	


	class Meta:
		model = RegisterStudents
		fields =['last_name']





class AddStudentMarksForm(forms.ModelForm):
	 
	
	
	class Meta:
		model = Marks
		fields ='__all__'
class UpdateStudentMarksForm(forms.ModelForm):
	 
	
	
	class Meta:
		model = Marks
		fields =["Test1","Test2","Test3","Test4","Test5","MidTerm", "Term","total_marks","marks", "Average"]

class SearchStudentMarksForm(forms.ModelForm):
	export_to_CSV = forms.BooleanField(
		required=True,
		widget = forms.CheckboxInput(attrs={'id':'checki'})
		)
	 
	
	
	class Meta:
		model = Marks
		fields =['export_to_CSV']





class AddMoreSubjectsForm(forms.ModelForm):
	image=forms.ImageField(
		required=False,

		widget = forms.FileInput(attrs={'id':'image'})

	)
	subject_no=forms.IntegerField(
	    
		widget = forms.NumberInput(attrs={'placeholder':'Enter Subject Number'})

	)
	subject_name=forms.CharField(
	    
		widget = forms.TextInput(attrs={'placeholder':'Enter Subject Name'})

	)
	link=forms.CharField(
	    
		widget = forms.TextInput(attrs={'placeholder':'Enter Subject Link'})

	)
	
	
	 
	
	
	class Meta:
		model = Subjects
		fields ='__all__'

class UpdateMoreSubjectsForm(forms.ModelForm):
	image=forms.ImageField(
		required=False,

		widget = forms.FileInput(attrs={'id':'image'})

	)
	subject_no=forms.IntegerField(
	    
		widget = forms.NumberInput(attrs={'placeholder':'Enter Subject Number'})

	)
	subject_name=forms.CharField(
	    
		widget = forms.TextInput(attrs={'placeholder':'Enter Subject Name'})

	)
	link=forms.CharField(
	    
		widget = forms.TextInput(attrs={'placeholder':'Enter Subject Link'})

	)
	 
	
	
	class Meta:
		model = Subjects
		fields ='__all__'




#GENERAL RESULTS

class AddGeneralResultsForm(forms.ModelForm):
	
	
	class Meta:
		model = GeneralResults
		fields ='__all__'

class UpdateGeneralResultsForm(forms.ModelForm):
	
	
	class Meta:
		model = GeneralResults
		fields = ['physics','chemistry','biology','english','civics','history','geography','mathematics','kiswahili','student_total','student_average','student_grade','student_point']


class ChangeGeneralResultsPageToExcelForm(forms.ModelForm):
	export_to_CSV = forms.BooleanField(
		required=True,
		widget = forms.CheckboxInput(attrs={'id':'checki'})
		)
	 
	
	
	class Meta:
		model = GeneralResults
		fields =['export_to_CSV']





#IMPORTANT INFORMATIONS

class AddImportantInformationsForm(forms.ModelForm):
	
	
	class Meta:
		model = ImportantInformations
		fields ='__all__'

class UpdateImportantInformationsForm(forms.ModelForm):
	
	
	class Meta:
		model = ImportantInformations
		fields =['habit','debt','description']

class ChangeImportantInformationsPageToExcelForm(forms.ModelForm):
	export_to_CSV = forms.BooleanField(
		required=True,
		widget = forms.CheckboxInput(attrs={'id':'checki'})
		)
	 
	
	
	class Meta:
		model = ImportantInformations
		fields =['export_to_CSV']




#SEND SMS AND EMAIL
class SendSmsEmailForm(forms.ModelForm):


    class Meta:
        model = SendSmsEmail
        fields ='__all__'

class ChangeSendSmsEmailPageToExcelForm(forms.ModelForm):
	export_to_CSV = forms.BooleanField(
		required=True,
		widget = forms.CheckboxInput(attrs={'id':'checki'})
		)
	 
	
	
	class Meta:
		model = SendSmsEmail
		fields =['export_to_CSV']

class UpdateSendSmsEmailForm(forms.ModelForm):


    class Meta:
        model = SendSmsEmail
        fields =['email','phone','send_through_email','send_through_text']








#PANGILIA ALAMA
class PangiliaAlamaForm(forms.ModelForm):


    class Meta:
        model = PangiliaAlama
        fields ='__all__'






#INDIVIDUAL RESULTS
class AddIndividualResultsForm(forms.ModelForm):
	
	
	class Meta:
		model = IndividualResults
		fields ='__all__'