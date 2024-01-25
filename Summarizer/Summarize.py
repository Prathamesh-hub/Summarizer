def summarizemain(transcript_file):
    import os
    from hugchat import hugchat
    
    if not os.path.exists(transcript_file): 
        print('The transcript file does not exist!')
        return False

    with open(transcript_file) as f:
        transcript = f.read()

    from hugchat.login import Login

    print('Summarizing...', end='')
    # login
    sign = Login("shubh2002", "Nothing@06")
    cookies = sign.login()
    sign.saveCookiesToDir("/content")
    
    # load cookies from usercookies
    cookies = sign.loadCookiesFromDir("/content") # This will detect if the JSON file exists, return cookies if it does and raise an Exception if it's not.
    
    # Create a ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
    prompt = f'''Create a summary of the following text.
    Text: {transcript}
    Add a title to the summary.
    Your summary should be informative and factual, covering the most important aspects of the topic 
    Start your summary with an INTRODUCTION PARAGRAPH that gives an overview of the topic FOLLOWED 
    by BULLET POINTS if possible AND end the summary with a CONCLUSION PHRASE.'''
    
    print('Done')
    #Summarise Transcript

    summarycode=str(chatbot.chat(prompt))

    return summarycode