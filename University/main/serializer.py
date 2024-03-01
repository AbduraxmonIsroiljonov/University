from main.models import *
from rest_framework import serializers


class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = "__all__"


class FiltrSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = "__all__"


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentList
        fields = "__all__"


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fiels = "__all__"


class PopularUniversityForm(serializers.ModelSerializer):
    class Meta:
        model = PopularUniversity
        fields = "__all__"


class HowWeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowWeWork
        fields = ["id", "photo", "steps"]


class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = "__all__"


class StudentsCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsComments
        fields = ["id", "student", "direction", "comment", "place"]


class StaticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statics
        flieds = "__all__"


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        field = "__all__"


class LogedOrUnlogedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogedOrUnlogedList
        fields = [
            "id",
            "place",
            "university",
            "time",
            "information",
            "loged",
            "unloged",
        ]

class LogedStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogedStudents
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields="__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class GetInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetInformation
        fields = ["id", "phone_number"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ["id", "user", "registration_date"]


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = ["id", "text", "profile", "phone_number", "email"]
