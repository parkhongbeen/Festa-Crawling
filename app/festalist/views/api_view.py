from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import get_object_or_404
from festalist.models import FestaList
from festalist.serializers import FestaListSerializer


@csrf_exempt
def festalist_list(request):
    if request.method == 'GET':
        festalists = FestaList.objects.all()
        serializer = FestaListSerializer(festalists, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def festalist_detail(request, pk):
    festalist = get_object_or_404(FestaList, pk=pk)

    if request.method == 'GET':
        serializer = FestaListSerializer(festalist)
        return JsonResponse(serializer.data)
