from django.db import models


class SubjectModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name = models.TextField()
    index = models.TextField()

    class Meta:
        db_table = "Subjects"


class SkillsModel(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    index = models.IntegerField()
    code = models.TextField()
    name = models.TextField()
    indicatorKnow = models.TextField()
    indicatorCan = models.TextField()
    indicatorOwn = models.TextField()
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "Skills"
