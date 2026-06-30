import uuid # for generating unique filenames. import uuid brings in Python's standard library module for generating universally unique identifiers (UUIDs)
from io import BytesIO # for working with image bytes in memory
from pathlib import Path # for working with files/file operations. This imports the Path class from Python's pathlib module, which is the standard library's modern, object-oriented way of working with filesystem paths 
# Once imported, Path lets you represent a file or directory location as an object and call methods on it directly, rather than passing strings around to separate functions

from PIL import Image, ImageOps # PIL hear is pillow. Image provides the main functionality and ImageOps provides some convenient Image Operations

# In main.py we already mount the media directory as static files
# So any file created there is accessible by our browser
PROFILE_PICS_DIR = Path("media/profile_pics")

# Note: Image processing is a CPU bound task
# Since our app is asynchronous, running a CPU bound task will halt the entire running program in order to execute this task
# Only after this CPU bound task is completed can the remaining functions proceed
# So we create the image processing function as a regular synchronous function and call it using run and thread pool
# this offloads it to a separate thread

# The below two functions are common image processing stuff and is how image processing is implemented in most systems

def process_profile_image(content: bytes) -> str:
    # Open the raw image bytes (e.g. from an upload) as a PIL Image.
    # BytesIO wraps the bytes in a file-like object since Image.open() expects
    # a file path or file-like object, not raw bytes.
    # The "with" block ensures the image file handle is properly closed afterward.
    with Image.open(BytesIO(content)) as original:

        # Some cameras/phones store images with an orientation tag (EXIF) instead
        # of physically rotating the pixels. exif_transpose() reads that tag and
        # actually rotates/flips the image so it displays right-side up everywhere,
        # then strips the orientation tag (since it's no longer needed).
        img = ImageOps.exif_transpose(original)

        # Resize and crop the image to exactly 300x300 pixels.
        # ImageOps.fit() scales the image to cover the target size, then crops
        # the overflow from the center, so the result is a perfect square
        # without distorting the aspect ratio. LANCZOS is a high-quality
        # resampling filter, good for downscaling photos.
        img = ImageOps.fit(img, (300, 300), method=Image.Resampling.LANCZOS)

        # JPEG doesn't support transparency (alpha channels) or palette mode.
        # RGBA = RGB + alpha, LA = grayscale + alpha, P = palette-based (e.g. GIFs/PNGs).
        # If the image is in any of these modes, convert it to plain RGB so it can
        # be saved as JPEG without errors (this also flattens transparency to opaque).
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGB")

        # Generate a random, collision-resistant filename using a UUID.
        # .hex gives the UUID as a plain hex string with no dashes (e.g. "3f29c6a2...").
        # This avoids using user-supplied filenames (security) and avoids collisions.
        filename = f"{uuid.uuid4().hex}.jpg"

        # Build the full filesystem path by joining the target directory with
        # the generated filename (PROFILE_PICS_DIR is presumably a Path object
        # defined elsewhere, pointing to where profile pictures are stored).
        filepath = PROFILE_PICS_DIR / filename

        # Make sure the destination directory exists before saving into it.
        # parents=True creates any missing parent directories too.
        # exist_ok=True prevents an error if the directory already exists.
        PROFILE_PICS_DIR.mkdir(parents=True, exist_ok=True)

        # Save the processed image to disk as a JPEG.
        # quality=85 is a good balance between file size and visual quality.
        # optimize=True tells PIL to spend extra effort producing a smaller file size.
        img.save(filepath, "JPEG", quality=85, optimize=True)

    # Return just the filename (not the full path) so the caller can store/reference
    # it (e.g. save it in a database record) without leaking the full server path.
    return filename


def delete_profile_image(filename: str | None) -> None:
    # If there's no filename (e.g. the user never had a profile picture),
    # there's nothing to delete, so exit early.
    if filename is None:
        return

    # Reconstruct the full path to the file on disk from the directory + filename.
    filepath = PROFILE_PICS_DIR / filename

    # Only attempt deletion if the file actually exists, to avoid raising
    # an error if it was already deleted or never existed.
    if filepath.exists():
        filepath.unlink()  # unlink() is pathlib's method for deleting a file.