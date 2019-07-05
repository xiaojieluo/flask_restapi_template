'''
自定义错误文件
'''

from flask import request, json
from werkzeug.exceptions import HTTPException

class APIException(HTTPException):
    '''
    自定义 API 请求错误， 返回的 json 格式
    '''
    code = 500
    msg = '抱歉，后台发生了错误 (*￣︶￣)!'
    error_code = 999

    def __init__(self, msg = None, code = None, error_code = None, headers = None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg

        super(APIException, self).__init__(msg, None)

    def get_body(self, environ = None):
        body = dict(
            msg = self.msg,
            error_code = self.error_code,
            request = request.method + ' ' + self.get_url_no_param()
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ = None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')

        return main_path[0]
