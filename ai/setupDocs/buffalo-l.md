# buffalo_l Model Setup

This guide explains how to download and set up the `buffalo_l` face recognition model.

## Prerequisites

Complete the [Python Environment Setup](./python-environment.md) first.

Make sure the virtual environment is activated:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 1. Run the Model Setup Script

From the `ai` directory, run:

```powershell
python setup_buffalo_l_model.py
```

The script automatically:

1. Creates the `models` directory if it does not exist.
2. Creates the `models/buffalo_l` directory.
3. Downloads the official `buffalo_l` model package.
4. Extracts the required model files into `models/buffalo_l`.
5. Removes the downloaded ZIP file after successful extraction.
6. Skips the download if all required model files are already present.

## 2. Verify the Model Files

Run:

```powershell
Get-ChildItem .\models\buffalo_l
```

The directory should contain:

```text
models/
└── buffalo_l/
    ├── 1k3d68.onnx
    ├── 2d106det.onnx
    ├── det_10g.onnx
    ├── genderage.onnx
    └── w600k_r50.onnx
```

If all five files are present, the `buffalo_l` model has been successfully installed.

## Important

The `models/` directory is excluded from Git because the model files are large.

Do not manually add the model files to Git.

When setting up the project on a new machine, run:

```powershell
python setup_buffalo_l_model.py
```

to recreate the local model directory.

## Troubleshooting

If the download is interrupted or fails, run the setup script again:

```powershell
python setup_buffalo_l_model.py
```

The script will download the model again if the required model files are not all present.
