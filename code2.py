import pandas as pd;
import csv;
import statistics;

df = pd.read_csv('height-weight.csv')

height_list = df['Height(Inches)'].tolist()
weight_list = df['Weight(Pounds)'].tolist()

hieght_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

hieght_std_dev = statistics.stdev(height_list)
weight_std_dev = statistics.stdev(weight_list)

hieght_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

hieght_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

print('Mean of Height is ' , height_mean)
print('Mean of Weight is ' , weight_mean)

print('Median of Height is ' , height_median)
print('Median of Weight is ' , weight_median)

print('Mode of Height is ' , height_mode)
print('Mode of Weight is ' , weight_mode)

height_1st_std_dev_start, height_1st_std_dev_end = height_mean - height_std_dev, height_mean + height_std_dev
height_2nd_std_dev_start, height_2nd_std_dev_end = height_mean - ( 2 * height_std_dev), height_mean + ( 2 * height_std_dev)
height_3rd_std_dev_start, height_3rd_std_dev_end = height_mean - ( 3 * height_std_dev), height_mean + ( 3 * height_std_dev)

height_list_of_data_within_1st_std_dev = [result for result in height_list if result > height_1st_std_dev_start and result < height_1st_std_dev_end]
height_list_of_data_within_2nd_std_dev = [result for result in height_list if result > height_2nd_std_dev_start and result < height_2nd_std_dev_end]
height_list_of_data_within_3rd_std_dev = [result for result in height_list if result > height_3rd_std_dev_start and result < height_3rd_std_dev_end]

weight_1st_std_dev_start, weight_1st_std_dev_end = weight_mean - weight_std_dev, weight_mean + weight_std_dev
weight_2nd_std_dev_start, weight_2nd_std_dev_end = weight_mean - ( 2 * weight_std_dev), weight_mean + ( 2 * weight_std_dev)
weight_3rd_std_dev_start, weight_3rd_std_dev_end = weight_mean - ( 3 * weight_std_dev), weight_mean + ( 3 * weight_std_dev)

weight_list_of_data_within_1st_std_dev = [result for result in weight_list if result > weight_1st_std_dev_start and result < weight_1st_std_dev_end]
weight_list_of_data_within_2nd_std_dev = [result for result in weight_list if result > weight_2nd_std_dev_start and result < weight_2nd_std_dev_end]
weight_list_of_data_within_3rd_std_dev = [result for result in weight_list if result > weight_3rd_std_dev_start and result < weight_3rd_std_dev_end]

print('{}% Of data for height lies within 1 std dev'.format(len(height_list_of_data_within_1st_std_dev)*100.0/len(height_list)))
print('{}% Of data for height lies within 2 std dev'.format(len(height_list_of_data_within_2nd_std_dev)*100.0/len(height_list)))
print('{}% Of data for height lies within 3 std dev'.format(len(height_list_of_data_within_3rd_std_dev)*100.0/len(height_list)))

print('{}% Of data for weight lies within 1 std dev'.format(len(weight_list_of_data_within_1st_std_dev)*100.0/len(weight_list)))
print('{}% Of data for weight lies within 2 std dev'.format(len(weight_list_of_data_within_2nd_std_dev)*100.0/len(weight_list)))
print('{}% Of data for weight lies within 3 std dev'.format(len(weight_list_of_data_within_3rd_std_dev)*100.0/len(weight_list)))