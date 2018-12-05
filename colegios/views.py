from django.shortcuts import redirect
from django.views.generic import TemplateView

from .models import Colegios


# Create your views here.
class ListaTipos(TemplateView):
    template_name = "get_tipo.html"

    def get_context_data(self, **kwargs):
        context = super(ListaTipos, self).get_context_data(**kwargs)
        context['get_tipo'] = Colegios.TIPO_CHOICES
        return context

    def post(self, request):
        self.request.session['tipo'] = self.request.POST['tipo']
        return redirect('list_sub_tipo')


class ListaSubTipos(TemplateView):
    template_name = "get_sub_tipo.html"

    def get_context_data(self, **kwargs):
        context = super(ListaSubTipos, self).get_context_data(**kwargs)
        tipo = self.request.session['tipo']
        sub_tipos_choices = Colegios.SUB_TIPO_CHOICES
        if tipo == "1":
            sub_tipo = sub_tipos_choices[:2]
        else:
            sub_tipo = sub_tipos_choices[2:]
        context['get_sub_tipo'] = sub_tipo
        return context

    def post(self, request):
        self.request.session['sub_tipo'] = self.request.POST['sub_tipo']
        return redirect('list_cole')


class ListaColegios(TemplateView):
    template_name = "lista_colegios.html"

    def get_context_data(self, **kwargs):
        context = super(ListaColegios, self).get_context_data(**kwargs)
        sub_tipo = self.request.session['sub_tipo']
        context['colegios'] = Colegios.objects.filter(sub_tipo=sub_tipo)
        return context

    def post(self, request):
        self.request.session['sub_tipo'] = self.request.POST['sub_tipo']
        return redirect('list_cole')
