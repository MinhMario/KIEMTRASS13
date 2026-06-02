parking_lots=[
    {"id":1,
     "type":"Xe may",
     "owner":"A"},
    
    {"id":2,
     "type":'Oto',
     "owner":"B"}
]
currentId=2
while True:
    choice=input('Nhập lựa chọn của bạn')
    match choice:
        case '1':
            id=currentId+1
            type=input('Nhập loại xe').strip()
            while True:
                if type=="":
                    print('Yêu cầu nhập lại')
                    type=input('Nhập loại xe').strip()
                if type!="":
                    break
            owner=input('Nhập chủ xe').strip()
            while True:
                if owner=="":
                    print('Yêu cầu nhập lại')
                    owner=input('Nhập chủ xe').strip()
                if owner!="":
                    break
            parking_lots.append({'id':id,'type':type,'owner':owner})
        case '2':
            if not parking_lots:
                print('Bãi xe hiện tại đang trống')
                continue
            print(f"{'ID':<5} | {'Loại xe':<10} | {'Chủ xe':<10}")
            for i in range(len(parking_lots)):
                print(f"{parking_lots[i]['id']:<5} | {parking_lots[i]['type']:<10} | {parking_lots[i]['owner']:<10}")
        case '3':
            search=input('Nhập ID của xe cần tìm').strip()
            found=False
            if not search.isdigit():
                print('ID cần nhập phải là số')
                continue
            search=int(search)
            for xe in parking_lots:
                if xe['id']==search:
                    found=True
                    print(xe)
            if not found:
                print(f"Không tìm thấy xe có ID:{search}")
        case '4':
            del_id=input('Nhập ID của xe cần tìm').strip()
            found=False
            if not del_id.isdigit():
                print('ID cần nhập phải là số')
                continue
            del_id=int(del_id)
            for xe in parking_lots:
                if xe['id']==del_id:
                    found=True
                    parking_lots.remove(xe)
                    print('Xoá thành công')
            if not found:
                print("Không tìm thấy xe để xoá")
        case _:
            print('Lựa chọn không hợp lệ')
                    
                                
            
    