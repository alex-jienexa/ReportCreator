from django.shortcuts import render, redirect
from .forms import TemplateForm, DocumentForm
from .models import Template
from django.http import JsonResponse

def get_template_fields(request, template_id):
    template = Template.objects.get(id=template_id)
    return JsonResponse({'custom': template.custom})

def create_template(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST, request.FILES)
        if form.is_valid():
            template = form.save(commit=False)
            custom_fields = zip(
                request.POST.getlist('custom_field_name[]'),
                request.POST.getlist('custom_field_type[]')
            )
            custom_data = {name: type_ for name, type_ in custom_fields if name}
            template.custom = custom_data
            template.save()
            return redirect('/')  # Перенаправление на страницу успешного создания
    else:
        form = TemplateForm()
    return render(request, 'create_template.html', {'form': form})


def create_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            additional_data = {
                key: value for key, value in request.POST.items()
                if key.startswith('additional_data[')
            }
            document.additional_data = additional_data
            document.save()
            return redirect('/')  # Перенаправление на страницу успешного создания
    else:
        form = DocumentForm()
    return render(request, 'create_document.html', {'form': form})