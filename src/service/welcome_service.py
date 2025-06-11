from django.conf import settings


class WelcomeService:
    @staticmethod
    def get_welcome_info():
        """获取欢迎信息"""
        return {
            "message": "欢迎使用 python-scaffold-template 脚手架",
            "version": "1.0.0",
            "framework": "Django REST framework",
        }
