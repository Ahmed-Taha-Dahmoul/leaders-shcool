from django import template

register = template.Library()

@register.filter
def get_by_student(student_grades, student):
    return student_grades.get(student.id)

