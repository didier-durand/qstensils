import json
import os
from pprint import pprint
import argparse

import boto3

q_client = boto3.client("qbusiness")  # noqa


def check_response(resp: dict, http_status_code=200) -> bool:
    assert resp['ResponseMetadata']['HTTPStatusCode'] == http_status_code
    return True


def chat_sync(app_id: str = "", usr_id: str = "",  # pylint: disable=too-many-arguments
              prompt="", file_path="", cnv_id: str = "", msg_id="",
              verbose=False) -> dict:
    if verbose:
        print("prompt:", "\"" + prompt + "\"")
    if cnv_id is None or cnv_id == "":
        if file_path is not None and file_path != "":
            with open(file_path) as f:  # pylint: disable=unspecified-encoding
                data = f.read()
            response = q_client.chat_sync(applicationId=app_id, userId=usr_id, userMessage=prompt,
                                          attachments=[{"name": file_path, "data": data}])
        else:
            response = q_client.chat_sync(applicationId=app_id, userId=usr_id, userMessage=prompt)
    else:
        response = q_client.chat_sync(applicationId=app_id, userId=usr_id, conversationId=cnv_id,
                                      parentMessageId=msg_id, userMessage=prompt)
    if verbose:
        pprint(response)
    check_response(response)
    del response["ResponseMetadata"]
    return response


def chat_sync_with_multiple_prompts(app_id="", usr_id="", prompts: list[str] = None, verbose=False) \
        -> list[dict] | None:
    if prompts is None or len(prompts) == 0:
        return None
    conversations: list[dict] = list[dict]()
    cnv_id: str = ""
    msg_id: str = ""
    for prompt in prompts:
        if prompt.startswith("c:"):
            if cnv_id is not None and cnv_id != "" and msg_id is not None and msg_id != "":
                resp = chat_sync(app_id=app_id, usr_id=usr_id, cnv_id=cnv_id, msg_id=msg_id,
                                 prompt=prompt, verbose=verbose)
            else:
                raise ValueError("conversation id and parent message id must be available for chained prompts")
        else:
            resp = chat_sync(app_id=app_id, usr_id=usr_id, prompt=prompt, verbose=args.verbose)
        conversations.append(resp)
        cnv_id = resp["conversationId"]
        msg_id = resp["systemMessageId"]
    if len(conversations) > 0:
        return conversations
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ask a question to a Q application and get answer")
    parser.add_argument("-a", "--app_id", type=str, help="Q application id")
    parser.add_argument("-u", "--usr_id", type=str, help="Q index id")
    parser.add_argument("-p", "--prompt", type=str, help="question prompt")
    parser.add_argument("-f", "--file", type=str, help="path to attachment file")
    parser.add_argument("-c", "--cnv_id", type=str, help="Q conversation id "
                                                         "(only to continue an existing conversation)")
    parser.add_argument("-m", "--msg_id", type=str, help="Q parent message id "
                                                         "(only to continue an existing ""conversation)")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")
    args = parser.parse_args()

    p_str = args.prompt
    if os.path.isfile(p_str):
        with open(p_str, encoding="us-ascii") as file:
            f_prompts = file.read()
            f_prompts: [str] = f_prompts.split("\n")
            answer = chat_sync_with_multiple_prompts(app_id=args.app_id, usr_id=args.usr_id,
                                                     prompts=f_prompts, verbose=args.verbose)
    else:
        answer = chat_sync(app_id=args.app_id, usr_id=args.usr_id, cnv_id=args.cnv_id, msg_id=args.msg_id,
                           prompt=args.prompt, file_path=args.file, verbose=args.verbose)
    print(json.dumps(answer, indent=4, default=str))
