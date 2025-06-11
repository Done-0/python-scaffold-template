import time
import uuid
from typing import Any, Dict, Optional

from rest_framework.request import Request
from rest_framework.response import Response

from utils.biz_error_utils import Err, new
from src.enums.err_code import ErrCode


class Result:
    """通用 API 响应结果"""

    def __init__(
        self,
        err: Optional[Err] = None,
        data: Any = None,
        request_id: Optional[str] = None,
    ):
        """初始化响应结果"""
        self.err = err
        self.data = data
        self.request_id = request_id or str(uuid.uuid4()).replace("-", "")[:32]
        self.timestamp = int(time.time())

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        if self.err:
            return {
                "code": self.err.code,
                "msg": self.err.msg,
                "data": self.data,
                "requestId": self.request_id,
                "timeStamp": self.timestamp,
            }
        else:
            return {
                "data": self.data,
                "requestId": self.request_id,
                "timeStamp": self.timestamp,
            }

    def to_response(self) -> Response:
        """转换为 DRF 响应对象"""
        return Response(self.to_dict())


def success(request: Optional[Request] = None, data: Any = None) -> Response:
    """成功响应"""
    request_id = request.headers.get("X-Request-ID") if request else None

    result = Result(err=None, data=data, request_id=request_id)
    return result.to_response()


def fail(
    request: Optional[Request] = None, data: Any = None, err: Any = None
) -> Response:
    """错误响应"""
    request_id = request.headers.get("X-Request-ID") if request else None

    if isinstance(err, Err):
        biz_err = err
    else:
        biz_err = new(ErrCode.SERVER_ERROR)
        if err:
            biz_err.msg = str(err)

    result = Result(err=biz_err, data=data, request_id=request_id)
    return result.to_response()
