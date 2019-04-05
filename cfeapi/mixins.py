from django.http import HttpResponse, JsonResponse


class HttpResponseMixin(object):
    # print('--> HttpResponseMixin')
    is_json = False

    def render_to_response(self, data, status=200):
        print('.. HttpResponseMixin.render_to_response')
        print('data TYPE is:', type(data))
        content_type = 'application/json' if self.is_json else 'text/html'
        print('.. content_type is:', content_type)
        return HttpResponse(data, content_type=content_type, status=status)

    # print('<-- HttpResponseMixin')


class JsonResponseMixin(object):

    def render_to_json_response(self, context, **response_kwargs):
        print('.. JsonResponseMixin.render_to_response ..')
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context
