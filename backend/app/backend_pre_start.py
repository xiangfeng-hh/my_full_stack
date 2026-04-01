import logging

from sqlalchemy import Engine
from sqlmodel import Session, select
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app.core.db import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1

# @retry 装饰器失败会继续重试，直到成功或超时
@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init(db_engine: Engine) -> None:
    try:
        with Session(db_engine) as session:
            # 尝试创建一个会话session来检查数据库是否处于运行状态
            # select(1)不查表,只验证数据库连接可建立、SQL 可执行
            session.exec(select(1))
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("初始化服务")
    init(engine)
    logger.info("服务初始化完成")


if __name__ == "__main__":
    main()
