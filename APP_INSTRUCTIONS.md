# Office description
- You set all the constants in the backend and create API to eventually retrieve them for the front end.
- You set them in the modelsConstants.py files

# Adding a new authorization for the user, custom field
- Go to Common > models.py, add the field
- Go to Common > views.py > get_user_profiles_auth function and include the field just added to data








# Send a list of objects to save to a single api
- Configure a serializer to handle multiple request adding many = True as in 
  class OrderSerializer(serializers.ModelSerializer):
    billing_details = BillingDetailsSerializer(many=True)