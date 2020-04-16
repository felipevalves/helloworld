from django.http.response import HttpResponseForbidden

class FiltraIPMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        ips_autorizados = ['127.0.0.1', '172.2.1.60']

        ip_usuario = request.META.get('REMOTE_ADDR')

        if ip_usuario not in ips_autorizados:
            return HttpResponseForbidden('IP não autorizado')

        return None
