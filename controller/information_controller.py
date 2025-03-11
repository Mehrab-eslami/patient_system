from model.information import PatientInformation
from service.information_service import InformationService
from validation.validator import information_validator


# decorator
def error_handler(my_function):
    def inner(*args, **kwargs):
        try:
            result = my_function(*args, **kwargs)
            return True, result
        except Exception as e:
            return False, e

    return inner

class InformationController:
    def __init__(self):
        self.service = InformationService()

    @error_handler
    def save(self, person, visit_date_time, hospital, prescription, extra_data):
        information = PatientInformation(None, person, visit_date_time, hospital, prescription, extra_data)
        errors = information_validator(information)
        if errors:
            raise Exception(errors)
        self.service.save(information)
        return "information Saved"

    @error_handler
    def edit(self, person, visit_date_time, hospital, prescription, extra_data):
        information = PatientInformation (None, person, visit_date_time, hospital, prescription, extra_data)
        errors = information_validator(information)
        if errors:
            raise Exception(errors)
        self.service.edit(information)
        return "information Edited"

    @error_handler
    def remove(self,information_id):
        self.service.remove(information_id)
        return "information Removed"

    @error_handler
    def find_all(self):
        return self.service.find_all()
