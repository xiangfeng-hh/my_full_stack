# Full Stack FastAPI Template

## Technology Stack and Features

- 基于https://github.com/fastapi/full-stack-fastapi-template

- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) for the Python backend API.
  - 🧰 [SQLModel](https://sqlmodel.tiangolo.com) for the Python SQL database interactions (ORM).
  - 🔍 [Pydantic](https://docs.pydantic.dev), used by FastAPI, for the data validation and settings management.
  - 💾 [PostgreSQL](https://www.postgresql.org) as the SQL database.
- 🚀 [React](https://react.dev) for the frontend.
  - 💃 Using TypeScript, hooks, [Vite](https://vitejs.dev), and other parts of a modern frontend stack.
  - 🎨 [Tailwind CSS](https://tailwindcss.com) and [shadcn/ui](https://ui.shadcn.com) for the frontend components.
  - 🤖 An automatically generated frontend client.
  - 🧪 [Playwright](https://playwright.dev) for End-to-End testing.
  - 🦇 Dark mode support.
- 🐋 [Docker Compose](https://www.docker.com) for development and production.

- 🔑 JWT (JSON Web Token) authentication.
- ✅ Tests with [Pytest](https://pytest.org).
- 📞 [Traefik](https://traefik.io) as a reverse proxy / load balancer.
- 🚢 Deployment instructions using Docker Compose, including how to set up a frontend Traefik proxy to handle automatic HTTPS certificates.
- 🏭 CI (continuous integration) and CD (continuous deployment) based on GitHub Actions.


### 配置

在`.env`更新配置

部署前，确保至少更改以下数值:

- `SECRET_KEY`
- `FIRST_SUPERUSER_PASSWORD`
- `POSTGRES_PASSWORD`

应该把这些作为秘密中的环境变量传递

详情阅读 [deployment.md](./deployment.md) 

### 生成秘密密钥

`.env`中的 密码/密钥的值使用命令生成


```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```
复制内容，并用它作为密码/密钥。然后再运行一次，生成另一个安全密钥。




## 后端开发

Backend docs: [backend/README.md](./backend/README.md).

## 前端开发

Frontend docs: [frontend/README.md](./frontend/README.md).

## 部署

Deployment docs: [deployment.md](./deployment.md).

## 开发

General development docs: [development.md](./development.md).

这包括使用 Docker Compose、自定义本地域名、配置等。