"""This script can be used to ensure consistency of YAML frontmatter in markdown files."""

from pathlib import Path


TEXT_TO_BE_REPLACED = 'Company: Inter IKEA Systems B.V.'
TEXT_TO_REPLACE_WITH = 'Company: "[[Inter IKEA Systems B.V.]]"\nFY: "[[FY26]]"'
EXTENSION_FILTER = "md"
EXTENSION_FILTER = EXTENSION_FILTER.lstrip(".")


def replace_text_in_frontmatter(content: str, old_text: str, new_text: str) -> str:
    separator = "---\r\n" if content.startswith("---\r\n") else "---\n"

    if not content.startswith(separator):
        return content

    parts = content.split(separator, 2)

    if len(parts) < 3:
        return content

    frontmatter = parts[1]
    body = parts[2]

    updated_frontmatter = frontmatter.replace(old_text, new_text)

    return f"{separator}{updated_frontmatter}{separator}{body}"
    

def replace_text_in_md_files(folder: Path, old_text: str, new_text: str) -> None:
    if not folder.exists():
        raise FileNotFoundError(f"Folder does not exist: {folder}")

    if not folder.is_dir():
        raise NotADirectoryError(f"Path is not a folder: {folder}")

    changed_files = 0

    for file_path in folder.rglob(f"*.{EXTENSION_FILTER}"):
        original_content = file_path.read_text(encoding="utf-8")

        updated_content = original_content.replace(old_text, new_text)

        if updated_content != original_content:
            file_path.write_text(updated_content, encoding="utf-8")
            changed_files += 1
            print(f"Updated: {file_path}")

    print(f"Done. Updated {changed_files} file(s).")


def get_folder() -> Path:
    folder = Path(input("Enter folder to scan: "))
    
    if not folder.exists():
        raise FileNotFoundError(f"Folder does not exist: {folder}")

    if not folder.is_dir():
        raise NotADirectoryError(f"Path is not a folder: {folder}")

    return folder


if __name__ == "__main__":
    raise NotImplemented("#TODO. NOT COMPLETED!!!")
    folder = get_folder()
    replace_text_in_md_files(
        folder=folder,
        old_text=TEXT_TO_BE_REPLACED,
        new_text=TEXT_TO_REPLACE_WITH,
    )
