# Getting Started

## Spotify
Create a .env file and copy the contents of .env.example to it.

Log in to [Spotify for Developers](https://developer.spotify.com/dashboard) and [Create An App](https://developer.spotify.com/dashboard/applications)

Copy the Client ID & the Client Secret to your .env file, in the SPOTIFY_CLIENT_ID, & SPOTIFY_CLIENT_SECRET variables. Also add your Spotify username to the SPOTIFY_USERNAME variable.

## Hue Bridge
Once your hue bridge is connected to your network, you'll need to find the IP address of the bridge. The easiest way to do this is by using [meethue](https://discovery.meethue.com/), where it will list the IP address as the "internalipaddress".

In your browser navigate to {{ YOUR_HUE_IP_ADDRESS }}/debug/clip.html, this allows you to easily interract with your bridge via an API.

You should see a form where you can input:
- A URL
- Message Body (In JSON)

Input /api into the url, and for the Message Body use
```
{
    "devicetype": "some_string"
}
```
Change "some_string" to whatever you want, and then click the POST button.

At this point you should receive an error message back saying "link button not pressed", at this point you'll want to press the button on your Hue Bridge, this confirms that whoever wants to create the user has physical access to the Bridge.

Once you've pressed the link button on your Bridge, click the POST button again, and you should now have an authorized user.

Copy the username returned into the HUE_USERNAME variable in the .env file, and also copy the IP address for your Bridge to the HUE_URL.

[Steps in full](https://developers.meethue.com/develop/get-started-2/)

## Pipenv

Install Pipenv

```
pip install pipenv
```

Activate the pipenv shell

```
pipenv shell
```


