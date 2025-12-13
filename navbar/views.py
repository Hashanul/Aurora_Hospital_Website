# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import MenuItem,MenuContent, PopUp
# from .serializers import MenuItemSerializer, MenuContentSerializer, PopUpSerializer
# from accounts.permissions import AdminPermission



# class PopUpViewSet(viewsets.ModelViewSet):
#     queryset = PopUp.objects.all()
#     serializer_class = PopUpSerializer
#     permission_classes = [AdminPermission]

#     def perform_create(self, serializer):
#         user = self.request.user

#         if user.is_authenticated:
#             serializer.save(created_by=user)
#         else:
#             serializer.save(created_by=None)


# class MenuItemViewSet(viewsets.ModelViewSet):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer


# class MenuContentViewSet(viewsets.ModelViewSet):
#     queryset = MenuContent.objects.all()
#     serializer_class = MenuContentSerializer

