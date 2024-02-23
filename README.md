<img src="img/q-logo.png" height="120" alt="Q logo">

# qstensils: tools and utility scripts for Amazon Q

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1c826b70f5dd4b45b350c0337f75075d)](https://app.codacy.com/gh/didier-durand/qstensils/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![build workflow](https://github.com/didier-durand/qstensils/actions/workflows/build.yml/badge.svg)](https://github.com/didier-durand/qstensils/actions)

This project gathers diverse tools and utility scripts to explore and operate Amazon Q for Business. 

Amazon Q is a fully managed, generative-AI powered assistant that you can configure to answer questions, provide summaries, generate content, and complete tasks based on data in your enterprise. Amazon Q provides immediate and relevant information to employees, and helps streamline tasks and accelerate problem solving.

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
% python3 q_list_docs.py -h                                                                                                  
usage: q_list_docs.py [-h] [-app APP_ID] [-idx IDX_ID] [-j] [-incl INCLUDE] [-excl EXCLUDE] [-inv] [-v]

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

## Security

The scripts assume that the user reflected by environment variables named `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` has proper credentials to access the APIs of Amazon Q. See [IAM policy examples](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/security_iam_id-based-policy-examples.html) in the [Security section](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/security-iam.html) of Q Documentation for all details.

