from leads.models import Lead
from rest_framework import viewsets,permissions
from .serializers import LeadSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializers_class = LeadSerializer

#@method_decorator(csrf_exempt, name='dispatch') ##not going to work unless student id is a foreign key in attendance
#class AttendanceList(generics.ListCreateAPIView):
#    serializer_class = serializers.EnrollmentSerializer
#    def get_object(self, course_section_id):
#        try:
#            attendance=models.Attendance.objects.filter(enrollment__course_section_id=course_section_id)
#            return attendance
#        except models.Attendance.DoesNotExist:
#            raise Http404

#    def get(self, request, course_section_id):
#        try:
#            attendance = self.get_object(course_section_id)
#            print(attendance)
#            serializer = serializers.EnrollmentSerializer(attendance, many=True)
#            print(serializer)
#            return Response(serializer.data)
#        except models.Attendance.DoesNotExist:
#            raise Http404
