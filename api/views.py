from .models import Application
from .serializers import ApplicationSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]


@api_view()
def test_view(request):
    api_key = request.GET.get('api_key')
    application = get_object_or_404(Application, key=api_key)
    serializer = ApplicationSerializer(application)
    return JsonResponse(serializer.data)

