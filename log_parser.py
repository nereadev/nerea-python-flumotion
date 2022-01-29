
file_name = "http_log.json"
file = open(file_name, "r")
ip_data = []
code_data = []

for line in file.readlines():
    data = line.split()
    ip_adress = data[0]
    code_status = data[7]
    if "50" in code_status:
        code_status = code_status[:2] + "X"
    ip_data.append(ip_adress)
    code_data.append(code_status)

ip_data_sorted = sorted(ip_data)
code_data_sorted = sorted(code_data)
    
def petitions(log_data):
    for log in [item for index, item in enumerate(log_data,1) 
                     if item not in log_data[index:]]:
        print("{} {}".format(log,log_data.count(log)))

petitions(ip_data_sorted)
petitions(code_data_sorted)
