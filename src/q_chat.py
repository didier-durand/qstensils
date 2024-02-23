import json
from pprint import pprint
import argparse

import boto3

q_client = boto3.client("qbusiness")  # noqa


def check_response(resp: dict, http_status_code=200) -> bool:
    assert resp['ResponseMetadata']['HTTPStatusCode'] == http_status_code
    return True


def chat_sync(app_id: str = "", usr_id: str = "", cnv_id: str = "", msg_id="", prompt="", file_path="",
              verbose=False) -> dict:
    if cnv_id is None or cnv_id == "":
        if file_path is not None and file_path != "":
            with open(file_path) as f:
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
    del response["ResponseMetadata"]
    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ask a question to a Q application and get answer")
    parser.add_argument("-a", "--app_id", type=str, help="Q application id")
    parser.add_argument("-u", "--usr_id", type=str, help="Q index id")
    parser.add_argument("-p", "--prompt", type=str, help="question prompt")
    parser.add_argument("-f", "--file", type=str, help="path to attached file")
    parser.add_argument("-c", "--cnv_id", type=str, help="Q conversation id "
                                                         "(only to continue an existing conversation)")
    parser.add_argument("-m", "--msg_id", type=str, help="Q parent message id "
                                                         "(only to continue an existing ""conversation)")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")
    args = parser.parse_args()

    answer = chat_sync(app_id=args.app_id, usr_id=args.usr_id, cnv_id=args.cnv_id, msg_id=args.msg_id,
                       prompt=args.prompt, file_path=args.file, verbose=args.verbose)
    print(json.dumps(answer, indent=4, default=str))
