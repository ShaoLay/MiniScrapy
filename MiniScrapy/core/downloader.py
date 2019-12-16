import requests

from MiniScrapy.https.response import Response


class Downloader():
    def get_response(self, request):
        if request.method.upper() == 'GET':
            resp = requests.get(request.url, headers=request.headers)
        elif request.method.upper() == 'POST':
            resp = requests.post(request.url, headers=request.headers, data=request.data)
        else:
            raise Exception('不支持的请求方法.')

        return Response(url=resp.url,
                        status_code=resp.status_code,
                        headers=resp.headers,
                        body=resp.content)