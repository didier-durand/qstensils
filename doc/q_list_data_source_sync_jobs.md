## q_list_data_source_sync_jobs

An Amazon Q application leverages [Retrieval-Augmented Generation](https://www.promptingguide.ai/techniques/rag) (RAG) to deliver more contextuality, 
better factual consistency, to improve reliability of the generated responses, and to help to mitigate the 
problem of "hallucinations".

The RAG index is built from the data source(s) associated to the application. The documents contained in 
those data sources are analyzed by the indexer. Their embeddings and other metadata are placed into the index 
to be able to select the most relevant documents improving the user prompt on each questions.

Script [q_list_data_source_sync_jobs ](../src/q_list_data_source_sync_jobs.py) will list the history of all index 
synchronization jobs that have executed on a given Q data source. It will add interesting metrics like job duration 
and document scan rate.

### Usage

```
% python3 q_list_data_source_sync_jobs.py -a 64ce5747-3ce5-43ec-a433-10c143d159f3 -i 69b850c2-3e91-4640-b4dc-3dcabdd28015 -d 7595f4bf-7de1-4821-8853-643798cf6b20


[
    {
        "endTime": "2024-02-25 07:28:12.576000+01:00",
        "error": {},
        "executionId": "1414a953-214e-4ff5-abc8-556d4ce3a1b1",
        "metrics": {
            "documentsAdded": "0",
            "documentsDeleted": "0",
            "documentsFailed": "0",
            "documentsModified": "810",
            "documentsScanned": "999",
            "scanRate": "2.692722371967655"
        },
        "startTime": "2024-02-25 07:22:00.869000+01:00",
        "status": "SYNCING_INDEXING",
        "duration": "0:06:11.707000",
        "duration_s": 371
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
            "scanRate": "0.43134715025906734"
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
            "scanRate": "0.4459821428571429"
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
            "scanRate": "0.4714487966021708"
        },
        "startTime": "2024-02-21 11:25:04.942000+01:00",
        "status": "INCOMPLETE",
        "duration": "0:35:19.414000",
        "duration_s": 2119
    }
]
```