from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from .models import SchoolClass, Student, Subject, Grade, Trimestre, Arbi 
from .forms import TeacherLoginForm

User = get_user_model()

@login_required
def home_page(request):
    
    teacher = request.user.teacher  # Assuming you have a OneToOne relationship between User and Teacher
    context = {
        'teacher_name': teacher.name
    }
    return render(request, 'home.html' , context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('a3ded:home')
    if request.method == 'POST':
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('a3ded:home')
    else:
        form = TeacherLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def classes_view(request):
    teacher = request.user.teacher
    classes = SchoolClass.objects.filter(teachers=teacher)

    context = {
        'classes': classes,
    }

    return render(request, 'classes.html', context)


@login_required
def trimestre_view(request, class_id):
    school_class = get_object_or_404(SchoolClass, id=class_id)
    trimestres = Trimestre.objects.all()

    context = {
        'school_class': school_class,
        'trimestres': trimestres
    }

    return render(request, 'trimestre.html', context)


@login_required
def subjects_view(request, class_id, trimestre_id):
    teacher = request.user.teacher
    school_class = get_object_or_404(SchoolClass, id=class_id, teachers=teacher)

    subjects = Subject.objects.filter(school_class=school_class, teachers=teacher)

    # Create a dictionary for subject name translations
    subject_name_translations = {
        'arbi': 'العربية',
        'francai':'français',
        'anglai' : 'anglais',
        # Add more mappings as needed
    }

    # Replace subject names with their Arabic equivalents
    for subject in subjects:
        subject.name = subject_name_translations.get(subject.name, subject.name)

    context = {
        'subjects': subjects,
        'class_id': class_id,
        'trimestre_id': trimestre_id
    }

    return render(request, 'subjects.html', context)



from .models import Francai, Anglai

@login_required
def grades_view(request, class_id, trimestre_id, subject_id):
    # Retrieve the school class, trimester, and subject
    school_class = get_object_or_404(SchoolClass, pk=class_id)
    trimestre = get_object_or_404(Trimestre, pk=trimestre_id)
    subject = get_object_or_404(Subject, pk=subject_id)

    # Retrieve the students in the school class
    students = Student.objects.filter(school_class=school_class)

    if request.method == 'POST':
        # Process the form submission and update the grades
        for student in students:
            # Get the grade for the student, if it exists
            try:
                grade = Grade.objects.select_related('arbi', 'francai', 'anglai').get(
                    student=student,
                    trimestre=trimestre,
                    subject=subject
                )
            except Grade.DoesNotExist:
                grade = Grade(
                    student=student,
                    trimestre=trimestre,
                    subject=subject
                )

            # Update the grade fields if provided in the form data
            test_grade = request.POST.get('test_{}'.format(student.id))
            if test_grade:
                grade.test = test_grade

            if subject.name.lower() == "arbi":
                # Get the related Arbi object
                arbi = grade.arbi
                if arbi is None:
                    arbi = Arbi(grade=grade)
                    grade.arbi = arbi

                arbi.chifehi = request.POST.get('chifehi_{}'.format(student.id))
                arbi.kira2a = request.POST.get('kira2a_{}'.format(student.id))
                arbi.intej = request.POST.get('intej_{}'.format(student.id))
                arbi.save()
            elif subject.name.lower() == "francai":
                # Get the related Francai object
                francai = grade.francai
                if francai is None:
                    francai = Francai(grade=grade)
                    grade.francai = francai

                francai.exp = request.POST.get('exp_{}'.format(student.id))
                francai.lecture = request.POST.get('lecture_{}'.format(student.id))
                francai.production = request.POST.get('production_{}'.format(student.id))
                francai.save()
            elif subject.name.lower() == "anglai":
                # Get the related Anglai object
                anglai = grade.anglai
                if anglai is None:
                    anglai = Anglai(grade=grade)
                    grade.anglai = anglai

                english_field = 'oral'
                if school_class.english == 1:
                    english_field = 'test'

                anglai_field = request.POST.get('anglai_{}'.format(student.id))
                if anglai_field:
                    setattr(anglai, english_field, anglai_field)
                anglai.oral = request.POST.get('oral_{}'.format(student.id))
                anglai.save()

            grade.save()

        return redirect('a3ded:grades', class_id=class_id, trimestre_id=trimestre_id, subject_id=subject_id)

    # Retrieve the grades for the given trimester and subject, including related Arbi, Francai, and Anglai objects
    grades = Grade.objects.select_related('arbi', 'francai', 'anglai').filter(trimestre=trimestre, subject=subject)

    # Create a dictionary to store student grades
    student_grades = {}

    # Populate the dictionary with student grades
    for student in students:
        try:
            grade = grades.get(student=student)
        except Grade.DoesNotExist:
            grade = None

        student_grades[student.id] = grade

    context = {
    'class_id': class_id,
    'trimestre_id': trimestre_id,
    'subject_id': subject_id,
    'students': students,
    'student_grades': student_grades,
    'trimestre': trimestre,
    'subject': subject,
    'class': school_class,  # Add this line to include the class object in the context
    }

    return render(request, 'grades.html', context)










