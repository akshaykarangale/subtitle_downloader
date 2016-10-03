from babelfish import Language
from subliminal import download_best_subtitles, region, save_subtitles, scan_videos
import subliminal

print("Scanning for videos in home folder....")
videos = scan_videos('/home')
print("Following videos were found in folder: ")
videos_list = []
i=1
for v in videos:
    try:
        print(str(i)+": "+ v.title)
        i = i+1
        videos_list.append(v)
    except TypeError:
        continue
subt_dl = input("Enter movie number for downloading subtitles: ")
print("Downloading subtitles for "+videos_list[int(subt_dl)-1].title)
subt_ = []
subt_.append(videos_list[int(subt_dl)-1])
subtitle = download_best_subtitles(subt_,{Language('eng')})
for v in subt_:
    save_subtitles(v, subtitle[v])
print("Your subtitles are downloaded successfully to the movie folder!")