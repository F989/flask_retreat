from flask import Blueprint, render_template, send_file,redirect,url_for,session,request,jsonify
from facades.vacation_facade import VacationFacade 
from models.client_error import * 
from facades.auth_facade import * 
from models.role_model import * 
from utils.image_handler import ImageHandler
from flask import Flask, render_template, request
import jinja2
from models.vacation_model import VacationModel
from facades.like_facade import LikeFacade  






vacations_blueprint = Blueprint("vacations_view", __name__)
facade = VacationFacade()
auth_facade = AuthFacade()
like_facade = LikeFacade()

@vacations_blueprint.route("/")
@vacations_blueprint.route("/vacations")



def list():
    user = session.get("current_user")
    all_vacations = facade.get_all_vacation_ordered_by_date()

    for vacation in all_vacations:
        print(f"Vacation ID: {vacation['vacationId']}, Like Count: {vacation['like_count']}")
    
    return render_template("vacations.html", vacations=all_vacations, active="vacations", current_user=user)


   

@vacations_blueprint.route("/first_project/details/<int:id>")
def details(id):
    facade =  VacationFacade()
    try:
        one_vacation = facade.get_one_vacation(vacationId=id)
        return render_template("vacations_details.html", vacation=one_vacation,active="details", current_user = session.get('current_user'), admin=RoleModel.Admin.value)
    except ResourceNotFoundError as err:
        return render_template("404.html", error=err.message)



@vacations_blueprint.route("/static/images/pic2/<string:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    return send_file(image_path)





@vacations_blueprint.route("/first_project/new", methods=['GET', 'POST'])
def insert():
    try:
        auth_facade.block_anonymous()
        auth_facade.block_non_admin()
        if request.method == "GET":
            countries = facade.get_all_countries()
            
            return render_template("vacations_insert.html", active="new", countries=countries, vacation=None)
        
        facade.add_new_vacation()
        return redirect(url_for("vacations_view.list"))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error=err.message, credentials={}))
    except ValidationError as err:
        countries = facade.get_all_countries()
        
        return render_template("vacations_insert.html", error=err.message, countries=countries, vacation=None)
   

    



@vacations_blueprint.route("/first_project/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    user = session.get('current_user')
    print(f"Current user in edit: {user}")
    try:
        auth_facade.block_non_admin()
        if request.method == "GET":
            one_vacation = facade.get_one_vacation(vacationId=id)
            countries = facade.get_all_countries()
            print("Countries fetched:", countries)
            return render_template("vacations_edit.html", vacation=one_vacation, countries=countries, current_user=user)
        facade.update_vacation()
        return redirect(url_for("vacations_view.list"))
    except AuthError as err:
        all_vacations = facade.get_all_vacation_ordered_by_date()
        return render_template("vacations.html", error=err.message, vacations=all_vacations, current_user=user)
    except ValidationError as err:
        one_vacation = facade.get_one_vacation(vacationId=id)
        return render_template("vacations_edit.html", error=err.message, vacation=one_vacation, current_user=user)


       

     
@vacations_blueprint.route("/first_project/delete/<int:id>")
def delete(id):
    try:
        auth_facade.block_non_admin()
        facade.delete_vacation(vacationId=id)
        return redirect(url_for("vacations_view.list"))
    except AuthError as err:
        all_vacations = facade.get_all_vacation_ordered_by_date() 
        return render_template("vacations.html", error=err.message, vacations=all_vacations, current_user=session.get('current_user'))



@vacations_blueprint.route('/vacations/add_like/<int:vacationId>/', methods=['POST'])
def add_like(vacationId):
    data = request.get_json()  
    userId = data.get('userId') if data else None  
    auth_facade.block_admin()
    if userId is None:
        return jsonify({"message": "User ID is missing"}), 400 
    
    like_count = like_facade.add_user_like(userId, vacationId)
    
    if like_count is not None:
        return jsonify({"success": True, "message": "Like added successfully", "likeCount": like_count}), 200
    # else:
    #     return jsonify({"success": False, "message": "Failed to add like"}), 500
    



@vacations_blueprint.route('/vacations/remove_like/<int:vacationId>/', methods=['POST'])
def remove_like(vacationId):
    data = request.get_json()
    userId = data.get('userId') if data else None
    auth_facade.block_admin()
    if userId is None:
        return jsonify({"message": "User ID is missing"}), 400

    like_count = like_facade.remove_user_like(userId, vacationId)

    # if like_count >=0:
        
    return jsonify({'success': True, 'likeCount': like_count, 'message': 'Like removed successfully'}), 200
    # else:
    #     return jsonify({"message": "Failed to remove like"}), 500
    

    


@vacations_blueprint.route('/images_view', methods=['GET'])
def get_all_images():
    try:
        images = ImageHandler.get_all_images()  
        return jsonify(images)
    except Exception as e:
        return jsonify({'error': str(e)}), 500




