from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, CreateView

from .models import Colegios, Actividades
from .forms import ColegiosForm


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
        self.request.session['cole_pk'] = self.request.POST['info_pk']
        print("----------")
        print(self.request.session['cole_pk'])
        print("----------")
        return redirect('list_cole')


class CreateColegios(CreateView):
    model = Colegios
    template_name = 'create_update_colegios.html'
    success_url = reverse_lazy('list_cole')
    form_class = ColegiosForm

    def get_context_data(self, **kwargs):
        context = super(CreateColegios, self).get_context_data(**kwargs)
        sub_tipos_choices = Colegios.SUB_TIPO_CHOICES
        context['clientes'] = sub_tipos_choices[:2]
        context['no_clientes'] = sub_tipos_choices[2:]
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.sub_tipo = self.request.POST['sub_tipo']
        self.object.save()
        colegio_created_id = self.object.id
        new_actividad = Actividades(colegio_id=colegio_created_id, observaciones_visita=self.request.POST['activida'])
        new_actividad.save()
        return super(CreateColegios, self).form_valid(form)


class UpdateColegios(UpdateView):
    template_name = "update_colegios.html"
