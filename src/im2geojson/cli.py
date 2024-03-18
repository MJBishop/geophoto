"""
cli
"""

import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog='im2geojson',
        description='Geojson from image metadata',
        epilog='Text at the bottom of help')
    
    parser.add_argument('-i', '--in_path', help='The path to images', type=str)

    return parser