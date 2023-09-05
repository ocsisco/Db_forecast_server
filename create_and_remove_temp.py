import os


def remove_temp_files():
            
    for file in os.listdir("/tmp/images/"):
        os.remove(os.path.join("/tmp/images/",file))

    for file in os.listdir("/tmp/images_color/"):
        os.remove(os.path.join("/tmp/images_color/",file))

    for file in os.listdir("/tmp/images_small/"):
        os.remove(os.path.join("/tmp/images_small/",file))

    for file in os.listdir("/tmp/static/"):
        os.remove(os.path.join("/tmp/static/",file))


def create_temp_folders():

    os.makedirs('/tmp/images/', exist_ok=True)
    os.makedirs('/tmp/images_color/', exist_ok=True)
    os.makedirs('/tmp/images_small/', exist_ok=True)
    os.makedirs('/tmp/static/', exist_ok=True)


def delete_temp_folders():

    os.rmdir('/tmp/images/')
    os.rmdir('/tmp/images_color/')
    os.rmdir('/tmp/images_small/')
    os.rmdir('/tmp/static/')
