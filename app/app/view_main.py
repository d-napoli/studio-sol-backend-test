from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app.verify_password_form import VerifyPasswordForm
from app.validate_password_svc import validate_password


@csrf_exempt
@require_POST
def verify_password(request):
    form = VerifyPasswordForm.parse_raw(request.body)

    password = form.password
    rules = form.rules

    for rule in form.rules:
        print(f"Rule: {rule.rule.value} - Value: {rule.value}")

    validate_password(password=password)

    response = {"verify": False, "noMatch": ["minDigit"]}
    return JsonResponse(response)
