from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import (ListAPIView, CreateAPIView, 
RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, 
RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView)


#------------------------List objects API ------------------------------

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# ----------------------Create objects API-------------------------------

# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# ----------------------Get/Read objects API-----------------------------

# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# ----------------------Update objects API----------------------------

# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# ---------------------Delete objects API-----------------------------

# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# --------------------List and Create objects API------------------------

class LCStudentAPI(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# --------------------Retrieve and Update objects API-------------------

# class RUStudentAPI(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# -------------------Retrieve and Delete objects API--------------------
# class RDStudentAPI(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# -------------------Retrieve, Update, and Delete objects API--------------------------

class RUDStudentAPI(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer