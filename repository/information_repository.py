import _mysql_connector
import mysql
from model.information import PatientInformation

class InformationRepository:
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="<root1234>",
            database="mehrab_PIS_app"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, patient_information):
        self.connect()
        self.cursor.execute(
            "INSERT INTO patient_db.information (visit_date_time, hospital, prescription, extra_data) VALUES (%s,%s,%s,%s)",
            [patient_information.visit_date_time, patient_information.hospital, patient_information.prescription, patient_information.extra_data]
        )
        self.connection.commit()
        self.disconnect()

    def edit(self, patient_information):
        self.connect()
        self.cursor.execute(
            "UPDATE patient_db.information SET visit_date_time=%s, hospital=%s, prescription=%s, extra_data=%s WHERE in_id=%s",
            [patient_information.visit_date_time, patient_information.hospital, patient_information.prescription, patient_information.extra_data, patient_information.id]
        )
        self.connection.commit()
        self.disconnect()

    def remove(self, patientInformation_id):
        self.connect()
        self.cursor.execute("DELETE FROM patient_db.information WHERE in_id=%s", [patientInformation_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM patient_db.information ORDER BY visit_date_time DESC")
        PatientInformation_list = self.cursor.fetchall()
        self.disconnect()
        return PatientInformation_list

    def find_by_id(self, patientInformation_id):
        self.connect()
        self.cursor.execute("SELECT * FROM patient_db.information WHERE in_id=%s", [patientInformation_id])
        PatientInformation = self.cursor.fetchone()
        self.disconnect()
        return PatientInformation

    def find_by_hospital(self, hospital_id):
        self.connect()
        self.cursor.execute("SELECT * FROM patient_db.information WHERE hospital_id=%s", [hospital_id])
        PatientInformation = self.cursor.fetchone()
        self.disconnect()
        return PatientInformation