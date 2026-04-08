#! /usr/bin/env bash

# 有报错，脚本立刻停止
set -e

#停止并删除容器 -v：删除数据卷（数据库数据等） 删除“孤儿容器” 清除在出现错误后可能遗留的已损坏的堆栈信息
# 清空上一次运行留下的所有状态
docker-compose down -v --remove-orphans 

# 删除所有 __pycache__ 目录
if [ $(uname -s) = "Linux" ]; then
    echo "Remove __pycache__ files"
    sudo find . -type d -name __pycache__ -exec rm -r {} \+
fi
#构建镜像
docker-compose build
#启动容器
docker-compose up -d
docker-compose exec -T backend bash scripts/tests-start.sh "$@"
