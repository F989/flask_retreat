from pathlib import Path
from flask import current_app
from uuid import uuid4
import shutil
from flask import Blueprint, jsonify

from pathlib import Path

images_blueprint = Blueprint('images_view', __name__)



@images_blueprint.route('/images_view/images')
def get_images():
    image_folder = Path(current_app.root_path) / 'static/images/pic2'
    images = [str(image.name) for image in image_folder.iterdir() if image.is_file()]
    return jsonify(images)




class ImageHandler:
    DEFAULT_IMAGE = "no-image.png"
    
    @staticmethod
    def get_image_folder():
        return Path(current_app.root_path) / "static/images/pic2"
    
    @staticmethod
    def get_backup_folder():
        return Path(current_app.root_path) / "static/images/backup_image"
    
    @staticmethod
    def save_image(image):
        if not image or image.filename == '':
            return None
        
        suffix = Path(image.filename).suffix
        if suffix not in ['.png', '.jpeg', '.jpg', '.gif']:
            raise ValueError("Unsupported file format")
        
        image_name = str(uuid4()) + suffix
        image_path = ImageHandler.get_image_folder() / image_name
        
        try:
            image.save(image_path)
        except Exception as e:
            raise IOError("Error saving image") from e
        
        return image_name

    @staticmethod
    def get_image_path(image_name):
        image_path = ImageHandler.get_image_folder() / image_name
        if not image_path.exists():
            image_path = ImageHandler.get_image_folder() / ImageHandler.DEFAULT_IMAGE
        return image_path

    @staticmethod
    def update_image(old_image_name, image):
        if not image or image.filename == '':
            return old_image_name 
        
        image_name = ImageHandler.save_image(image)
        ImageHandler.backup_image(old_image_name)
        return image_name
    
    @staticmethod
    def backup_image(image_name):
        if not image_name or image_name == ImageHandler.DEFAULT_IMAGE:
            return 
        
        image_path = ImageHandler.get_image_folder() / image_name
        if image_path.exists():
            try:
                # Make sure the backup folder exists
                backup_folder = ImageHandler.get_backup_folder()
                backup_folder.mkdir(parents=True, exist_ok=True)
                
                # Move the image to the backup folder
                backup_path = backup_folder / image_name
                shutil.move(str(image_path), str(backup_path))
            except Exception as e:
                raise IOError("Error backing up image") from e
    
    @staticmethod
    def delete_image(image_name):
        if not image_name or image_name == ImageHandler.DEFAULT_IMAGE:
            return 
        
        image_path = ImageHandler.get_image_folder() / image_name
        
        try:
            image_path.unlink(missing_ok=True)
        except Exception as e:
            raise IOError("Error deleting image") from e
        

    




  

