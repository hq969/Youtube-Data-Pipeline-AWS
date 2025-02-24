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

# Define the pushdown predicate
predicate_pushdown = "region in ('ca','gb','us')"

# Script generated for node Source S3 using catalog table
SourceS3_node = glueContext.create_dynamic_frame.from_catalog(
    database = "db_de_project_raw_statistics_reference",
    table_name = "raw_statistics",
    push_down_predicate = predicate_pushdown,
    transformation_ctx = "SourceS3_node"
)

# Check the schema of the dynamic frame
SourceS3_node.printSchema()

# Script generated for node change data type
changedatatype_node = ApplyMapping.apply(
    frame=SourceS3_node,
    mappings=[
        ("video_id", "string", "video_id", "string"),
        ("trending_date", "string", "trending_date", "string"),
        ("title", "string", "title", "string"),
        ("channel_title", "string", "channel_title", "string"),
        ("category_id", "bigint", "category_id", "bigint"),
        ("publish_time", "string", "publish_time", "string"),
        ("tags", "string", "tags", "string"),
        ("views", "bigint", "views", "bigint"),
        ("likes", "bigint", "likes", "bigint"),
        ("dislikes", "bigint", "dislikes", "bigint"),
        ("comment_count", "bigint", "comment_count", "bigint"),
        ("thumbnail_link", "string", "thumbnail_link", "string"),
        ("comments_disabled", "boolean", "comments_disabled", "boolean"),
        ("ratings_disabled", "boolean", "ratings_disabled", "boolean"),
        ("video_error_or_removed", "boolean", "video_error_or_removed", "boolean"),
        ("description", "string", "description", "string"),
        ("region", "string", "region", "string")  # Ensure region is included
    ],
    transformation_ctx="changedatatype_node"
)



# Convert DynamicFrame to DataFrame and coalesce to a single partition
dataframe = changedatatype_node.toDF().coalesce(1)

# Script generated for node Parquet in S3 with partitioning by "region"
dataframe.write.partitionBy("region").parquet(
    path="s3://youtube-data-eng-project-cleansed-useast1-767398140492-dev/youtube/cleansed_statistics/",
    mode="append",
    compression="snappy"
)

job.commit()
