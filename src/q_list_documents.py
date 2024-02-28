import json
from pprint import pprint
import argparse

import boto3

q_client = boto3.client("qbusiness")  # noqa


def check_response(response: dict, http_status_code=200) -> bool:
    assert response['ResponseMetadata']['HTTPStatusCode'] == http_status_code
    return True


def list_documents(app_id="", idx_id="", verbose=False) -> list[dict] | None:
    r_docs: list[dict] = list[dict]()
    next_token: str = ""
    while True:
        if next_token == "":
            # maxResults cannot be bigger than 100 currently
            response = q_client.list_documents(applicationId=app_id, indexId=idx_id,
                                               maxResults=100)
            if verbose:
                pprint(response)
            check_response(response)
        else:
            response = q_client.list_documents(applicationId=app_id, indexId=idx_id,
                                               maxResults=100, nextToken=next_token)
            if verbose:
                pprint(response)
            check_response(response)
        if "documentDetailList" in response:
            docs: list = response["documentDetailList"]
            if len(docs) > 0:
                r_docs.extend(docs)
        if "nextToken" not in response or response["nextToken"] == "":  # pylint: disable=no-else-break
            break
        else:
            next_token = response["nextToken"]
    if len(r_docs) > 0:
        return r_docs
    return None


def pretty_print(docs: list[dict] = None):
    for i, doc in enumerate(docs):
        print("#" + str(i) + ":")
        for key in doc.keys():
            print("   " + key + ":", str(doc[key]))


def inventory(docs):
    states: dict[str, int] = dict[str, int]()
    for doc in docs:
        status = doc['status']
        if status not in states.keys():
            states[status] = 0
        states[status] += 1
    states["TOTAL"] = len(docs)
    print("--- document inventory")
    for status in states:
        print(status + ":", states[status])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="list documents indexed by Amazon Q")
    parser.add_argument("-app", "--app_id", type=str, help="Q application id")
    parser.add_argument("-idx", "--idx_id", type=str, help="Q index id")
    parser.add_argument("-incl", "--include", type=str, help="comma-separated list of status to include")
    parser.add_argument("-excl", "--exclude", type=str, help="comma-separated list of status to exclude")
    parser.add_argument("-inv", "--inventory", action="store_true", help="with document inventory")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")
    args = parser.parse_args()

    if args.app_id is None or args.idx_id is None:
        raise ValueError("Q application id and index id must be specified - usage: python3 q_list_documents.py "
                         "--app_id <q-app-id> --idx_id <q-idx-id>")
    if args.include is not None and args.exclude is not None:
        raise ValueError("either --include or --exclude list of status can be specified but not both simultaneously")
    if args.verbose:
        print("Q API list_docs() called with app_id:", args.app_id, " - idx-id:", args.idx_id)

    documents: list[dict] = list_documents(app_id=args.app_id, idx_id=args.idx_id, verbose=args.verbose)
    filtered: list[dict] = list[dict]()
    if args.include:
        status_list = args.include.split(",")
        for document in documents:
            if document["status"] in status_list:
                filtered.append(document)
    elif args.exclude:
        status_list = args.exclude.split(",")
        for document in documents:
            if document["status"] not in status_list:
                filtered.append(document)
    else:
        filtered = documents

    print(json.dumps(filtered, indent=4, default=str))

    if args.inventory:
        inventory(documents)
