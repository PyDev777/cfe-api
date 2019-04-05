print()
print('---> API/VIEWS.PY')


import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View
# from django.http import HttpResponse
from updates.models import Update as UpdateModel
from updates.forms import UpdateModelForm
# from .mixins import CSRFExemptMixin
from cfeapi.mixins import HttpResponseMixin
from .utils import is_json


@method_decorator(csrf_exempt, name='dispatch')
class UpdateModelDetailAPIView(HttpResponseMixin, View):
    """
    Retrieve, Update, Delete --> Object
    """
    print()
    print('--> UpdateModelDetailAPIView')

    is_json = True

    def get_object(self, id=None):

        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj = None
        # return obj

        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

        # qs = UpdateModel.objects.filter(id=id).first()
        # return qs

        # obj = UpdateModel.objects.get(id=id)
        # return obj

    def get(self, request, id, *args, **kwargs):
        print()
        print('-> UpdateModelDetailAPIView.get')
        print('[UpdateModelDetailAPIView].get BEFORE obj = UpdateModel.objects.get(id=', id, ')')

        obj = self.get_object(id=id)

        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)

        print('[UpdateModelDetailAPIView].get AFTER obj = UpdateModel.objects.get(id=', id, ')')
        print()
        print('[UpdateModelDetailAPIView].get BEFORE json_data = obj.serialize()')

        json_dumps_data = obj.serialize()
        print('json_dumps_data TYPE is:', type(json_dumps_data))

        print('[UpdateModelDetailAPIView].get AFTER json_data = obj.serialize()')
        print('<- UpdateModelDetailAPIView.get')

        return self.render_to_response(json_dumps_data)

    def post(self, request, *args, **kwargs):
        print('request.POST:', request.POST)
        json_data = json.dumps({"message": "Method not Allowed, please create /api/updates/ Endpoint"})
        return self.render_to_response(json_data, status=403)

    def put(self, request, id, *args, **kwargs):
        print()
        print('-> UpdateModelDetailAPIView.put')

        request_body = request.body.decode()

        valid_json = is_json(request_body)
        # print('[UpdateModelDetailAPIView].put -> valid_json:', valid_json)
        if not valid_json:
            error_data = json.dumps({"message": "Invalid data sent, please send using JSON!"})
            return self.render_to_response(error_data, status=400)

        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)

        data = json.loads(obj.serialize())
        print('[UpdateModelDetailAPIView].put -> data:', data)
        passed_data = json.loads(request_body)
        print('[UpdateModelDetailAPIView].put -> passed_data:', passed_data)

        for (key, value) in passed_data.items():
            data[key] = value

        form = UpdateModelForm(data, instance=obj)
        # print('[UpdateModelDetailAPIView].put: form =', form)

        if form.is_valid():
            print()
            print('>[UpdateModelDetailAPIView].put: form.is_valid()!')

            obj = form.save(commit=True)
            print('[UpdateModelDetailAPIView].put -> obj:', obj)
            obj_data = json.dumps(data)
            # obj_data = obj.serialize()
            print('[UpdateModelDetailAPIView].put -> obj_data:', obj_data)

            print('<[UpdateModelDetailAPIView].put.form.is_valid()')
            print('<- UpdateModelDetailAPIView].put')
            return self.render_to_response(obj_data, status=201)

        if form.errors:
            data = json.dumps(form.errors)
            print('[UpdateModelDetailAPIView].put -> form.errors:', data)

            print('<- UpdateModelDetailAPIView.put')
            return self.render_to_response(data, status=400)

        json_dumps_data = json.dumps({"Message": "Something on put"})

        print('<- UpdateModelDetailAPIView.put')
        return self.render_to_response(json_dumps_data)

    def delete(self, request, id, *args, **kwargs):
        print()
        print('-> UpdateModelDetailAPIView.delete')

        # print('[UpdateModelDetailAPIView].delete BEFORE obj = self.get_object(id=', id, ')')
        obj = self.get_object(id=id)
        # print('[UpdateModelDetailAPIView].delete AFTER obj = self.get_object(id=', id, ')')

        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)

        deleted_, item_deleted = obj.delete()
        print('deleted_:', deleted_)
        print('[id=', id, '] -> item_deleted:', item_deleted)

        if deleted_ == 1:
            json_data = json.dumps({"message": "Successfully deleted"})
            print('<- UpdateModelDetailAPIView.delete')
            return self.render_to_response(json_data, status=200)

        data = json.dumps({"message": "Could not delete item. Try again later."})
        print('<- UpdateModelDetailAPIView.delete')
        return self.render_to_response(data, status=403)

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

    # def render_to_response(self, data, status=200):
    #     print()
    #     print('-> UpdateModelListAPIView.render_to_response')
    #
    #     print('<- UpdateModelListAPIView.render_to_response')
    #     return HttpResponse(data, content_type='application/json', status=status)

    def get(self, request, *args, **kwargs):
        print()
        print('-> UpdateModelListAPIView.get')
        # print('[UpdateModelListAPIView].get BEFORE qs = UpdateModel.objects.all()')

        qs = UpdateModel.objects.all()

        # print('[UpdateModelListAPIView].get AFTER qs = UpdateModel.objects.all()')
        # print()
        # print('[UpdateModelListAPIView].get BEFORE json_data = obj.serialize()')

        json_dumps_data = qs.serialize()

        # print('[UpdateModelListAPIView].get AFTER json_data = obj.serialize()')
        print('<- UpdateModelListAPIView.get')

        return self.render_to_response(json_dumps_data)

    def post(self, request, *args, **kwargs):
        print()
        print('-> UpdateModelListAPIView.post')
        # print()
        # print('[UpdateModelListAPIView].post: request.POST =', request.POST)
        # print()
        # print('[UpdateModelListAPIView].post: BEFORE form = UpdateModelForm(request)')

        request_body = request.body.decode()
        # print('request_body:', request_body)
        # print()

        valid_json = is_json(request_body)
        # print('[UpdateModelListAPIView].post -> valid_json:', valid_json)

        if not valid_json:
            error_data = json.dumps({"message": "Invalid data sent, please send using JSON!"})
            return self.render_to_response(error_data, status=400)

        data = json.loads(request_body)
        form = UpdateModelForm(data)
        # form = UpdateModelForm(request.POST)
        # print()
        # print('[UpdateModelListAPIView].post: form =', form)
        # print()

        # print('[UpdateModelListAPIView].post: AFTER form = UpdateModelForm(request)')

        if form.is_valid():
            print()
            print('>[UpdateModelListAPIView].post: form.is_valid()!')

            obj = form.save(commit=True)
            obj_data = obj.serialize()
            # print('>[UpdateModelListAPIView].post: obj_data =', obj_data)

            print('<[UpdateModelListAPIView].post.form.is_valid()')
            print('<- UpdateModelListAPIView.post')
            return self.render_to_response(obj_data, status=201)

        if form.errors:
            print('>[UpdateModelListAPIView].post form.errors')

            data = json.dumps(form.errors)
            print('>[UpdateModelListAPIView].post: data =', data)

            print('<[UpdateModelListAPIView].post.form.errors')
            print('<- UpdateModelListAPIView.post')
            return self.render_to_response(data, status=400)

        data = json.dumps({'message': 'Not Allowed'})

        print('------------------> Not Valid, but No Errors! <--------------------')
        print('<- UpdateModelListAPIView.post')
        return self.render_to_response(data, status=406)

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
