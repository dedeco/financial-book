import os
import shutil

import pandas as pd
import uuid

from google.cloud import storage


class DataTransformation:
    """A helper class which contains the logic to translate a csv into a
    format BigQuery will accept.
    """

    def __init__(self, schema, bucket_name, credentials):
        """ Here we read the input schema and which file will be transformed. This is used to specify the types
        of data to create a pandas dataframe.
        """
        self.schema = schema
        self.files = []
        self.blob_files = []
        self.client = storage.Client(credentials=credentials, project="stewardshipbh")
        self.bucket = self.client.get_bucket(bucket_name)

    def parse_method(self, csv_file):
        """This method translates csv_file in a pandas dataframe which can be loaded into BigQuery.
        Args:
            csv_file: some.csv

        Returns:
            A pandas dataframe.
        """
        df = pd.read_csv(csv_file,
                         skiprows=[1],
                         sep=self.schema.get('sep'),
                         decimal=self.schema.get('decimal'),
                         thousands=self.schema.get('thousands')
                         )
        df.columns = self.schema.get('fields')
        for col in self.schema.get('numeric_fields'):
            df[col] = pd.to_numeric(df[col])
        shutil.move(csv_file, "./temp/processed/{0}".format(
            os.path.splitext(os.path.basename(csv_file))[0])
                    )
        return df

    def process_files(self):
        """This method process all files and concat to a unique dataframe
        Returns:
            A pandas dataframe contained.
        """
        frames = []
        for file in self.files:
            frames.append(self.parse_method(file))
        if frames:
            return pd.concat(frames)
        else:
            return pd.DataFrame([], columns=['a'])

    def download_blob(self):
        """Downloads a blob from the bucket."""
        for blob_file in self.bucket.list_blobs(prefix="input"):
            if self.schema.get("file_name").upper() in blob_file.name.upper():
                unique_filename = "{0}_{1}".format(self.schema.get("file_name"), str(uuid.uuid4()))
                destination_file = os.path.join("./temp/input", unique_filename + ".csv")
                blob_file.download_to_filename(
                    destination_file
                )
                self.files.append(destination_file)
                self.blob_files.append(blob_file)
        return True if len(self.blob_files) > 0 else False

    def upload_blob(self, destination_blob_name):
        """Uploads a file to the bucket."""
        blob = self.bucket.blob(destination_blob_name)
        blob.upload_from_filename(os.path.splitext(os.path.basename(destination_blob_name))[0] +
                                  os.path.splitext(os.path.basename(destination_blob_name))[1])

    def move_processed_files(self):
        """Move processed files to processed folder"""
        for blob_file in self.blob_files:
            self.bucket.rename_blob(blob_file, "processed/" + blob_file.name)
        return [b.name for b in self.blob_files]
