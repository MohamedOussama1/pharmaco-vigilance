from mongoengine import *


class Medicine(DynamicDocument):
    common_name = StringField(max_length=200, required=True)
    scientific_name = StringField(max_length=200)
    category = StringField(max_length=200)


class User(DynamicDocument):
    first_name = StringField(max_length=200)
    last_name = StringField(max_length=200)
    age = IntField()
    # gender = EnumField(enum=["Male", "Female"])
    national_identifier_code = StringField(max_length=10)
    phone_number = StringField(max_length=20)
    email = StringField(max_length=200)

    meta = {
        "allow_inheritance": True
    }

    def __str__(self):
        return self.to_json()


class Doctor(User):
    speciality = StringField(max_length=200)


class Patient(User):
    doctors = ListField(ReferenceField(Doctor))
    state = StringField()


class PrescriptionDetail(EmbeddedDocument):
    medicine = ReferenceField(Medicine, required=True)
    dosage = StringField()


class Prescription(DynamicDocument):
    doctor = ReferenceField(Doctor)
    patient = ReferenceField(Patient)
    date_prescription = DateTimeField()
    description = StringField(max_length=1000)
    prescription_details = ListField(PrescriptionDetail)


class Rendezvous(DynamicDocument):
    doctor = ReferenceField(Doctor)
    patient = ReferenceField(Patient)
    rendezvous_date = DateTimeField()
    description = StringField(max_length=1000)


class Urgent_Rendezvous(DynamicDocument):
    doctor = ReferenceField(Doctor)
    patient = ReferenceField(Patient)
    rendezvous_date = DateTimeField()
    description = StringField(max_length=1000)


class Alert(DynamicDocument):
    patient = ReferenceField(Patient)
    description = StringField(max_length=1000)


class Question(DynamicDocument):
    title = StringField()
    patient = ReferenceField(Patient)
    doctor = ReferenceField(Doctor)
    date = DateTimeField()

class Answer(DynamicDocument):
    question = ReferenceField(Question)
    answer = StringField()

#class Consultant(DynamicDocument):
#    patient = ReferenceField(Patient)

