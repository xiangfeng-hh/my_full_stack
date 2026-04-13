# Full Stack FastAPI Template

## Technology Stack and Features

基于https://github.com/fastapi/full-stack-fastapi-template

- [FastAPI]
  - 🧰 [SQLModel](https://sqlmodel.tiangolo.com) for the Python SQL database interactions (ORM).
  - 🔍 [Pydantic](https://docs.pydantic.dev), used by FastAPI, for the data validation and settings management.
  - 💾 [PostgreSQL](https://www.postgresql.org) as the SQL database.
- [React] 
  - 💃 Using TypeScript, hooks, [Vite](https://vitejs.dev), and other parts of a modern frontend stack.
  - 🎨 [Tailwind CSS](https://tailwindcss.com) and [shadcn/ui](https://ui.shadcn.com) for the frontend components.
  - 🤖 An automatically generated frontend client.



- 📞 [Traefik](https://traefik.io) as a reverse proxy / load balancer.
- 🚢 Deployment instructions using Docker Compose, including how to set up a frontend Traefik proxy to handle automatic HTTPS certificates.


### 配置

在`.env`更新配置，部署前至少更改:

- `SECRET_KEY`
- `FIRST_SUPERUSER_PASSWORD`
- `POSTGRES_PASSWORD`

应该把这些作为秘密中的环境变量传递

 



`.env`中的 密码/密钥的值使用命令生成


```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```
复制内容，并用它作为密码/密钥。然后再运行一次，生成另一个安全密钥。






