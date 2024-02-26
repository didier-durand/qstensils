import json
from pprint import pprint
import argparse

import boto3

q_client = boto3.client("qbusiness")  # noqa


def check_response(response: dict, http_status_code=200) -> bool:
    assert response['ResponseMetadata']['HTTPStatusCode'] == http_status_code
    return True


def list_conversations(app_id: str = "", usr_id: str = "", verbose: bool = False) -> list[dict] | None:
    convs: list[dict] = list[dict]()
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
                convs.extend(convs)
        if "nextToken" not in response or response["nextToken"] == "":
            break
        next_token = response["nextToken"]
    if len(convs) > 0:
        return convs
    return None


def list_messages(app_id: str = "", usr_id: str = "", conv_id: str = "", verbose: bool = False) -> list[dict] | None:
    msgs: list[dict] = list[dict]()
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
            r_msgs: list = response["messages"]
            if len(r_msgs) > 0:
                msgs.extend(r_msgs)
        if "nextToken" not in response or response["nextToken"] == "":
            break
        next_token = response["nextToken"]
    if len(msgs) > 0:
        return msgs
    return None


def list_conversations_with_messages(app_id: str = "", usr_id: str = "", verbose=False) -> list[dict] | None:
    convs: list[dict] = list_conversations(app_id=app_id, usr_id=usr_id, verbose=verbose)
    if convs is not None and len(convs) > 0:
        for conv in convs:
            messages: list[dict] = list_messages(app_id=app_id, usr_id=usr_id,
                                                 conv_id=conv["conversationId"], verbose=verbose)
            if messages is not None and len(messages) > 0:
                conv['messages'] = messages
        return convs
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="list documents indexed by Amazon Q")
    parser.add_argument("-a", "--app_id", type=str, help="Q application id")
    parser.add_argument("-u", "--usr_id", type=str, help="Q user id")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")
    args = parser.parse_args()

    if args.app_id is None or args.usr_id is None:
        raise ValueError("Q application id and user id must be specified - usage: python3 q_list_documents.py "
                         "--app_id <q-app-id> --usr_id <q-usr-id>")
    if args.verbose:
        print("Q API list_conversations() called with app_id:", args.app_id, " - usr-id:", args.usr_id)

    conversations: list[dict] = list_conversations_with_messages(app_id=args.app_id, usr_id=args.usr_id,
                                                                 verbose=args.verbose)
    print(json.dumps(conversations, indent=4, default=str))
