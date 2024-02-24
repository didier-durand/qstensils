q_list_docs is a tool to list the documents loaded into the Q index as part of its features based on Retrieval-Augmented Generation (RAG). Retrieval Augmented Generation
Retrieval Augmented Generation (RAG) is a natural language processing (NLP) technique. Using RAG, generative artificial intelligence (generative AI) is conditioned on specific documents that are retrieved from a dataset. Amazon Q has a built-in RAG system. A RAG model has the following two components: a) a retrieval component retrieves relevant documents for the user query.
b) b generation component takes the query and the retrieved documents and then generates an answer to the query using a large language model.

q_list_docs inventories those docs and returns them in JSON structure that can be further processed by piping it into other shell utilities like jq, sed, etc.

Filtering based on file status is available. For example, to retrieve all files that could not be properly indexed by the indexeer of your Amazon Q application, you can type the following comm

Usage:

Help: to obtain all details about possible command options, 


## To obtain a list indexed documents with their metadata
to obtain a full list of all documents, enter on command line from /src directory:
```shell
python3 list_docs.py --app_id <your-q-app-id> --idx_id <your-q-idx-id>  
```

some example:
```
    % python3 q_list_docs.py --app_id 64ce5747-3e5-4ec-a43-10c14d159f3 --idx_id 6b850c2-3e9-440-b4c-3dcabd8015 --json --inv

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
        "status": "INDEXED",
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

For help, use -h or --help option:
```shell
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



