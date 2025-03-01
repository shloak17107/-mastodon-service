from mastodon import Mastodon

#Step 1
#Registers whatever app we create with Mastodon. Only needs to be done ONCE. Comment out code after running. 
#Returns id and secret as strings, saving this into clientcreds.secret
Mastodon.create_app(
    'cs272app',
    api_base_url = 'https://mastodon.social',   # change url to whatever we end up making, perhaps Flask app?
    to_file = 'clientcreds.secret'
)

## in case we want to fetch these differently, shouldn't be required hopefully
#client_id = creds['client_id']
#client_secret = creds['client_secret']


#Step 2
#new mastodon class instance, just to use our client creds to print out a URL for auth request. Copy and paste into a browser
mastodon_client = Mastodon(client_id = 'clientcreds.secret',)
print(mastodon_client.auth_request_url())

# open the URL in the browser and paste the code you get. 
# Alternatively, we can instead create an account with mastodon.create_account() and it'll also return access token
# Input URL Code or Create a new Account. Either option works, the important part is fetching access tokens to use. I'll leave which method to you guys
# Below is using the URL code input option
#should paste the access token into usercreds.secret
mastodon_client.log_in(
    code=input("Enter the OAuth authorization code: "),
    to_file="usercreds.secret"
)

#Step 3
#now our actual Mastodon instance that is properly authenticated and ready to do real stuff
mastodon_user = Mastodon(access_token = 'usercreds.secret')

#### up until this point should handle all the initializing and auth for Mastodon I believe. ####
#### now actual API calls and stuff can be made to handle the rest of the Twitter app thing ####
mastodon_user.toot('It Works !')

