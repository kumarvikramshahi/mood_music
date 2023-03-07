from django.http import JsonResponse

def file_upload(request):
    file = request.FILES.get('file')
    return JsonResponse({'name': file.name})
