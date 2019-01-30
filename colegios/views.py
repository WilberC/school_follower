from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, UpdateView, CreateView, DetailView

from .models import Colegios, Actividades
from .forms import ColegiosForm


# Create your views here.
@method_decorator(login_required, name='dispatch')
class ListaTipos(TemplateView):
    template_name = "get_tipo.html"

    def get_context_data(self, **kwargs):
        context = super(ListaTipos, self).get_context_data(**kwargs)
        context['get_tipo'] = Colegios.TIPO_CHOICES
        return context

    def post(self, request):
        tipo = self.request.POST['tipo']
        self.request.session['tipo'] = tipo
        if tipo == '3':
            return redirect('list_cole')
        return redirect('list_sub_tipo')


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class ListaColegios(TemplateView):
    template_name = "lista_colegios.html"

    def get_context_data(self, **kwargs):
        context = super(ListaColegios, self).get_context_data(**kwargs)
        tipo = self.request.session['tipo']
        if tipo == "3":
            context['colegios'] = Colegios.objects.all()
            return context
        else:
            sub_tipo = self.request.session['sub_tipo']
            context['colegios'] = Colegios.objects.filter(sub_tipo=sub_tipo)
            return context

    def post(self, request):
        self.request.session['cole_pk'] = self.request.POST['info_pk']
        print("----------")
        print(self.request.session['cole_pk'])
        print("----------")
        return redirect('list_cole')


@method_decorator(login_required, name='dispatch')
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
        self.object.user = self.request.user
        self.object.sub_tipo = self.request.POST['sub_tipo']
        self.object.save()
        colegio_created_id = self.object.id
        new_actividad = Actividades(colegio_id=colegio_created_id, observaciones_visita=self.request.POST['activida'])
        new_actividad.save()
        return super(CreateColegios, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class DetallesColegios(DetailView):
    model = Colegios
    template_name = "colegios_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetallesColegios, self).get_context_data(**kwargs)
        my_pk = self.kwargs['pk']
        context['actividades'] = Actividades.objects.filter(colegio_id=my_pk)
        return context


@method_decorator(login_required, name='dispatch')
class CreateActividad(CreateView):
    model = Actividades
    template_name = 'create_actividad.html'
    success_url = reverse_lazy('list_cole')
    fields = ['observaciones_visita']

    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.colegio_id = self.kwargs['pk']
        self.object.save()
        return super(CreateActividad, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ColegioUpdate(UpdateView):
    model = Colegios
    success_url = reverse_lazy('list_cole')
    form_class = ColegiosForm
    template_name = 'update_colegios.html'
