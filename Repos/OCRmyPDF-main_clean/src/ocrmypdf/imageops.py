                                              
                                  

"""OCR-related image manipulation."""

from __future__ import annotations

import logging
from math import floor, sqrt

from PIL import Image

log = logging.getLogger(__name__)


def bytes_per_pixel(mode: str) -> int:
           
    if mode in ('1', 'L', 'P'):
        return 1
    if mode in ('LA', 'PA', 'La') or mode.startswith('I;16'):
        return 2
    return 4


def _calculate_downsample(
    image_size: tuple[int, int],
    bytes_per_pixel: int,
    *,
    max_size: tuple[int, int] | None = None,
    max_pixels: int | None = None,
    max_bytes: int | None = None,
) -> tuple[int, int]:
           
    size = image_size

    if max_size is not None:
        overage = max_size[0] / size[0], max_size[1] / size[1]
        size_factor = min(overage)
        if size_factor < 1.0:
            log.debug("Resizing image to fit image dimensions limit")
            size = floor(size[0] * size_factor), floor(size[1] * size_factor)
            if size[0] == 0:
                size = 1, min(size[1], max_size[1])
            elif size[1] == 0:
                size = min(size[0], max_size[0]), 1

    if max_pixels is not None:
        if size[0] * size[1] > max_pixels:
            log.debug("Resizing image to fit image pixel limit")
            pixels_factor = sqrt(max_pixels / (size[0] * size[1]))
            size = floor(size[0] * pixels_factor), floor(size[1] * pixels_factor)

    if max_bytes is not None:
        bpp = bytes_per_pixel
                                 
        stride = size[0] * bpp
        height = size[1]
        if stride * height > max_bytes:
            log.debug("Resizing image to fit image byte size limit")
            bytes_factor = sqrt(max_bytes / (stride * height))
            scaled_stride = floor(stride * bytes_factor)
            scaled_height = floor(height * bytes_factor)
            if scaled_stride == 0:
                scaled_stride = bpp
                scaled_height = min(max_bytes // bpp, scaled_height)
            if scaled_height == 0:
                scaled_height = 1
                scaled_stride = min(max_bytes // scaled_height, scaled_stride)
            size = floor(scaled_stride / bpp), scaled_height

    return size


def calculate_downsample(
    image: Image.Image,
    *,
    max_size: tuple[int, int] | None = None,
    max_pixels: int | None = None,
    max_bytes: int | None = None,
) -> tuple[int, int]:
           
    return _calculate_downsample(
        image.size,
        bytes_per_pixel(image.mode),
        max_size=max_size,
        max_pixels=max_pixels,
        max_bytes=max_bytes,
    )


def downsample_image(
    image: Image.Image,
    new_size: tuple[int, int],
    *,
    resample_mode: Image.Resampling = Image.Resampling.BICUBIC,
    reducing_gap: int = 3,
) -> Image.Image:
           
    if new_size == image.size:
        return image

    original_size = image.size
    original_dpi = image.info['dpi']
    image = image.resize(
        new_size,
        resample=resample_mode,
        reducing_gap=reducing_gap,
    )
    image.info['dpi'] = (
        round(original_dpi[0] * new_size[0] / original_size[0]),
        round(original_dpi[1] * new_size[1] / original_size[1]),
    )
    log.debug(f"Rescaled image to {image.size} pixels and {image.info['dpi']} dpi")
    return image
