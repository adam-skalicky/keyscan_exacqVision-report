import os
import csv
import datetime
import json


conf=json.loads(open('conf.json').read())
(system_name, username, password, lookback, lookforward, devices, root_path) = conf["system_name"], conf["username"], conf["password"], conf["lookback"], conf["lookforward"], conf["devices"], conf["root_path"]

def main():
    report=[]
    output='<exacqVisionInit>\n'
    files = os.listdir('./reports')
    for f in files:
        if f.endswith('.csv'):
            with open(f'./reports/{f}', 'r') as csv_file:
                reader = csv.reader(csv_file)
                i=0
                for row in reader:
                    i+=1
                    if i == 1:
                        pass
                    else:
                        (site,acu,dev_id,dev,txn,pid,person,cred_id,cred,date) = row
                        date=datetime.datetime.strptime(date, '%m/%d/%Y %I:%M:%S.%f %p')
                        date_epoch = int(date.timestamp())
                        date_string = date.strftime('%Y-%m-%d__%H-%M-%S')
                        start = date_epoch - lookback
                        end = date_epoch + lookforward                        
                        camera = devices.get(acu, acu)
                        report.append({"person": person, "camera": camera, "start": start, "end": end, "date": date_string})

    for r in report:
        (person, camera, start, end, date) = (r["person"], r["camera"], r["start"], r["end"], r["date"])

        if isinstance(camera, list):
            for c in camera:
                file_path=f'{date}__{person}__{c}.mp4'
                #Remove invalid characters from file path
                file_path = file_path.replace('/', '_')
                file_path = file_path.replace('\\', '_')
                file_path = file_path.replace(':', '_')
                file_path = file_path.replace('*', '_')
                file_path = file_path.replace('?', '_')
                file_path = file_path.replace('"', '_')
                file_path = file_path.replace('<', '_')
                file_path = file_path.replace('>', '_')
                file_path = file_path.replace('|', '_')
                file_path = file_path.replace(' ', '_')
                file_path = f'{root_path}\\{file_path}'
                xml =f'''<Search Start="{start}" End="{end}" Filename="{file_path}">
  <System Name="{system_name}" Username="{username}" Password="{password}">
   <Video>
    <Input Name="{c}" Position="0" />
   </Video>
  </System>
 </Search>
'''
                output+=xml
        else:
            print(f'Unmapped camera: {camera}')
    output+="</exacqVisionInit>"
    out_file=open('./report.xdv', 'w')
    out_file.write(output)
    out_file.close()
    
        



if __name__ == '__main__':
    main()