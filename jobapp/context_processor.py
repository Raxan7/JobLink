from django.urls import reverse


def first_candidate_id(request):
    try:
        if request.user.is_authenticated and request.user.role == 'employee':
            candidate_id = request.user.candidate.first().id
        return {'candidate_id': candidate_id}
    except Exception as e:
        candidate_id = 0
        return {'candidate_id': candidate_id}

