## q_chat
the q_chat script allows you to chat with the Amazon Q assistant from the command line.
The question prompt is sent to the Q application (defined by its id) and a json structure is returned.

If you don't provide a conversation id, Amazon Q will assume that you start a new conversation with him.
If you provide a conversation id (obtained from a previous exchange in field "conversationId") the Q assistant will assume that you continue this conversation and restore the context of this precedent conversation to continue the chat.

This script is based on the chat_sync() API provided by the Amazon Q service.

The userid should be one of the user created in the Q application as per documentation

### Usage 
Use with a simple text prompt

```
python3 q_chat.py -a app-id -u foo -p "what is Amazon?"
{
    "conversationId": "0425f8de-6c9b-4de3-846a-ce212e8dbedd",
    "failedAttachments": [],
    "sourceAttributions": [],
    "systemMessage": "Amazon is an American multinational technology company based in Seattle, Washington, that focuses 
    on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is one of the Big Five 
    companies in the U.S. information technology industry, along with Google, Apple, Microsoft, and Facebook. 
    Amazon was founded by Jeff Bezos in 1994 and started as an online marketplace for books but has since 
    expanded to sell a wide variety of products and services primarily through its Amazon.com and Amazon 
    Prime subscription programs. Amazon is also a major provider of cloud computing services through 
    Amazon Web Services, which powers many large websites and applications.",
    "systemMessageId": "03ef7c0d-d802-4954-9722-170aa5c6ef4f",
    "userMessageId": "6e0f11c8-b909-4a2f-a4c3-d54325b1e98a"
}
```

Use with an attachment, here the poem The Tyger by William Blake (see /data to use it)

```
 % python3 q_chat.py -a 64ce5747-3ce5-43ec-a433-10c143d159f3 -u foo -p "can you summarize attached file ?" -f ../data/the-tyger-poem-by-william-blake.txt 

{
    "conversationId": "5e215c71-7683-4c90-bbf0-61cb56f11baa",
    "failedAttachments": [],
    "systemMessage": "The poem "The Tyger" by William Blake raises many philosophical questions about the 
    creator of the fearsome tiger. It wonders who could have framed the tiger's fearful symmetry and u
    sed what tools and techniques to bring it to life. By posing rhetorical questions, the poem reflects 
    on the power of the creator to bring into existence such a strong and dangerous creature.",
    "systemMessageId": "46ef9447-b286-4cca-b83f-a660565cbb6c",
    "userMessageId": "96233176-153f-4bf0-ac20-6e0d35689a64"
}

```