import os
import datetime

from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details(tmp_path, capsys):
    file_name = "banana.png"
    file_path = tmp_path / file_name
    file_path.touch()
    context = {"base_path": str(file_path)}
    _, file_extension = os.path.splitext(file_name)
    mod_date = datetime.date.fromtimestamp(os.path.getmtime(file_path))

    show_details(context)
    captured = capsys.readouterr()

    assert captured.out == (
        f"File name: {file_name}\n"
        f"File size in bytes: {os.path.getsize(file_path)}\n"
        f"File type: {'directory' if os.path.isdir(file_path) else 'file'}\n"
        f"File extension: {file_extension or '[no extension]'}\n"
        f"Last modified date: {mod_date}\n"
    )


def test_inexistent_file(capsys):
    context = {"base_path": "/home/trybe/????"}

    show_details(context)
    captured = capsys.readouterr()

    assert captured.out == "File '????' does not exist\n"
