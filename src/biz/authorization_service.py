# coding=utf-8

from biz.services.biz_service import BizServiceException, BizService
from utils.date_utils import DateUtils
from data.daos.study_dao import StudyDAO
from data.daos.user_dao import UserDAO



class AuthorizationServiceException(BizServiceException):
    pass


class AuthorizationService(BizService):

    """
    
    Service to manage the Authorization

    """
    def signup(self, signup_data):

        study = signup_data.get("study", None)
        email = signup_data.get("email", None)
        username = signup_data.get("username", None)
        password = signup_data.get("password", None)
        self._validate_signup_data(study, email, username, password)
        self._validate_study(study)
        user_dao = UserDAO()
        user = user_dao.get_user_by_email(email)
        created_datetime = DateUtils.get_datetime_utc()
        if not user:

            user = user_dao.create(username, email, password, study, created_datetime)
        else:
            user["studies"].append({"username": username, "password":password, "id":study, "created_datetime": created_datetime} )
            user_dao.save(user)
        #Create a record in User Linked to the Study
        #Creadentials per Study?
        return  {"message": "Signed up."}

    def _validate_study(self, study):
        study_dao = StudyDAO()
        study_obj = study_dao.get(study_id=study)
        limit = study_obj.max_limit

        user_dao = UserDAO()
        total_partipants = user_dao.count_users_in_study(study)  + 1 #Added the future participant
        if (total_partipants > limit):
            raise AuthorizationServiceException("The study '%s' has reached the limit of allowed participants."%study)

    def _validate_signup_data(self, study, email, username, password):
        errors = []
        if not study:
            errors.append("Missing study value")
        if not email:
            errors.append("Missing email value")
        if not username:
            errors.append("Missing username value")
        else:
            user_dao = UserDAO()
            users = user_dao.get_user_by_username(username)
            if users:
                errors.append("username taken")
        if not password:
            errors.append("Missing password value")

        if errors:
            raise AuthorizationServiceException(errors.join(", "))

    def signin(self, signin_data):
        study = signin_data.get("study", None)
        username = signin_data.get("username", None)
        password = signin_data.get("password", None)
        self._validate_signin_data(study, username, password)


    def _validate_signin_data(self, study, username, password):
        pass

    def consent(self, consent_data):
        pass