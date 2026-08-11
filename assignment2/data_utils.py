import os
import ssl
import sys
import tarfile
import urllib.request
from pathlib import Path

# Bypass SSL certificate verification for legacy academic servers
ssl._create_default_https_context = ssl._create_unverified_context

# Target directory: assignment2/cs231n/datasets/
BASE_DIR = Path(__file__).parent / "cs231n" / "datasets"
BASE_DIR.mkdir(parents=True, exist_ok=True)

cifar_folder = BASE_DIR / "cifar-10-batches-py"
tar_file = BASE_DIR / "cifar-10-python.tar.gz"
imagenet_file = BASE_DIR / "imagenet_val_25.npz"


def show_progress(block_num, block_size, total_size):
    """Callback to display download progress in real-time."""
    downloaded = block_num * block_size
    if total_size > 0:
        percent = min(100.0, downloaded / total_size * 100)
        downloaded_mb = downloaded / (1024 * 1024)
        total_mb = total_size / (1024 * 1024)
        progress_bar = "=" * int(percent // 4) + ">"
        sys.stdout.write(
            f"\r  [{progress_bar:<25}] {percent:5.1f}% ({downloaded_mb:.1f}/{total_mb:.1f} MB)"
        )
    else:
        downloaded_mb = downloaded / (1024 * 1024)
        sys.stdout.write(f"\r  Downloaded {downloaded_mb:.1f} MB")
    sys.stdout.flush()


if not cifar_folder.exists():
    print(f"[*] Downloading CIFAR-10 to {BASE_DIR}...")
    urllib.request.urlretrieve(
        "http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz",
        tar_file,
        reporthook=show_progress,
    )
    print("\n[*] Extracting CIFAR-10 archive...")
    with tarfile.open(tar_file, "r:gz") as tar:
        tar.extractall(path=BASE_DIR)

    if tar_file.exists():
        os.remove(tar_file)

    print("[*] Downloading ImageNet validation subset...")
    urllib.request.urlretrieve(
        "http://cs231n.stanford.edu/imagenet_val_25.npz",
        imagenet_file,
        reporthook=show_progress,
    )
    print("\n[+] Dataset setup completed successfully!")
else:
    print(f"[=] Datasets already present in {BASE_DIR}")