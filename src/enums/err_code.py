from typing import Dict


class ErrCode:
    """错误码常量定义"""

    SUCCESS = 200
    UNKNOWN_ERROR = 0
    SERVER_ERROR = 10000
    BAD_REQUEST = 20000


CODE_MSG: Dict[int, str] = {
    ErrCode.SUCCESS: "请求成功",
    ErrCode.UNKNOWN_ERROR: "未知业务异常",
    ErrCode.SERVER_ERROR: "服务端异常",
    ErrCode.BAD_REQUEST: "错误请求",
}


def get_message(code: int) -> str:
    """
    根据错误码获取对应的错误信息

    Args:
        code: 错误码

    Returns:
        str: 错误信息
    """
    return CODE_MSG.get(code, CODE_MSG[ErrCode.UNKNOWN_ERROR])
