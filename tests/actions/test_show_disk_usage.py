import os

from pro_filer.cli_helpers import _get_printable_file_path
from pro_filer.actions.main_actions import show_disk_usage  # NOQA


def test_show_disk_usage(tmp_path, capsys):
    dir = tmp_path / "dir"
    dir.mkdir()
    file1 = dir / "Aatrox.txt"
    file1.write_text("I am not a king, I am not a god, I am... worse...")
    file2 = dir / "Yorick.txt"
    file2.write_text("All things fade... but me.")

    context = {"all_files": [str(file1), str(file2)]}

    show_disk_usage(context)
    file_size1 = os.path.getsize(str(file1))
    file_size2 = os.path.getsize(str(file2))
    total_size = sum((file_size1, file_size2))
    percentage_file1 = int(file_size1 / total_size * 100)
    percentage_file2 = int(file_size2 / total_size * 100)

    captured = capsys.readouterr()
    assert captured.out == (
        f"'{_get_printable_file_path(str(file1))}':        " +
        f"{os.path.getsize(str(file1))} ({percentage_file1}%)\n"
        f"'{_get_printable_file_path(str(file2))}':        " +
        f"{os.path.getsize(str(file2))} ({percentage_file2}%)\n"
        f"Total size: {total_size}\n"
    )
