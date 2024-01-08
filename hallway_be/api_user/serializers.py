from .models import customUser, askUser, PAUser, PAOffice, PACredential
from rest_framework import serializers
from .modelsConstants import LAN_OFFICE_CHOICES, LAN_ROLES_CHOICES, MAIL_OFFICE_CHOICES, ADWEB_OFFICE_CHOICES, ADWEB_ROLES_CHOICES, ASCOT_OFFICE_CHOICES, ASCOT_ROLES_CHOICES, GIFRA_OFFICE_CHOICES, GIFRA_ROLES_CHOICES

# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = ('id', 'name', 'surname', 'jobCategory')


class PAOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PAOffice
        fields = '__all__'



# UserListSerializer 
# retrieves only the data needed to work with api_peg and create a list of users
class PAUserPEGSerializer(serializers.ModelSerializer):
    managerOfOffices = PAOfficeSerializer(many=True, read_only=True)

    class Meta:
        model = PAUser
        fields = ('id', 'name', 'surname', 'jobCategory', 'manager', 'managerOfOffices')


class PAOfficeAndPOSerializer(serializers.ModelSerializer):
    manager = PAUserPEGSerializer(source='get_manager', read_only=True)

    class Meta:
        model = PAOffice
        fields = ('id', 'name', 'manager')

class PACredentialSerializer(serializers.ModelSerializer):
    user = PAUserPEGSerializer()


    def to_representation(self, instance):
        # this is required to get the data and then modify them as you want
        ret = super().to_representation(instance)

        # create a dictionary 
        lan_office_mapping = {code: label for code, label in LAN_OFFICE_CHOICES}
        mail_office_mapping = {code: label for code, label in MAIL_OFFICE_CHOICES}
        adweb_office_mapping = {code: label for code, label in ADWEB_OFFICE_CHOICES}
        ascot_office_mapping = {code: label for code, label in ASCOT_OFFICE_CHOICES}
        gifra_office_mapping = {code: label for code, label in GIFRA_OFFICE_CHOICES}

        #lan_role_mapping = {code: label for code, label in LAN_ROLES_CHOICES}
        adweb_role_mapping = {code: label for code, label in ADWEB_ROLES_CHOICES}
        ascot_role_mapping = {code: label for code, label in ASCOT_ROLES_CHOICES}
        gifra_role_mapping = {code: label for code, label in GIFRA_ROLES_CHOICES}

        # look for the label inside the dictionary based on the code and then return it
        ret['lanOffice'] = [lan_office_mapping.get(code) for code in ret['lanOffice']]
        ret['mailOffice'] = [mail_office_mapping.get(code) for code in ret['mailOffice']]
        ret['adwebOffice'] = [adweb_office_mapping.get(code) for code in ret['adwebOffice']]
        ret['ascotOffice'] = [ascot_office_mapping.get(code) for code in ret['ascotOffice']]
        ret['gifraOffice'] = [gifra_office_mapping.get(code) for code in ret['gifraOffice']]

        
        #ret['lanRole'] = [lan_role_mapping.get(code) for code in ret['lanRole']]
        ret['adwebRole'] = [adweb_role_mapping.get(code) for code in ret['adwebRole']]
        ret['ascotRole'] = [ascot_role_mapping.get(code) for code in ret['ascotRole']]
        ret['gifraRole'] = [gifra_role_mapping.get(code) for code in ret['gifraRole']]

        return ret

    class Meta:
        model = PACredential
        fields = '__all__'