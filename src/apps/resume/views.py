from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class ResumeView(TemplateView):
    template_name = "resume/resume.html"