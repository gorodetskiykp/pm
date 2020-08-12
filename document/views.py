from django.shortcuts import render
from django.utils import timezone
from django.utils.datetime_safe import date
from .models import Document, DocumentComment
from .forms import CommentForm


def documents(request):
    document_list = Document.objects.all()
    context = {
        "document_list": document_list,
        "title": "Документы",
    }
    return render(request, "document/documents.html", context)


def documents_control(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        document = Document.objects.get(pk=request.POST['document_id'])
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.document = document
            new_comment.save()
    document_list = Document.objects.filter(control=True)
    today = timezone.localdate()
    today_weekday = date.isoweekday(today)
    week_days = [day - today_weekday for day in range(1, 8)]
    days = [today + timezone.timedelta(days=day) for day in week_days]
    days_str = [day.strftime("%d.%m.%Y") for day in days]
    documents_table_head = ["Документы"]
    documents_table_head.extend(days_str)
    documents_table_body = []
    for document in document_list:
        document_cell = [document.id, document.status, document.sed_number, document.name]
        document_row = [document_cell]
        for day in days:
            comments = document.documentcomment_set.filter(date__year=day.year,
                                                           date__month=day.month,
                                                           date__day=day.day)
            if comments:
                document_row.append(comments)
            else:
                document_row.append("-")
        documents_table_body.append(document_row)
    context = {
        "days": days,
        "document_list": document_list,
        "documents_table_head": documents_table_head,
        "documents_table_body": documents_table_body,
        "form": CommentForm(),
        "title": "Документы на контроле",
    }
    return render(request, "document/documents_control.html", context)


def document(request, pk):
    document = Document.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.document = document
            new_comment.save()
    context = {
        "title": document.sed_number,
        "document": document,
        "form": CommentForm(instance=document),
        "today": timezone.localdate(),
    }
    return render(request, "document/document.html", context)

def add(request):
    pass