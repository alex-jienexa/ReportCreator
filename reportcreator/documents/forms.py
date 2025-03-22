from django import forms
from .models import Document, Template
from companies.models import Executor, Contractor
from django.db.utils import OperationalError

class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ['name', 'type', 'file', 'related_company']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['template', 'id', 'contrator', 'executor', 'showDate']
        widgets = {
            'showDate': forms.DateInput(attrs={'type': 'date'}),
        }

    try:
        id = forms.IntegerField(required=True, initial=Document.objects.all().last().id + 1)
    except OperationalError:
        pass

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['contrator'].queryset = Contractor.objects.all()
        self.fields['executor'].queryset = Executor.objects.all()

        # Динамически добавляем поля для переменных шаблона
        if 'template' in self.data:
            try:
                template_id = int(self.data.get('template'))
                template = Template.objects.get(id=template_id)
                for variable in template.get_deferred_fields():
                    self.fields[variable] = forms.CharField(label=variable)
            except (ValueError, Template.DoesNotExist):
                pass