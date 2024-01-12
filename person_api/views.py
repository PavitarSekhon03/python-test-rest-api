# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from person_api.pagination import CustomPageNumberPagination

# Create your views here.
# crud

class PersonListView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class=PersonSerializer
    pagination_class=CustomPageNumberPagination
    permission_classes=[IsAuthenticated, IsAdminUser]


class PersonDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class=PersonSerializer
    permission_classes=[IsAuthenticated, IsAdminUser]

    

class PersonFilterListView(ListAPIView):
    serializer_class=PersonSerializer
    permission_classes=[IsAuthenticated]


    def get_queryset(self):
        queryset = Person.objects.all()

        # check if they are not admin
        name = self.request.query_params.get('name', None)
        if name is not None and not self.request.user.is_staff:
            return None
        # check if they are admin
        if name is not None and self.request.user.is_staff:
            queryset = queryset.filter(name__icontains=name)

        
        #filter by age
        age = self.request.query_params.get('age', None)
        if age is not None:
            queryset = queryset.filter(age=age)

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if queryset is None:
            # Guest user is not allowed to filter by name
            return Response({"detail": "Guest users are not allowed to filter by name."}, status=403)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)