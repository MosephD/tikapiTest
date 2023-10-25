from tikapi import TikAPI, ValidationException, ResponseException

# Initialize the TikAPI object with your API key
api = TikAPI('aBOB8dZdV3wzuKxfjkmDPtA2DgpfdyDuoavCbKuqiGGaw7fK')


def search_users_by_region(category, country):
    try:
        # Assuming the 'search' endpoint is accessible as a method on the TikAPI object
        # and 'country' can be passed as a parameter.
        response = api.search(category=category, country=country)

        # Process the response
        if response:
            # Assuming the response contains a list of users
            for user in response.get('users', []):
                print(f'User: {user.get("username")}, Region: {country}')

    except ValidationException as ve:
        print(f'Validation Exception: {ve}')
    except ResponseException as re:
        print(f'Response Exception: {re}')


# Call the function with desired search term and country
search_users_by_region('desired_search_term', 'us')
