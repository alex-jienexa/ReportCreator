from django.shortcuts import render, redirect
from .forms import TemplateForm, DocumentForm

def create_template(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')  # Перенаправление на страницу успешного создания
    else:
        form = TemplateForm()
    return render(request, 'create_template.html', {'form': form})


def create_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.created_by = request.user  # Устанавливаем текущего пользователя
            document.save()
            return redirect('/')  # Перенаправление на страницу успешного создания
    else:
        form = DocumentForm()
    return render(request, 'create_document.html', {'form': form})