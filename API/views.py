from rest_framework import viewsets, filters, status
from rest_framework.response import Response

from API.models import Users
from API.serializers import UsersSerializer


class UsersViewSet(viewsets.ModelViewSet):
    """
        This view got 2 custom methods:
        CREATE which is available at /users/add/ url. Create method allows user to create single or multiple objects
        at the same endpoint.
        LIST method which allows to view all records from app, available at /users/ url.

    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        many = isinstance(data, list)
        serializer = self.get_serializer(data=data, many=many)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                {"status": "OK"},
            )
        else:
            return Response({"status": "error",
                             "message": f"{serializer.errors}"})

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UsersSerializer(queryset, many=True)
        return Response({
            "status": "OK",
            "data": serializer.data
        })
