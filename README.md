# Python项目脚手架

Python 项目脚手架模板，提供基础的工程化目录布局。

## 项目工程目录

```
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
└── test/                 # 测试目录
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
