
def get_spank_embed(message):
    keyfile = open('keys/google-key', 'r') 
    GOOGLE_TOKEN = keyfile.readline()

    emb = discord.Embed(colour = discord.Color.red())
    emb.title = '{0.author.mention} spanks '.format(message) + str(message.mentions[0])
    response = requests.get(url = "http://www.googleapis.com/customsearch/v1",
        params = {'cx': e9c1c4e0ed4372ac7, 'key': GOOGLE_TOKEN})



    #emb.set_image(url = 
 
