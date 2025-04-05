
from model.person import Person
from model.information import PatientInformation
from model.prescription import Prescription
import re
from datetime import datetime, date

def person_validator(person):
    errors = []

    # Validate name
    if not isinstance(person.name, str) or not person.name.strip() or not re.match(r"^[a-zA-Z\s]{2,50}$", person.name):
        errors.append({"field": "name", "message": "invalid name"})

    # Validate family
    if not isinstance(person.family, str) or not person.family.strip() or not re.match(r"^[a-zA-Z\s]{2,50}$", person.family):
        errors.append({"field": "family", "message": "invalid family"})

    # Validate birth_date
    if isinstance(person.birth_date, str):
        try:
            person.birth_date = datetime.strptime(person.birth_date, "%m/%d/%Y").date()
        except ValueError:
            errors.append({"field": "birth_date", "message": "invalid birth date"})
    elif not isinstance(person.birth_date, date):
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
