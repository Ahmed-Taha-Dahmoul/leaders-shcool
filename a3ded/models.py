from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class SchoolClass(models.Model):
    name = models.CharField(max_length=255)
    teachers = models.ManyToManyField(Teacher)
    english = models.PositiveIntegerField(choices=[(1, 'One Field'), (2, 'Two Fields')], default=1)
    
    def __str__(self):
        return self.name


class Trimestre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=255)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        created = not self.pk  # Check if the student is being created or updated

        super().save(*args, **kwargs)

        if created:
            trimestres = Trimestre.objects.all()
            subjects = Subject.objects.filter(school_class=self.school_class)
            special_subject_names = ['arbi', 'francai', 'anglai']

            for trimestre in trimestres:
                for subject in subjects:
                    if subject.name.lower() in special_subject_names:
                        if subject.name.lower() == 'arbi':
                            model = Arbi
                            defaults = {
                                'test': 0,
                                'chifehi': 0,
                                'kira2a': 0,
                                'intej': 0,
                            }
                        elif subject.name.lower() == 'francai':
                            model = Francai
                            defaults = {
                                'test': 0,
                                'exp': 0,
                                'lecture': 0,
                                'production': 0,
                            }
                        elif subject.name.lower() == 'anglai':
                            model = Anglai
                            defaults = {
                                'test': 0,
                            }

                        # Check the value of the 'english' field in the associated SchoolClass
                            if self.school_class.english == 2:
                                defaults['oral'] = 0

                        model.objects.create(
                            trimestre=trimestre,
                            student=self,
                            subject=subject,
                            **defaults
                        )
                    else:
                        Grade.objects.create(
                            trimestre=trimestre,
                            student=self,
                            subject=subject,
                            test=0
                    )



class Grade(models.Model):
    trimestre = models.ForeignKey(Trimestre, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    test = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return f"Grade for {self.student} in {self.subject}"


class Arbi(Grade):
    chifehi = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    kira2a = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    intej = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return f"Arbi Grade for {self.student} in {self.subject}"
    



class Francai(Grade):
    exp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    lecture = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    production = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return f"Francai Grade for {self.student} in {self.subject}"
    



class Anglai(Grade):
    oral = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    

    def __str__(self):
        return f"Anglai Grade for {self.student} in {self.subject}"

