import argparse
import codecs
import os
import sys


def change_encoding(source_dir, source_encoding, target_encoding, file_extensions):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(tuple(file_extensions)):
                file_path = os.path.join(root, file)
                with codecs.open(
                    file_path, "r", encoding=source_encoding
                ) as source_file:
                    content = source_file.read()
                with codecs.open(
                    file_path, "w", encoding=target_encoding
                ) as target_file:
                    target_file.write(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Change encoding of files in a directory."
    )
    parser.add_argument("source_dir", help="The directory containing the files.")
    parser.add_argument("source_encoding", help="The current encoding of the files.")
    parser.add_argument("target_encoding", help="The target encoding for the files.")
    parser.add_argument(
        "--file_extensions",
        nargs="+",
        default=[".txt", ".md", ".html"],
        help="List of file extensions to process. Default: .txt, .md, .html",
    )

    args = parser.parse_args()
    change_encoding(
        args.source_dir,
        args.source_encoding,
        args.target_encoding,
        args.file_extensions,
    )
