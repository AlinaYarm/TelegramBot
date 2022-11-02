from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
# from django.utils import timezone
from core import models


class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['person_name'] = 'Masha'
        return c

class Person(ListView):
    model = models.Person


def persons(request, id):
    if request.method == 'GET':
        p = get_object_or_404(models.Person, user_id=id)
        detail = {
            'user_id': p.id,
            'username': p.name,
        }
        return JsonResponse(detail)
    #elif request.method == ''
