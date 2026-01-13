#
# Marp環境構築
#
FROM node:24-slim

# PythonとChrome入れる（不要なら外す）
# - python3 / pip : 前処理用
# - chromium      : PDF変換用
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      python3 \
      python3-pip \
      ca-certificates \
      chromium \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Node.jsパッケージ
COPY package*.json ./
RUN npm ci && npm cache clean --force

# Pythonの依存ライブラリ（不要なら以下2行は外す）
# COPY requirements.txt ./
# RUN pip3 install --no-cache-dir -r requirements.txt

# 全部/appにコピー
COPY . /app
RUN chmod +x /app/*.sh

# 起動スクリプト
# - ENTRYPOINTは固定の起動スクリプト。docker runでは変更不可
# - CMDはENTRYPOINTに与える引数。docker runにて変更可能
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["--html"]

