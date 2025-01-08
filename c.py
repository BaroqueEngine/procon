import os
import sys


def write_numbered_file(content, directory):
    """
    指定されたディレクトリに、連番のファイル名で内容を書き込む。

    Args:
        content: 書き込む内容 (文字列)。
        directory: 書き込み先のディレクトリ (文字列)。
    """
    i = 0
    while True:
        filename = os.path.join(directory, f"{i}.py")
        if not os.path.exists(filename):
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"ファイル {filename} を作成しました。")
                return
            except Exception as e:
                print(f"ファイル書き込みエラー: {e}", file=sys.stderr)
                return
        i += 1


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python b.py <入力ファイル> <出力ディレクトリ>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = "abc/" + sys.argv[2].upper()

    if not os.path.exists(input_file):
        print(f"エラー: 入力ファイル {input_file} が存在しません。", file=sys.stderr)
        sys.exit(1)

    # 出力ディレクトリが存在しない場合は作成
    if not os.path.isdir(output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)  # exist_ok=True を追加
            print(f"ディレクトリ {output_dir} を作成しました。")
        except OSError as e:
            print(f"エラー: ディレクトリ {output_dir} の作成に失敗しました: {e}", file=sys.stderr)
            sys.exit(1)

    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            file_content = infile.read()
    except Exception as e:
        print(f"ファイル読み込みエラー: {e}", file=sys.stderr)
        sys.exit(1)

    write_numbered_file(file_content, output_dir)
    sys.exit(0)
