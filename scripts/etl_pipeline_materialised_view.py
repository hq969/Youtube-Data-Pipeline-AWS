import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog- reference
AWSGlueDataCatalogreference_node1717006854575 = glueContext.create_dynamic_frame.from_catalog(database="db_de_project_cleansed_statistics_reference", table_name="cleansed_statisitics_reference_data", transformation_ctx="AWSGlueDataCatalogreference_node1717006854575")

# Script generated for node AWS Glue Data Catalog- stats
AWSGlueDataCatalogstats_node1717006797829 = glueContext.create_dynamic_frame.from_catalog(database="db_de_project_cleansed_statistics_reference", table_name="cleansed_statistics", transformation_ctx="AWSGlueDataCatalogstats_node1717006797829")

# Script generated for node Inner Join
InnerJoin_node1717006913509 = Join.apply(frame1=AWSGlueDataCatalogstats_node1717006797829, frame2=AWSGlueDataCatalogreference_node1717006854575, keys1=["category_id"], keys2=["id"], transformation_ctx="InnerJoin_node1717006913509")

# Script generated for node Amazon S3- analytics
AmazonS3analytics_node1717007001029 = glueContext.getSink(path="s3://youtube-data-eng-project-analytics-useast1-767398140492-dev/youtube/materialsed-view/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=["region", "category_id"], enableUpdateCatalog=True, transformation_ctx="AmazonS3analytics_node1717007001029")
AmazonS3analytics_node1717007001029.setCatalogInfo(catalogDatabase="db_de_project_analytics_materialised",catalogTableName="materialised_view")
AmazonS3analytics_node1717007001029.setFormat("glueparquet", compression="snappy")
AmazonS3analytics_node1717007001029.writeFrame(InnerJoin_node1717006913509)
job.commit()