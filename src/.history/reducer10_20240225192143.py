import sys

requested_data = 0

target_date = "16/Jan/2022"  
target_status_code = "200"  

for line in sys.stdin:
    date, status_code, size = line.strip().split('\t')  
    if date == target_date and status_code == target_status_code:  
        requested_data += int(size)  

print(f"Total data requested with status code 200 on {target_date}: {requested_data} bytes")
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -mapper /scripts/mapper1.py -file /scripts/reducer1.py -reducer "python3 /scripts/reducer1.py" -input /access_log -output /outputone