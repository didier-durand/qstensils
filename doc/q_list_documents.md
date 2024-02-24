## q_list_documents

* [Rationale](#rationale)
* [Usage](#usage)
* [Help and Security](#help-and-security)

### Rationale

q_list_documents is a tool to list the documents loaded into the Q index. This list can be used to confirm its content, 
confirm its completeness (via document status), establish its freshness (via dates of last updates), etc.

An Amazon Q application relies on a corpus of documents to build its specific Q index. This corpus of documents is 
stored in one or more document repositories (S3, Jira, Quip, etc.) called Q data sources. The answers to user questions 
by the assistant will be prepared through the leverage of RAG technology. [Retrieval-Augmented Generation](https://www.promptingguide.ai/techniques/rag) 
(RAG) is a natural language processing (NLP) technique. It is composed of a language model-based system, 
usually a [Large Language Model](https://en.wikipedia.org/wiki/Large_language_model) (LLM), that accesses 
external knowledge sources to complete tasks. 
This enables more factual consistency, improves reliability of the generated responses, and helps to mitigate the 
problem of "hallucination". Using RAG, generative artificial intelligence (generative AI) is conditioned on specific 
documents that are retrieved from a well-defined dataset. 

Amazon Q has a built-in RAG system. The RAG model has the following two components: a) a retrieval component retrieves 
relevant documents for the user query. b) a generation component (based on LLM(s)) which takes the query and 
the retrieved documents and then generates an answer to the query using a large language model. The documents provided 
by the retriever allow the LLM to deliver a more specific answer to the question.

q_list_docs inventories those docs and returns them in JSON structure that can be further processed by piping it into other shell utilities like jq, sed, etc.

Filtering based on file status is available. For example, to retrieve all files that could not be properly indexed by the indexeer of your Amazon Q application, you can type the following comm

### Usage

to obtain a full list of all documents, enter on command line from /src directory:
```
python3 list_docs.py --app_id <your-q-app-id> --idx_id <your-q-idx-id>  
```

some example (with a fraction of the results):
```
    % python3 q_list_docs.py --app_id 123-abc-456 --idx_id 789-xyz-987  --json --inv

    <.....> 
    {
        "createdAt": "2024-02-21 11:31:00.618000+01:00",
        "documentId": "s3://bucket-name/Ying xiong.json",
        "error": {},
        "status": "INDEXED",
        "updatedAt": "2024-02-21 11:47:25.755000+01:00"
    },
    {
        "createdAt": "2024-02-21 11:31:00.500000+01:00",
        "documentId": "s3://bucket-name/Watership Down.json",
        "error": {},
        "status": "INDEXED",
        "updatedAt": "2024-02-21 11:47:30.810000+01:00"
    },
    {
        "createdAt": "2024-02-21 11:31:00.236000+01:00",
        "documentId": "s3://bucket-name/Unforgiven.json",
        "error": {},
        "status": "INDEXED",
        "updatedAt": "2024-02-21 11:47:02.884000+01:00"
    },
    {
        "createdAt": "2024-02-21 11:31:00.238000+01:00",
        "documentId": "s3://bucket-name/Viskningar och rop.json",
        "error": {},
        "status": "INDEXED",
        "updatedAt": "2024-02-21 11:47:14.965000+01:00"
    },
    {
        "createdAt": "2024-02-21 11:31:00.422000+01:00",
        "documentId": "s3://bucket-name/Togo.json",
        "error": {},
        "status": "INDEXED",
        "updatedAt": "2024-02-21 11:47:09.220000+01:00"
    },
    {
        "createdAt": "2024-02-21 11:31:00.709000+01:00",
        "documentId": "s3://bucket-name/What Ever Happened to Baby Jane?.json",
        "error": {},
        "status": "DOCUMENT_FAILED_TO_INDEX",
        "updatedAt": "2024-02-21 11:47:46.031000+01:00"
    },
    {
        "createdAt": "2024-02-21 11:31:00.698000+01:00",
        "documentId": "s3://bucket-name/Vicky Donor.json",
        "error": {},
        "status": "INDEXED",
        "updatedAt": "2024-02-21 11:47:53.677000+01:00"
    }
]
--- document inventory
INDEXED: 992
DOCUMENT_FAILED_TO_INDEX: 7
TOTAL: 999
```

### Help and Security

To properly set up the security definitions in AWS account for use of this script, see [README](/README.md)

```
% python3 q_list_documents.py -h


usage: q_list_documents.py [-h] [-app APP_ID] [-idx IDX_ID] [-j] [-incl INCLUDE] [-excl EXCLUDE] [-inv] [-v]

list documents indexed by Amazon Q

options:
  -h, --help            show this help message and exit
  -app APP_ID, --app_id APP_ID
                        Q application id
  -idx IDX_ID, --idx_id IDX_ID
                        Q index id
  -j, --json            json format for results
  -incl INCLUDE, --include INCLUDE
                        comma-separated list of status to include
  -excl EXCLUDE, --exclude EXCLUDE
                        comma-separated list of status to exclude
  -inv, --inventory     with document inventory
  -v, --verbose         verbose mode
```



