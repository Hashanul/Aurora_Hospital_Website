# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from django.contrib.auth import get_user_model
# from .serializers import UserSerializer, RegisterSerializer
# from .permissions import IsAdminOrSelf

# User = get_user_model()

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated, IsAdminOrSelf]

#     def get_queryset(self):
#         # Admins see all users; others only see themselves
#         user = self.request.user
#         if user.is_staff:
#             return User.objects.all()
#         return User.objects.filter(id=user.id)


# class RegisterViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     permission_classes = [AllowAny]
#     serializer_class = RegisterSerializer
