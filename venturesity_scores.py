import csv
#print dir(csv)
from user_score_calculate import github_score
#from get_user_score import get_relative_score
import operator

venturesity_user_list = []
venturesity_score_dict = {}
with open('Seq_Hack_Apurv_Data.csv', 'rb') as csvfile:
    github_urls = csv.reader(csvfile)
    i = 0
    writer = csv.writer(open('Sequioa_Final_List.csv', 'wb'))
    for handle in github_urls:
        with open('number_of_API_calls.txt','w') as f:
                f.write(str(i))
        i = i + 1
        if (handle[3].split("/")[-1] != "NA"):
            if (handle[3].split("/")[-1] == ""):
              print handle[3].split("/")[-2]
              #venturesity_user_list.append(handle[3].split("/")[-2])
              writer.writerow([handle[1], handle[2], handle[3], github_score(handle[3].split("/")[-2])])
            else:
              print handle[3].split("/")[-1]
              #venturesity_user_list.append(handle[3].split("/")[-1])
              writer.writerow([handle[1], handle[2], handle[3], github_score(handle[3].split("/")[-1])])
        else:
            writer.writerow([handle[1], handle[2], handle[3], "NA"])
            #venturesity_user_list.append("NA")
            #pass

#print len(venturesity_user_list)



    # for handle in github_urls:
    #    if (len(handle) != 0):
    #         venturesity_user_list.append(handle[0].split("/")[-1])

            #print handle
#print venturesity_user_list
#with open('github_venturesity_users.txt','w') as f:
#    for x in venturesity_user_list:
#        f.write(x + '\n')
#Calculating score in the Sequioa database
# i = 1
# for x in venturesity_user_list:
#        with open('number_of_API_calls.txt', 'w') as f:
#            f.write(str(i))
#        score = github_score(x)
#        if type(score) == type(0.5):
#            venturesity_score_dict[x] = get_relative_score(score)
#        else:
#            venturesity_score_dict[x] = score
#        i = i + 1
# #
# venturesity_score_dict = sorted(venturesity_score_dict.items(), key=operator.itemgetter(1), reverse=True)
# file = open('ranked_list.txt', 'w')
# for x in venturesity_score_dict:
#      file.write(str(x) + '\n')
# file.close()
#####################################################
# venturesity_score_dict = dict(venturesity_score_dict)
# print venturesity_score_dict
# f = open('github_results.txt', 'w')
# for keys, value in venturesity_score_dict.items():
#     f.write("Github Handle: " + str(keys) + " Score: " + str(value) + '\n')
# f.close()
