import pytest

from pro_filer.actions.main_actions import show_preview  # NOQA


@pytest.mark.parametrize(
    "context, output",
    [
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/__init__.py",
                ],
                "all_dirs": ["src", "src/utils"],
            },
            """Found 3 files and 2 directories
First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']
First 5 directories: ['src', 'src/utils']
""",
        ),
        (
            {
                "all_files": [],
                "all_dirs": [],
            },
            """Found 0 files and 0 directories
""",
        ),
    ],
)
def test_show_preview(context, output, capsys):
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == output
