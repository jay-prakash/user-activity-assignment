from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import User
from .serializers import UserSerializer


# Show user activity json data on homepage
@api_view(['GET'])
def user_activities(request):
    users = User.objects.all().order_by('-id')
    api_data = {
        'ok': True,
        'members': UserSerializer(users, many=True).data
    }
    return Response(api_data)
