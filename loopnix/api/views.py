from loopnix.api.serializers import RegistrationSerializer,ChangePasswordSerializer,UpdateUserSerializer
from django.contrib.auth.models import User
from rest_framework import generics,views,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.db.models import Q
from loopnix.api.permissions import IsUserOrReadOnly
from loopnix.api.pagination import UsersPageLOP

class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.filter(is_active__in=[True])
    permission_classes = [IsUserOrReadOnly]
    serializer_class = ChangePasswordSerializer


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = User.objects.filter(is_active__in=[True])

class UserListView(generics.ListAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = UsersPageLOP
    queryset = User.objects.filter(is_active__in=[True])

class UpdateProfileView(generics.RetrieveUpdateAPIView):

    serializer_class = UpdateUserSerializer
    permission_classes = [IsUserOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return User.objects.filter(Q(is_active__in=[True]) & Q(pk=pk))


class DeleteUserView(views.APIView):
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        if user.is_active==True:
            user.is_active=False
            user.save()
            return Response("Your account has been delted",status=status.HTTP_204_NO_CONTENT)
    
        else:
            return Response("No user Found")  
