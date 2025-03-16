from django import forms
from .models import Document, Template
from companies.models import Executor, Contractor
from users.models import CustomUser

class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ['name', 'type', 'file', 'variables']
        widgets = {
            'variables': forms.Textarea(attrs={'placeholder': 'Введите переменные в формате JSON списка, например: ["поле1", "поле2"]'}),
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['template', 'id',  'contrator', 'executor', 'created_by', 'showDate', 'custom']
        widgets = {
            'showDate': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['contrator'].queryset = Contractor.objects.all()
        self.fields['executor'].queryset = Executor.objects.all()
        self.fields['created_by'].queryset = CustomUser.objects.all()

        # Динамически добавляем поля для переменных шаблона
        if 'template' in self.data:
            try:
                template_id = int(self.data.get('template'))
                template = Template.objects.get(id=template_id)
                for variable in template.variables:
                    self.fields[variable] = forms.CharField(label=variable)
            except (ValueError, Template.DoesNotExist):
                pass