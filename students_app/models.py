
from django.db import models

# student_class:
# 	first_name
# 	last_name
# 	date_of_birth
# 	phone_number
# 	email
# 	gender
# 	id_course
# import courses_app.models
#
# GENDER_CHOICES = (
#     ('female', 'female'),
#     ('male', 'male'),
#     ('-', '-'),
#                   )
#
#
# class Gender(models.Model):
#
import courses_app.models


class Student(models.Model):
    GENDER_CHOICES = (
        ('female', 'female'),
        ('male', 'male'),
        ('-', '-'),
                      )

    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='-'
                              )
    course = models.ForeignKey(courses_app.models.Course, on_delete=models.CASCADE)

    class Meta:
        ordering = ['second_name']
        unique_together = (
            'first_name',
            'second_name',
            'date_of_birth',
            'email',
        )

    def __str__(self):
        return f'{self.second_name}' f' {self.first_name}'

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.second_name = self.second_name.capitalize()
        super(Student, self).save(*args, **kwargs)
        # for field_name in ['first_name', 'second_name']:
        #     val = getattr(self, field_name, False)
        #     if val:
        #         setattr(self, field_name, val.capitalize())
        # super(Student, self).save(*args, **kwargs)



