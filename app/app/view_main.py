from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app.verify_password_form import VerifyPasswordForm

@csrf_exempt
@require_POST
def verify_password(request):
    form = VerifyPasswordForm.parse_raw(request.body)

    for rule in form.rules:
        print(f"Rule: {rule.rule.value} - Value: {rule.value}")

    response = {
        "verify": False,
        "noMatch": ["minDigit"]
    }
    return JsonResponse(response)
