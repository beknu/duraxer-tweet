import tweepy
auth = tweepy.OAuthHandler("EnHGNIkx9UBwF1AKSG9Vz8ju5", "l0eRFst2EXdgWUt0Ko1nEwZc0AgzQAONc7BIQdwrhrxlhlPVqp") 
auth.set_access_token("2904544801-eRKQlREVbAigQ7xomqlfnEY2rnK72Urdf8vcJLU", "yksLKSWEbWnYNNbHxMR9ue7h1WTlqqQgsQZKOZdilc5xX") 
api = tweepy.API(auth)
print ("Tweet From Terminal!")
print ("Twitter For Everyone")
tweet = input("What Would You Like To Tweet? ")
api.update_status(status =(tweet))
print ("Done!")

API Consumer Key
EnHGNIkx9UBwF1AKSG9Vz8ju5

API Consumer Secret Key
l0eRFst2EXdgWUt0Ko1nEwZc0AgzQAONc7BIQdwrhrxlhlPVqp

Bearer TOKEN
AAAAAAAAAAAAAAAAAAAAAJKzcQEAAAAAE7Q8WyGHQDvfc3vBU73sjf1bGe4%3DVO1b5CChghj26fTudNm0v6z6pVmEzahMZJx2iKBI7b0zVFKvFl

ACCESS TOKEN
2904544801-eRKQlREVbAigQ7xomqlfnEY2rnK72Urdf8vcJLU

SECRET TOKEN
yksLKSWEbWnYNNbHxMR9ue7h1WTlqqQgsQZKOZdilc5xX
