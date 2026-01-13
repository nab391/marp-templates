import glob
import os
import sys
import argparse

# ファイル一覧取得（path名でソート）
def get_files_sorted(directory, ext):
    # 指定ディレクトリ以下の全ての.extファイルを取得
    files = glob.glob(os.path.join(directory, "**", f"*.{ext}"), recursive=True)
    files.sort(key=lambda x: os.path.basename(x).lower()) # ファイル名でソート
    return files

# 除外ファイル処理
def get_files_excluded(files, args):
    excludes = [] # 除外ファイル名パターン
    excludes.extend([x.strip().strip('"') for x in args.split(',')])
    # print(excludes, file=sys.stderr) # for debug
    for x in excludes:
        files = [f for f in files if x not in f]
    return files

# ファイル結合本体
def merge_files(files):
    text = ""
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            text=text + f.read() + "\n" # 改行必須（Marpの誤判定回避）
    return text

# 1) 引数処理
parser = argparse.ArgumentParser(description='usage: join-files.py [-h] srcdir [--output <filepath>] [--srcext <ext>] [--exclude <str> [str ...]]')
parser.add_argument('srcdir', default="src", help='source directory')
parser.add_argument('-o', '--output', default=None, help='output filename')
parser.add_argument('-x', '--exclude', default=None, help='除外するファイル名（部分指定、複数可）')
parser.add_argument('--srcext', default="md", help='source file extension')
args = parser.parse_args()

# 2) ファイル一覧取得
files = get_files_sorted(args.srcdir, args.srcext)
# print(args.exclude, file=sys.stderr) # for debug
if args.exclude:
    files = get_files_excluded(files, args.exclude)

if not files:
    print(f"指定のディレクトリには有効な{args.srcext}ファイルが見つかりませんでした。")
    exit()

# 3) ファイル結合
text = merge_files(files)

# 4) 出力
if args.output:
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(text)
else:
    sys.stdout.write(text)

