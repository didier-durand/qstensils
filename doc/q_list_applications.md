# UNDER CONSTRUCTION !

### Usage

```
%python3 q_list_applications.py

[
    {
        "applicationArn": "arn:aws:qbusiness:region:account-id:application/application-id",
        "applicationId": "application-id",
        "attachmentsConfiguration": {
            "attachmentsControlMode": "ENABLED"
        },
        "createdAt": "2024-02-21 11:00:00.581000+01:00",
        "displayName": "QMovies-2",
        "error": {},
        "roleArn": "arn:aws:iam::account-id:role/role-name,
        "status": "ACTIVE",
        "updatedAt": "2024-02-21 11:00:00.581000+01:00",
        "indices": [
            {
                "applicationId": "application-id",
                "capacityConfiguration": {
                    "units": 1
                },
                "createdAt": "2024-02-21 11:00:01.196000+01:00",
                "displayName": "QMovies-2-idx",
                "documentAttributeConfigurations": [
                    {
                        "name": "_authors",
                        "search": "DISABLED",
                        "type": "STRING_LIST"
                    },
                    {
                        "name": "_category",
                        "search": "DISABLED",
                        "type": "STRING"
                    },
                    {
                        "name": "_created_at",
                        "search": "DISABLED",
                        "type": "DATE"
                    },
                    {
                        "name": "_data_source_id",
                        "search": "DISABLED",
                        "type": "STRING"
                    },
                    {
                        "name": "_document_title",
                        "search": "ENABLED",
                        "type": "STRING"
                    },
                    {
                        "name": "_file_type",
                        "search": "DISABLED",
                        "type": "STRING"
                    },
                    {
                        "name": "_language_code",
                        "search": "DISABLED",
                        "type": "STRING"
                    },
                    {
                        "name": "_last_updated_at",
                        "search": "DISABLED",
                        "type": "DATE"
                    },
                    {
                        "name": "_source_uri",
                        "search": "DISABLED",
                        "type": "STRING"
                    },
                    {
                        "name": "_version",
                        "search": "DISABLED",
                        "type": "STRING"
                    },
                    {
                        "name": "_view_count",
                        "search": "DISABLED",
                        "type": "NUMBER"
                    }
                ],
                "error": {},
                "indexArn": "arn:aws:qbusiness:region:account-id:application/application-id/index/index-id",
                "indexId": "index-id",
                "indexStatistics": {
                    "textDocumentStatistics": {
                        "indexedTextBytes": 720135,
                        "indexedTextDocumentCount": 992
                    }
                },
                "status": "ACTIVE",
                "updatedAt": "2024-02-21 11:00:01.196000+01:00",
                "dataSources": [
                    {
                        "applicationId": "application-id",
                        "configuration": {
                            "syncMode": "FORCED_FULL_CRAWL",
                            "additionalProperties": {
                                "inclusionPatterns": [],
                                "maxFileSizeInMegaBytes": "50",
                                "inclusionPrefixes": [],
                                "exclusionPatterns": [],
                                "exclusionPrefixes": []
                            },
                            "type": "S3",
                            "repositoryConfigurations": {
                                "document": {
                                    "fieldMappings": [
                                        {
                                            "dataSourceFieldName": "s3_document_id",
                                            "indexFieldName": "s3_document_id",
                                            "indexFieldType": "STRING"
                                        }
                                    ]
                                }
                            },
                            "connectionConfiguration": {
                                "repositoryEndpointMetadata": {
                                    "BucketName": "aws-q-didier-durand"
                                }
                            }
                        },
                        "createdAt": "2024-02-21 11:00:03.819000+01:00",
                        "dataSourceArn": "arn:aws:qbusiness:region:account-id:application/application-id/index/index-id/data-source/data-source-id",
                        "dataSourceId": "data-source-id",
                        "description": "",
                        "displayName": "QMovies-2-ds-0",
                        "error": {},
                        "indexId": "index-id",
                        "roleArn": "arn:aws:iam::account-id:role/role-name",
                        "status": "ACTIVE",
                        "syncSchedule": "",
                        "type": "S3",
                        "updatedAt": "2024-02-21 11:00:03.819000+01:00"
                    }
                ]
            }
        ],
        "retrievers": [
            {
                "applicationId": "application-id",
                "configuration": {
                    "nativeIndexConfiguration": {
                        "indexId": "69b850c2-3e91-4640-b4dc-3dcabdd28015"
                    }
                },
                "createdAt": "2024-02-21 13:14:17.446000+01:00",
                "displayName": "QMovies-2-rtv",
                "retrieverArn": "arn:aws:qbusiness:region:account-id:application/application-id/retriever/retriever-id",
                "retrieverId": "retriever-id",
                "roleArn": "arn:aws:iam::account-id:role/role-name",
                "status": "ACTIVE",
                "type": "NATIVE_INDEX",
                "updatedAt": "2024-02-21 13:14:17.447000+01:00"
            }
        ],
        "webExperiences": [
            {
                "createdAt": "2024-02-21 11:00:01.983000+01:00",
                "defaultEndpoint": "https://ymajundt.chat.qbusiness.region.on.aws/",
                "status": "PENDING_AUTH_CONFIG",
                "updatedAt": "2024-02-23 09:46:27.369000+01:00",
                "webExperienceId": "web-experience-id"
            }
        ]
    }
]

```

An Amazon Q application is a bundle of multiple components working together. 
They are defined in the service documentation at page.

The most important ones are the application itself, its index delivering the RAG features, 
the data source(s) from which the index is built, a retriever retrieving the documents used 
for answering the user prompts, the web experience offering a default interactive user interface.