from models.vacation_model import VacationModel
from logic.vacation_logic import VacationLogic
from flask import request
from models.client_error import *

class VacationFacade:

    def __init__(self):
        self.logic = VacationLogic()

    def get_all_vacation_ordered_by_date(self):
        return self.logic.get_all_vacation_ordered_by_date()

    def get_one_vacation(self, vacationId):
        vacation = self.logic.get_one_vacation(vacationId)
        if not vacation:
            raise ResourceNotFoundError(vacationId)
        return vacation

    def add_new_vacation(self):
        v_description = request.form.get("v_description")
        StartDay = request.form.get("StartDay")
        LastDay = request.form.get("LastDay")
        price = request.form.get("price")
        image = request.files.get("image")
        countryId = request.form.get("countryId")

        vacation = VacationModel(None, v_description, StartDay, LastDay, price, image, countryId, None)
        error = vacation.validate_insert()
        if error:
            raise ValidationError(error)

        vacationId = self.logic.add_new_vacation(vacation)
        return f"Vacation successfully created \nVacation ID = {vacationId}"

    def update_vacation(self):
        vacationId = request.form.get("vacationId")
        v_description = request.form.get("v_description")
        StartDay = request.form.get("StartDay")
        LastDay = request.form.get("LastDay")
        price = request.form.get("price")
        image = request.files.get("image")
        countryId = request.form.get("countryId")

        vacation = VacationModel(vacationId, v_description, StartDay, LastDay, price, image, countryId, None)
        error = vacation.validate_edit()
        if error:
            raise ValidationError(error)

        self.logic.update_vacation(vacation)
        return f"Vacation successfully updated \nVacation ID = {vacationId}"

    def delete_vacation(self, vacationId):
        if not vacationId or not str(vacationId).isnumeric():
            raise TypeError("Vacation ID must be numeric.")
        if self.logic.vacationId_not_in_system(vacationId):
            raise ValueError("Vacation ID does not exist.")

        self.logic.delete_vacation(vacationId)
        return f"Vacation successfully deleted \nVacation ID = {vacationId}"

    def get_all_countries(self):
        return self.logic.get_all_countries()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.logic.close()

