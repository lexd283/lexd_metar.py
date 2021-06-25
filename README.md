<div align="center">
  <strong><i>lexd_metar.py</i></strong>
  <br>
  <br>
 </div>

FYI: i am new to making README files so bare with me if i make mistakes lol

This was a side-project, because honestly, I was bored lol
This can give you the METAR for the airport of your choice.

To setup this code, head to https://account.avwx.rest, and sign up for Hobby 
(you can choose the other plans, but they cost money)

Once you signed up, do the necessary steps to sign up.

After signing up, head to https://account.avwx.rest/manage, and copy your API token.

Go to the folder that this file is in. You should see a .env.EXAMPLE file. 
Convert it back to an .env file, and make sure the type is "ENV File".

Now, open the .env file with any text editor, and replace the example API_TOKEN, with 
your awesome new token. If there are any problems, please message me on discord.

Discord: big bus man#8780

# KNOWN BUGS
Because AVWX (the api this file uses) doesn't support certain airports right now, the api request is invalid, thus showing an error.
 
