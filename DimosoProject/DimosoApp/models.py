from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

    

  #HII NI PATH KWA AJILI YA KUHIFADHI HIZO IMAGE      
def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"44.jpg"}'

#HII NI KWA AJILI YA KUPATA DEFAULT IMAGE KM MTU ASIPO INGIZA IMAGE ILI ISILETE ERRORS
def get_default_profile_image():
    return "media/44.jpg"

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    middle_name=models.CharField(verbose_name="middle name", max_length=100, unique=False)
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    company_name=models.CharField(verbose_name="company name", max_length=100, unique=False)
    phone=models.CharField(verbose_name="phone", max_length=15)
    profile_image = models.ImageField(upload_to='get_profile_image_filepath', blank=True, null=True)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    Role_Choices = (
            ('MULTI TEACHER', 'MULTI TEACHER'),
            ('PHYSICS TEACHER', 'PHYSICS TEACHER'),
            ('CHEMISTRY TEACHER', 'CHEMISTRY TEACHER'),
            ('BIOLOGY TEACHER', 'BIOLOGY TEACHER'),
            ('ENGLISH TEACHER', 'ENGLISH TEACHER'),
            ('CIVICS TEACHER', 'CIVICS TEACHER'),
            ('MATHEMATICS TEACHER', 'MATHEMATICS TEACHER'),
            ('HISTORY TEACHER', 'HISTORY TEACHER'),
            ('GEOGRAPHY TEACHER', 'GEOGRAPHY TEACHER'),
            ('KISWAHILI TEACHER', 'KISWAHILI TEACHER'),
        )

    role=models.CharField(verbose_name="role", choices=Role_Choices, max_length=50)
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


        
class Activities(models.Model):
    #id = models.CharField(max_length=100, primary_key=True)
    activity_name = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="Activities/")
    recorded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True, null=True)

    def __str__(self):
        return self.activity_name
    class Meta:
        verbose_name_plural = "Activities"


class RegisterStudents(models.Model):
    #id = models.CharField(max_length=100, primary_key=True)
    regno=models.IntegerField(unique=True)
    first_name=models.CharField(max_length=200)
    middle_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email = models.EmailField(max_length=30,unique=True)

    
    Gender_Choices = (
            ('', 'Choose Gender'),
            ('Male', 'Male'),
            ('Female', 'Female'),
        )
    gender = models.CharField(choices=Gender_Choices,max_length=7, blank=True,null=True)
    
    recorded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True, null=True)
    image = models.ImageField(upload_to="StudentsImages/", blank=True,null=True)
    phone=models.CharField(max_length=13)

    def __str__(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name 
    class Meta:
        verbose_name_plural = "RegisterStudents"

class Subjects(models.Model):
    #id = models.CharField(max_length=100, primary_key=True)
    subject_no=models.IntegerField(unique=True)
    subject_name=models.CharField(max_length=200)
    link = models.CharField(max_length=200, blank=True, null=True)
    recorded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now = True, blank=True, null=True)
    image = models.ImageField(upload_to="SubjectsImages/", blank=True,null=True)
    

    def __str__(self):
        return self.subject_name  
    class Meta:
        verbose_name_plural = "Subjects"


class Marks(models.Model):
    #id = models.CharField(max_length=100, primary_key=True)
    registerstudents=models.ForeignKey(RegisterStudents,on_delete=models.CASCADE)
    subjects=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    Test1=models.IntegerField(default=0, blank=True, null=True)
    Test2=models.IntegerField(default=0, blank=True, null=True)
    Test3=models.IntegerField(default=0, blank=True, null=True)
    Test4=models.IntegerField(default=0, blank=True, null=True)
    Test5=models.IntegerField(default=0, blank=True, null=True)
    MidTerm=models.IntegerField(default=0, blank=True, null=True)
    Term=models.IntegerField(default=0, blank=True, null=True)
    subject_point=models.CharField(max_length=50, default="A", blank=True, null=True)
    marks = RichTextUploadingField(blank=True, null=True)
    total_marks=models.IntegerField(blank=False, null=False)
    Average=models.DecimalField(decimal_places=3, max_digits=100,blank=False, null=False)
    
    def __str__(self):
        return self.registerstudents.first_name  
    class Meta:
        verbose_name_plural = "Marks"



class GeneralResults(models.Model):
    #id = models.CharField(max_length=100, primary_key=True)
    students=models.OneToOneField(RegisterStudents,on_delete=models.CASCADE)
    #subjects=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    link = models.CharField(max_length=200, blank=True, null=True)

    physics=models.IntegerField(default=0, blank=True, null=True)
    physics_total_marks=models.IntegerField(default=0, blank=True, null=True)
    physics_average=models.DecimalField(decimal_places=4, max_digits=5,blank=True, null=True)

    chemistry=models.IntegerField(default=0, blank=True, null=True)
    chemistry_total_marks=models.IntegerField(default=0, blank=True, null=True)
    chemistry_average=models.DecimalField(decimal_places=4, max_digits=5,blank=True, null=True)

    biology=models.IntegerField(default=0, blank=True, null=True)
    biology_total_marks=models.IntegerField(default=0, blank=True, null=True)
    biology_average=models.DecimalField(decimal_places=4, max_digits=5,blank=True, null=True)

    civics=models.IntegerField(default=0, blank=True, null=True)
    civics_total_marks=models.IntegerField(default=0, blank=True, null=True)
    civics_average=models.DecimalField(decimal_places=4, max_digits=5,blank=True, null=True)

    history=models.IntegerField(default=0, blank=True, null=True)
    history_total_marks=models.IntegerField(default=0, blank=True, null=True)
    history_average=models.DecimalField(decimal_places=4, max_digits=10,blank=True, null=True)


    english=models.IntegerField(default=0, blank=True, null=True)
    english_total_marks=models.IntegerField(default=0, blank=True, null=True)
    english_average=models.DecimalField(decimal_places=4, max_digits=5,blank=True, null=True)

    kiswahili=models.IntegerField(default=0, blank=True, null=True)
    kiswahili_total_marks=models.IntegerField(default=0, blank=True, null=True)
    kiswahili_average=models.DecimalField(decimal_places=4, max_digits=5,blank=True, null=True)

    mathematics=models.IntegerField(default=0, blank=True, null=True)
    mathematics_total_marks=models.IntegerField(default=0, blank=True, null=True)
    mathematics_average=models.DecimalField(decimal_places=4, max_digits=5,blank=True, null=True)

    geography=models.IntegerField(default=0, blank=True, null=True)
    geography_total_marks=models.IntegerField(default=0, blank=True, null=True)
    geography_average=models.DecimalField(decimal_places=4, max_digits=5,blank=True, null=True)


    student_total=models.IntegerField(default=0, blank=True, null=True)
    student_average=models.DecimalField(default=0.0000, decimal_places=3, max_digits=100,blank=True, null=True)
    student_point = models.CharField(max_length=200, blank=True, null=True)
    student_grade = models.CharField(max_length=200, blank=True, null=True)
    
    
    
    
    

    def __str__(self):
        return self.students.first_name + " " + self.students.middle_name + " " + self.students.last_name  
    class Meta:
        verbose_name_plural = "GeneralResults"




#IMPORTANT INFORMATIONS
class ImportantInformations(models.Model):
    
    students=models.OneToOneField(RegisterStudents,on_delete=models.CASCADE)
    Habit_Choices = (
            
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
            ("F", "F"),
            
        )
    habit = models.CharField(max_length=200, choices=Habit_Choices, blank=True, null=True)
    Debt_Choices = (
            
            ("No", "No"),
            ("Yes", "Yes"),
            
            
        )
    debt = models.CharField(max_length=30, choices=Debt_Choices, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    def __str__(self):
        return self.students.first_name + " " + self.students.middle_name + " " + self.students.last_name  
    class Meta:
        verbose_name_plural = "ImportantInformations"



class SendSmsEmail(models.Model):
    students=models.OneToOneField(RegisterStudents,on_delete=models.CASCADE)
    
    email = models.EmailField(default="@gmail.com",unique=True, blank=True, null=True)
    phone = models.CharField(default="+255",unique=True, max_length=13, blank=True, null=True)
    
    send_through_email = RichTextUploadingField(blank=True, null=True)
    send_through_text = models.TextField(blank=True, null=True)
        
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    

    def __str__(self):
        return self.students.first_name + " " + self.students.middle_name + " " + self.students.last_name 

    class Meta:
        verbose_name_plural = "SendSmsEmail"



#PANGILIA ALAMA
class PangiliaAlama(models.Model):
    
    A_start = models.CharField(max_length=3, blank=True, null=True)
    B_start = models.CharField(max_length=3, blank=True, null=True)
    C_start = models.CharField(max_length=3, blank=True, null=True)
    D_start = models.CharField(max_length=3, blank=True, null=True)
    E_start = models.CharField(max_length=3, blank=True, null=True)
    F_start = models.CharField(max_length=3, blank=True, null=True)

    A_end = models.CharField(max_length=3, blank=True, null=True)
    B_end = models.CharField(max_length=3, blank=True, null=True)
    C_end = models.CharField(max_length=3, blank=True, null=True)
    D_end = models.CharField(max_length=3, blank=True, null=True)
    E_end = models.CharField(max_length=3, blank=True, null=True)
    F_end = models.CharField(max_length=3, blank=True, null=True)
    
    
    

    def __str__(self):
        return self.A_start + " " + self.B_start + " " + self.C_start

    class Meta:
        verbose_name_plural = "PangiliaAlama"







#INDIVIDUAL RESULTS
class IndividualResults(models.Model):
    students=models.OneToOneField(GeneralResults,on_delete=models.CASCADE)
    alama=models.OneToOneField(PangiliaAlama,on_delete=models.CASCADE,blank=True, null=True)
    #results=models.OneToOneField(GeneralResults,on_delete=models.CASCADE, blank=True,null=True)
    Tabia_Choices = (
            
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
            ("F", "F"),
            
        )
    tabia=models.CharField(max_length=10,choices=Tabia_Choices, blank=True,null=True)

    school_name = models.CharField(default="ST DIMOSO SEMINARY", max_length=200, blank=True, null=True)
    kidato = models.CharField(default="I", max_length=30, blank=True, null=True)
    mhula = models.CharField(default="I", max_length=30, blank=True, null=True)
    mwaka = models.CharField(default="2022", max_length=30, blank=True, null=True)
    amekuwa_wa = models.CharField(default="5", max_length=30, blank=True, null=True)
    kati_ya = models.CharField(default="200", max_length=30, blank=True, null=True)

    #division = models.CharField(default="I", max_length=30, blank=True, null=True)
    #point = models.CharField(default="8",max_length=30, blank=True, null=True)
    school_close = models.CharField(default="20/11/2022", max_length=50, blank=True, null=True)
    school_open = models.CharField(default="20/01/2022", max_length=50, blank=True, null=True)
    maoni_ya_mwalimu_wa_darasa = models.TextField(max_length=1000, blank=True, null=True)
    maoni_ya_mkuu_wa_shule = models.TextField(max_length=1000, blank=True, null=True)

    jina_la_mkuu_wa_shule = models.CharField(max_length=50, blank=True, null=True)
    mahitaji = models.TextField(max_length=300, blank=True, null=True)
    maoni_ya_mzazi = models.TextField(max_length=300, blank=True, null=True)
    jina_la_mzazi = models.CharField(default="200", max_length=50, blank=True, null=True)
    tarehe = models.CharField(max_length=30, blank=True, null=True)
    saini = models.CharField(max_length=30, blank=True, null=True)    
    
    

    def __str__(self):
        return self.students.students.first_name + " " + self.students.students.middle_name + " " + self.students.students.last_name 

    class Meta:
        verbose_name_plural = "IndividualResults"