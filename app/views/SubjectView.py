from django.http import HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from app.models import SubjectModel, SkillsModel


class SubjectView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        subjects = SubjectModel.objects.all()

        return render(request, 'subjects/subjects.html', {"subjects": subjects})

    @staticmethod
    def post(request, value) -> HttpResponse:
        subject_id = int(value)
        subject = SubjectModel.objects.get(id=subject_id)
        skills = SkillsModel.objects.all().filter(subject=subject)

        return render(request, 'subjects/skills.html', {"skills": skills})
