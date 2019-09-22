import setuptools
import glob

setuptools.setup(
  name="mecab-cygwin32",
  version="0.996.1",
  packages=setuptools.find_packages(),
  data_files=[
    ("local/bin",glob.glob("bin/*")),
    ("local/libexec/mecab",glob.glob("libexec/mecab/*")),
    ("local/lib",glob.glob("lib/*.*")),
    ("local/include",glob.glob("include/*")),
    ("local/share/man/man1",glob.glob("share/man/man1/*")),
    ("local/lib/mecab/dic/ipadic",glob.glob("lib/mecab/dic/ipadic/*"))
  ]
)
