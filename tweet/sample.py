from config import api_config
import tweepy as tp
k,t = api_config('@_kirei_zukin_')
auth = tp.OAuthHandler(k[0], k[1])
auth.set_access_token(t[0],t[1])

api = tp.API(auth)

ret = api.update_status(input())
print(ret)