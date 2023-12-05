from django.shortcuts import render
from swaggerapp import models, serializers
# from swaggerapp.models import patient_detail
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class PatientCreateView(GenericAPIView):
    serializer_class = serializers.patient_serializer

    def post(self, request, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Exception as e:
            print("Error:", e)
            return Response({"error": str(e)})


class PatientGetView(GenericAPIView):
    serializer_class = serializers.patient_serializer
    queryset = models.patient_detail
    def get(self, request, **kwargs):
        try:
            query = models.patient_detail.objects.all()
            serializer_class = serializers.patient_serializer(query, many=True)
            return Response(serializer_class.data)
        except Exception as e:
            print("Error:", e)
            return Response({"error": str(e)})


class PatientGetByID(GenericAPIView):
    serializer_class = serializers.patient_serializer

    def get(self, request, id, **kwargs):
        model = models.patient_detail.objects.get(id=id)
        serializer_class = serializers.patient_serializer(model)
        return Response(serializer_class.data)


class PatientPut(GenericAPIView):
    serializer_class = serializers.patient_serializer

    def put(self, request, id):
        try:
            query_set = models.patient_detail.objects.get(id=id)
            serializer_class = serializers.patient_serializer(instance=query_set, data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data)
        except Exception as e:
            print('invalid')
            return Response(e)


class DeleteID(GenericAPIView):
    #serializer_class = serializers.patient_serializer

    def delete(self, request,id):
        try:
            # id=request.data('id')
            patient_delete = models.patient_detail.objects.get(id=id).delete()
            return Response("deleted")
        except Exception as e:
            print("invalid", e)
            return Response(e)


