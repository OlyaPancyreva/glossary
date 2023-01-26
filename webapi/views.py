from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import generics

from .models import Terms
from .serializers import TermsSerializer


# show template of term
def terms(request):
    all_terms = Terms.objects.all().values()
    template = loader.get_template('glossary/terms.html')
    context = {
        'all_terms': all_terms
    }
    return HttpResponse(template.render(context, request))


def mindmap(request):
    template = loader.get_template('glossary/mindmap.html')
    context = {}
    return HttpResponse(template.render(context, request))


# create new term
class CreateTerm(generics.CreateAPIView):
    serializer_class = TermsSerializer


# get all terms
class GetTerm(generics.ListAPIView):
    serializer_class = TermsSerializer
    queryset = Terms.objects.all()
