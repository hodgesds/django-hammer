from django.http import HttpResponse
from django.core import serializers
import json


class AJAXResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)

    def render_obj_to_json(self, context, **response_kwargs):
        if hasattr(self, 'object'):
            object_set = self.object.__class__.objects.filter(id=self.object.id)
        elif hasattr(self, 'object_list'):
            object_set = self.object_list
        return HttpResponse(
            serializers.serialize('json', object_set),
            content_type='application/json',
            **response_kwargs
        )

    def render_obj_to_xml(self, context, **response_kwargs):
        if hasattr(self, 'object'):
            object_set = self.object.__class__.objects.filter(id=self.object.id)
        elif hasattr(self, 'object_list'):
            object_set = self.object_list
        return HttpResponse(
            serializers.serialize('xml', object_set),
            content_type='application/xml',
            **response_kwargs
        )