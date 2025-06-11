# Python项目脚手架

基于 Django + DRF 的 Python 项目脚手架模板，提供完整的工程化目录布局和开箱即用的功能。

## 技术栈

- **Web框架**: Django 5.2.3 + Django REST Framework
- **API文档**: drf-spectacular (Swagger/OpenAPI)
- **身份验证**: JWT (djangorestframework-simplejwt)
- **数据库**: PostgreSQL / SQLite
- **跨域支持**: django-cors-headers
- **过滤器**: django-filter
- **包管理**: uv (推荐) / pip

## 项目工程目录

```bash
.
├── configs/              # 配置文件和配置管理
├── docker-compose.yml    # Docker Compose 配置文件
├── docs/                 # 项目文档
├── requirements.txt      # 项目依赖
├── scripts/              # 实用脚本
├── src/                  # 项目代码
│   ├── controller/       # 控制器，RESTful 接口文件目录
│   ├── dto/              # 数据传输对象
│   ├── entity/           # 实体类，对应数据库模型
│   ├── enums/            # 枚举定义
│   ├── middleware/       # 中间件目录
│   ├── repository/       # 数据访问层
│   ├── service/          # 业务逻辑层
│   ├── utils/            # 通用工具目录
│   └── vo/               # 视图对象，数据模型处理类目录
├── test/                 # 测试目录
├── static/               # 静态文件
├── media/                # 媒体文件上传目录
└── logs/                 # 日志文件                
```

## 开发范式

1. 业务逻辑在 service 层中实现
2. 数据库操作逻辑在 repository 层中实现
3. API路由和控制器在 controller 层中实现
4. 通用工具函数在 utils 层中实现
5. 实体类在 entity 目录中实现
6. 配置文件在 configs 目录下实现
7. 状态码枚举在 enums 目录下实现
8. 测试代码在 test 目录下实现

## 快速开始

### 1. 安装依赖
```bash
git clone https://github.com/Done-0/python-scaffold-template.git
cd python-scaffold-template
uv venv && source .venv/bin/activate
uv pip install -r pyproject.toml
```

### 2. 🔴 重要配置修改 (configs/settings.py)
```python
# 数据库配置
DB = {
    'postgresql': {
        'NAME': 'your_db_name',      # 🔴 修改数据库名
        'USER': 'your_db_user',      # 🔴 修改用户名
        'PASSWORD': 'your_password', # 🔴 修改密码
        # ...其他配置
    }
}

# 使用 SQLite (开发环境)
DATABASES = {'default': DB.get('sqlite')}

# 生产环境安全配置
SECRET_KEY = 'your-secret-key'  # 🔴 必须修改
DEBUG = False                   # 🔴 生产环境设为 False
ALLOWED_HOSTS = ['your-domain.com']
```

### 3. 数据库初始化
```bash
python src/main.py migrate           # 执行迁移
python src/main.py createsuperuser   # 创建管理员
python src/main.py runserver         # 启动服务
```

### 4. 访问地址
- 主页: http://localhost:8000/
- API文档: http://localhost:8000/api/docs/
- 管理后台: http://localhost:8000/admin/

## 核心功能特性

### 1. 统一响应格式

项目提供了统一的 API 响应格式，位于 `src/vo/result.py`：

```python
# 成功响应
{
  "data": T,
  "requestId": string,
  "timeStamp": number
}

# 错误响应
{
    "code": number,
    "msg": string,
    "data": T,
    "requestId": string,
    "timeStamp": number
}
```

### 3. API 文档

集成了 drf-spectacular，自动生成 Swagger 文档：
- 访问地址: `http://localhost:8000/api/docs/`
- Schema: `http://localhost:8000/api/schema/`

### 4. JWT 身份验证

- 登录后获取 access_token 和 refresh_token
- 请求头格式: `Authorization: Bearer <token>`
- 自动处理 token 刷新机制

### 5. 跨域支持

已配置 django-cors-headers，支持前后端分离开发。

## 许可证

[MIT License](LICENSE)
