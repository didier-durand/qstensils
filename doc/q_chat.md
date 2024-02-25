## q_chat
the q_chat script allows you to chat with the Amazon Q assistant from the command line.
The question prompt is sent to the Q application (defined by its id) and a json structure is returned. 
It is also possible to attach a file to the chat question.

If you don't provide a conversation id, Amazon Q will assume that you start a new conversation with him.
If you provide a conversation id (obtained from a previous exchange in field "conversationId") and the 
message id - as last returned systemMessageId" (see example below) - of last the assistant response, Q will 
assume that you continue this conversation and restore the context of this precedent conversation to 
continue the chat based on the conversation context.

This script is based on the [boto3("qbusiness").chat_sync() API](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness/client/chat_sync.html) provided by the Amazon Q service. The userid should be one of 
the user created in the Q application as per documentation.

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
 python3 q_chat.py -a app-id -u foo -p "can you summarize attached file ?" -f ../data/the-tyger-poem-by-william-blake.txt            
{
    "conversationId": "ec55c237-2389-4ff3-9316-3c826893a1ba",
    "failedAttachments": [],
    "systemMessage": "The poem \"The Tyger\" by William Blake raises many philosophical questions about the creator of the fearsome tiger. It wonders who could have framed the tiger's fearful symmetry and used what tools and techniques to bring it to life. By posing rhetorical questions, the poem reflects on the power of the creator to bring into existence such a strong and dangerous creature.",
    "systemMessageId": "b01f4168-4e51-405e-ba7e-93640e4ce700",
    "userMessageId": "9f32de25-68cc-4066-a611-d482ef695d20"
}
```

Use when continuing a conversation: -c and -m parameter are set to match the values provided by Q answer, 
here the conversation and message ids of poem explanation above. In particular -m must be set to value 
of "systemMessageId", which is last message in conversation flow.

```
% python3 q_chat.py -a 64ce5747-3ce5-43ec-a433-10c143d159f3 -u foo -c ec55c237-2389-4ff3-9316-3c826893a1ba -m b01f4168-4e51-405e-ba7e-93640e4ce700 -p "what are those rethorical questions that you mention ?"
{
    "conversationId": "ec55c237-2389-4ff3-9316-3c826893a1ba",
    "failedAttachments": [],
    "systemMessage": "The rhetorical questions posed in the poem "The Tyger" by William Blake include:
    - "What immortal hand or eye, could frame thy fearful symmetry?"
    - "In what distant deeps or skies. Burnt the fire of thine eyes?" 
    - "On what wings dare he aspire? What the hand, dare seize the fire?"
     - "And what shoulder, & what art, could twist the sinews of thy heart?"
     - "And when thy heart began to beat. What dread hand? & what dread feet?"
     - "What the hammer? what the chain, in what furnace was thy brain?"
     - "What the anvil? what dread grasp. Dare its deadly terrors clasp?"
     By asking these questions, the poem reflects on the power of the creator to bring into existence such 
     a strong and dangerous creature like the tiger.",
    "systemMessageId": "7f66a7b5-cf35-4385-a9d9-6b479a185bba",
    "userMessageId": "d51cd11f-1e62-4d93-9560-6c63c7d6d5bc"
}
```