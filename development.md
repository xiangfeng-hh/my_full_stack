# 开发文档

## Docker Compose

* 用 Docker Compose 启动本地栈 local stack:

```bash
docker compose watch
```

* 现在可以打开浏览器，与以下网址进行交互:

Frontend: <http://localhost:5173>

Backend, JSON based web API based on OpenAPI: <http://localhost:8000>

自动交互式文档: <http://localhost:8000/docs>

管理员，数据库网页管理: <http://localhost:8080>

Traefik UI, to see how the routes are being handled by the proxy: <http://localhost:8090>


要检查日志，请在另一个终端运行:

```bash
docker compose logs
```

要查看特定服务的日志，请添加服务名称，例如:

```bash
docker compose logs backend
```


## Local Development

Docker Compose 文件配置为每个服务在 `localhost`中的不同端口中可用 

可以关闭 Docker Compose 的某个服务，启动其本地开发服务

例如:

```bash
docker compose stop frontend
```

启动本地前端开发服务器:

```bash
bun run dev
```
或者你可以停止backend Docker Compose 服务：
:

```bash
docker compose stop backend
```

启动本地后端开发服务器:

```bash
cd backend
fastapi dev app/main.py
```

## Docker Compose in `localhost.tiangolo.com`

当你启动 Docker Compose 栈时，默认会使用`localhost` ，每个服务（后端、前端、管理员程序等）都有不同的端口。

当你将其部署到生产环境时，它会将每个服务部署在不同的子域subdomain，比如后端 `api.example.com`和前端`dashboard.example.com` 

In the guide about [deployment](deployment.md) you can read about Traefik, the configured proxy. That's the component in charge of transmitting traffic to each service based on the subdomain.

If you want to test that it's all working locally, you can edit the local `.env` file, and change:

```dotenv
DOMAIN=localhost.tiangolo.com
```

That will be used by the Docker Compose files to configure the base domain for the services.

Traefik will use this to transmit traffic at `api.localhost.tiangolo.com` to the backend, and traffic at `dashboard.localhost.tiangolo.com` to the frontend.

The domain `localhost.tiangolo.com` is a special domain that is configured (with all its subdomains) to point to `127.0.0.1`. This way you can use that for your local development.

After you update it, run again:

```bash
docker compose watch
```

When deploying, for example in production, the main Traefik is configured outside of the Docker Compose files. For local development, there's an included Traefik in `compose.override.yml`, just to let you test that the domains work as expected, for example with `api.localhost.tiangolo.com` and `dashboard.localhost.tiangolo.com`.

## Docker Compose files and env vars

Docker Compose 文件会使用包含配置信息的“.env”文件，将这些配置作为环境变量注入到容器中。

它们还会使用脚本中设置的环境变量中的额外配置

更改变量后，确保重启堆栈

```bash
docker compose watch
```

## The .env file
根据你的工作流程，你可能想把它排除在 Git 之外，比如你的项目是公开的。在这种情况下，你必须确保在构建或部署项目时为 CI 工具设置一个获取该信息的方法。

One way to do it could be to add each environment variable to your CI/CD system, and updating the `compose.yml` file to read that specific env var instead of reading the `.env` file.


## URLs


### Development URLs

local development

Frontend: <http://localhost:5173>

Backend: <http://localhost:8000>

Automatic Interactive Docs (Swagger UI): <http://localhost:8000/docs>

Automatic Alternative Docs (ReDoc): <http://localhost:8000/redoc>

Adminer: <http://localhost:8080>

Traefik UI: <http://localhost:8090>



配置 `localhost.tiangolo.com`的本地开发 

Frontend: <http://dashboard.localhost.tiangolo.com>

Backend: <http://api.localhost.tiangolo.com>

Automatic Interactive Docs (Swagger UI): <http://api.localhost.tiangolo.com/docs>

Automatic Alternative Docs (ReDoc): <http://api.localhost.tiangolo.com/redoc>

Adminer: <http://localhost.tiangolo.com:8080>

Traefik UI: <http://localhost.tiangolo.com:8090>
