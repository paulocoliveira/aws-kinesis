import boto3

def create_stream(stream_name):
    client = boto3.client('kinesis')
    # Create kinesis stream
    client.create_stream(StreamName=stream_name, ShardCount=1)
    # Wait until the end of stream creation
    waiter = client.get_waiter('stream_exists')
    waiter.wait(StreamName=stream_name)
    print("Created Stream: " + stream_name)

def put_data(stream_name, input_data):
    client = boto3.client('kinesis')
    # Inserting data in a stream
    client.put_record(StreamName=stream_name, Data=input_data, PartitionKey="1")
    print("Stored Data: " + input_data)

def get_data(stream_name):
    client = boto3.client('kinesis')
    # Get information about a Kinesis stream
    kinesis_stream = client.describe_stream(StreamName=stream_name)
    # Get shards of stream
    shards = kinesis_stream['StreamDescription']['Shards']
    # Get shard IDs
    shard_ids = [shard['ShardId'] for shard in shards]
    # Get shard iterator
    iter_response = client.get_shard_iterator(StreamName=stream_name, ShardId=shard_ids[0], ShardIteratorType="TRIM_HORIZON")
    shard_iterator = iter_response['ShardIterator']
    # Get all data stored in the stream
    record_response = client.get_records(ShardIterator=shard_iterator)
    records_list = record_response['Records']
    for record in records_list:
        print("Retrieved Data: " + record['Data'].decode("utf-8"))
    return records_list