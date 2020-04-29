import logging

from google.oauth2 import service_account
from pandas.tests.io.test_gbq import pandas_gbq

from src.data_transformation import DataTransformation
from src.schemas import schema_files_csv

KEY_JSON = './instance/stewardshipbh-3ca7bd9e0bfc-magna.json'
PROJECT_ID = "stewardshipbh"
SUFIX_TABLE_NAME = "stewardshipbh."
BUCKET_NAME = "stewardship_bh"


def run():
    credentials = service_account. \
        Credentials. \
        from_service_account_file(KEY_JSON, )
    # DataTransformation is a class we built in this script to hold the logic for
    # transforming the file into a BigQuery table.
    for table, schema in schema_files_csv.items():
        try:
            logging.info("Processing schema for {}".format(schema.get("file_name")))

            data_ingestion = DataTransformation(schema, BUCKET_NAME, credentials)

            if not data_ingestion.download_blob():
                logging.info(" 0 files to process")
                continue
            logging.info("Downloaded files: {}".format(",".join(data_ingestion.files) or "0 files"))

            frame = data_ingestion.process_files()

            logging.info("Dataframe created with some {} lines".format(str(frame.shape)))

            if not frame.empty:
                pandas_gbq.context.project, pandas_gbq.context.credentials = (PROJECT_ID, credentials)

                pandas_gbq.to_gbq(frame,
                                  table.replace(SUFIX_TABLE_NAME, ""),
                                  if_exists=schema.get("action")
                                  )
                logging.info("Table {} was loaded on Big Query".format(table.replace(SUFIX_TABLE_NAME, "")))

                blob_files = data_ingestion.move_processed_files()
                logging.info("Moving files {} to processed folder".format(",".join(blob_files)))

            data_ingestion.upload_blob("info.log")

        except ValueError as err:
            logging.error("csv schema expected are wrong, please ask to some dev update the schema. "
                          "Error: {}".format(err.__str__()))


if __name__ == "__main__":
    logging.basicConfig(filename='info.log', level=logging.INFO)
    run()
