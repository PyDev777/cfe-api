print()
print('---> API/VIEWS.PY')


import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel
# from .mixins import CSRFExemptMixin
from cfeapi.mixins import HttpResponseMixin


@method_decorator(csrf_exempt, name='dispatch')
class UpdateModelDetailAPIView(HttpResponseMixin, View):
    """
    Retrieve, Update, Delete --> Object
    """
    print()
    print('--> UpdateModelDetailAPIView')

    is_json = True

    def get(self, request, id, *args, **kwargs):
        print()
        print('-> UpdateModelDetailAPIView.get')
        print('[UpdateModelDetailAPIView].get BEFORE obj = UpdateModel.objects.get(id=', id, ')')
        obj = UpdateModel.objects.get(id=id)
        print('[UpdateModelDetailAPIView].get AFTER obj = UpdateModel.objects.get(id=', id, ')')
        print()
        print('[UpdateModelDetailAPIView].get BEFORE json_data = obj.serialize()')
        json_data = obj.serialize()
        print('[UpdateModelDetailAPIView].get AFTER json_data = obj.serialize()')
        print('<- UpdateModelDetailAPIView.get')
        # return HttpResponse(json_data, content_type='application/json')
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        # return HttpResponse({}, content_type='application/json')
        json_data = {}
        return self.render_to_response(json_data)

    def put(self, request, *args, **kwargs):
        # return HttpResponse({}, content_type='application/json')
        json_data = {}
        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        # return HttpResponse({}, content_type='application/json')
        json_data = {}
        return self.render_to_response(json_data, status=403)

    print()
    print('<-- UpdateModelDetailAPIView')


# class UpdateModelChangeAPIView(View):
#
#     def put(self, request, *args, **kwargs):
#         return  # json

@method_decorator(csrf_exempt, name='dispatch')
class UpdateModelListAPIView(HttpResponseMixin, View):
    """
    List View
    Create View
    """

    print()
    print('--> UpdateModelListAPIView')

    is_json = True

    # @method_decorator(csrf_exempt)
    # def dispatch(self, *args, **kwargs):
    #     print('UpdateModelListAPIView.DISPATCH !!!')
    #     return super(UpdateModelListAPIView, self).dispatch(*args, **kwargs)

    # def render_to_response(self, data, status=200):
    #     print()
    #     print('-> UpdateModelListAPIView.render_to_response')
    #
    #     print('<- UpdateModelListAPIView.render_to_response')
    #     return HttpResponse(data, content_type='application/json', status=status)

    def get(self, request, *args, **kwargs):
        print()
        print('-> UpdateModelListAPIView.get')
        print('[UpdateModelListAPIView].get BEFORE qs = UpdateModel.objects.all()')
        qs = UpdateModel.objects.all()
        print('[UpdateModelListAPIView].get AFTER qs = UpdateModel.objects.all()')
        print()
        print('[UpdateModelListAPIView].get BEFORE json_data = obj.serialize()')
        json_data = qs.serialize()
        print('[UpdateModelListAPIView].get AFTER json_data = obj.serialize()')
        print('<- UpdateModelListAPIView.get')
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        print()
        print('-> UpdateModelListAPIView.post')
        data = json.dumps({'message': 'Unknown data'})
        print('<- UpdateModelListAPIView.post')
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        print()
        print('-> UpdateModelListAPIView.delete')
        data = json.dumps({'message': 'You can not delete an entire list'})
        # status_code = 403
        print('<- UpdateModelListAPIView.delete')
        return self.render_to_response(data, status=403)

    print()
    print('<-- UpdateModelListAPIView')


print('<--- API/VIEWS.PY')
