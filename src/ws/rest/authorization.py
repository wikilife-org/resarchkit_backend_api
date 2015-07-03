# coding=utf-8


from ws.rest.base_handler import BaseHandler
from ws.utils.oauth import authenticated, userless, catch_exceptions
from utils.parsers.json_parser import JSONParser
from biz.authorization_service import AuthorizationService


class SignUpHandler(BaseHandler):

    """
    study     String     The study identifier under which the user is creating an account
    email     String     Cannot be change once created
    username     String
    password     String     Constrains for an acceptable password can be set per study.
    type     String     "SignUp"
    """
    @userless
    @catch_exceptions
    def post(self):
        sign_up_data = JSONParser.to_collection(self.request.body)
        serv = AuthorizationService()
        result = serv.signup(sign_up_data)
        self.success(response=result)


class SignInHandler(BaseHandler):
    """
    study     String     The identifier for the study under which the user is signing in
    username     String     
    password     String     
    type     String     "SignIn"
    """
    @userless
    @catch_exceptions
    def post(self):
        sign_in_data = JSONParser.to_collection(self.request.body)
        serv = AuthorizationService()
        result = serv.signin(sign_in_data)
        self.success(response=result)


class ConsentHandler(BaseHandler):
    """
    name     String     The user's "signature", recorded exactly as entered
    birthdate     String     The user's birthday in the format "YYYY-MM-DD".
    imageData     String     Image file of the user's signature, as a Base64 encoded string. Should be less than 10kb. Optional.
    imageMimeType     String     MIME type of the image data (ex: "image/png"). Optional
    scope     String     Required. This property must have one of three values: "no_sharing";"sponsors_and_partners";"all_qualified_researchers"
    type     String     "ConsentSignature"
    """
    @userless
    @catch_exceptions
    def post(self):
        consent_data = JSONParser.to_collection(self.request.body)
        serv = AuthorizationService()
        result = serv.consent(consent_data)
        self.success(response=result)