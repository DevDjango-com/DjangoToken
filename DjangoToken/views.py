from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Aqui



class HolaView(APIView):
	permission_classes = (IsAuthenticated,)   # <-- y Aqu
	def get(self, request):
 		content = {'message': 'Hola, comunidad DevDjango!'}
 		return Response(content)