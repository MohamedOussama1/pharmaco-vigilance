from django.core import serializers
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from pharmaco.utils import *
from pharmaco.models import *

from pharmabackend.settings import DB_NAME


# @csrf_protect
@csrf_exempt
def patients(request):
    with connect_to_db(DB_NAME):
        if request.method == 'GET':
            patients = Patient.objects.all() # Get all patients as a dictionary
            return HttpResponse(patients, content_type='application/json')

        elif request.method == 'POST':
            # Extract data from request body
            data = request.POST  # Assuming form data is being sent
            # Create and save patient
            patient = Patient.objects.create(
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                email=data.get("email"),
                age=data.get("age"),
                national_identifier_code=data.get("national_identifier_code"),
                phone_number=data.get("phone_number")
            )
            return HttpResponse(patient, status=201)

        elif request.method == 'PUT':
            # Extract data from request body
            data = request.POST  # Assuming form data is being sent
            patient_id = data.get("id")
            patient = Patient.objects.get(id=patient_id)
            if not patient:
                return HttpResponse({"error": "Patient not found"}, status=404)

            # Update patient fields if provided
            for field in ['first_name', 'last_name', 'email', 'age', 'national_identifier_code', 'phone_number']:
                value = data.get(field)
                if value:
                    setattr(patient, field, value)

            patient.save()
            return HttpResponse({"message": "Patient updated successfully", "patient": patient.to_dict()})

        elif request.method == 'DELETE':
            # Extract patient_id from request body
            patient_id = request.POST.get("id")
            patient = Patient.objects.get(id=patient_id)
            if patient:
                patient.delete()
                return HttpResponse("Patient deleted successfully", status=200)
        return HttpResponse("Patient not found", status=404)
