# Django
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Third Party
import twilio.twiml
 
@csrf_exempt
def receive_message(request):

    response = twilio.twiml.Response()
    response.message("""
        Open the door?  Reply with yes or no.
        """)

    return HttpResponse(response, content_type='text/xml')