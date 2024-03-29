import argparse
import pathlib


class Parser:
    # define parser
    parser = argparse.ArgumentParser(
        prog="image_label.py",
        argument_default=None,
        allow_abbrev=False
    )

    # add arguments to parser
    # --- required
    parser.add_argument(
        "--input-folder",
        type=pathlib.Path,
        action="store",
        required=True,
        help=":\033[96mfull path to folder\033[0m where to-be-processed images are stored."
    )
    parser.add_argument(
        "--output-folder",
        type=pathlib.Path,
        action="store",
        required=True,
        help=":\033[96mfull path to folder\033[0m where output images are stored."
    )

    # --- optional
    parser.add_argument(
        "--label-preview-color",
        type=str,
        action="store",
        required=False,
        help=":\033[96mcolor\033[0m of text printed on image preview."
    )
    parser.add_argument(
        "--label-preview-size",
        type=str,
        action="store",
        required=False,
        choices=['tiny', 'small', 'medium', 'large'],
        help=":\033[96msize\033[0m of text printed on image preview."
    )

    def __init__(self, arg_string) -> None:
        self.args = self.parser.parse_args(
            arg_string
        )

        # runtime parse checking
        # --- ensure hex value for color
        if self.args.label_preview_color:
            color = self.args.label_preview_color
            color = color.lstrip("#")
            if not color.isalnum() or len(color) != 6:
                self.parser.error(f"---> --label-preview-color=[{self.args.label_preview_color}]: \033[93m{self.args.label_preview_color}\033[0m is not a proper hex code.\n")
