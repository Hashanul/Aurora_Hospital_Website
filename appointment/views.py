
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.exceptions import ValidationError


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

