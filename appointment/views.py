
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Appointment, AppointmentBanner
from .serializers import AppointmentSerializer, AppointmentBannerSerializer
from rest_framework.exceptions import ValidationError
from accounts.permissions import AdminPermission



class AppointmentBannerViewSet(viewsets.ModelViewSet):
    queryset = AppointmentBanner.objects.all()
    serializer_class = AppointmentBannerSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    # -------------------------
    # Override create()
    # -------------------------
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            appointment = serializer.save()

            return Response({
                "Output": "success",
                "Msg": "Appointment created successfully",
                "Returnvalue": serializer.data
            })

        except ValidationError as e:
            # extract first message
            msg = list(e.detail.values())[0]
            return Response({
                "Output": "failed",
                "Msg": msg,
                "Returnvalue": {}
            }, status=status.HTTP_400_BAD_REQUEST)

    # -------------------------
    # Override update()
    # -------------------------
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        try:
            serializer.is_valid(raise_exception=True)
            appointment = serializer.save()

            return Response({
                "Output": "success",
                "Msg": "Appointment updated successfully",
                "Returnvalue": serializer.data
            })

        except ValidationError as e:
            msg = list(e.detail.values())[0]
            return Response({
                "Output": "failed",
                "Msg": msg,
                "Returnvalue": {}
            }, status=status.HTTP_400_BAD_REQUEST)

