import mysql.connector
from model.prescription import Prescription
from repository.prescription_repository import PrescriptionRepository

class PrescriptionService:
    def __init__(self):
        self.repo = PrescriptionRepository()

    def save(self, prescription):
        self.repo.save(prescription)

    def edit(self, prescription):
        self.repo.edit(prescription)

    def remove(self, prescription_id):
        self.repo.remove(prescription_id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self, prescription_id):
        return self.repo.find_by_id(prescription_id)

    def find_by_doctor_and_drug(self, doctor, drug):
        return self.repo.find_by_doctor_and_drug(doctor, drug)

    def find_by_dosage_and_password(self, dosage, description):
        return self.repo.find_by_dosage_and_description(dosage, description)
