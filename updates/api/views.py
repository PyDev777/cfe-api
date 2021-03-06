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


# @method_decorator(csrf_exempt, name='dispatch')
# class UpdateModelDetailAPIView(HttpResponseMixin, View):
#     """
#     Retrieve, Update, Delete --> Object
#     """
#
#     is_json = True
#
#     def get_object(self, id=None):
#         qs = UpdateModel.objects.filter(id=id)
#         if qs.count() == 1:
#             return qs.first()
#         return None
#
#     def get(self, request, id, *args, **kwargs):
#         obj = self.get_object(id=id)
#         if obj is None:
#             error_data = json.dumps({"message": "Update not found"})
#             return self.render_to_response(error_data, status=404)
#         json_dumps_data = obj.serialize()
#         return self.render_to_response(json_dumps_data)
#
#     def post(self, request, *args, **kwargs):
#         json_data = json.dumps({"message": "Method not Allowed, please create /api/updates/ Endpoint"})
#         return self.render_to_response(json_data, status=403)
#
#     def put(self, request, id, *args, **kwargs):
#         request_body = request.body.decode()
#         valid_json = is_json(request_body)
#         if not valid_json:
#             error_data = json.dumps({"message": "Invalid data sent, please send using JSON!"})
#             return self.render_to_response(error_data, status=400)
#         obj = self.get_object(id=id)
#         if obj is None:
#             error_data = json.dumps({"message": "Update not found"})
#             return self.render_to_response(error_data, status=404)
#         data = json.loads(obj.serialize())
#         passed_data = json.loads(request_body)
#         for (key, value) in passed_data.items():
#             data[key] = value
#         form = UpdateModelForm(data, instance=obj)
#         if form.is_valid():
#             obj = form.save(commit=True)
#             obj_data = json.dumps(data)
#             return self.render_to_response(obj_data, status=201)
#         if form.errors:
#             data = json.dumps(form.errors)
#             return self.render_to_response(data, status=400)
#         json_dumps_data = json.dumps({"Message": "Something on put"})
#         return self.render_to_response(json_dumps_data)
#
#     def delete(self, request, id, *args, **kwargs):
#         obj = self.get_object(id=id)
#         if obj is None:
#             error_data = json.dumps({"message": "Update not found"})
#             return self.render_to_response(error_data, status=404)
#         deleted_, item_deleted = obj.delete()
#         if deleted_ == 1:
#             json_data = json.dumps({"message": "Successfully deleted"})
#             return self.render_to_response(json_data, status=200)
#         data = json.dumps({"message": "Could not delete item. Try again later."})
#         return self.render_to_response(data, status=403)


# AUTH / Permissions -- Django REST Framework


@method_decorator(csrf_exempt, name='dispatch')
class UpdateModelListAPIView(HttpResponseMixin, View):
    """
    List View --> Retrieve -- Detail View
    Create View
    Update
    Delete
    """

    is_json = True
    queryset = None

    def get_queryset(self):
        qs = UpdateModel.objects.all()
        self.queryset = qs
        return qs

    def get_object(self, id=None):
        if id is None:
            return None
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, *args, **kwargs):
        request_body = request.body.decode()
        data = json.loads(request_body)
        passed_id = data.get('id', None)
        if passed_id is not None:
            obj = self.get_object(id=passed_id)
            if obj is None:
                error_data = json.dumps({"message": "Object not found for get"})
                return self.render_to_response(error_data, status=404)
            json_dumps_data = obj.serialize()
            return self.render_to_response(json_dumps_data)
        else:
            qs = self.get_queryset()
            json_dumps_data = qs.serialize()
            return self.render_to_response(json_dumps_data)

    def post(self, request, *args, **kwargs):
        request_body = request.body.decode()
        valid_json = is_json(request_body)
        if not valid_json:
            error_data = json.dumps({"message": "Invalid data sent, please send using JSON!"})
            return self.render_to_response(error_data, status=400)
        data = json.loads(request_body)
        form = UpdateModelForm(data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = json.dumps({'message': 'Not Allowed'})
        return self.render_to_response(data, status=406)

    def put(self, request, *args, **kwargs):
        request_body = request.body.decode()
        valid_json = is_json(request_body)
        if not valid_json:
            error_data = json.dumps({"message": "Invalid data sent, please send using JSON!"})
            return self.render_to_response(error_data, status=400)

        passed_data = json.loads(request_body)
        passed_id = passed_data.get('id', None)
        if not passed_id:
            error_data = json.dumps({"id": "This is required field for update an item"})
            return self.render_to_response(error_data, status=400)
        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({"message": "Object not found for update"})
            return self.render_to_response(error_data, status=404)
        data = json.loads(obj.serialize())
        for (key, value) in passed_data.items():
            data[key] = value

        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        json_dumps_data = json.dumps({"Message": "Something on put"})
        return self.render_to_response(json_dumps_data)

    def delete(self, request, *args, **kwargs):
        request_body = request.body.decode()
        valid_json = is_json(request_body)
        if not valid_json:
            error_data = json.dumps({"message": "Invalid data sent, please send using JSON!"})
            return self.render_to_response(error_data, status=400)

        passed_data = json.loads(request_body)
        passed_id = passed_data.get('id', None)
        if not passed_id:
            error_data = json.dumps({"id": "This is required field for delete an item"})
            return self.render_to_response(error_data, status=400)
        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({"message": "Object not found for delete"})
            return self.render_to_response(error_data, status=404)

        deleted_, item_deleted = obj.delete()
        if deleted_ == 1:
            json_data = json.dumps({"message": "Successfully deleted"})
            return self.render_to_response(json_data, status=200)
        data = json.dumps({"message": "Could not delete item. Try again later."})
        return self.render_to_response(data, status=403)
