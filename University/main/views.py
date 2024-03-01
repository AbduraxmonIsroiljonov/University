from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import *
from main.serializer import *
from rest_framework import generics


@api_view
def create_student(request):
    Profile.objects.create(
        fist_name=request.POST.get("First_name"),
        last_name=request.POST.get("last_name"),
        middle_name=request.POST.get("middle_name"),
        photo=request.POST.get("photo"),
        direction=request.POST.get("direction"),
        university=request.POST.get("university"),
        degree=request.POST.get("degree"),
        passport=request.POST.get("passport"),
        ielts=request.POST.get("ielts"),
    )


@api_view(["POST"])
def check_ielts_score(score):
    good_score_threshold = 1
    for i in Profile:
        if i.ielts >= good_score_threshold:
            return True
    else:
        return False


def register_at_university(student_name, ielts_score):
    if not check_ielts_score(ielts_score):
        print(
            f"Congratulations, {student_name}! Your IELTS score is not good. You can register at the university."
        )
    else:
        print(
            f"Sorry, {student_name}. Your IELTS score is good. You should not be registered at the university."
        )


student_name = input("Enter student name: ")
ielts_score = float(input("Enter IELTS score: "))

register_at_university(student_name, ielts_score)


@api_view("POST")
def create_university(request):
    University.objects.create(
        location=request.POST.get("location"),
        name=request.POST.get("name"),
        directions=request.POST.get("direction"),
        price=request.POST.get("price"),
        place=request.POST.get("place"),
        describtion=request.POST.get("describtion"),
        photo=request.POST.get("photo"),
    )


@api_view(["POST"])
def create_direction(request):
    Direction.objects.create(name=request.POST.get("name"))


@api_view(["POST"])
def create_university(request):
    University.objects.create(
        name=request.POST.get("name"),
        location=request.POST.get("location"),
        describtion=request.POST.get("describtion"),
        directions=request.POST.get("directions"),
        price=request.POST.get("price"),
        photo=request.POST.get("photo"),
        place=request.POST.get("place"),
    )



@api_view(["POST"])
def create_category(request):
    Category.objects.create(
        name=request.POST.get("name"),
        degree=request.POST.get("degree"),
        direction=request.POST.get("direction"),
    )


@api_view(["POST"])
def edit_profile(request):
    user_profile = EditProfileSerializer.objects.get_or_create(user=request.user)[0]

    if request.method == "POST":
        form = EditProfileSerializer(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return EditProfileSerializer("profile")
        form = EditProfileSerializer(instance=user_profile)


@api_view(["POST"])
def create_degree(request):
    Degree.objects.create(university=request.POST.get("university"))


@api_view(["POST"])
def create_popular_university(request):
    if request.method == "POST":
        form = PopularUniversityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_popular_universities")
    else:
        form = PopularUniversityForm()


def my_filter(request):
    filter = Filtr.objects.all().filter(date=None)
    place = Filtr.objects.all().filter(place=None)
    place = Filtr.objects.all().filter(place=None)
    context = {"place": place, "place": place, "filter": filter}
    return render(request, context)


@api_view(["POST"])
def create_studentlist(request):
    StudentList.objects.create(
        ielts=request.POST.get("ielts"),
        first_name=request.POST.get("first_name"),
        last_name=request.POST.get("last_name"),
        photo=request.POST.get("photo"),
        middle_name=request.POST.get("middle_name"),
        direction=request.POST.get("direction"),
        degree=request.POST.get("degree"),
        passport=request.POST.get("passport"),
        university=request.POST.get("university"),
    )


@api_view(["POST"])
class HowWeWorkListCreateView(generics.ListCreateAPIView):
    queryset = HowWeWork.objects.all()
    serializer_class = HowWeWorkSerializer


@api_view(["POST"])
class HowWeWorkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HowWeWork.objects.all()
    serializer_class = HowWeWorkSerializer


@api_view("POST")
class StudentsCommentsListCreateView(generics.ListCreateAPIView):
    queryset = StudentsComments.objects.all()
    serializer_class = StudentsCommentsSerializer


@api_view("POST")
class StudentsCommentsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentsComments.objects.all()
    serializer_class = StudentsCommentsSerializer


@api_view("POST")
class GetInformationListCreateView(generics.ListCreateAPIView):
    queryset = GetInformation.objects.all()
    serializer_class = GetInformationSerializer


@api_view("POST")
class GetInformationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GetInformation.objects.all()
    serializer_class = GetInformationSerializer


@api_view("POST")
class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


@api_view("POST")
class UserProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


@api_view("POST")
def loged_students(request):
    for i in LogedStudents.objects:
        if i.objects.all == True:
            pass
        else:
            print("you need IELTS")


class LogedOrUnlogedListListCreateView(generics.ListCreateAPIView):
    queryset = LogedOrUnlogedList.objects.all()
    serializer_class = LogedOrUnlogedListSerializer


class LogedOrUnlogedListRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = LogedOrUnlogedList.objects.all()
    serializer_class = LogedOrUnlogedListSerializer


class LetterListCreateView(generics.ListCreateAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer


@api_view("POST")
def statics_view(request):
    for i in Statics.objects.all:
        Statics.objects.check()
        if Statics.objects.all == True:
            print("hello new student")
        else:
            print("You have to more documation")


class LetterRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
