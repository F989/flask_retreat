class LikeModel :

    def __init__(self,vacationId,userId):
            self.userId = userId
            self.vacationId = vacationId
            

    def __str__(self):
         return  (f"userId: {self.userId } vacationId: {self.vacationId} " )

    
    @staticmethod
    def dictionary_to_like(dictionary):
        if dictionary is None:
            return None
        vacationId = dictionary.get("vacationId")
        userId =  dictionary.get("userId")
        like = LikeModel(userId , vacationId,)
        return like



    @staticmethod
    def dictionaries_to_likes(list_of_dictionary):
        likes = [ ]
        for item in list_of_dictionary:
            like = LikeModel.dictionary_to_like(item)
            likes.append(like)
        return likes