import datetime as dt

from users.models import User


class UserInteractionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            user.last_request = dt.datetime.utcnow()
            user.save(update_fields=['last_request'])

        return response
