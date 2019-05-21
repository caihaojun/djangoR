from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length =100)
    email = models.EmailField(max_length=100,unique=True)
    message = models.CharField(max_length =500,blank=True)
    created_at= models.DateTimeField(auto_now_add=True)
#creating models only file,need migration to run,put table in db;

#class Attendance(models.Model):
#    REQUIRED_FIELDS = ('Enrollment')
#    id = models.AutoField(primary_key=True)
#    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
#    isPresent = models.BooleanField()
#    dayAttended = models.DateField(default=datetime.now)
#    class Meta:
#        db_table = "attendance"
