import argparse
import sys
import re
import os
import importlib.util

###### {{{classname ... }}}
# - {{{classname →<div class="classname">\n
# - }}}          →</div>
def replace_class(text):
    pattern = r'^{{{{*\s*([a-zA-Z0-9_ -]+)$'
    text = re.sub(pattern, lambda m: f'<div class="{m.group(1)}">\n',
                  text, flags=re.MULTILINE)
    text = re.sub(r'^}}}}*(.*)$', lambda m: f'</div>\n',
                  text, flags=re.MULTILINE)
    return text

###### callouts対応
def convert_callouts(text):
    icons_dict = {
        'INFO': '', # 󰋽 
        'NOTE': '',
        'TODO': '',
        'TIP': '',
        'HINT': '',
        'ABSTRACT': '',
        'SUMMARY': '󰨸',
        'TLDR': '󰨸',
        'QUESTION': '', # 󰘥 
        'SUCCESS': '',
        'IMPORTANT': '󰅾',
        'CAUTION': '󰒡',
        'ALERT': '󰀪', #  󰀪
        'WARNING': '',
        'BUG': '',
        'ERROR': '',
        'FAIL': '',
        'FAILURE': '',
        'DANGER': '⚡', # 󱐌⚡
        'QUOTE': '୨୧', #  󱆨 ୨୧
        'EXAMPLE': '󰉹', # 󰉹 
        'STICKY': '󰐃',
        'TEA': ' ',
    }

    #pattern = r"^>\s*\[!(.+?)\]\s*(.+?)\n((?:^>.*(?:\n|$))+)" # 複数行のみ対応
    pattern = r"^>\s*\[!(.+?)\]\s*(.+?)\n(?:((?:^>.*(?:\n|$))*))?" # 1行のみも対応

    def replace_func(m):
        # 1行目：アイコンとタイトル
        callout_type = m.group(1).strip().upper()
        icon = icons_dict.get(callout_type, '') # fallback=infoアイコン
        title = m.group(2).strip()

        # 2行目以降：本文
        raw_body = m.group(3)
        body_lines = raw_body.strip().splitlines() if raw_body else ""
        body = "\n".join("<p>" + line[1:].strip() + "</p>" for line in body_lines if line.startswith('>'))

        # HTMLに変換
        html = f'''
<div class="callout" data-callout="{callout_type}">
  <div class="callout-title">
    <div class="callout-title-icon">{icon}</div>&nbsp;
    <div class="callout-title-inner">{title}</div>
  </div>
  <div class="callout-content">{body}</div>
</div>'''
        # デバッグ用
        #print(m.groups())
        #print((callout_type, title, body))
        #print(html)
        return html

    return re.sub(pattern, replace_func, text, flags=re.MULTILINE)


###### メイン処理 ######
def main():
    # 引数処理
    parser = argparse.ArgumentParser(description='usage: filter4marp.py [-h] [--input <filepath>] [--output <filepath>]')
    parser.add_argument('-i', '--input', default=None)
    parser.add_argument('-o', '--output', default=None)
    args = parser.parse_args()

    # 入力テキスト取得
    if args.input:
        with open(args.input, encoding="UTF-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()
    #print(text) # for debug

    # フィルター通す
    text = replace_class(text)
    text = convert_callouts(text)

    # 出力
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        sys.stdout.write(text)

if __name__ == "__main__":
    main()
