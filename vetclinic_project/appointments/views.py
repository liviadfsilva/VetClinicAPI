from rest_framework import viewsets
from .models import Appointments
from .serializer import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=["get"], url_path="by-date")
    def by_date(self, request):
        date_str = request.query_params.get("date")
        if not date_str:
            return Response({"error": "Date parameter is required"}, status=400)

        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD"}, status=400)

        appointments = Appointments.objects.filter(date=date_obj)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=["get"], url_path="by-type")
    def by_type(self, request):
        type_param = request.query_params.get("type")
        
        if not type_param:
            return Response({"error": "Type parameter is required"}, status=400)
        
        appointments = Appointments.objects.filter(type=type_param)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)