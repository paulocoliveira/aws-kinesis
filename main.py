from kinesis_functions import create_stream, put_data, get_data
from random import randrange

my_data_1 = '{"ID":1,"date":"2019-11-05 12:59:59.358","value":"some sample value","floatValue":6.0}'
my_data_2 = '{"ID":2,"date":"2019-11-05 12:59:59.358","value":"some sample value","floatValue":6.0}'
my_data_3 = '{"ID":3,"date":"2019-11-05 12:59:59.358","value":"some sample value","floatValue":6.0}'

my_stream_name = "stream_" + str(randrange(1000))

create_stream(my_stream_name)

put_data(my_stream_name, my_data_1)
put_data(my_stream_name, my_data_2)
put_data(my_stream_name, my_data_3)

get_data(my_stream_name)