from pathlib import Path
import hashlib
import shutil
import urllib.request
import zipfile


# Project paths
BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"
BUFFALO_DIR = MODELS_DIR / "buffalo_l"
ZIP_PATH = MODELS_DIR / "buffalo_l.zip"


# Official InsightFace buffalo_l release
MODEL_URL = (
    "https://github.com/deepinsight/insightface"
    "/releases/download/v0.7/buffalo_l.zip"
)

# SHA-256 of the official buffalo_l.zip
EXPECTED_SHA256 = (
    "80ffe37d8a5940d59a7384c201a2a38d4741f2f3c51eef46ebb28218a7b0ca2f"
)

REQUIRED_FILES = [
    "1k3d68.onnx",
    "2d106det.onnx",
    "det_10g.onnx",
    "genderage.onnx",
    "w600k_r50.onnx",
]


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def model_is_installed():
    return all(
        (BUFFALO_DIR / filename).is_file()
        for filename in REQUIRED_FILES
    )


def main():
    # Create models/ and buffalo_l/ automatically
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    BUFFALO_DIR.mkdir(parents=True, exist_ok=True)

    # Don't download again if the model is already complete
    if model_is_installed():
        print("buffalo_l is already installed.")
        print(f"Location: {BUFFALO_DIR}")
        return

    print("Downloading buffalo_l...")
    print("This is approximately 326 MB.")

    try:
        urllib.request.urlretrieve(MODEL_URL, ZIP_PATH)
    except Exception:
        if ZIP_PATH.exists():
            ZIP_PATH.unlink()
        raise

    print("Verifying download...")

    actual_sha256 = calculate_sha256(ZIP_PATH)

    if actual_sha256 != EXPECTED_SHA256:
        ZIP_PATH.unlink(missing_ok=True)
        raise RuntimeError(
            "Downloaded buffalo_l.zip failed SHA-256 verification.\n"
            f"Expected: {EXPECTED_SHA256}\n"
            f"Actual:   {actual_sha256}"
        )

    print("Download verified.")

    print("Extracting buffalo_l...")

    # Extract to a temporary directory first.
    temp_dir = MODELS_DIR / "buffalo_l_temp"

    if temp_dir.exists():
        shutil.rmtree(temp_dir)

    temp_dir.mkdir()

    try:
        with zipfile.ZipFile(ZIP_PATH, "r") as zip_file:
            for member in zip_file.infolist():
                if member.is_dir():
                    continue

                filename = Path(member.filename).name

                if filename in REQUIRED_FILES:
                    destination = temp_dir / filename

                    with zip_file.open(member) as source:
                        with open(destination, "wb") as target:
                            shutil.copyfileobj(source, target)

        # Verify all expected model files were extracted
        if not all(
            (temp_dir / filename).is_file()
            for filename in REQUIRED_FILES
        ):
            raise RuntimeError(
                "Extraction failed: one or more buffalo_l model files "
                "are missing."
            )

        # Replace the final model directory only after successful extraction
        if BUFFALO_DIR.exists():
            shutil.rmtree(BUFFALO_DIR)

        temp_dir.rename(BUFFALO_DIR)

    except Exception:
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        raise

    finally:
        ZIP_PATH.unlink(missing_ok=True)

    print()
    print("buffalo_l installed successfully.")
    print(f"Location: {BUFFALO_DIR}")


if __name__ == "__main__":
    main()