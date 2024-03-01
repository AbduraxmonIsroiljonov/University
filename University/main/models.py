from django.db import models
from django.contrib.auth.models import User


class Direction(models.Model):
    name = models.CharField(max_length=255)


class University(models.Model):
    location = models.ImageField()
    name = models.CharField(max_length=255)
    directions = models.ForeignKey(Direction, on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateTimeField()
    place = models.IntegerField()
    describtion = models.CharField(max_length=255)
    photo = models.ImageField()


class Degree(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)


class Category(models.Model):
    place = models.CharField(max_length=255)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)


class Profile(models.Model):
    fist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    photo = models.ImageField()
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    passport = models.CharField(max_length=255)
    ielts = models.IntegerField()


class PopularUniversity(models.Model):
    name = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    quality = models.IntegerField()
    describtion = models.CharField(max_length=255)
    price = models.IntegerField()
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)


class HowWeWork(models.Model):
    photo = models.ImageField()
    steps = models.CharField()


class StudentsComments(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    place = models.CharField(maxlengtj=255)


class GetInformation(models.Model):
    phone_number = models.IntegerField()


class Login(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    regitrate = models.CharField(max_length=255)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)


class LogedOrUnlogedList(models.Model):
    place = models.ImageField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    information = models.CharField(max_length=255)
    loged = models.CharField(max_length=50)
    unloged = models.CharField(max_length=50)


class Letter(models.Model):
    text = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=255)


class Agreement(models.Model):
    date = models.DateTimeField()
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    signature = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()


class Statics(models.Model):
    students = models.ForeignKey(Profile, on_delete=models.CASCADE)
    universities = models.ForeignKey(University, on_delete=models.CASCADE)
    place = models.CharField(max_length=255)
    directions = models.ForeignKey(Direction, on_delete=models.CASCADE)


class Filtr(models.Model):
    place = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    date = models.DateTimeField()


class LogedStudents(models.Model):
    fist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    photo = models.ImageField()
    ielts=models.IntegerField(max=9)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    passport = models.CharField(max_length=255)


class StudentList(models.Model):
    fist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    passport = models.CharField(max_length=255)
    ielts = models.IntegerField()


class StudentInfo(models.Model):
    fist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    photo = models.ImageField()
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    passport = models.CharField(max_length=255)
    ielts = models.IntegerField()


class ReasonforRejection(models.Model):
    reason = models.CharField(max_length=255)
