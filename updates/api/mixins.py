# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class CSRFExemptMixin(object):
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, *args, **kwargs):
#         print('UpdateModelListAPIView.DISPATCH !!!')
#         return super(UpdateModelListAPIView, self).dispatch(*args, **kwargs)
#
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(self, *args, **kwargs)
