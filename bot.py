import discord
import aiohttp
import time
from random import randint
from keep_alive import keep_alive
import pandas as pd
import random
import requests
import json

client = discord.Client()

# TOKEN removed for security purposes
TOKEN = ''

user_input = ["tgb hello", "tgb hii", "tgb hi", "tgb bot", "tgb yo", "tgb yoo", "tgb hey", "tgb bro",
              "tgb hola", "tgb what's up", "tgb dude", "tgb what's up dude", "tgb ciao", "tgb buddy"
              ]

bot_reply = ["Hello!", "Hii", "CIAO", "Hey Buddy!", "Heya, how's it going?", "Hey, What's up?", "Good to see you",
             "Great to see you", "Glad to see you", "Look who it is!", "Nice to see you again", "Hi there",
             "Long time no see",
             "Howdy-doody!", "Hiya!", "Howdy, howdy, howdy!", "Yoo!", "Cool dude!", "Hola", "Bonjour",
             "What's going on?",
             "Doing OK", "Everything Alright!"]

trivia = [
    "The Firefox logo isn’t a fox.",
    "The first Apple logo isn’t what you would think.",
    "Google rents out goats",
    "The name for “robot” has dark origins",
    "The first-ever VCR was the size of a piano",
    "Samsung is 38 years and 1 month older than Apple",
    "A Petabyte is a lot of data",
    "Domain name registration used to be free",
    "Megabytes used to weigh hundreds of pounds",
    "The Radio took 38 years to reach an audience of 50 million",
    "The first camera needed an incredibly long exposure",
    "Credit card chips have been around for a LONG time",
    'Google rents out goats',
    'The name for “robot” has dark origins',
    'The first-ever VCR was the size of a piano',
    'Samsung is 38 years and 1 month older than Apple',
    'A Petabyte is a lot of data',
    'Domain name registration used to be free',
    'Megabytes used to weigh hundreds of pounds',
    'The Radio took 38 years to reach an audience of 50 million',
    'The first camera needed an incredibly long exposure',
    'Credit card chips have been around for a LONG time',
    'Alexa is always listening to your conversations',
    'People read faster or slower depending on what they read from',
    'GPS is free for some',
    'There are Amish computers',
    'Mac computers were named after the apple',
    'The first computer mouse wasn’t made from plastic',
    'Which came first, Spam mail or Spam meat',
    'The original Xbox had sound snippets of real space missions',
    'The majority of the people plug in their USB wrong',
    'Steve Jobs used sleight of hand at the first iPhone presentation',
    'The first alarm clock could only ring at one time',
    'Computer Security Day is celebrated on November 30th',
    'The government used PlayStation 3’s… but not for gaming',
    'The first online gaming was before the year 2000',
    'The first product scanned was a packet of chewing gum in 1974',
    'You’re in good hands if your surgeon was a gamer',
    'iTunes has unusual Terms & Conditions',
    'Nintendo didn’t start as a video games company',
    'Apollo 11 astronauts couldn’t afford insurance',
    'People are still using dial-up',
    "You can spell your email in Morse code",
    'Yahoo’s original name was a mouthful',
    'Everyone uses Google as a spellchecker',
    'The first word to ever be auto-corrected was “teh"',
    'The Nintendo Game Boy went to space',
    'PlayStation 1 had Scratch and Sniff discs',
    '“Android” is gender-specific',
    'Google searches hit the billions every month',
    "There’s a name for when you feel your phone vibrate… but it doesn’t",
    'Smoking will void your Apple warranty',
    'Technology is now influencing baby names',
    'Blind people can use cell phones',
    'Google’s first tweet was gibberish',
    'The first cell phone call was in New York City',
    'The first commercial text message was sent in 1992',
    'Over 6,000 new computer viruses are created and released every month',
    'There are more likes than photos on Facebook',
    'iPhones were almost in the shape of an apple',
    'Comic Sans is the most hated font in the world',
    'NASA’s internet speed is 91 GB per second',
    'Nokia is the largest company from Finland',
    'More people have cell phones than toilets',
    'The Apple Lisa was the first commercial computer with a Graphical User Interface (GUI) and a mouse',
    'Some people are afraid of technology',
    'The most expensive phone number cost millions',
    'Mark Zuckerberg is color blind',
    '40% of American couples meet online',
    'Music content makes up 5% of YouTube',
    'Finding a security bug in Facebook’s code will pay off',
    'Kids that are on social media for 1 hour a day have less chance of being happy',
    'MySpace lost all of its content before 2016',
    'Nearly one third of divorces are because of Facebook',
    'Using a thinner font can save printer ink',
    'The QWERTY keyboard was originally designed to slow you down',
    'The first webpage is still running',
    'Some countries skipped the era of landlines,'
    'The passwords for the nuclear missiles were just a string of zero’s',
    'Over 90% of the world’s currency is digital',
    'Millions of hours of TV and movies are watched every day on Netflix',
    'Technical degrees are almost useless by the time you graduate',
    'There’s a term for old people who use the internet',
    'Tech companies often test their products in New Zealand',
    'There are fake Apple stores in China',
    'Until 2010, carrier pigeons were faster than the internet',
    'The first photo ever uploaded to the internet was a comedy band',
    'Every advertisement for iPhone’s have 9:41 set as the time',
    'A “jiffy” is a real measurement',
    'An average 21 year old has spent 5,000 hours playing video games',
    'Most of today’s successful companies started in garages',
    'Most internet traffic isn’t from real humans',
    'CAPTCHA is a long acronym',
    'The three most common passwords are also the weakest',
    'There wasn’t an app store in the first iPhone',
    'We only keep 1 out of every 10 apps we try',
    'Digital music sales surpassed physical sales in 2014',
    'The @ symbol was chosen kind of randomly',
    'There is a machine that can predict heart attacks',
    'There is also artificial intelligence than can predict epidemics',
    'The Amazon’s robot workers skyrocketed in less than five years',
    'Digital tech is good for the environment',
    'The average Facebook user has less than 200 friends',
    'Google uses the same amount of energy as 200,000 homes',
    'The first computer virus was harmless',
    'There are only 21 million Bitcoins that can be mined in total',
    'Filipinos use social media more than Americans',
    'Most of the purchases in China are done with mobile phones',
    'Robot laws are being put into place',
    'Millions of tons of technology are thrown out each year',
    'People read faster or slower depending on what they read from',
    'GPS is free… for some',
    'There are Amish computers',
    'Mac computers were named after the apple',
    'The first computer mouse wasn’t made from plastic',
    'Which came first, Spam mail or Spam meat?',
    'The original Xbox had sound snippets of real space missions',
    'The majority of the people plug in their USB wrong',
    'Steve Jobs used sleight of hand at the first iPhone presentation',
    'The first alarm clock could only ring at one time',
    'Computer Security Day is celebrated on November 30th',
    'The government used PlayStation 3’s… but not for gaming',
    'The first online gaming was before the year 2000',
    'The first product scanned was a packet of chewing gum in 1974',
    'You’re in good hands if your surgeon was a gamer',
    'iTunes has unusual Terms & Conditions',
    'Nintendo didn’t start as a video games company',
    'Apollo 11 astronauts couldn’t afford insurance',
    'People are still using dial-up',
    'You can spell your email in Morse code',
    'Yahoo’s original name was a mouthful',
    'Everyone uses Google as a spellchecker',
    'The first word to ever be auto-corrected was “teh”',
    'The Nintendo Game Boy went to space',
    'PlayStation 1 had Scratch and Sniff discs',
    '“Android” is gender-specific',
    'Google searches hit the billions every month',
    "There’s a name for when you feel your phone vibrate… but it doesn’t",
    'Smoking will void your Apple warranty',
    'Technology is now influencing baby names',
    'Blind people can use cell phones',
    'Google’s first tweet was gibberish',
    'The first cell phone call was in New York City',
    'The first commercial text message was sent in 1992',
    'Over 6,000 new computer viruses are created and released every month',
    'There are more likes than photos on Facebook',
    'iPhones were almost in the shape of an apple',
    'Comic Sans is the most hated font in the world',
    'NASA’s internet speed is 91 GB per second',
    'Nokia is the largest company from Finland',
    'More people have cell phones than toilets',
    'The Apple Lisa was the first commercial computer with a Graphical User Interface (GUI) and a mouse',
    'Some people are afraid of technology',
    'The most expensive phone number cost millions',
    'Mark Zuckerberg is color blind',
    '40% of American couples meet online',
    'Music content makes up 5% of YouTube',
    'Finding a security bug in Facebook’s code will pay off',
    'Kids that are on social media for 1 hour a day have less chance of being happy',
    'MySpace lost all of its content before 2016',
    'Nearly one third of divorces are because of Facebook',
    'Using a thinner font can save printer ink',
    'The QWERTY keyboard was originally designed to slow you down',
    'The first webpage is still running',
    'Some countries skipped the era of landlines',
    "The passwords for the nuclear missiles were just a string of zero’s",
    'Over 90% of the world’s currency is digital',
    'Millions of hours of TV and movies are watched every day on Netflix',
    'Technical degrees are almost useless by the time you graduate',
    'There’s a term for old people who use the internet',
    'Tech companies often test their products in New Zealand',
    'There are fake Apple stores in China',
    'Until 2010, carrier pigeons were faster than the internet',
    'The first photo ever uploaded to the internet was a comedy band',
    'Every advertisement for iPhone’s have 9:41 set as the time',
    'A “jiffy” is a real measurement',
    'An average 21 year old has spent 5,000 hours playing video games',
    'Most of today’s successful companies started in garages',
    'Most internet traffic isn’t from real humans',
    'CAPTCHA is a long acronym',
    'The three most common passwords are also the weakest',
    'There wasn’t an app store in the first iPhone',
    'We only keep 1 out of every 10 apps we try',
    'Digital music sales surpassed physical sales in 2014',
    'The @ symbol was chosen kind of randomly',
    'There is a machine that can predict heart attacks',
    'There is also artificial intelligence than can predict epidemics',
    'The Amazon’s robot workers skyrocketed in less than five years',
    'Digital tech is good for the environment',
    'The average Facebook user has less than 200 friends',
    'Google uses the same amount of energy as 200,000 homes',
    'The first computer virus was harmless',
    'There are only 21 million Bitcoins that can be mined in total',
    'Filipinos use social media more than Americans',
    'Most of the purchases in China are done with mobile phones',
    'Robot laws are being put into place',
    'Millions of tons of technology are thrown out each year',
]


def quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.content)
    quo = json_data[0]['q'] + " " + json_data[0]['a']
    return quo


@client.event
async def on_ready():
    print('Ready {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    if any(word in msg for word in user_input):
        await message.channel.send(random.choice(bot_reply) + '  {0.author.name}'.format(message))

    if message.content.lower() == 'tgb help me':
        await message.channel.send('How can I help you?')

    if message.content.lower() == 'tgb cmdlist':
        embed = discord.Embed(
            title="***TGB Command list***",
            description="*tgb hi, hello, hey, ciao, yoo, hola, dude, buddy\ntgb council\ntgb core\ntgb exec\ntgb trivia\n"
                        "tgb help me\ntgb meme\ntgb quotes\ntgb bio\ntgb bio:@<user>\ntgb add bio:<ADD_YOUR_BIO_TEXT>*",
            colour=discord.Colour.teal()
        )

        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb council':
        embed = discord.Embed(
            title="***Council Members***",
            description="***Nishant Gandhi*** >>> Chairman\n***Sarthak Khandelwal*** >>> Vice-Chairman\n***Hiteshi Gupta***  >>> Treasurer",
            colour=discord.Colour.red()
        )
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb core':
        embed = discord.Embed(
            title="***Head Members***",
            description="***Saud Hashmi*** -->  Content Head\n***Riya Ahuja*** -->  Management Head\n***Ritika Maheshwari*** -->  Marketing Head\n"
                        "***Mihir Dutta*** -->  Technical Head\n***Samriddhi Kaur*** -->  Graphics Head\n***Yash Sehgal*** -->  Junior Coordinator",
            colour=discord.Colour.blue()
        )
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb exec':
        embed = discord.Embed(
            title="***Executives Members***",
            description="*Mayank Verma\nJaspreet Singh Saini\nSamarth Sharma\nAditi Mandlik\nPrateeti Mehta Jain\n"
                        "Rajesh Nathani\nIshika Shahaney\nRaj Soni\nAnushka Jain\nTanisha Jain\nAditi Dandawate\n"
                        "Suchismita Nanda*",
            colour=discord.Colour.green()
        )
        await message.channel.send(embed=embed)

    if message.content.lower() == ("tgb contacts"):
        embed = discord.Embed(
            title='***Connect us on*** !',
            description='**[Instagram](https://instagram.com/mu_acm?utm_medium=copy_link)**\n\n'
                        '**[LinkedIn](https://www.linkedin.com/company/acm-student-chapter-medicaps/)**'
                        '\n\n**[Website](http://medicaps.hosting.acm.org/)**',
            colour=discord.Colour.orange()
        )
        embed.set_image(url='https://i.ibb.co/YWV5Bx0/Mu-ACMlogo.png')
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb trivia':
        embed = discord.Embed(color=discord.Color.random())
        embed.add_field(name="***Trivia requested***  !", value=trivia[randint(0, len(trivia) - 1)])
        embed.set_footer(text="\nEnjoy! {0.author.name}".format(message))
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb meme':

        await message.channel.send(embed=await pyrandmeme())


    if message.content.lower() == "tgb quotes":
        quo = quote()
        embed = discord.Embed(color=discord.Color.random())
        embed.add_field(name="***Quote***  !", value=quo)
        embed.set_footer(text="Requested by {0.author.name}".format(message))
        await message.channel.send(embed=embed)

    if message.content.lower() == 'tgb bio':
        await message.channel.send(tgb_bio(message))

    if 'tgb bio: ' in message.content.lower() and message.content[9] != None:
        code = message.content[9:]
        userid = int(code[3:len(code) - 1])
        await message.channel.send(tgb_bio_with_user(message, userid))

    if ("tgb add bio: " in message.content.lower()) and (message.content[13] != None):
        await message.channel.send(add_bio(message))

    if ("tgb change bio: " in message.content.lower()) and (message.content[16] != None):
        await message.channel.send(change_bio(message))


async def pyrandmeme():
    pymeme = discord.Embed(title="Tech Meme requested", description="Here you go!", color=0x84d4f4)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/TechMemes/new.json?sort=new') as r:
            res = await r.json()
            pymeme.set_image(url=res['data']['children'][randint(0, 25)]['data']['url'])
            return pymeme
        await pyrandmeme()


def tgb_bio(message):
    df = pd.read_csv(r'bio.csv')
    user = str(message.author)
    users = list(df['user'].values)
    if user in users:
        return df[df['user'] == user].bio.values[0]
    else:
        rtn = f"No bio found for {user}"
        return rtn


def tgb_bio_with_user(message, userid):
    df = pd.read_csv(r'bio.csv')
    user = str(message.author)
    users = list(df['user'].values)
    if user in users:
        return df[df['userid'] == userid].bio.values[0]
    else:
        rtn = f"No bio found for {user}"
        return rtn


def add_bio(message):
    df = pd.read_csv(r'bio.csv')
    bio = str(message.content[13:])
    user = str(message.author)
    userid = str(message.author.id)
    df.loc[len(df.index)] = [userid, user, bio]
    df.to_csv(r'bio.csv', index=False)
    return 'Bio added!'


def change_bio(message):
    df = pd.read_csv(r'bio.csv')
    new_bio = str(message.content[16:])
    curr_user = str(message.author)
    users = list(df['user'].values)
    if curr_user in users:
        df.loc[df.user == curr_user, 'bio'] = new_bio
        df.to_csv(r'bio.csv', index=False)
        return 'Bio changed!'


keep_alive()
client.run(TOKEN)