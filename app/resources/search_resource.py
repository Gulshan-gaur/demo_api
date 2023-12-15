# app/resources/user_resource.py
from flask_restx import Namespace, Resource
from app.models import Patient

patient_ns = Namespace('patient', description='Patient operations')

@patient_ns.route('/<int:patient_id>')
class UserResource(Resource):
    def get(self, patient_id):
        # Implement logic to load patient details for a given patient_id
        # Example: patient = get_patient_details(patient_id)
        patient = Patient(id=patient_id, name=f'Patient{patient_id}', details=['PA Examine','DicomTAG'])
        
        if not patient:
            return {'message': 'Patient not found'}, 404

        return {
            'id': patient.id,
            'name': patient.name,
            'details': patient.details
        }