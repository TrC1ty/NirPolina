from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import render
from app.models import SubjectModel, SkillsModel
import requests


class ApiView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:

        return render(request, 'api/api.html', {})

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:
        url = "https://eis.mephi.ru/eis_api/BasicEducationalPrograms/items_with_competence?login=PVIshchenko&password=gelnlQpi_4324_uZx-a&program_id=354&curriculum_id=759413f4-1e56-4395-95b4-06019579b254"
        res = requests.get(url)

        if res:
            json = res.json()

            for subject in json["Items"]:
                new_subject = SubjectModel.objects.create(
                    name=subject["Name"],
                    index=subject["Index"],
                )
                new_subject.save()

                for skill in subject["Skills"]:
                    new_skill = SkillsModel.objects.create(
                        index=skill["Id"],
                        code=skill["Code"],
                        name=skill["Name"],
                        indicatorKnow=skill["IndicatorKnow"],
                        indicatorCan=skill["IndicatorCan"],
                        indicatorOwn=skill["IndicatorOwn"],
                        subject=new_subject,
                    )
                    new_skill.save()

            return HttpResponseRedirect('get-api', {"response": res.status_code})
        else:
            return HttpResponseRedirect('get-api', {"response": res.status_code})
