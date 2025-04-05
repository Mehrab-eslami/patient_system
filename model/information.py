class PatientInformation:
        def __init__(self, id=None, person=None, visit_date_time=None, hospital="", prescription="", extra_data=""):
            self.id = id
            self.person = person
            self.visit_date_time = visit_date_time
            self.hospital = hospital
            self.prescription = prescription
            self.extra_data = extra_data

        def __repr__(self):
            return f"{self.__dict__}"
