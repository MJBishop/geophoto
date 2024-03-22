"""
cli.py
"""

import argparse

from im2geojson.im2geojson import ImageToGeoJSON


def create_parser():
    parser = argparse.ArgumentParser(
        argument_default=argparse.SUPPRESS,
        prog='im2geojson',
        description='Parse GeoJSON from image metadata',
        # epilog='Text at the bottom of help'
        )
    parser.add_argument(
        'input_directory', 
        help='Set the path to the images to process', 
        type=str,
        )
    parser.add_argument(
        '-o', 
        '--output_directory', 
        help='Set the output path', 
        type=str
        )
    parser.add_argument(
        '-s', 
        '--save_images', 
        help='Save Images stripped of metadata', 
        action='store_true'
        )
    parser.add_argument(
        '-t', 
        '--save_thumbnails', 
        help='Save thumbnail images', 
        action='store_true'
        )
    return parser

def parse_args_to_dict(args):
    parser = create_parser()
    parsed_args = parser.parse_args(args)
    parsed_args_dict = vars(parsed_args)
    return parsed_args_dict

def main(args=None):
    parsed_args_dict = parse_args_to_dict(args)
    im2geo = ImageToGeoJSON(**parsed_args_dict)
    im2geo.start()
    print(im2geo.summary)
    print(im2geo.errors_or_none)


if __name__ == '__main__':
    main(args=None)                 # pragma: no cover