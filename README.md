# Part 1
We use this command to run the inbuilt wordcount example with the 500 random words generated using the random word generator,
```bash
hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.2.1.jar wordcount /scripts/wordcountinput.txt /scripts/wordcountop
```
We get the output using,
```bash
hdfs dfs -get /scripts/* /scripts
```
To view the output we use,
```bash
hdfs dfs -cat /wordcountop/part-00000
```
# Part 2
We first create a folder named scripts in the hdfs
```bash
hdfs dfs -mkdir /scripts
```
To execute the program, we first put the input file, mapper and reducer to dfs by,
```bash
hdfs dfs -put /scripts/ngraminput.txt /scripts
```
```bash
hdfs dfs -put /scripts/ngrammapper.py /scripts
```
```bash
hdfs dfs -put /scripts/ngramreducer.py /scripts
```
This will put the files into the hdfs

Now we run using the following command,
```bash
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -mapper "python3 /scripts/ngrammapper.py 2" -reducer "python3 /scripts/ngramreducer.py" -input /ngraminput.txt -output /outputngram
```


To view the output we use the following command,
```bash
hdfs dfs -cat /outputngram/part-00000
```
We get outputs from hdfs using the following command
```bash
hdfs dfs -get /scripts/* /scripts
```
# Part 3
We use the folder that we have previously created in Part 2 and use it to put the mapper and reducer files into hdfs using the following command,
```bash
hdfs dfs -put /scripts/* /scripts
```
We should also put the access_log,
```bash
hdfs dfs -put /access_log /scripts
```
To run the code we use the following command,
```bash
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -mapper "python3 /scripts/mapper1.py" -reducer "python3 /scripts/reducer1.py" -input /access_log -output /outputone
```
We use the above command to run the code for the first set of mapper and reducer, similarly we do it for all the 10 mappers and reducers.
To view the output we use,
```bash
hdfs dfs -cat /outputone/part-00000
```
Then we get the output files with the following command,
```bash
hdfs dfs -get /scripts/* /scripts
```