#! /usr/bin/env bash

set -e
set -x

# 检测数据库连接是否可用
python app/backend_pre_start.py

# Run migrations更新数据库表结构
alembic upgrade head

# Create initial data in DB 写入初始业务数据（如超级管理员）
python app/initial_data.py
