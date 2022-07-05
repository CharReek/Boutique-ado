from django.http import HttpResponse


class StripeWH_Handler:
    """ handle stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        hanfle a generic unknown unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200)
