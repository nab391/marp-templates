# marp-templates

Dockerベースの Marp スライド作成テンプレートです。
Markdownファイルを分割管理しつつ、拡張書式・独自フィルタ・HTML/PDF出力の構成変更を手軽に扱える環境です。


## 目的・概要

Marpでのスライド作成にあたって、下記を実現＆手軽にするために構築しました。

- Markdownファイルを分割管理し、スライド作成時には自動で結合する
- 分割したファイルのうち含めるファイルを手軽に切り替えたい（PDF生成では使わない等々）
- Markdownの書式拡張プラグインや独自書式フィルターを毎回指定せずに使いたい
- OSによらず同一の手順で動かしたい＆同一の出力を得たい

環境としてはDocker化＆Docker内に上記のスクリプトを組み込む、という形になっています。
結果として「環境構築で悩まない」「書くことに集中できる」 環境が整ったと思います。


## ディレクトリ構成と手順概要

ディレクトリ構成は下記の通りです。
直接使うのは★をつけた3箇所のみです。

```text
marp-templates/
├─ ★build-marp.sh / .bat
│
├─ marp/
│  ├─ Dockerfile
│  ├─ <Dockerコンテナ内の環境>
│
├─ template-01-minimum/
│  ├─ ★slide-make.sh / .bat
│  ├─ ★src/      # 入力Markdown（分割管理）
│  ├─ dist/       # 出力先
│       ├─ css/   # テーマCSS
│       ├─ img/   # 画像などの参照ファイル
│
├─ template-02/
│  ├─ 以下同様
│
```


## セットアップ

セットアップはリポジトリ直下で`build-marp.sh`を実行すれば完了です。
※Windowsの場合は`.bat`を使用

この時点で以下がすべて組み込まれます。

* Markdownの自動結合
* 拡張Markdown書式
* 独自フィルタ処理


## スライド生成方法

スライドのサンプル生成（動作確認）は
いずれかのtemplate内で`slide-make.sh`を実行すれば完了です。

出力先はテンプレート内の`dist`ディレクトリ内の`slide.html`です。

サンプルではないスライドを作成する場合、ソースとなるmarkdownファイルは
テンプレート内の`src`ディレクトリ内に配置してください。
名前順で自動で結合されます。

なお、template-04でサンプルのPDFを生成した場合、
本レポジトリのトップに置いてある`slide.pdf`と同じ物が出力されます。


## オプション一覧

スライド生成のオプションは下記の通りです。

- **基本(HTML生成、自動結合)**
    - `slide-make.sh`
- **結合時、一部ファイルを除外**
    - `--exclude=<文字列>`
        - ファイル名に指定文字列を含むファイルは除外
    - 例）`htmlonly`を含むファイルを除外：  
      `slide-make.sh --exclude=htmlonly`
- **PDF生成**
    - `--pdf`
    - 例）PDF生成（htmlonlyを除外）
    - `slide-make.sh --pdf --exclude=htmlonly`
    - デフォルトで`--exclude=-exclude`が指定されています
- **テーマ設定（CSS指定）**
    - `--css=<cssファイルパス>`
    - デフォルトは`css/style.css`
    - フォルダは`dist`基点


## Markdown書式（文字装飾）

Markdownの書式について、拡張部分をメインに説明します。

| 意味       | タグ   | 記述             | 表示例         |
| ---        | ---    | ---              | ---            |
| 強調1      | mark   | `==text==`       | ==text==       |
| 強調2      | em     | `*text*`         | *text*         |
| 強調3      | strong | `**text**`       | **text**       |
| 取り消し線 | s      | `~~text~~`       | ~~text~~       |
| 下線       | u      | `_text_`         | _text_         |
| 下付       | sub    | `text~下~`       | text~下~       |
| 上付       | sup    | `text^上^`       | text^上^       |
| ルビ       | ruby   | `{漢字\|かんじ}` | {漢字\|かんじ} |


## Markdown書式（他）

文字装飾以外の書式です。

| md記述        | 変換後                         | 備考                     |
| ---           | ---                            | ---                      |
| `# text{.name}` | `<h1 class="name">text</h1>`     | 手軽にクラス付与できる |
| `[text]{.name}` | `<span class="name">text</span>` | 手軽にspanできる         |
| `:::name` ～`:::` | `<div class="name">～</div>`     | ~~手軽にdivできる~~←手軽でない    |
| `{{{name` ～`}}}` | `<div class="name">～</div>`     | 手軽にdivできる(独自フィルタ)    |


## ライセンス

好きに使ってください。
ただし **自己責任**です。

## コメント

テンプレートは整理中です。ちょくちょく修正入ります。

