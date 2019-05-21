from rest_framework import serializers
from leads.models import Lead

#lead serializers
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model =Lead
        fields = '__all__'

#class AttendanceSerializer(serializers.ModelSerializer):
#    enrollment = EnrollmentSerializer(many=False)
#    class Meta:
#        model = Attendance
#        fields = ('__all__')
