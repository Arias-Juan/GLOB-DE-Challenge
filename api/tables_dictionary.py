from pyspark.sql.types import *

"""
    Schema to table jobs.csv file.
"""
schema_jobs = StructType([
    StructField("id", IntegerType(), True),
    StructField("job", StringType(), True)
])

"""
    Schema to table departments.csv file.
"""
schema_departments = StructType([
    StructField("id", IntegerType(), True),
    StructField("department", StringType(), True)
])

"""
    Schema to table hired_employess.csv file.
"""
schema_hired_employess = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("datetime", StringType(), True),
    StructField("department_id", IntegerType(), True),
    StructField("job_id", IntegerType(), True)
])

"""
    Dictionary schemas
"""
schemas = {
    "jobs": schema_jobs,
    "departments": schema_departments,
    "hired_employess": schema_hired_employess
}
