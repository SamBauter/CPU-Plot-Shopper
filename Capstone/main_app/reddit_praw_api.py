import praw
import csv

reddit = praw.Reddit(
    client_id="QCT_5RnVNwcU9Q",
    client_secret="Pb7jKExpO2fq2x6rwITAepQFV4g",
    user_agent="my user agent"
)

fields = ['id', 'title', 'url', 'time', 'num_comments', 'score', 'upvote_ratio']

# Meta is the only flair left out
cpu_component_names = ['Case', 'Controller', 'Cooler', 'CPU', 'FAN', 'GPU', 'HDD', 'Headphones', 'Keyboard', 'Monitor',
                       'Mouse', 'PSU', 'RAM', 'SSD', 'MOBO', 'Prebuilt', 'VR']


def create_csv_files(component_name_list):
    files = []
    for name in component_name_list:
        files.append(open('component_titles/'+name + '.csv', 'x'))
    return files


def getRedditSearchResults(cpu_component_list, search_fields):
    files = create_csv_files(cpu_component_list)
    for component_type, file in zip(cpu_component_list, files):
        csvwriter = csv.writer(file)
        csvwriter.writerow(search_fields)
        for submission in reddit.subreddit("buildapcsales").search("flair:" + component_type, sort="new",
                                                                   time_filter="year",
                                                                   limit=300):
            csvwriter.writerow([submission.id, submission.title, submission.url, submission.created_utc,
                                submission.num_comments, submission.score, submission.upvote_ratio])


if __name__ == '__main__':
    getRedditSearchResults(cpu_component_names, fields)


