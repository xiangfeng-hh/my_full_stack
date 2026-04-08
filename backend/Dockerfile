FROM python:3.10

ENV PYTHONUNBUFFERED=1

# 使用阿里云 PyPI 镜像源（加速 uv 下载依赖）
ENV UV_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/
# 请求失败自动重试 3 次（提高 VPN / 不稳定网络环境下成功率）
ENV UV_HTTP_RETRIES=3

# 安装 uv
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=ghcr.io/astral-sh/uv:0.9.26 /uv /uvx /bin/
ENV UV_COMPILE_BYTECODE=1
# uv Cache
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#caching
ENV UV_LINK_MODE=copy


WORKDIR /app/

# Place executables in the environment at the front of the path
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#using-the-environment
ENV PATH="/app/.venv/bin:$PATH"



# 安装依赖
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=backend/uv.lock,target=uv.lock \
    --mount=type=bind,source=backend/pyproject.toml,target=pyproject.toml \
    uv sync --frozen

COPY ./backend/scripts /app/backend/scripts

COPY ./backend/pyproject.toml ./backend/alembic.ini /app/backend/

COPY ./backend/app /app/backend/app



WORKDIR /app/backend/




# 设置 Python 能找到 app
ENV PYTHONPATH=/app/backend

CMD ["fastapi", "run", "--workers", "4", "app/main.py"]
