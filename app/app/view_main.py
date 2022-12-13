from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app.verify_password_form import VerifyPasswordForm
from app.validate_password_svc import get_no_matches_in_password


@csrf_exempt
@require_POST
def verify_password(request):
    form = VerifyPasswordForm.parse_raw(request.body)

    no_matches = get_no_matches_in_password(password=form.password, rules=form.rules)
    verify = len(no_matches) == 0

    response = {"verify": verify, "noMatch": no_matches}
    return JsonResponse(response)
