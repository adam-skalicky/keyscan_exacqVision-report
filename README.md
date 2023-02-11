# keyscan_exacqVision-report

A script that ingests Keyscan transaction reports and generates exacqVision XDV files that can be run to export footage.

# Getting Started

1. Clone this repo somewhere. The conf example and batch file included assume in the root of your C drive.

2. Copy the conf.json.example to conf.json

3. Update the values in your conf.json to match your system configuration.

- **user** represents the username for your exacqVision server.
- **password** represents the password for your exacqVision server.
- **system_name** represents the IP and portof your exacqVision server.
- **output_dir** represents the directory where you want the XDV files to be generated. Note that this should also contain your Output directory.
- **devices** is a object defining with the key name being the ACU that Keyscan is reporting on, and its value being an array of the exacqVision devices that are associated with that ACU. If you only have one camera, an array of one is fine. The purpose of this being an array is to capture multiple cameras on the same ACU - ie. lobby ACU that has 2 cameras.
- **lookback** and **lookforward** can be left as the default values, but represent the number of seconds before and after the transaction time that the XDV file will capture. This can be useful if you want to capture a few seconds before and after the transaction or if there is a clock skew between your exacqVision server and your Keyscan server.

4. If you cloned this repo to somewhere other than the root of your C drive, update the batch file to point to the correct location of the python script and output directory.

5. Copy your Keyscan transaction report to the reports directory. This should be exported from Keyscan as a CSV file. This script assumes the following columns are present in the CSV file in the following order:

"Site", "Access Control Unit", "DeviceID", "Device", "Transaction", "PersonID", "Person", "CredentialID", "Credential", "Date"

6. Run the batch file.

7. The XDV files will be generated in the output directory. The batch file will automatically run the XDV file to export the footage. Note that you must have the exacqVision client installed on the machine you are running this script from.

8. The exported footage will be in the Output directory in the output directory.

# Trouble Shooting

- If you are getting an error about footage not being found, try adjusting the lookback and lookforward values in your conf.json file. This can be an issue if you have a clock skew between your exacqVision server and your Keyscan server and only retain footage with motion detection.
