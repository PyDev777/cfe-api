print()
print('---> VIEWS.PY')


import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from cfeapi.mixins import JsonResponseMixin
from .models import Update
from django.core.serializers import serialize


# obj = Update.objects.get(id=1)


# def json_example_view(request):
#     data = {
#         'count': 800,
#         'content': 'json_example_view',
#     }
#     json_data = json.dumps(data)
#     return HttpResponse(json_data, content_type='application/json', charset='UTF8')
#
#
# class JsonCBV(View):
#
#     def get(self, request, *args, **kwargs):
#         data = {
#             'count': 900,
#             'content': 'JsonCBV',
#         }
#         return JsonResponse(data)
#
#
# class JsonCBV2(JsonResponseMixin, View):
#     def get(self, request, *args, **kwargs):
#         data = {
#             'count': 1000,
#             'content': 'JsonCBV2',
#         }
#         return self.render_to_json_response(data)


class SerializedDetailView(View):
    print('')
    print('--> SerializedDetailView')

    def get(self, request, *args, **kwargs):
        print('-> SerializedDetailView.get')

        print('[SerializedDetailView].get BEFORE obj = Update.objects.get(id=1)')
        obj = Update.objects.get(id=1)
        print('[SerializedDetailView].get AFTER obj = Update.objects.get(id=1)')

        # data = serialize("json", [obj, ], fields=('user', 'content'))
        # print(data)
        # json_data = data
        # data = {
        #     'user': obj.user.username,
        #     'content': obj.content,
        # }
        #

        print()
        print('[SerializedDetailView].get BEFORE json_data = obj.serialize()')
        json_data = obj.serialize()
        print('[SerializedDetailView].get AFTER json_data = obj.serialize()')

        print()
        print('<- SerializedDetailView.get')
        return HttpResponse(json_data, content_type='application/json')

    print()
    print('<-[SerializedDetailView]')


class SerializedListView(View):
    print('')
    print('--> [SerializedListView]')

    def get(self, request, *args, **kwargs):
        print('-> SerializedListView.get')

        print()
        print('[SerializedListView].get BEFORE qs = Update.objects.all()')
        qs = Update.objects.all()
        print('[SerializedListView].get AFTER qs = Update.objects.all()')

        # data = serialize("json", qs, fields=('user', 'content'))
        # print(data)
        # json_data = data

        print()
        print('[SerializedListView].get BEFORE json_data = qs.serialize()')
        json_data = qs.serialize()
        print('[SerializedListView].get AFTER json_data = qs.serialize()')

        print()
        print('<-[SerializedListView].get')
        return HttpResponse(json_data, content_type='application/json')

    print()
    print('<-[SerializedListView]')


print('<--- VIEWS.PY')
