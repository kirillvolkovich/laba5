alpha = 0.2
prev_filtered_value = 0

for new_measurement in [1, 2, 3, 4, 5]:
    filtered_value = alpha * new_measurement + (1 - alpha) * prev_filtered_value
    prev_filtered_value = filtered_value
    print(filtered_value)


