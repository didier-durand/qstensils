import json
from pprint import pprint
import argparse

import boto3

q_client = boto3.client("qbusiness")  # noqa


def check_response(resp: dict, http_status_code=200) -> bool:
    assert resp['ResponseMetadata']['HTTPStatusCode'] == http_status_code
    return True


def list_applications(verbose: bool = False) -> list[dict] | None:
    resp = q_client.list_applications(maxResults=100)
    if verbose:
        pprint(resp)
    check_response(resp)
    if "nextToken" in resp:
        print("ERROR: paginated response not yet implemented for applications: please,"
              "open a ticket at https://github.com/didier-durand/qstensils/issues")
    if "applications" in resp:
        return resp["applications"]
    return None


def list_plugins(application_id: str = "", verbose: bool = False) -> list[dict] | None:
    resp = q_client.list_plugins(applicationId=application_id, maxResults=50)
    if verbose:
        pprint(resp)
    check_response(resp)
    if "nextToken" in resp:
        print("ERROR: paginated response not yet implemented for plugins: please,"
              " open a ticket at https://github.com/didier-durand/qstensils/issues")
    if "plugins" in resp:
        return resp["plugins"]
    return None


def list_indices(application_id: str = "", verbose: bool = False) -> list[dict] | None:
    resp = q_client.list_indices(applicationId=application_id, maxResults=100)
    if verbose:
        pprint(resp)
    check_response(resp)
    if "nextToken" in resp:
        print("ERROR: paginated response not yet implemented for indices: please,"
              " open a ticket at https://github.com/didier-durand/qstensils/issues")
    if "indices" in resp:
        return resp["indices"]
    return None


def list_data_sources(application_id: str = "", index_id: str = "", verbose: bool = False) -> list[dict] | None:
    resp = q_client.list_data_sources(applicationId=application_id, indexId=index_id, maxResults=10)
    if verbose:
        pprint(resp)
    check_response(resp)
    if "nextToken" in resp:
        print("ERROR: paginated response not yet implemented for indices: please,"
              "o pen a ticket at https://github.com/didier-durand/qstensils/issues")
    if "dataSources" in resp:
        return resp["dataSources"]
    return None


def list_retrievers(application_id: str = "", verbose: bool = False) -> list[dict] | None:
    resp = q_client.list_retrievers(applicationId=application_id, maxResults=50)
    if verbose:
        pprint(resp)
    check_response(resp)
    if "nextToken" in resp:
        print("ERROR: paginated response not yet implemented for retrievers: please,"
              " open a ticket at https://github.com/didier-durand/qstensils/issues")
    if "retrievers" in resp:
        return resp["retrievers"]
    return None


def list_web_experiences(application_id: str = "", verbose: bool = False) -> list[dict] | None:
    resp = q_client.list_web_experiences(applicationId=application_id, maxResults=100)
    if verbose:
        pprint(resp)
    check_response(resp)
    if "nextToken" in resp:
        print("ERROR: paginated response not yet implemented for web experiences: please,"
              " open a ticket at https://github.com/didier-durand/qstensils/issues")
    if "webExperiences" in resp:
        return resp["webExperiences"]
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="list applications, indexes, retrievers, web experiences, plugins,  "
                                                 "etc,running in Amazon Q for business")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")
    args = parser.parse_args()

    q_objects: list[dict] = list[dict]()
    applications: list[dict] = list_applications(verbose=args.verbose)
    if applications is not None and len(applications) > 0:
        for application in applications:
            app_id = application["applicationId"]
            application = q_client.get_application(applicationId=app_id)
            check_response(application)
            del application["ResponseMetadata"]
            q_objects.append(application)
            indices: list[dict] = list_indices(application_id=app_id, verbose=args.verbose)
            if indices is not None and len(indices) > 0:
                app_indices: list[dict] = list[dict]()
                for index in indices:
                    idx_id = index["indexId"]
                    index = q_client.get_index(applicationId=app_id, indexId=idx_id)
                    check_response(index)
                    del index["ResponseMetadata"]
                    app_indices.append(index)
                    data_sources: list[dict] = list_data_sources(application_id=app_id, index_id=idx_id,
                                                                 verbose=args.verbose)
                    if data_sources is not None and len(data_sources) > 0:
                        idx_data_sources: list[dict] = list[dict]()
                        for data_source in data_sources:
                            ds_id = data_source["dataSourceId"]
                            data_source = q_client.get_data_source(applicationId=app_id, indexId=idx_id,
                                                                   dataSourceId=ds_id)
                            check_response(data_source)
                            del data_source["ResponseMetadata"]
                            idx_data_sources.append(data_source)
                        index["dataSources"] = idx_data_sources
                application["indices"] = app_indices
            plugins: list[dict] = list_plugins(application_id=app_id, verbose=args.verbose)
            if plugins is not None and len(plugins) > 0:
                app_plugins: list[dict] = list[dict]()
                for plugin in plugins:
                    plg_id = plugin["pluginId"]
                    plugin = q_client.get_plugin(applicationId=app_id)
                    check_response(plugin)
                    del plugin["ResponseMetadata"]
                    app_plugins.append(plugin)
                application["plugins"] = app_plugins
            retrievers: list[dict] = list_retrievers(application_id=app_id, verbose=args.verbose)
            if retrievers is not None and len(retrievers) > 0:
                app_retrievers: list[dict] = list[dict]()
                for retriever in retrievers:
                    rtv_id = retriever["retrieverId"]
                    retriever = q_client.get_retriever(applicationId=app_id, retrieverId=rtv_id)
                    check_response(retriever)
                    del retriever["ResponseMetadata"]
                    app_retrievers.append(retriever)
                application["retrievers"] = app_retrievers
            web_experiences: list[dict] = list_web_experiences(application_id=app_id, verbose=args.verbose)
            if web_experiences is not None and len(retrievers) > 0:
                app_web_experiences: list[dict] = list[dict]()
                for web_experience in web_experiences:
                    wxp_id = web_experience["webExperienceId"]
                    web_experience = q_client.get_web_experience(applicationId=app_id, webExperienceId=wxp_id)
                    check_response(web_experience)
                    del web_experience["ResponseMetadata"]
                    app_web_experiences.append(web_experience)
                application["webExperiences"] = web_experiences

    print(json.dumps(q_objects, indent=4, default=str))
