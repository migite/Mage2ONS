# Mage2ONS

未展開のゲームデータから、[ONScripter](https://ogapee.github.io/www/onscripter.html) でプレイ可能な環境を生成するコンバータです。

> 本コンバータはAIエージェントによって生成されました。

## 対象作品

| 項目 | 内容 |
|---|---|
| ブランド | MOONSTONE |
| タイトル | 何処へ行くの、あの日 |
| 対象バージョン | FANZA DL版 |
| 元の解像度 | 800x600 |
| 作品情報 | https://erogamescape.dyndns.org/~ap2/ero/toukei_kaiseki/game.php?game=3697#ad |

## 必要環境

- Python 3.10 以上
- [Pillow](https://pillow.readthedocs.io/)（`pip install pillow`）

実行・検証には別途 [ONScripter](https://ogapee.github.io/www/onscripter.html)（または対応する派生実行ファイル）と `default.ttf` が必要です。

## 使い方

### 単体実行

```
python Mage2ONS.py -i <未展開データのパス> -o <出力先>
```

- `-i`：ゲームの `data.pak` / `updata.pak` / `bgm.pak` / `voice.pak` / `doko_op.mpg` が置かれたフォルダを指定します。
- `-o`：変換結果の出力先。省略時はカレントディレクトリ。
- `-i` を省略した場合は、`-o` の出力先に既に展開済みのデータがあるものとして変換のみ行います。

### モジュールとして利用（サブモジュール想定）

```python
import Mage2ONS

conv = Mage2ONS.main(
    values={'input_dir': '未展開データのパス'},
    values_ex={},
    pre_converted_dir='出力先のパス',
)

conv.conflicts   # 展開時に同名ファイルが競合し、後から展開したファイルで上書きされたものの一覧
conv.unreached   # シナリオ本文(s_で始まるラベル)のうち、開始地点から到達できなかったラベル一覧
```

`values` を空の辞書にすると展開処理はスキップされ、出力先に既にあるデータの変換のみ行われます。

## 処理の流れ

1. **リソース展開**（`extract_resource` / `extract_pak`）
   独自形式のpakファイルを `data → updata → bgm → voice` の順に展開します。同一パスのファイルが競合した場合は、後から展開したファイルで上書きされます（`conv.conflicts` で確認可能）。pak内のファイル展開はスレッドプールで並列実行し、高速化しています。
2. **シナリオ変換**（`Conv`）
   元のシナリオスクリプトをONScripter書式に変換し、ランタイム部分（タイトル画面・コンフィグ画面など）と結合して `0.txt` を生成します。生成後、ラベルの未定義参照や、開始地点からシナリオ全体へ到達できるかの簡易チェックを行います。
3. **画像加工**（`image_processing`）
   メッセージウィンドウ・名前枠・選択肢帯・時間帯別の立ち絵フィルタなどをPillowで加工します。
4. **不要データの削除**（`cleanup`）
   `0.txt` から参照されていない画像・音声や、変換・実行に不要なファイルを削除します。

## 未実装・簡略化した演出

- おまけ（CG/音楽モード等）は未実装
- 雪などの一部演出は未実装または簡略化
- 画面遷移はフェード系のみ

## 検証方法

`testspace` フォルダ（`pre_converted_dir` に相当）に ONScripter 本体（`ONScripter.exe` または `onsyuri_v0.7.4_amd64_win.exe`）と `default.ttf` を配置し、実際に起動してシナリオが最後まで途切れず読めるかを確認します。
