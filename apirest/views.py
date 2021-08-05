from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from apirest.models import logTres
from apirest.serializer import logTresSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def logTres_data_list(request):
  if request.method == 'GET':
    logTres_data = logTres.objects.all()
    logTres_data_serializer = logTresSerializer(logTres_data,
                                                many=True)
    return JsonResponse(logTres_data_serializer.data, safe=False)
  elif request.method == 'POST':
    logTres_data = JSONParser().parse(request)
    logTres_data_serializer = logTresSerializer(data=logTres_data)
    if logTres_data_serializer.is_valid():
      logTres_data_serializer.save()
      return JsonResponse(logTres_data_serializer.data, 
                          status=status.HTTP_201_CREATED) 
    return JsonResponse(logTres_data_serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST)
 

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def logTres_data_detail(request, pk):
  try: 
    logTres_data = logTres.objects.get(pk=pk) 
    if request.method == 'GET': 
      logTres_data_serializer = logTresSerializer(logTres_data) 
      return JsonResponse(logTres_data_serializer.data)
    elif request.method == 'PUT': 
      logTres_data = JSONParser().parse(request) 
      logTres_data_serializer = logTresSerializer(logTres_data, 
                                              data=logTres_data) 
      if logTres_data_serializer.is_valid(): 
        logTres_data_serializer.save() 
        return JsonResponse(logTres_data_serializer.data) 
      return JsonResponse(logTres_data_serializer.errors,
                          status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
      logTres_data.delete() 
      return JsonResponse(
          {'message': 'logTres data was deleted successfully!'}, 
               status=status.HTTP_204_NO_CONTENT)
  except logTres.DoesNotExist: 
    return JsonResponse(
             {'message': 'The logTres data does not exist'}, 
               status=status.HTTP_404_NOT_FOUND) 
