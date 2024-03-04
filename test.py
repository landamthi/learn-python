class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link

def read_video():
	title = input("Enter in title: ")
	link = input("Enter in link: ")
	video = Video(title, link)
	return video

def print_video(video):
	print("Video title: ", video.title)
	print("Enter link:", video.link)

def read_videos():
	videos = []
	total_videos = int(input("Enter How many videos: "))

	for i in range(total_videos):
		print("Video ", i+1)
		video = read_video()
		videos.append(video)
	return videos
	
def print_videos(videos):
	for i in range(len(videos)):
		print_video(videos[i])

def write_video_txt(videos, file):
	file.write(videos.title )
	file.write(videos.link )

def write_videos_txt(videos):
	total = len(videos)
	with open("thinh.txt", "w") as file:
		file.write(str(total) + "\n")
		for i in range (total):
			write_video_txt(videos[i], file)

def read_from_video_txt(file):
	title  = file.readline()
	link  = file.readline()
	video = Video(title, link)
	return video

def read_from_videos_txt():
	videos = []

	with open("thinh.txt", "r")as file:
		total = int(file.readline())
		for i in range(total):
			video = read_from_video_txt(file)
			videos.append(video)
		return videos


def main():

	videos = read_videos()
	write_videos_txt(videos)
	print("---------")
	videos = read_from_videos_txt()
	print_videos(videos)

main()

		