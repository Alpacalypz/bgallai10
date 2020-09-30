def csv_format(csv, dictionary):
    in_stream = open(csv)
    jobs = in_stream.read()
    in_stream.close()

    jobs = jobs.split('\n')

    for j in jobs    
