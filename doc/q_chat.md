## q_chat

* [Description](#description)
* [Usage](#usage)
* [Help and Security](#help-and-security)

### Description

The q_chat script allows to chat with the Amazon Q assistant from the command line. For example, to be 
more efficient when creating some new prompt or when testing Q responses with some questions archived in a 
text file. The question prompt is sent to the Q application (defined by its id) under the chosen user name 
and a json structure is 
returned. 


It is also possible to attach a file to the chat question as part of the prompt (see example below asking for a 
summarization of a poem)

If you don't provide a conversation id, Amazon Q will assume that you start a new conversation with him.
If you provide a conversation id - as obtained from a previous exchange in field "conversationId - and the 
message id - as last returned systemMessageId" (see example below) - of last the assistant response, Q will 
assume that you continue this conversation and restore the [LLM context window](https://klu.ai/glossary/context-window) 
of this precedent conversation to continue the chat based on this LLM context.

The q_chat script allows you to run conversations with Q. You have to provide a text file with 1 prompt per line. 
Prompts that are part of same conversation will be chained by prefix 'c:' at beginning of line. See example in 
[sample file](/data/prompt_list.txt)

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

Use with a list of prompts, 3 of then in a conversation + 1 isolated proopt, resulting in 2 distinct 
conversations:

```
% python3 q_chat.py  -a <your-app-id> -u sammy -p ../data/prompt_list.txt 
[
    {
        "conversationId": "a86bc9f6-2ace-4535-8634-3be3660e9ab8",
        "startTime": "2024-02-28 11:21:11.105000+01:00",
        "title": "what is a cat?",
        "messages": [
            {
                "body": "There's no single right answer as to whether a cat or dog is better as a pet - it depends on individual preferences and lifestyle. Here are a few factors to consider when deciding: \n\n- Care requirements - Dogs generally need more exercise and attention than cats. Cats can be left alone for longer periods. \n\n- Living space - Dogs need more room to play and exercise. Cats are more adaptable to small living spaces. \n\n- Affection levels - Dogs are often more interactive and eager to please. Cats can be more independent but will seek attention on their terms. \n\n- Allergies - Dogs tend to cause more pet dander allergies than cats. Hypoallergenic breeds exist for both. \n\n- Training - Dogs are more trainable but require consistency. Cats don't always respond to commands but can be litter trained. \n\n- Costs - Dogs often have higher food, medical and supplies costs over their lifetime. But upfront costs are similar. \n\n- Personality match - Consider your lifestyle and whether you prefer an energetic canine companion or a more solitary feline friend. \n\nI'd recommend considering your needs, researching breeds, and seeing how different pets interact in shelters before deciding. Both cats and dogs can make wonderful pets for the right owners.",
                "messageId": "c5103006-ada3-4ce1-b240-b1587d1a201b",
                "time": "2024-02-28 11:21:28.577000+01:00",
                "type": "SYSTEM"
            },
            {
                "attachments": [],
                "body": "c:should I prefer a cat or dog?",
                "messageId": "776c7117-4ac8-4b85-a4c7-b9ef78bf0050",
                "time": "2024-02-28 11:21:21.124000+01:00",
                "type": "USER"
            },
            {
                "body": "A dog is a domesticated carnivorous mammal. It is commonly kept as a household pet and comes in a variety of sizes, coat colors and patterns. Dogs have sharp teeth, keen senses of smell and hearing, and a strong sense of loyalty to their human owners. They are trainable animals that can be taught basic commands and tasks. Dogs communicate through body language, vocalizations like barking and whining, and facial expressions. They seek affection from humans and enjoy activities like walking, playing fetch and going to the park. Dogs make devoted companions while also serving important roles like assistance, protection, detection and rescue work.",
                "messageId": "e231cb45-1aa4-46a2-a86d-91f8f4723987",
                "time": "2024-02-28 11:21:20.787000+01:00",
                "type": "SYSTEM"
            },
            {
                "attachments": [],
                "body": "c:what is a dog?",
                "messageId": "d7a340ce-dcf1-4e1d-9f87-9234078b778d",
                "time": "2024-02-28 11:21:16.386000+01:00",
                "type": "USER"
            },
            {
                "body": "A cat is a small domesticated carnivorous mammal. It is commonly kept as a household pet and comes in a variety of sizes, coat colors and patterns. Cats have sharp retractable claws, keen eyesight in low light and a strong sense of smell. They are agile hunters known for catching mice and other small animals. Cats communicate through vocalizations like meowing, purring and hissing. They are intelligent, playful animals that seek affection from their human owners. Cats make loving companions while also helping control rodent populations in homes and farms.",
                "messageId": "7e72e6bb-237b-4235-8f37-90ce9c180ea8",
                "time": "2024-02-28 11:21:15.977000+01:00",
                "type": "SYSTEM"
            },
            {
                "attachments": [],
                "body": "what is a cat?",
                "messageId": "8799e878-4005-4f7b-b65c-44c25a27f25c",
                "time": "2024-02-28 11:21:11.105000+01:00",
                "type": "USER"
            }
        ]
    },
    {
        "conversationId": "e5bbba10-d5b9-42c2-bb11-f3112e62a56c",
        "startTime": "2024-02-28 11:21:28.950000+01:00",
        "title": "what is Amazon?",
        "messages": [
            {
                "body": "Amazon is an American multinational technology company based in Seattle, Washington, that focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It is one of the Big Five companies in the U.S. information technology industry, along with Google, Apple, Microsoft, and Facebook. Amazon was founded by Jeff Bezos in 1994 and started as an online marketplace for books but has since expanded to sell a wide variety of products and services primarily through its Amazon.com and Amazon Prime subscription programs. Amazon is also a major provider of cloud computing services through Amazon Web Services, which powers many large websites and applications.",
                "messageId": "ba7536b6-0f89-441f-b080-12edf134b98e",
                "time": "2024-02-28 11:21:33.135000+01:00",
                "type": "SYSTEM"
            },
            {
                "attachments": [],
                "body": "what is Amazon?",
                "messageId": "139477bf-2fe0-4d94-93d0-e837a1e4d171",
                "time": "2024-02-28 11:21:28.950000+01:00",
                "type": "USER"
            }
        ]
    }
]
```
### Help and Security

To properly set up the security definitions in AWS account for use of this script, see [README](/)

```
% python3 q_chat.py  -h
usage: q_chat.py [-h] [-a APP_ID] [-u USR_ID] [-p PROMPT] [-f FILE] [-c CNV_ID] [-m MSG_ID] [-d] [-v]

ask a question to a Q application and get answer

options:
  -h, --help            show this help message and exit
  -a APP_ID, --app_id APP_ID
                        Q application id
  -u USR_ID, --usr_id USR_ID
                        Q index id
  -p PROMPT, --prompt PROMPT
                        question prompt or path to file with list of prompts
  -f FILE, --file FILE  path to attachment file
  -c CNV_ID, --cnv_id CNV_ID
                        Q conversation id (only to continue an existing conversation)
  -m MSG_ID, --msg_id MSG_ID
                        Q parent message id (only to continue an existing conversation)
  -d, --details         full conversation details
  -v, --verbose         verbose mode
```