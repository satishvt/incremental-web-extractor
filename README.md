# Incremental Web Data Extraction Tool

This application was for built for personal purposes, to extract the pages from a website "incrementally" i.e. any new pages or identify/extract new web pages.

Backgroun and more details of the application is available in the below Medium article.

https://medium.com/@satish.vt/incremental-web-data-extraction-with-an-intentional-complex-architecture-to-learn-experiment-622696c09ba3


**Disclaimer**: 
- **This code base is a reference**, One need to inspect the code and change any parameters like User-ids, paths, table names etc. 
- I wrote this code on Mac (OSX), so you might need to tweak to suite your run time environment

**Pre-requisites**:
- Install PostgreSQL OR any other RDBMS. I've named the schema "news" and table name as "firstpost" with fields as "url":bigint, "hash":varchar(32)
- Install Kafka, and create topics. 

**Code**:
- Components named "producer_\*.py" does the bulk of the job
- Components named "consumer_\*.py" does the consuming of the messages and stores the file
- "create_crons.py" is to create crons
