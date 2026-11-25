import os


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    glyph = "🐙"
    with open(entry_path, "wb") as handle:
        handle.write(glyph.encode("utf-8"))


if __name__ == "__main__":
    main()
