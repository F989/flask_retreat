from flask import Blueprint
from flask import jsonify
images_blueprint = Blueprint('images_view', __name__)


@images_blueprint.route('/images_view/images')
def get_images():
    images = [
    
         
        '79cf16c2-82a4-4f8a-a0cb-8a5c84ad98f0.png', 
        "88f68046-be49-433b-afb3-d48c713d3350.jpg",
        "ae956b7e-ebb7-444e-bde9-3369ce150387.jpg",
        "c3f00752-efea-4018-b084-f20495845def.jpg",
        # "f0c4fa11-9ab3-4d36-b4e1-c0a09ac642c8.jpg",
        "29c3ce67-236e-41ca-8b96-9016fa59a8b3.jpg",
        "a532bf4c-4bbd-483f-93b1-c041c0e536ad.jpg"
        # "f0c4fa11-9ab3-4d36-b4e1-c0a09ac642c8.jpg"
       
       
        
    ]
    return jsonify(images)

