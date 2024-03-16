from mongoengine import *


class Choice(EmbeddedDocument):
    choice_text = StringField(max_length=200)


class Question(Document):
    question_text = StringField(max_length=200)
    pub_date = DateTimeField("date published")
    choices = ListField(EmbeddedDocumentField(Choice))

    def __str__(self):
        return self.to_json()





# class Medicine(models.Model):
#     medicine_id = models.IntegerField(primary_key=True)
#     common_name = models.CharField(max_length=200, required=True)
#     scientific_name = models.CharField(max_length=200)
#     available = models.BooleanField(default=True)
#     category = models.CharField(max_length=200)
