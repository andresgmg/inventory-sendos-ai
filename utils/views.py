from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Base de todas las views para homologar los mensajes de errores
class BaseView(APIView):
    def error_response(self, message, status_code=status.HTTP_400_BAD_REQUEST):
        """
        Helper method to generate error responses consistently.
        :param message: Error message or list of error messages.
        :param status_code: HTTP status code for the response. Default is 400 (Bad Request).
        :return: Response object with error details.
        """
        errors = message if isinstance(message, dict) else {"detail": message}
        return Response({"errors": errors}, status=status_code)