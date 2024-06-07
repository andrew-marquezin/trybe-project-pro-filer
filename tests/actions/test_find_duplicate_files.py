import pytest

from pro_filer.actions.main_actions import find_duplicate_files  # NOQA

"""percorrer os dados recebidos usando a funcao que compara o conteudo
e tuplar os pares que retornem true

mas sem for aninhado?"""


def test_dont_find_duplicate_files(tmp_path):
    dir = tmp_path / "dir"
    dir.mkdir()
    file1 = dir / "Aatrox.txt"
    file1.write_text("I am not a king, I am not a god, I am... worse...")
    file2 = dir / "Yorick.txt"
    file2.write_text("All things fade... but me.")

    context = {"all_files": [str(file1), str(file2)]}

    assert find_duplicate_files(context) == []


def test_find_duplicate_files(tmp_path):
    dir = tmp_path / "dir"
    dir.mkdir()
    file1 = dir / "file.txt"
    file1.write_text("")
    file2 = dir / "same_file.txt"
    file2.write_text("")

    context = {"all_files": [str(file1), str(file2)]}

    assert find_duplicate_files(context) == [(str(file1), str(file2))]


def test_find_inexistent_files(tmp_path):
    dir = tmp_path / "dir"
    dir.mkdir()
    file1 = dir / "file.txt"
    file2 = dir / "same_file.txt"
    file2.write_text("")

    context = {"all_files": [str(file1), str(file2)]}

    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)
