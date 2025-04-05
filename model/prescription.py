class Prescription:
    def __init__(self, id=None, date_time=None, doctor="", drug="", dosage="", description=""):
        self.id = id
        self.date_time = date_time
        self.doctor = doctor
        self.drug = drug
        self.dosage = dosage
        self.description = description

    def __repr__(self):
        return f"{self.__dict__}"