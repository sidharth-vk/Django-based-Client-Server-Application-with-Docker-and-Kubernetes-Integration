import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger('django')

@csrf_exempt
def message_view(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        logger.info(f"Message received: {message}")
        if message == 'hello':
            response = {'response': 'hi'}
        else:
            response = {'response': 'unknown message'}
        logger.info(f"Response sent: {response['response']}")
        return JsonResponse(response)
    return JsonResponse({'response': 'only POST requests are allowed'})
