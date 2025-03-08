from datetime import datetime
import _mysql_connector
from model.person import Person
from model.prescription import Prescription
from model.information import PatientInformation

class PrescriptionRepository:
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root1234",
            database="mehrab_PIS_app"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
            self.cursor.close()
            self.connection.close()



