# デフォルト：1. src/*.mdを全て結合。2. HTML出力
# - src/がmarkdown保存場所。*.mdが集約されている
# - dist/が出力先。css/やimg/はこちらに配置しておく
./slide-make.sh

# 結合対象から名前にhtmlonlyを含むファイルを除外する
./slide-make.sh --exclude=htmlonly

# テーマ設定：テーマ名を指定
./slide-make.sh --css=gaia

# テーマ設定：CSSファイルを指定（カスタムテーマ）
./slide-make.sh --css=./css/style.css

# PDF出力
./slide-make.sh --exclude=htmlonly --pdf

# 組み合わせ例（HTML専用のページを除いてPDF出力。ログ出力あり）
./slide-make.sh --exclude=htmlonly --pdf --debug

# markdownの結合をしない。marpによる変換のみ実行する
./slide-make.sh --convert

# デバッグモード：1. 環境変数を表示。2. marpをデバッグモードで起動
./slide-make.sh --debug

# 組み合わせ例（HTML専用のページを除いてPDF出力。ログ出力あり）
./slide-make.sh --exclude=htmlonly --pdf --debug

