import glob
import pdftotext

# get all files in folder
l = sorted(list(glob.glob("./Dibbs/*/*")))

# set limit test of files to analize  set 1000 if you do not want a limit
limit = 1000
filters = ["critical safety item"]
list_to_review = list()
list_n_review = list()

#loop for all files
for i in range(len(l)):

    # Load your PDF
    with open(l[i], "rb") as f:
        pdf = pdftotext.PDF(f)

    # How many pages?
    print(len(pdf))

    # Iterate over all the pages
    text_in_pdf = ""
    for page in pdf:
        text_in_pdf += page.lower()
    
    #print(text_in_pdf)
    # if there are not any of the text in 'filters' in the pdf
    # save the path of the file in a list
    if any(x in text_in_pdf for x in filters):
        print("yes")
        print(l[i])
        list_n_review.append(l[i])
    else:
        list_to_review.append(l[i])
        
    # check how it goes
    print("{0} of {1} files".format(i+1, len(l)))
    if i >= limit:
        break

# create html file with the proper files
with open('helloworld.html','w') as f:

    message = "<html>\n<head></head>\n<body>\n"
    for x in list_to_review:
        message += '<li><a href="{0}">file {0}</a></li>'.format(x)
    message += "</body></html>"

    f.write(message)
    f.close()

# create html file with the files that we do not need to review
with open('no_needed.html','w') as f:

    message = "<html>\n<head></head>\n<body>\n"
    for x in list_n_review:
        message += '<li><a href="{0}">file {0}</a></li>'.format(x)
    message += "</body></html>"

    f.write(message)
    f.close()






