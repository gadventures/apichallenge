from django.views.generic import TemplateView
from rest_framework.decorators import api_view

class TripView(TemplateView):
    template_name = 'trips/index.html'
    @api_view(['GET'])
    def tripapi(request):
        serializer = TripAPISerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
