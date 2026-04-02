#!/usr/bin/env bash

#任一步失败就立刻退出脚本
set -e
#执行时打印每条命令
set -x

coverage run -m pytest tests/
coverage report
#生成 HTML 覆盖率报告 通常在 htmlcov/
coverage html --title "${@-coverage}"
