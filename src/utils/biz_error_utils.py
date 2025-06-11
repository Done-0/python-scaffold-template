from typing import Optional

from src.enums.err_code import get_message


class Err(Exception):
    """业务错误类"""

    def __init__(self, code: int, msg: Optional[str] = None):
        """
        初始化业务错误

        Args:
            code: 错误码
            msg: 错误信息，不传则使用错误码对应的默认信息
        """
        self.code = code
        self.msg = msg if msg else get_message(code)
        super().__init__(self.msg)

    def __str__(self) -> str:
        """
        返回错误信息字符串

        Returns:
            str: 错误信息
        """
        return self.msg


def new(code: int, msg: Optional[str] = None) -> Err:
    """
    创建业务错误实例

    Args:
        code: 错误码
        msg: 可选的错误信息

    Returns:
        Err: 业务错误实例
    """
    return Err(code, msg)
