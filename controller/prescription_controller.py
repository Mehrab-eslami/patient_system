from model.prescription import Prescription
from service.prescription_service import PrescriptionService
from validation.validator import prescription_validator


# decorator
def error_handler(my_function):
    def inner(*args, **kwargs):
        try:
            result = my_function(*args, **kwargs)
            return True, result
        except Exception as e:
            return False, e

    return inner


class PrescriptionController:
    def __init__(self):
        self.service = PrescriptionService()

    @error_handler
    def save(self, date_time, doctor, drug, dosage, description):
        prescription = Prescription(None, doctor, date_time, drug, dosage, description)
        errors = prescription_validator(prescription)
        if errors:
            raise Exception(errors)
        self.service.save(prescription)
        return "Prescription Saved"

    @error_handler
    def edit(self, date_time, doctor, drug, dosage, description):
        prescription = Prescription(None, doctor, date_time, drug, dosage, description)
        errors = prescription_validator(prescription)
        if errors:
            raise Exception(errors)
        self.service.save(prescription)
        return "Prescription Edited"

    @error_handler
    def remove(self, prescription_id):
        self.service.remove(prescription_id)
        return "Prescription Removed"

    @error_handler
    def find_all(self):
        return self.service.find_all()
