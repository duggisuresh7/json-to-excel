from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from app.models import *
from django.shortcuts import render
from django_excel import make_response_from_query_sets
from django.http import HttpResponse


@csrf_exempt
def import_data(request):
    if request.method == 'POST':
        file = request.FILES['file']
        data = json.loads(file.read())
        for item in data:
            model_instance = jsondata.objects.create(**item)
        return JsonResponse({'success': True})
    return render(request,'jsonhtml.html')



def export_to_excel(request):
    data = jsondata.objects.all()
    return render(request, 'export.html', {'data': data})

import io

from openpyxl import Workbook

def export_to_excel1(request):
    # Get data from the database
    data = jsondata.objects.all()

    # Create a new workbook and add a worksheet
    wb = Workbook()
    ws = wb.active

    # Add data to the worksheet
    for row in data:
        ws.append([row.end_year, row.intensity, row.sector,row.topic, row.insight, row.url,row.region, row.start_year, row.impact,row.country, row.relevance, row.pestle,row.source,row.title,row.likelihood])

    # Create a response object with the workbook content
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="my_data.xlsx"'

    # Write the workbook content to the response
    wb.save(response)

    return response
