## q_list_conversations

* [Description](#description)
* [Usage](#usage)
* [Help and Security](#help-and-security)

### Description
q_list_conversations is a script allowing the retrieval in a json structure of the conversations 
that happened between an named user and the Q application. It combines 2 APIs boto3("qbusiness").list_conversations() 
and boto3("qbusiness").list_messages() to bring together conversation and message details together in one place.

The returned json can be further processed by utilities like sed, jq, etc. in a [shell pipeline](https://en.wikipedia.org/wiki/Pipeline_(Unix))

The title of the conversation is the first prompt emitted by the user. Two types of messages exist. Those of type 
'USER' are emitted by the user. Those of type 'SYSTEM' are returned by the Amazon Q Assistant. When the user question 
or assistant answer contain one or more attachments, they are referred to in the description of the message.
includes or 

### Usage

```
% python3 q_list_conversations.py -a 64ce5747-3ce5-43ec-a433-10c143d159f3 -u foo                  
[
    {
        "conversationId": "ec55c237-2389-4ff3-9316-3c826893a1ba",
        "startTime": "2024-02-25 09:10:44.188000+01:00",
        "title": "can you summarize attached file ?",
        "messages": [
            {
                "body": "The rhetorical questions posed in the poem \"The Tyger\" by William Blake include:\n\n- \"What immortal hand or eye, could frame thy fearful symmetry?\" \n\n- \"In what distant deeps or skies. Burnt the fire of thine eyes?\" \n\n- \"On what wings dare he aspire? What the hand, dare seize the fire?\"\n\n- \"And what shoulder, & what art, could twist the sinews of thy heart?\" \n\n- \"And when thy heart began to beat. What dread hand? & what dread feet?\"\n\n- \"What the hammer? what the chain, in what furnace was thy brain?\"\n\n- \"What the anvil? what dread grasp. Dare its deadly terrors clasp?\"\n\nBy asking these questions, the poem reflects on the power of the creator to bring into existence such a strong and dangerous creature like the tiger.",
                "messageId": "7f66a7b5-cf35-4385-a9d9-6b479a185bba",
                "time": "2024-02-25 09:14:21.567000+01:00",
                "type": "SYSTEM"
            },
            {
                "attachments": [],
                "body": "what are those rethorical questions that you mention ?",
                "messageId": "d51cd11f-1e62-4d93-9560-6c63c7d6d5bc",
                "time": "2024-02-25 09:14:15.393000+01:00",
                "type": "USER"
            },
            {
                "body": "The poem \"The Tyger\" by William Blake raises many philosophical questions about the creator of the fearsome tiger. It wonders who could have framed the tiger's fearful symmetry and used what tools and techniques to bring it to life. By posing rhetorical questions, the poem reflects on the power of the creator to bring into existence such a strong and dangerous creature.",
                "messageId": "b01f4168-4e51-405e-ba7e-93640e4ce700",
                "time": "2024-02-25 09:10:50.302000+01:00",
                "type": "SYSTEM"
            },
            {
                "attachments": [
                    {
                        "error": {},
                        "name": "../data/the-tyger-poem-by-william-blake.txt",
                        "status": "SUCCESS"
                    }
                ],
                "body": "can you summarize attached file ?",
                "messageId": "9f32de25-68cc-4066-a611-d482ef695d20",
                "time": "2024-02-25 09:10:44.188000+01:00",
                "type": "USER"
            }
        ]
    },
    {
        "conversationId": "5e215c71-7683-4c90-bbf0-61cb56f11baa",
        "startTime": "2024-02-25 08:45:17.890000+01:00",
        "title": "can you summarize attached file ?",
        "messages": [
            {
                "body": "The poem \"The Tyger\" by William Blake raises many philosophical questions about the creator of the fearsome tiger. It wonders who could have framed the tiger's fearful symmetry and used what tools and techniques to bring it to life. By posing rhetorical questions, the poem reflects on the power of the creator to bring into existence such a strong and dangerous creature.",
                "messageId": "46ef9447-b286-4cca-b83f-a660565cbb6c",
                "time": "2024-02-25 08:45:24.013000+01:00",
                "type": "SYSTEM"
            },
            {
                "attachments": [
                    {
                        "error": {},
                        "name": "../data/the-tyger-poem-by-william-blake.txt",
                        "status": "SUCCESS"
                    }
                ],
                "body": "can you summarize attached file ?",
                "messageId": "96233176-153f-4bf0-ac20-6e0d35689a64",
                "time": "2024-02-25 08:45:17.890000+01:00",
                "type": "USER"
            }
        ]
    },
    {
        "conversationId": "0425f8de-6c9b-4de3-846a-ce212e8dbedd",
        "startTime": "2024-02-25 08:38:40.500000+01:00",
        "title": "what is Amazon?",
        "messages": [
            {
                "body": "Sorry, I could not find relevant information to complete your request.",
                "messageId": "6389c535-5fea-4cd0-be73-9926c4b18726",
                "time": "2024-02-25 09:02:37.775000+01:00",
                "type": "SYSTEM"
            },
            {
                "attachments": [],
                "body": "can you tell me more about the cloud computing services that you mention?",
                "messageId": "6d388808-bc3a-4a80-8168-bfd9b6c12c2c",
                "time": "2024-02-25 09:02:33.591000+01:00",
                "type": "USER"
            },
            {
                "body": "Amazon is an American multinational technology company based in Seattle, Washington, 
                that focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is 
                one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, 
                Microsoft, and Facebook. Amazon was founded by Jeff Bezos in 1994 and started as an online 
                marketplace for books but has since expanded to sell a wide variety of products and services primarily 
                through its Amazon.com and Amazon Prime subscription programs. Amazon is also a major provider of 
                cloud computing services through Amazon Web Services, which powers many large websites and applications.",
                "messageId": "03ef7c0d-d802-4954-9722-170aa5c6ef4f",
                "time": "2024-02-25 08:38:44.773000+01:00",
                "type": "SYSTEM"
            },
            {
                "attachments": [],
                "body": "what is Amazon?",
                "messageId": "6e0f11c8-b909-4a2f-a4c3-d54325b1e98a",
                "time": "2024-02-25 08:38:40.500000+01:00",
                "type": "USER"
            }
        ]
    }
]
```

### Help and Security

To properly set up the security definitions in AWS account for use of this script, see [README](/)

```
% python3 q_list_conversations.py -h                                            
usage: q_list_conversations.py [-h] [-a APP_ID] [-u USR_ID] [-v]

list documents indexed by Amazon Q

options:
  -h, --help            show this help message and exit
  -a APP_ID, --app_id APP_ID
                        Q application id
  -u USR_ID, --usr_id USR_ID
                        Q user id
  -v, --verbose         verbose mode

```
