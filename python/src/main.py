import sys, os
from interpreter.scanner.scanner import Scanner

class Dexter:

    had_error = False

    def __init__(self):
        pass

    def start(self):
        if len(sys.argv) == 2:
            self._run_file(sys.argv[1])
        elif len(sys.argv) == 1:
            self._run_prompt()
        else:
            self._print_error()

    def _run_file(self, file_path:str):
        try:
            with open(file_path, 'r') as fp:
                self._run_interpreter(fp.read())
                if Dexter.had_error: sys.exit(65)
        except IOError:
            self._print_error(f"Unable to open file at path: {file_path}")
            sys.exit(1)

    def _run_prompt(self):
        while True:
            self._run_interpreter(input("> "))

    def _print_error(self, optional_error=None):
        if optional_error:
            print(f"\u001b[31m{optional_error}\u001b[0m")

    def _error(self, line:int, message:str):
        self._report(line, "", message)

    def _report(self, line:int, where:str, message:str):
        self._print_error(f"line {line} Error {where}: {message}")
        Dexter.had_error = True

    def _run_interpreter(self, code:str):
        scanner = Scanner(code)
        tokens = scanner.scan_tokens()
        for token in tokens:
            print(token)

if __name__ == '__main__':
    dexter = Dexter()
    dexter.start()
