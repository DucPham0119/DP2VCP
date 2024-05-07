def get_file(path, outpath):
    wf = open(outpath, 'w', encoding="utf-8")
    with open(path, 'r', encoding="utf-8") as f:
        dt = f.readlines()
        for data in dt:
            if str(data).strip() != '':
                wf.write(data)

get_file("./data/ground_truth.csv", './data/ground_truth_format.csv')