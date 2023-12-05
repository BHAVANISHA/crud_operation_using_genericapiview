from django.contrib import admin
from swaggerapp.models import patient_detail
class patient(admin.ModelAdmin):
    table=['name','age','gender','disease']
    admin.site.register(patient_detail)
# Register your models here.
