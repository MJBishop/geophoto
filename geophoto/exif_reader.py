'''

'''
from exif import Image
from geophoto.dms_conversion import dms_to_decimal
from datetime import datetime


def read_exif(image_file):
    '''
    
    '''
    image = Image(image_file)
    if not image.has_exif:
        # print(f'KeyError: No metadata in file {image_file.name}')
        raise KeyError(f'KeyError: No metadata in file {image_file.name}')


    # coord
    try:
        lat = dms_to_decimal(*image.gps_latitude, image.gps_latitude_ref)
        long = dms_to_decimal(*image.gps_longitude, image.gps_longitude_ref)
    except AttributeError as e:
        # print(f'AttributeError: Missing metadata, {e} in file {image_file.name}')
        raise e
    except ValueError as e:
        print(f'{e}, in file {image_file.name}')
        raise e
    
    coord = (lat, long)
    

    # props : datetime
    try:
        datetime_object = datetime.strptime(image.datetime_original, '%Y:%m:%d %H:%M:%S')
    except AttributeError as e:
        # print(f'AttributeError: Missing metadata, {e} in file {image_file.name}')
        raise e
    except ValueError as e:
        # print(f'ValueError: {e}, in file {image_file.name}')
        raise e

    props = { "datetime": str(datetime_object) }


    # thumb
    thumb_f = image.get_thumbnail()

    return coord, props, thumb_f