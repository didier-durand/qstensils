<img src="img/q-logo.png" height="120" alt="Q logo">

## qstensils: tools and utility scripts for Amazon Q

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/1c826b70f5dd4b45b350c0337f75075d)](https://app.codacy.com/gh/didier-durand/qstensils/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![build workflow](https://github.com/didier-durand/qstensils/actions/workflows/build.yml/badge.svg)](https://github.com/didier-durand/qstensils/actions)

 * [Provided Tools ](#provided-tools)
 * [About Amazon Q](#about-amazon-q) 
 * [Usage](#usage)
 * [Security](#security)

### Provided Tools

**Disclaimer**: the scripts provided in this repository reflect the state of service Amazon Q for Business as it was launched 
in December 2023 by AWS in Preview mode. Due to this Preview mode, the features of Amazon Q and their 
implementation can change at any time during Preview and for General Availability. Such changes may require updates to this repository.

This project gathers diverse tools and utility scripts to explore and operate Amazon Q for Business. 
We will add new scripts based on your demand: feel free to cut a ticket
[here](https://github.com/didier-durand/qstensils/issues) if you have a need or idea!

We currently provide the following utilities:
1. [q_list_applications](doc/q_list_applications.md) to inventory the applications existing in a given region of an AWS account. The returned 
json structure details the various components (indices, data source, retrievers, etc.) of those Amazon Q 
applications.
2. [q_list_data_source_sync_jobs](doc/q_list_data_source_sync_jobs.md) to list the history of index synchronization 
jobs executed on a given Q data source. This script adds additional metric like total job duration, document scan rate 
and average scan duration per document.
3. [q_list_documents](doc/q_list_documents.md) to list all the documents of an Amazon Q index and get all their associated metadata,
in particular their status. The returned list can be filtered (via inclusion or exclusion) to return 
only a fraction of those documents for example based on their indexing status.
4. [q_list_conversations](doc/q_list_conversations.md) to obtain all list of all past conversations between 
a given application and a user as remembered by Amazon Q.
5. [q_chat](doc/q_chat.md) to be able to script conversations (based on single or multiple messages) with the 
assistant of Amazon Q.

All those scripts return json structures that can be further processed in [shell pipelines](https://en.wikipedia.org/wiki/Pipeline_(Unix)) with various utilities 
like jq, sed, awk, etc.

Those scripts rely on the Python AWS SDK. All APIs related to Q for business are described in details in the 
[SDK boto3 public documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qbusiness.html).

### About Amazon Q

[![IMAGE ALT TEXT](http://img.youtube.com/vi/bZsIPinetV4/0.jpg)](http://www.youtube.com/watch?v=bZsIPinetV4 "Amazon Q")

Amazon Q is a fully managed, generative-AI powered assistant that can be configured to answer questions, 
provide summaries, generate content, and complete tasks based on data in your enterprise. Amazon Q 
provides immediate and relevant information to its users, and helps streamline tasks and 
accelerate problem-solving.

An Amazon Q application relies on a corpus of documents to build its specific Q index. This corpus of documents is 
stored in one or more document repositories (S3, Jira, Quip, etc.) called Q data sources. The answers to user questions 
by the assistant will be prepared through the leverage of RAG technology. 

[Retrieval-Augmented Generation](https://www.promptingguide.ai/techniques/rag) (RAG) is a natural language processing (NLP) technique. It is composed of a 
language model-based system, usually a [Large Language Model](https://en.wikipedia.org/wiki/Large_language_model) (LLM), that accesses external knowledge sources 
to complete tasks. This enables more contextuality, factual consistency, improves reliability of the generated 
responses, and helps to mitigate the problem of "hallucinations".

### Security

The scripts of this project assume that the AWS user reflected by environment variables named `AWS_ACCESS_KEY_ID` and 
`AWS_SECRET_ACCESS_KEY` has proper [IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) in terms of authorizations 
to access the APIs of Amazon Q in the AWS account. See 
[IAM policy examples](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/security_iam_id-based-policy-examples.html) 
in the [Security section](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/security-iam.html) of Q Documentation for all details.

### Usage

from the /src directory of this project, the following commands can be used to get all command options

for list_applications.py

```
%python3 q_list_applications.py -h
usage: q_list_applications.py [-h] [-v]

list applications, indexes, retrievers, web experiences, plugins, etc. running in Amazon Q for business

options:
  -h, --help     show this help message and exit
  -v, --verbose  verbose mode
```

q_list_data_source_sync_jobs

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

for q_list_documents.py

```
% python3 q_list_documents.py  -h                                                                                                   
usage: q_list_documents.py [-h] [-a APP_ID] [-i IDX_ID] [-incl INCLUDE] [-excl EXCLUDE] [-inv] [-v]

list documents indexed by Amazon Q

options:
  -h, --help            show this help message and exit
  -a APP_ID, --app_id APP_ID
                        Q application id
  -i IDX_ID, --idx_id IDX_ID
                        Q index id
  -incl INCLUDE, --include INCLUDE
                        comma-separated list of status to include
  -excl EXCLUDE, --exclude EXCLUDE
                        comma-separated list of status to exclude
  -inv, --inventory     with document inventory
  -v, --verbose         verbose mode
```

for q_list_conversations.py

```
% python3 q_list_conversations.py -h
usage: q_list_conversations.py [-h] [-a APP_ID] [-u USR_ID] [-v]

list documents indexed by Amazon Q

options:
  -h, --help            show this help message and exit
  -a APP_ID, --app_id APP_ID
                        Q application id
  -u USR_ID, --usr_id USR_ID
                        Q user id
  -v, --verbose         verbose mode
```
for q_chat.py

```
% python3 q_chat.py  -h
usage: q_chat.py [-h] [-a APP_ID] [-u USR_ID] [-p PROMPT] [-f FILE] [-c CNV_ID] [-m MSG_ID] [-d] [-v]

ask a question to a Q application and get answer

options:
  -h, --help            show this help message and exit
  -a APP_ID, --app_id APP_ID
                        Q application id
  -u USR_ID, --usr_id USR_ID
                        Q index id
  -p PROMPT, --prompt PROMPT
                        question prompt or path to file with list of prompts
  -f FILE, --file FILE  path to attachment file
  -c CNV_ID, --cnv_id CNV_ID
                        Q conversation id (only to continue an existing conversation)
  -m MSG_ID, --msg_id MSG_ID
                        Q parent message id (only to continue an existing conversation)
  -d, --details         full conversation details
  -v, --verbose         verbose mode
```
