messages = [
    {
        "sender": "99155 71177",
        "receiver": "99999 11111",
        "conversation":[
            "Hello",
            "How are you", 
            "Its Friday",
            "Lets Party. No Code today"
        ]
    },
    {
        "sender": "99155 71177",
        "receiver": "99999 22222",
        "conversation":[
            "Hello",
            "Kaisa hai bhai", 
            "Aj Friday hai",
            "lets party."
        ]
    },
    {
        "sender": "98765 12345",
        "receiver": "99155 71177",
        "conversation":[
            "Beta",
            "Bahut Kaam Hai", 
            "Sabji leni hai",
            "jaldio aa jana. mummy here"
        ]
    }

]

search_keyword = input("Enter Word to Search: ")
search_keyword = search_keyword.upper()
# Logic
# Firday Assignment :)
for idx in range(0,3):
    for i in range (0 , 2):
        if search_keyword in list(messages[idx].values())[i] or search_keyword in list(messages[idx].values())[i]:
            print(list(messages[idx].values())[i])
            break
    
    chat = list(messages[idx].values())[2]
    for i in range (0,len(chat)):
            o_message = str(chat[i])
            message = o_message.upper()
            if search_keyword in message:
                print(o_message)
 