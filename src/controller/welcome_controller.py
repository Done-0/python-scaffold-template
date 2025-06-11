from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiResponse

from src.service.welcome_service import WelcomeService
from utils.response_utils import success, fail
from utils.biz_error_utils import new
from src.enums.err_code import ErrCode


@extend_schema(
    summary="欢迎接口",
    description="获取系统欢迎信息",
    responses={200: OpenApiResponse(description="成功")},
    tags=["系统"],
)
@api_view(["GET"])
@permission_classes([AllowAny])
def welcome(request):
    """欢迎接口"""
    welcome_info = WelcomeService.get_welcome_info()
    return success(request, welcome_info)


@extend_schema(
    summary="错误演示接口",
    description="演示错误处理",
    responses={200: OpenApiResponse(description="成功")},
    tags=["演示"],
)
@api_view(["GET"])
@permission_classes([AllowAny])
def error_demo(request):
    """错误演示接口"""
    error_type = request.GET.get("type", "server")

    if error_type == "server":
        try:
            result = 1 / 0
        except Exception as e:
            return fail(request, err=e)
    elif error_type == "business":
        biz_error = new(ErrCode.BAD_REQUEST, "请求参数验证失败")
        return fail(request, err=biz_error)
    else:
        validation_errors = {"username": "用户名不能为空", "email": "邮箱格式不正确"}
        biz_error = new(ErrCode.BAD_REQUEST, "表单验证失败")
        return fail(request, data=validation_errors, err=biz_error)
