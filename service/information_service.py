import mysql.connector
from model.information import PatientInformation
from repository.information_repository import InformationRepository

class InformationService:
    def __init__(self):
        self.repository = InformationRepository()

    def save(self, information):
        self.repository.save(information)

    def edit(self, information):
        self.repository.edit(information)

    def remove(self, information_id):
        self.repository.remove(information_id)

    def find_all(self):
        self.repository.find_all()

    def find_by_id(self, in_id):
        self.repository.find_by_id(in_id)

    def find_by_hospital(self,hospital_id):
        return self.repository.find_by_hospital(hospital_id)
