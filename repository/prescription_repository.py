import mysql.connector
from model.prescription import Prescription



class PrescriptionRepository:
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="<root1234>",
            database="patient_db"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, prescription):
        self.connect()
        self.cursor.execute(
            "INSERT INTO PRESCRIPTIONS (DATE_TIME, DOCTOR, DRUG, DOSAGE, DESCRIPTION) VALUES (%s,%s,%s,%s,%s)",
            [prescription.date_time, prescription.doctor, prescription.drug, prescription.dosage,
             prescription.description]
        )
        self.connection.commit()
        self.disconnect()

    def edit(self, prescription):
        self.connect()
        self.cursor.execute(
            "UPDATE PRESCRIPTIONS SET DATE_TIME=%s, DOCTOR=%s,DRUG=%s,DOSAGE=%s,DESCRIPTION=%s WHERE PRESCRIPTION_ID=%s",
            [prescription.date_time, prescription.doctor, prescription.drug, prescription.dosage,
             prescription.description, prescription.id]

        )
        self.connection.commit()
        self.disconnect()

    def remove(self, prescription_id):
        self.connect()
        self.cursor.execute("DELETE FROM PRESCRIPTIONS WHERE PRESCRIPTION_ID=%s", [prescription_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM PRESCRIPTIONS ORDER BY DOCTOR, DRUG")
        prescription_list = list(
            map(lambda pe: Prescription(pe[0], pe[1], pe[2], str(pe[3]), pe[4], pe[5], ), self.cursor.fetchall()))
        self.disconnect()
        return prescription_list

    def find_by_id(self, prescription_id):
        self.connect()
        self.cursor.execute("SELECT * FROM PRESCRIPTIONS WHERE PRESCRIPTION_ID=%s", [prescription_id])
        prescription = self.cursor.fetchone()
        self.disconnect()
        return prescription

    def find_by_doctor_and_drug(self, doctor, drug):
        self.connect()
        self.cursor.execute("SELECT * FROM PRESCRIPTIONS WHERE DOCTOR LIKE %s AND DRUG LIKE %s",
                            [doctor + "%", drug + "%"])
        prescription_list = self.cursor.fetchall()
        self.disconnect()
        return prescription_list

    def find_by_dosage_and_description(self, dosage, description):
        self.connect()
        self.cursor.execute("SELECT * FROM PERSONS WHERE DOSAGE=%s AND DESCRIPTION=%s", [dosage, description])
        prescription = self.cursor.fetchone()
        self.disconnect()
        return prescription
