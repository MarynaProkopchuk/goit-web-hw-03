
import argparse
from pathlib import Path
import shutil
import concurrent.futures

parser = argparse.ArgumentParser(description="Sorting folders")
parser.add_argument("--from_folder", "-f", required=True)
parser.add_argument("--to_folder", "-t", default="dist1")

args = parser.parse_args()

source = Path(args.from_folder)
output = Path(args.to_folder)

folders = []

def grabs_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)
    
def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext_folder = output / (el.suffix[1:])
            ext_folder.mkdir(exist_ok=True, parents=True)
            shutil.copy(el, ext_folder / el.name)


if __name__ == "__main__":
    folders.append(source)
    grabs_folder(source)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(copy_file, folders)