from django.http import HttpResponse


class HttpResponseMixin(object):
    is_json = False

    def render_to_response(self, data, status=200):
        content_type = 'application/json' if self.is_json else 'text/html'
        return HttpResponse(data, content_type=content_type, status=status)
