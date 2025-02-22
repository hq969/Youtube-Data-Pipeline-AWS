<p align='center'>
<img src='https://github.com/waqarg2001/Youtube-Data-Pipeline-AWS/blob/main/assets/Icon.png' width=430 height=270 >
</p>

---

<h4 align='center'> Leveraging <a href='https://aws.amazon.com/' target='_blank'>AWS Cloud Services,</a> an ETL pipeline transforms YouTube video statistics data. Data is downloaded from <a href='https://kaggle.com/datasnaek/youtube-new'>Kaggle</a>, uploaded to an S3 bucket, and cataloged using AWS Glue for querying with Athena. AWS Lambda converts to Parquet format and stores it in a clean S3 bucket. AWS QuickSight then visualizes the materialised data, providing insights into YouTube video performance. </h4>

<p align='center'>
<img src="https://i.ibb.co/KxfMMsP/built-with-love.png" alt="built-with-love" border="0">
<img src="https://i.ibb.co/MBDK1Pk/powered-by-coffee.png" alt="powered-by-coffee" border="0">
<img src="https://i.ibb.co/CtGqhQH/cc-nc-sa.png" alt="cc-nc-sa" border="0">
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#tools">Tools</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#dashboard">Dashboard</a> •
  <a href="#screenshots">Screenshots</a> •
  <a href="#support">Support</a> •
  <a href="#license">License</a>
</p>


## Overview


This project utilizes AWS Cloud Services to build an efficient ETL pipeline for processing YouTube video statistics data. The data, available [here](https://kaggle.com/datasnaek/youtube-new), is downloaded from Kaggle and uploaded to an S3 bucket. AWS Glue catalogs the data, enabling seamless querying using Amazon Athena. The pipeline processes both JSON and CSV data, converting them into Parquet format. JSON data is transformed using AWS Lambda functions with AWS Data Wrangler layers, while CSV data is processed through visual ETL jobs in AWS Glue.

Data is first stored in a raw S3 bucket, then cleaned and organized in a cleansed bucket, and finally joined and stored in an analytics or materialized bucket. Automated ETL jobs run daily using AWS Glue workflows, ensuring up-to-date data processing. A simple QuickSight dashboard visualizes the cleansed data, providing valuable insights into YouTube video performance across different regions. This setup ensures a scalable and efficient data processing workflow, facilitating detailed analysis and reporting.



The repository directory structure is as follows:
```
├── assets/                        <- Includes assets for the repo.
│   └── (Contains images, architecture and quicksight dashboard)
│
├── data/                          <- Contains data used and processed by the project.
│   ├── raw/                      <- Raw data files (not included here due to large files size).
│   ├── cleansed/                 <- Cleansed data files.
│   └── analytics/                <- Materialized view for analytics and reporting.
│
├── docs/                          <- Documentation for the project.
│   └── solution methodology.pdf   <- Detailed project documentation.
│
├── scripts/                                       <- Python scripts for the ETL pipeline.
│   ├── etl_pipeline_csv_to_parquet.py             <- csv to parquet pipeline glue script.
│   ├── lambda_function.py                         <- Lambda function code.
│   └── etl_pipeline_materialised_view.py          <- materialised view pipeline glue script
│
├── README.md                      <- The top-level README for developers using this project.

```



## Tools 

To build this project, the following tools were used:

- AWS S3
- AWS Glue
- AWS Lambda/Layers
- Amazon Athena
- AWS QuickSight
- AWS Data Wrangler
- AWS Cloudwatch
- AWS IAM
- Python
- Pandas
- Spark
- Git

## Architecture

Following is the architecture of the project.

<p align='center'>
  <img src='https://github.com/waqarg2001/Youtube-Data-Pipeline-AWS/blob/main/assets/AWS_Python_ETL_Project_Architecture.png' height=385 width=650>
</p>  

## Dashboard

Access simplified dashboard from <a href='https://github.com/waqarg2001/Youtube-Data-Pipeline-AWS/blob/main/assets/dashboard.pdf'>here</a>.


## Screenshots

Following are project execution screenshots from AWS portal.

<img src="https://github.com/waqarg2001/Youtube-Data-Pipeline-AWS/blob/main/assets/ss1.png" width=900 height=400>
<br>
<img src="https://github.com/waqarg2001/Youtube-Data-Pipeline-AWS/blob/main/assets/ss2.png" width=900 height=400>

## Support

If you have any doubts, queries, or suggestions then, please connect with me on any of the following platforms:

[![Linkedin Badge][linkedinbadge]][linkedin] 
[![Gmail Badge][gmailbadge]][gmail]


## License

<a href = 'https://creativecommons.org/licenses/by-nc-sa/4.0/' target="_blank">
    <img src="https://i.ibb.co/mvmWGkm/by-nc-sa.png" alt="by-nc-sa" border="0" width="88" height="31">
</a>

This license allows reusers to distribute, remix, adapt, and build upon the material in any medium or format for noncommercial purposes only, and only so long as attribution is given to the creator. If you remix, adapt, or build upon the material, you must license the modified material under identical terms.



<!--Profile Link-->
[linkedin]: https://www.linkedin.com/in/waqargul
[gmail]: mailto:waqargul6@gmail.com

<!--Logo Link -->
[linkedinbadge]: https://img.shields.io/badge/waqargul-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[gmailbadge]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
