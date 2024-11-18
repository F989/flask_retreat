import re
class VacationModel:
    def __init__(self, vacationId, v_description, StartDay, LastDay, price, image, countryId, country=None, like_count=0):
        self.vacationId = vacationId
        self.v_description = v_description
        self.StartDay = StartDay
        self.LastDay = LastDay
        self.price = price
        self.image = image
        self.country = country  
        self.countryId = countryId  
        self.like_count = like_count  

    def __str__(self):
        return (f"vacationId: {self.vacationId}  v_description: {self.v_description} StartDay: {self.StartDay} "
                f"LastDay: {self.LastDay} price: {self.price} image: {self.image} country: {self.country} "
                f"countryId: {self.countryId} like_count: {self.like_count}")  

    @staticmethod
    def dictionary_to_vacations(dictionary):
        if dictionary is None:
            return None
        vacationId = dictionary.get("vacationId")
        v_description = dictionary.get("v_description")
        StartDay = dictionary.get("StartDay")
        LastDay = dictionary.get("LastDay")
        price = dictionary.get("price")
        image = dictionary.get("image")
        country =  dictionary.get("country")
        countryId =  dictionary.get("countryId")
        like_count = dictionary.get("like_count", 0)  
        vacation = VacationModel(vacationId, v_description, StartDay, LastDay, price, image, countryId, country, like_count)
        return vacation

    @staticmethod
    def dictionaries_to_vacations(list_of_dictionary):
        vacations = []
        for item in list_of_dictionary:
            vacation = VacationModel.dictionary_to_vacations(item)
            vacations.append(vacation)
        return vacations

    def validate_insert(self):
        if not self.v_description or len(self.v_description) > 255:
            return "v_description must be 1-255 characters"
        if not self.StartDay or not re.match(r'\d{4}-\d{2}-\d{2}', self.StartDay):
            return "StartDay must be in the format YYYY-MM-DD"
        if not self.LastDay or not re.match(r'\d{4}-\d{2}-\d{2}', self.LastDay):
            return "LastDay must be in the format YYYY-MM-DD"
        if self.StartDay > self.LastDay:
            return "StartDay must be before or equal to LastDay"
        if not self.price or not re.match(r'^\d+(\.\d{1,2})?$', self.price):
            return "price must be a number and can include up to two decimal places"
        if float(self.price) <= 0 or float(self.price) >= 10000:
            return "price must be between 0 and 10000"
        if not self.image:
            return "missing image"
        if not self.countryId or not str(self.countryId).isnumeric():
            return "countryId must be numeric"
        return None

    def validate_edit(self):
        if not self.vacationId or not str(self.vacationId).isnumeric():
            return "vacationId must be numeric"
        return self.validate_insert()  


