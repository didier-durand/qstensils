## q_list_data_source_sync_jobs

* [Description](#description)
* [Usage](#usage)
* [Help and Security](#help-and-security)

## Description

An Amazon Q application leverages [Retrieval-Augmented Generation](https://www.promptingguide.ai/techniques/rag) (aka RAG) to deliver more contextuality, 
better factual consistency, to improve reliability of the generated responses and to help to mitigate the 
problem of ["hallucinations"](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)).

The Q RAG index is built from the content of the Q data source(s) like S3, relational databases,etc. associated to the 
application. The documents contained in those data sources are analyzed by the indexer. Their [vector embeddings](https://en.wikipedia.org/wiki/Sentence_embedding) 
and other metadata are placed into the index to be able to select the most relevant documents improving the user prompt 
on each question. The Q retriever will leverage the data contained in the RAG index to fetch and add additional documents to 
question / prompt coming from the user. This enriched prompt will allow the Q LLM to provide a better answer.

Script [q_list_data_source_sync_jobs ](../src/q_list_data_source_sync_jobs.py) will list the history of all index 
synchronization jobs that have executed on a given Q data source. It will add interesting metrics like job duration 
and document scan rate.

### Usage

```
% python3 q_list_data_source_sync_jobs.py -a <app-id> -i <idx_id> -d <data-source-id>

[
    {
        "endTime": "2024-02-25 07:48:40.853000+01:00",
        "error": {},
        "executionId": "1414a953-214e-4ff5-abc8-556d4ce3a1b1",
        "metrics": {
            "documentsAdded": "0",
            "documentsDeleted": "0",
            "documentsFailed": "6",
            "documentsModified": "993",
            "documentsScanned": "999",
            "scanRate": "0.624765478424015",
            "averageDocumentScanDuration": "1.6006006006006006"
        },
        "startTime": "2024-02-25 07:22:00.869000+01:00",
        "status": "INCOMPLETE",
        "duration": "0:26:39.984000",
        "duration_s": 1599
    },
    {
        "endTime": "2024-02-24 11:40:38.389000+01:00",
        "error": {},
        "executionId": "c0bda9b8-1b54-41b2-af26-ee559e6406da",
        "metrics": {
            "documentsAdded": "0",
            "documentsDeleted": "0",
            "documentsFailed": "8",
            "documentsModified": "991",
            "documentsScanned": "999",
            "scanRate": "0.43134715025906734",
            "averageDocumentScanDuration": "2.3183183183183185"
        },
        "startTime": "2024-02-24 11:02:01.815000+01:00",
        "status": "INCOMPLETE",
        "duration": "0:38:36.574000",
        "duration_s": 2316
    },
    {
        "endTime": "2024-02-24 10:02:37.580000+01:00",
        "error": {},
        "executionId": "44e993e2-15a0-40cb-9f89-5dc14cdf1eab",
        "metrics": {
            "documentsAdded": "7",
            "documentsDeleted": "0",
            "documentsFailed": "13",
            "documentsModified": "979",
            "documentsScanned": "999",
            "scanRate": "0.4459821428571429",
            "averageDocumentScanDuration": "2.2422422422422423"
        },
        "startTime": "2024-02-24 09:25:17.527000+01:00",
        "status": "INCOMPLETE",
        "duration": "0:37:20.053000",
        "duration_s": 2240
    },
    {
        "endTime": "2024-02-21 12:00:24.356000+01:00",
        "error": {},
        "executionId": "4ec5a054-c430-4fec-907e-333b20d9693f",
        "metrics": {
            "documentsAdded": "992",
            "documentsDeleted": "0",
            "documentsFailed": "7",
            "documentsModified": "0",
            "documentsScanned": "999",
            "scanRate": "0.4714487966021708",
            "averageDocumentScanDuration": "2.121121121121121"
        },
        "startTime": "2024-02-21 11:25:04.942000+01:00",
        "status": "INCOMPLETE",
        "duration": "0:35:19.414000",
        "duration_s": 2119
    }
]
```

### Help and Security

To properly set up the security definitions in AWS account for use of this script, see [README](/)

```
% python3 q_list_data_source_sync_jobs.py -h
usage: q_list_data_source_sync_jobs.py [-h] [-a APP_ID] [-i IDX_ID] [-d DS_ID] [-v]

list synchronization jobs executed for a given data source of an Amazon Q application

options:
  -h, --help            show this help message and exit
  -a APP_ID, --app_id APP_ID
                        Q application id
  -i IDX_ID, --idx_id IDX_ID
                        Q data source id
  -d DS_ID, --ds_id DS_ID
                        Q data source id
  -v, --verbose         verbose mode
```
