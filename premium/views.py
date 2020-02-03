from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse


@api_view(['POST'])
def premium(request):
    if request.method == 'POST':
        data = request.data
        if isinstance(data['RATE'], str) or isinstance(data['SA'], str):
            return HttpResponse("{} & {} should be integer value".format(data['RATE'],
                                            data['SA']), status=status.HTTP_406_NOT_ACCEPTABLE)
        else :
            result = (data['RATE'] * data['SA'])/1000
            return Response({"premium": result}, status=status.HTTP_200_OK)