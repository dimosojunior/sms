
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('base/', views.base, name="base"),
    path('students/', views.students, name="students"),


    path('all_students/', views.all_students, name="all_students"),
    path('search_student_autocomplete/', views.search_student_autocomplete, name="search_student_autocomplete"),
    path('add_student/', views.add_student, name="add_student"),
    path('update_student/<int:id>/', views.update_student, name="update_student"),
    path('delete_student/<int:id>/', views.delete_student, name="delete_student"),


    path('subjects/', views.subjects, name="subjects"),
    path('add_student_marks/', views.add_student_marks, name="add_student_marks"),
    path('view_subject_marks/<int:id>/', views.view_subject_marks, name="view_subject_marks"),


    path('physics_subject_marks/', views.physics_subject_marks, name="physics_subject_marks"),
    path('update_physics_subject_marks/<int:id>/', views.update_physics_subject_marks, name="update_physics_subject_marks"),
    path('delete_physics_subject_marks/<int:id>/', views.delete_physics_subject_marks, name="delete_physics_subject_marks"),
    path('search_physics_subject_marks/', views.search_physics_subject_marks, name="search_physics_subject_marks"),
    


    path('chemistry_subject_marks/', views.chemistry_subject_marks, name="chemistry_subject_marks"),
    path('update_chemistry_subject_marks/<int:id>/', views.update_chemistry_subject_marks, name="update_chemistry_subject_marks"),
    path('delete_chemistry_subject_marks/<int:id>/', views.delete_chemistry_subject_marks, name="delete_chemistry_subject_marks"),
    path('search_chemistry_subject_marks/', views.search_chemistry_subject_marks, name="search_chemistry_subject_marks"),


    path('biology_subject_marks/', views.biology_subject_marks, name="biology_subject_marks"),
    path('update_biology_subject_marks/<int:id>/', views.update_biology_subject_marks, name="update_biology_subject_marks"),
    path('delete_biology_subject_marks/<int:id>/', views.delete_biology_subject_marks, name="delete_biology_subject_marks"),
    path('search_biology_subject_marks/', views.search_biology_subject_marks, name="search_biology_subject_marks"),
    

    path('english_subject_marks/', views.english_subject_marks, name="english_subject_marks"),
    path('update_english_subject_marks/<int:id>/', views.update_english_subject_marks, name="update_english_subject_marks"),
    path('delete_english_subject_marks/<int:id>/', views.delete_english_subject_marks, name="delete_english_subject_marks"),
    path('search_english_subject_marks/', views.search_english_subject_marks, name="search_english_subject_marks"),

    path('history_subject_marks/', views.history_subject_marks, name="history_subject_marks"),
    path('update_history_subject_marks/<int:id>/', views.update_history_subject_marks, name="update_history_subject_marks"),
    path('delete_history_subject_marks/<int:id>/', views.delete_history_subject_marks, name="delete_history_subject_marks"),
    path('search_history_subject_marks/', views.search_history_subject_marks, name="search_history_subject_marks"),


    path('kiswahili_subject_marks/', views.kiswahili_subject_marks, name="kiswahili_subject_marks"),
    path('update_kiswahili_subject_marks/<int:id>/', views.update_kiswahili_subject_marks, name="update_kiswahili_subject_marks"),
    path('delete_kiswahili_subject_marks/<int:id>/', views.delete_kiswahili_subject_marks, name="delete_kiswahili_subject_marks"),
    path('search_kiswahili_subject_marks/', views.search_kiswahili_subject_marks, name="search_kiswahili_subject_marks"),

    path('civics_subject_marks/', views.civics_subject_marks, name="civics_subject_marks"),
    path('update_civics_subject_marks/<int:id>/', views.update_civics_subject_marks, name="update_civics_subject_marks"),
    path('delete_civics_subject_marks/<int:id>/', views.delete_civics_subject_marks, name="delete_civics_subject_marks"),
    path('search_civics_subject_marks/', views.search_civics_subject_marks, name="search_civics_subject_marks"),


    path('geography_subject_marks/', views.geography_subject_marks, name="geography_subject_marks"),
    path('update_geography_subject_marks/<int:id>/', views.update_geography_subject_marks, name="update_geography_subject_marks"),
    path('delete_geography_subject_marks/<int:id>/', views.delete_geography_subject_marks, name="delete_geography_subject_marks"),
    path('search_geography_subject_marks/', views.search_geography_subject_marks, name="search_geography_subject_marks"),


    path('mathematics_subject_marks/', views.mathematics_subject_marks, name="mathematics_subject_marks"),
    path('update_mathematics_subject_marks/<int:id>/', views.update_mathematics_subject_marks, name="update_mathematics_subject_marks"),
    path('delete_mathematics_subject_marks/<int:id>/', views.delete_mathematics_subject_marks, name="delete_mathematics_subject_marks"),
    path('search_mathematics_subject_marks/', views.search_mathematics_subject_marks, name="search_mathematics_subject_marks"),



    #MORE SUBJECTS
    path('add_more_subjects/', views.add_more_subjects, name="add_more_subjects"),
    path('update_more_subjects/<int:id>/', views.update_more_subjects, name="update_more_subjects"),
    path('delete_more_subjects/<int:id>/', views.delete_more_subjects, name="delete_more_subjects"),


    #GENERAL RESULTS
    path('add_general_results/', views.add_general_results, name="add_general_results"),
    path('students_general_results/', views.students_general_results, name="students_general_results"),
    path('update_general_results/<int:id>/', views.update_general_results, name="update_general_results"),
    path('delete_general_results/<int:id>/', views.delete_general_results, name="delete_general_results"),
    path('search_general_results/', views.search_general_results, name="search_general_results"),
    path('print_students_general_results/', views.print_students_general_results, name="print_students_general_results"),

  

    #IMOPRTANT INFORMATIONS
    path('add_important_informations/', views.add_important_informations, name="add_important_informations"),  
    path('important_informations/', views.important_informations, name="important_informations"),
    path('update_important_informations/<int:id>/', views.update_important_informations, name="update_important_informations"),
    path('delete_important_informations/<int:id>/', views.delete_important_informations, name="delete_important_informations"),
    path('view_important_informations/<int:id>/', views.view_important_informations, name="view_important_informations"),
    path('search_important_informations/', views.search_important_informations, name="search_important_informations"),




    #SEND SMS AND EMAIL
    path('add_send_sms_and_email/', views.add_send_sms_and_email, name="add_send_sms_and_email"),
    path('all_sms_email_sent_students/', views.all_sms_email_sent_students, name="all_sms_email_sent_students"),
    path('update_send_sms_and_email/<int:id>/', views.update_send_sms_and_email, name="update_send_sms_and_email"),
    path('delete_sms_email_sent_students/<int:id>/', views.delete_sms_email_sent_students, name="delete_sms_email_sent_students"),
    path('view_sms_email_sent_students/<int:id>/', views.view_sms_email_sent_students, name="view_sms_email_sent_students"),
    path('search_sms_email_sent_students/', views.search_sms_email_sent_students, name="search_sms_email_sent_students"),







    #PANGILIA ALAMA
    path('alama/', views.alama, name="alama"),
    path('add_pangilia_alama/', views.add_pangilia_alama, name="add_pangilia_alama"),




    #OTHER SYSTEMS MADE BY ME
    path('other_systems_made_by_me/', views.other_systems_made_by_me, name="other_systems_made_by_me"),

    #HOW TO USE THIS SYSTEM
    path('how_to_use_this_system/', views.how_to_use_this_system, name="how_to_use_this_system"),








    #INDIVIDUAL RESULTS
    path('add_individual_results/', views.add_individual_results, name="add_individual_results"),
    path('all_individual_results/', views.all_individual_results, name="all_individual_results"),
    path('search_individual_results/', views.search_individual_results, name="search_individual_results"),
    path('view_individual_results/<int:id>/', views.view_individual_results, name="view_individual_results"),
    path('update_individual_results/<int:id>/', views.update_individual_results, name="update_individual_results"),
    path('delete_individual_results/<int:id>/', views.delete_individual_results, name="delete_individual_results"),
    path('print_individual_results/', views.print_individual_results, name="print_individual_results"),


]