# WebP to PNG

A small Tkinter desktop app that converts a WebP image to PNG using Pillow. Converted files are saved in the current user's Downloads folder.

## Features

- Native file picker restricted to WebP images
- Preserves the source filename while changing the extension to `.png`
- Creates the Downloads folder when it does not exist
- Shows clear messages for missing selections and conversion failures
- Requires only Pillow; no separate `webp` package is needed

## Requirements

- Python 3
- Tkinter (included with most standard Python installations)
- Pillow

## Installation

```bash
git clone https://github.com/Sequence9/WEBP-to-PNG.git
cd WEBP-to-PNG
python -m pip install Pillow
```

## Run

```bash
python "webp to png/webp_to_png.py"
```

## Usage

1. Click **Select File** and choose a `.webp` image.
2. Click **Convert**.
3. Find the converted PNG in your Downloads folder.

If a PNG with the same name already exists in Downloads, the app asks before replacing it. Choose **No** to keep the existing file.
