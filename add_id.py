import os


def read_file(path, result_path):
    # files = os.listdir(path)
    # for file_path in files:
    #     with open(os.path.join(path, file_path), 'r', encoding='UTF-8') as f:
    #         dt = f.readlines()
    #         write_file(os.path.join(path, file_path.replace(".txt", "_id.txt")), dt)
    # ids = []
    # with open(id_path, 'r', encoding='UTF-8') as f:
    #     dt = f.readlines()
    #     # print(dt)
    #     # print(len(dt))
    #     for line in dt:
    #         if "<s id = " in line:
    #             ids.append(line.replace("id = ", "id="))

    # print(ids)
    with open(path, 'r', encoding='UTF-8') as f:
        dt = f.readlines()
        write_file(result_path, dt, [])


def write_file(path, data, ids):
    # count = 1
    i = 1
    with open(path, 'w', encoding='UTF-8') as file:
        for dt in data:
            if dt.startswith('<s>'):
                dt = dt.replace('\n','').replace("<s>", "<s id="+str(i)+">\n")
                i += 1
            # file.write("<s id = " + str(count) + ">\n")
            file.write(dt)
            # file.write("</s>" + '\n')
            # file.write('\n')
            # count += 1


read_file("D:/Nghien_cuu/DP2VCP/data/vtb2022.txt", "D:/Nghien_cuu/DP2VCP/data/vtb2022_id.txt")
