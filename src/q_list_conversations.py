import json
from pprint import pprint

import boto3
import argparse

q_client = boto3.client("qbusiness")  # noqa


def check_response(response: dict, http_status_code=200) -> bool:
    assert response['ResponseMetadata']['HTTPStatusCode'] == http_status_code
    return True


def list_conversations(app_id="", usr_id="", verbose=False) -> list[dict]:
    r_conversations: list[dict] = list[dict]()
    next_token: str = ""
    while True:
        if next_token == "":
            # maxResults cannot be bigger than 100 currently
            response = q_client.list_conversations(applicationId=app_id, userId=usr_id,
                                                   maxResults=100)
            if verbose:
                pprint(response)
            check_response(response)
        else:
            response = q_client.list_conversations(applicationId=app_id, userId=usr_id,
                                                   maxResults=100, nextToken=next_token)
            if verbose:
                pprint(response)
            check_response(response)
        if "conversations" in response:
            convs: list = response["conversations"]
            if len(convs) > 0:
                r_conversations.extend(convs)
        if "nextToken" not in response or response["nextToken"] == "":
            break
        else:
            next_token = response["nextToken"]
    if len(r_conversations) > 0:
        return r_conversations


def list_messages(app_id="", usr_id="", conv_id="", verbose=False) -> list[dict]:
    r_messages: list[dict] = list[dict]()
    next_token: str = ""
    while True:
        if next_token == "":
            # maxResults cannot be bigger than 100 currently
            response = q_client.list_messages(applicationId=app_id, userId=usr_id, conversationId=conv_id,
                                              maxResults=100)
            if verbose:
                pprint(response)
            check_response(response)
        else:
            response = q_client.list_conversations(applicationId=app_id, userId=usr_id, conversationId=conv_id,
                                                   maxResults=100, nextToken=next_token)
            if verbose:
                pprint(response)
            check_response(response)
        if "messages" in response:
            convs: list = response["messages"]
            if len(convs) > 0:
                r_messages.extend(convs)
        if "nextToken" not in response or response["nextToken"] == "":
            break
        else:
            next_token = response["nextToken"]
    if len(r_messages) > 0:
        return r_messages


def pretty_print(convs: list[dict] = None):
    for i, conv in enumerate(convs):
        print("#conv-" + str(i) + ":")
        for key in conv.keys():
            if key == "messages":
                for j, msg in enumerate(conv[key]):
                    print("   #msg-" + str(j) + ":")
                    for key2 in msg:
                        print("      " + key2 + ":", str(msg[key2]))
            else:
                print("   " + key + ":", str(conv[key]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="list documents indexed by Amazon Q")
    parser.add_argument("-a", "--app_id", type=str, help="Q application id")
    parser.add_argument("-u", "--usr_id", type=str, help="Q index id")
    parser.add_argument("-j", "--json", action="store_true", help="json format for results")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")
    args = parser.parse_args()

    if args.app_id is None or args.usr_id is None:
        raise ValueError("Q application id and user id must be specified - usage: python3 q_list_docs.py "
                         "--app_id <q-app-id> --usr_id <q-usr-id>")
    if args.verbose:
        print("Q API list_docs() called with app_id:", args.app_id, " - usr-id:", args.usr_id)

    conversations: list[dict] = list_conversations(app_id=args.app_id, usr_id=args.usr_id, verbose=args.verbose)
    for conversation in conversations:
        messages: list[dict] = list_messages(app_id=args.app_id, usr_id=args.usr_id,
                                             conv_id=conversation["conversationId"], verbose=args.verbose)
        if messages is not None and len(messages) > 0:
            conversation['messages'] = messages

    if args.json:
        print(json.dumps(conversations, indent=4, default=str))
    else:
        pretty_print(conversations)
