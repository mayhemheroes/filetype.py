#! /usr/bin/python3

import atheris
import sys
import tempfile

with atheris.instrument_imports():
    import filetype

def TestOneInput(data):
    f = tempfile.NamedTemporaryFile()
    f.write(data)
    f.flush()
    try:
        filetype.guess(f.name)
    except TypeError as e:
        if 'Unsupported type' in str(e):
            return -1
        else:
            raise

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
