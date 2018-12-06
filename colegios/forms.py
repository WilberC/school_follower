from collections import OrderedDict

from django.forms import ModelForm

from colegios.models import Colegios


class ColegiosForm(ModelForm):
    class Meta:
        model = Colegios
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        my_empty_choice = [('', '---------')]
        self.fields['sub_tipo'].choices = my_empty_choice
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        if 'tipo' in self.data:
            try:
                tipo_id = int(self.data.get('tipo'))
                sub_tipos_choices = Colegios.SUB_TIPO_CHOICES
                if tipo_id == 1:
                    self.fields['sub_tipo'].choices = get_choices_with_empty(sub_tipos_choices[:2])
                elif tipo_id == 2:
                    self.fields['sub_tipo'].choices = get_choices_with_empty(sub_tipos_choices[2:])
                else:
                    self.fields['sub_tipo'].choices = my_empty_choice
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['sub_tipo'].choices = Colegios.SUB_TIPO_CHOICES

    def clean(self):
        cleaned_data = super(ColegiosForm, self).clean()
        get_sub_tipo = self.cleaned_data.get('sub_tipo')
        if get_sub_tipo == '' or get_sub_tipo == ' ' or get_sub_tipo is None:
            self.add_error('sub_tipo', 'Seleccione una opción valida')
        return cleaned_data


def get_choices_with_empty(array_to_modify):
    empty_element = {'': '---------'}
    array = OrderedDict(array_to_modify)
    array.update(empty_element)
    array.move_to_end('', last=False)
    new_array = list(array.items())
    return new_array
