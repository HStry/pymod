"argparse patches"

__all__ = ['argparse']

import argparse

def _exit(self: argparse.ArgumentParser,
          status: int = 0,
          message: None | str = None) -> None:
    if message:
        self._print_message(message, argparse._sys.stderr)
    if status and self.exit_on_error:
        argparse._sys.exit(status)

def _fmt_invoc(self: argparse.HelpFormatter,
               action: argparse.Action) -> str:
    if not action.option_strings:
        default = self._get_default_metavar_for_positional(action)
        metavar, = self._metavar_formatter(action, default)(1)
        return metavar

    else:
        # if the Optional doesn't take a value, format is:
        #    -s, --long
        # if it does, the format is:
        #    -s, --long ARGS
        invoc = ', '.join(action.option_strings)
        
        if action.nargs == 0:
            return invoc
        
        mvar = self._get_default_metavar_for_optional(action)
        return f"{invoc} {self._format_args(action, mvar)}"

argparse.ArgumentParser.exit = _exit
argparse.HelpFormatter._format_action_invocation = _fmt_invoc
