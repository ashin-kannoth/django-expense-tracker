from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth.models import User
from .models import Expense, Category
from .serializers import RegisterSerializer, UserSerializer, ExpenseSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Expense Tracker API!")

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        return Response(UserSerializer(user).data)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({'detail': 'User deleted.'}, status=status.HTTP_204_NO_CONTENT)

class ExpenseSummaryView(APIView):
    def get(self, request):
        expenses = Expense.objects.values('category__name').annotate(total=Sum('amount'))
        result = {item['category__name']: float(item['total']) for item in expenses}
        return Response(result)