import time
from django.http import HttpResponse


class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Request to {request.path} took {elapsed_time:.2f} seconds')