# Define a video class, a video has title and link
class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link

# Ask an user to enter information of a video
def read_video():
		title = input("Enter in title: ")
		link = input("Enter in link: ")
		video = Video(title, link)
		return video


# Show information of the video
def print_video(video):
	print("Enter title: ", video.title)
	print("Enter link: ", video.link)


# Ask an user information of all videos, they firt choose how many videos are there
def read_videos():
	videos =[]
	total_video = int(input("Enter how many videos: "))
	for i in range(total_video):
		print("Video title", i+1)
		vid = read_video()
		videos.append(vid)
	return videos

# Show information of all videos
def  print_videos(videos):
	for i in range (len(videos)):
		print_video(videos[i])     

# write a video information to text file
def write_video_txt(video, file):
	file.write(video.title + "\n")
	file.write(video.link + "\n")

# Write videos to text file, first line is the total number of videos
def write_videos_txt(videos):
	total = len(videos)
	with open("lan.txt", "w") as file:
		file.write(str(total) + "\n")
		for i in range(total):
			 write_video_txt(videos[i], file)
			# file.write(videos[i].title)
			# file.write(videos[i].link)

# Read 2 line from a text file and retirn a video
def read_video_from_txt(file):
	pass

# Read data.txt and return a list of videos
def read_videos_from_txt():
	pass



def main():
# Ask user to enter information of all video one by one 
	videos = read_videos()
# Write videos infomation to a text file
	write_videos_txt(videos)
# Read the text file to get the video list
	# videos = read_videos_from_txt
# User list above and show all information of videos inside that list
	print("-----")
	print_videos(videos)
main()