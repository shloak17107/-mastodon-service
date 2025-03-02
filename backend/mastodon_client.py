from mastodon import Mastodon

class MastodonClient:
    def __init__(self, client_creds_file='clientcreds.secret', user_creds_file='usercreds.secret'):
        self.client_creds_file = client_creds_file
        self.user_creds_file = user_creds_file
        self.mastodon_client = None
        self.mastodon_user = None
        
    def register_app(self, app_name, api_base_url):
        """
        Registers a new application with the Mastodon server.

        Args:
            app_name (str): The name of the application to register.
            api_base_url (str): The base URL of the Mastodon instance.

        Returns:
            None
        """
        Mastodon.create_app(
            app_name,
            api_base_url = api_base_url,
            to_file = 'clientcreds.secret'
        )
    
    def authenticate_client(self):
        """
        Authenticates the Mastodon client using the provided client credentials file.

        This method initializes the Mastodon client with the client credentials file
        and prints the authentication request URL.

        Raises:
            MastodonError: If there is an error during the authentication process.
        """
        self.mastodon_client = Mastodon(client_id=self.client_creds_file)
        print(self.mastodon_client.auth_request_url())
    
    def log_in(self, auth_code):
        """
        Logs in to the Mastodon client using the provided authorization code.

        Args:
            auth_code (str): The authorization code to log in with.

        Returns:
            None
        """
        self.mastodon_client.log_in(
            code=auth_code,
            to_file=self.user_creds_file
        )
    
    def initialize_user(self):
        """
        Initializes the Mastodon user by creating an instance of the Mastodon class
        with the access token provided in the user's credentials file.

        Attributes:
            mastodon_user (Mastodon): An instance of the Mastodon class initialized
                                      with the user's access token.
        """
        self.mastodon_user = Mastodon(access_token=self.user_creds_file)
        
    def create_post(self, message):
        """
        Posts a toot (status update) to the authenticated Mastodon user's account.

        Args:
            message (str): The content of the toot to be posted.

        Raises:
            ValueError: If the user is not authenticated.
        """
        if self.mastodon_user:
            status = self.mastodon_user.toot(message)
            return status
        else:
            print("User not authenticated. Please intiialize the user first!")

    def get_post(self, post_id):
        """
        Retrieves a specific post (toot) by its ID.

        Args:
            post_id (int): The ID of the post to retrieve.

        Returns:
            dict: The retrieved post data.

        Raises:
            ValueError: If the user is not authenticated.
        """
        if self.mastodon_user:
            post = self.mastodon_user.status(post_id)
            return post
        else:
            raise ValueError("User not authenticated. Please initialize the user first!")

    def delete_post(self, post_id):
        """
        Deletes a specific post (toot) by its ID.

        Args:
            post_id (int): The ID of the post to delete.

        Returns:
            None

        Raises:
            ValueError: If the user is not authenticated.
        """
        if self.mastodon_user:
            self.mastodon_user.status_delete(post_id)
        else:
            raise ValueError("User not authenticated. Please initialize the user first!")

# EXAMPLE USAGE:
#
# Step 1: Initialize the class
# client = MastodonClient()
#
# Step 2: Register the app with Mastodon. This only needs to be done once, so `register_app`
# doesn't need to be called every time. Saves the secret to a clientcreds.secret file.
# client.register_app('cs272app', 'https://mastodon.social')
#
# Step 3: Instantiates the Mastodon client and uses `clientcreds.secret` file to authenticate.
# Prints out a URL for auth request, which needs to be copied and pasted into a browser. 
# client.authenticate_client()
#
# Step 4: Enter the auth code as input and login. Saves user creds to a file. 
# client.log_in(input("Enter the OAuth authorization code: "))
#
# Step 5: Initialize user using `usercreds.secret` 
# client.initialize_user()
#
# Step 6: Post a toot
# client.toot('It Works !')
