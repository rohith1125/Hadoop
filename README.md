# Hadoop
```bash
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -mapper "python3 /scripts/mapper8.py" -reducer "python3 /scripts/reducer8.py" -input /access_log -output /outputeight
```
```bash
hdfs dfs -cat /outputeight/part-00000
```
```bash
hdfs dfs -put -f /scripts/* /scripts
```
```bash
hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.1.jar wordcount /scripts/wordcountop.txt /scripts/wrdop
```
