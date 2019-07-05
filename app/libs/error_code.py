from werkzeug.exceptions import HTTPException
from app.libs.error import APIException

class Success(APIException):
    code = 201
    msg = 'success'
    error_code = 0

class DeleteSuccess(Success):
    code = 202
    error_code = 1

class ServerError(APIException):
    code = 500
    error_code = 999

class ClientTypeError(APIException):
    code = 400
    msg = '未检测到客户端类型'
    error_code = 1006

class ParameterException(APIException):
    code = 400
    msg = '无效参数'
    error_code = 1000

class NotFound(APIException):
    code = 404
    msg = '没有找到对应的资源 O__O...'
    error_code = 1001

class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = '认证失败'

class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = '禁止访问，不在对应权限内'

class SingleLogin(APIException):
    code = 400
    error_code = 2002
    msg = '请重新登陆'

class DuplicateAct(APIException):
    code = 400
    error_code = 2001
    msg = '请勿重复操作'
