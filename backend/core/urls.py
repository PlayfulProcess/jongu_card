from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ErrorLogViewSet, UserViewSet, CheckViewSet
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 


app_name = "core"

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"error-logs", ErrorLogViewSet)
router.register(r"check", CheckViewSet, basename="check")

@csrf_exempt 
def test_login_view(request):
    return JsonResponse({
        "message": "🎉 Welcome to the login endpoint! You've successfully hit the route.",
        "method": request.method,
        "headers": dict(request.headers),
        "body": request.body.decode("utf-8") if request.body else None
    })

@csrf_exempt 
def test_signup_view(request):
    if request.method == 'POST':
        return JsonResponse({
            "message": "Welcome to the signup endpoint!",
            "method": request.method,
            "headers": dict(request.headers),
            "body": request.body.decode("utf-8") if request.body else None
        })
    return JsonResponse({"message": "Please use POST method"}, status=405)

urlpatterns = [
    path("login/", test_login_view, name="login"),
    path("signup/", test_signup_view, name="signup"),
    path("", include(router.urls)),
]