import re
from datetime import datetime, date
from model.person import Person
from model.information import PatientInformation
from model.prescription import Prescription


def person_validator(person):
    errors = []
    if not type(person.name) == str or not re.match(r"^[a-zA-Z\s]{3,30}$", person.name):
        errors.append({"field": "name", "message": "invalid name"})

    if not type(person.family) == str or not re.match(r"^[a-zA-Z\s]{3,30}$", person.family):
        errors.append({"field": "family", "message": "invalid family"})

    if not isinstance(person.birth_date, date) == date or type(person.birth_date) == str:
        try:
            person.birth_date = datetime.strptime(person.birth_date, "%Y-%m-%d").date()
        except ValueError:
            errors.append({"field": "birth_date", "message": "invalid birth date"})
    else:
        errors.append({"field": "birth_date", "message": "invalid birth_date"})
    return errors


def information_validator(information):
    errors = []
    if not type(information) == str or not re.match(r"^[a-zA-Z\s]{3,30}$", information):
        errors.append({"field": "information", "message": "invalid information"})








def prescription_validator(prescription):
    errors = []
    if not type(prescription) == Prescription:
        errors.append({"field": "prescription", "message": "invalid prescription"})
