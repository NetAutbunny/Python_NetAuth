ip_lst = ['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4']
print(ip_lst)
ip_lst.append('10.0.0.5')
ip_lst.extend(['10.0.0.6', '10.0.0.7'])
ip_lst = ip_lst + ['10.0.0.8', '10.0.0.9']
print(ip_lst)
print(f"First IP of the list: {ip_lst[0]}", f"\nLast IP of the List: {ip_lst[-1]}")
print(ip_lst.pop(0))
print(ip_lst.pop(-1))
print(ip_lst)
ip_lst[0] = '10.0.0.1'
print(ip_lst)