from pathlib import Path

text_path = Path(__file__).resolve().parent.parent / "DeppendMessageText" / "text.txt"

print(text_path.read_text(encoding="utf-8"))