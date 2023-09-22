from rest_framework.renderers import JSONRenderer


class DFJsonRender(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code
        if 200 <= status_code < 400:
            resp = {"success": True, "msg": "", "data": data}
        else:
            resp = {"success": False, "msg": data.get("detail", ""), "data": data}

        return super().render(data=resp, accepted_media_type=accepted_media_type, renderer_context=renderer_context)
