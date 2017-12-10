CREATE EXTERNAL TABLE IF NOT EXISTS ClickStream (
  `browseraction` String,
  `site` String
)
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
LOCATION 's3://bstraining-doroszl/transform2017/'
TBLPROPERTIES ('has_encrypted_data'='false');
