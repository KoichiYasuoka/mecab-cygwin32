import setuptools
import glob
import os
if os.uname().sysname.startswith("CYGWIN") and os.uname().machine=="i686":
  pass
else:
  raise OSError("mecab-cygwin32 only for 32-bit Cygwin")

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
