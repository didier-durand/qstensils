import json
from pprint import pprint
import argparse

import boto3

q_client = boto3.client("qbusiness")  # noqa


def check_response(resp: dict, http_status_code=200) -> bool:
    assert resp["ResponseMetadata"]["HTTPStatusCode"] == http_status_code
    return True


def list_data_source_sync_jobs(app_id: str = "", idx_id: str = "",
                               ds_id: str = "", verbose: bool = False) -> list[dict] | None:
    resp = q_client.list_data_source_sync_jobs(applicationId=app_id, indexId=idx_id, dataSourceId=ds_id,
                                               maxResults=10)
    if verbose:
        pprint(resp)
    check_response(resp)
    if "nextToken" in resp:
        print("ERROR: paginated response not yet implemented for sync jobs: please,"
              "open a ticket at https://github.com/didier-durand/qstensils/issues")
    if "history" in resp:
        return resp["history"]
    return None


def list_data_source_sync_jobs_with_details(app_id: str = "", idx_id: str = "",
                                            ds_id: str = "", verbose: bool = False) -> list[dict] | None:
    jobs = list_data_source_sync_jobs(app_id=app_id, idx_id=idx_id, ds_id=ds_id, verbose=verbose)
    if jobs is not None and len(jobs) > 0:
        for job in jobs:
            if "endTime" in job:
                duration = job["endTime"] - job["startTime"]
                if "duration_s" in job:
                    raise ValueError("duration_s dict key already present")
                job["duration"] = duration
                job["duration_s"] = duration.seconds
                if "metrics" in job and "documentsScanned" in job["metrics"]:
                    scan_rate = int(job["metrics"]["documentsScanned"]) / int(duration.seconds)
                    job["metrics"]["scanRate"] = str(scan_rate)
                    job["metrics"]["averageDocumentScanDuration"] = str(1 / scan_rate)
        return jobs
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="list synchronization jobs executed for a given data source "
                                                 "of an Amazon Q application")
    parser.add_argument("-a", "--app_id", type=str, help="Q application id")
    parser.add_argument("-i", "--idx_id", type=str, help="Q data source id")
    parser.add_argument("-d", "--ds_id", type=str, help="Q data source id")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")
    args = parser.parse_args()
    sync_jobs = list_data_source_sync_jobs_with_details(app_id=args.app_id, idx_id=args.idx_id, ds_id=args.ds_id,
                                                        verbose=args.verbose)
    print(json.dumps(sync_jobs, indent=4, default=str))
