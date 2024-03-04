# Define a video class, a video has title and link
class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos
		
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
def write_videos_txt(videos, file):
	total = len(videos)
	
	file.write(str(total) + "\n")
	for i in range(total):
			write_video_txt(videos[i], file)
			# file.write(videos[i].title)
			# file.write(videos[i].link)

# Read 2 line from a text file and retirn a video
def read_video_from_txt(file):
	title = file.readline() 
	# .strip()
	link = file.readline()
	video = Video(title, link)
	return video

# Read data.txt and return a list of videos
def read_videos_from_txt(file):
	videos = []
	total = int(file.readline())
	for i in range(total):
		video = read_video_from_txt(file)
		videos.append(video)
	return videos



def read_playlist():
	playlist_name = input("Enter playlist name: ")
	playlist_description = input("Enter playlist description: ")
	playlist_rating = input("Enter rating (1-5): ")
	playlist_videos = read_videos()
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

def write_playlist_txt(playlist):
	with open("data.txt", "w") as file:
		file.write(playlist.name + "\n")
		file.write(playlist.description + "\n")
		file.write(playlist.rating + "\n")
		write_videos_txt(playlist.videos, file)
	print("Successfully write playlist to txt")

def read_playlist_from_txt():
	
	with open("data.txt", "r") as file:
		playlist_name = file.readline()
		playlist_description = file.readline()
		playlist_rating = file.readline()
		playlist_videos = read_videos_from_txt(file)
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

def print_playlist(playlist ):
	print("palylist name: " + playlist.name, end="")
	print("playlist description: " + playlist.description, end="" )
	print("playlist rating: " + playlist.rating, end="" )
	print_videos(playlist.videos)


def main():
# # Ask user to enter information of all video one by one 
# 	videos = read_videos()
# # Write videos infomation to a text file
# 	write_videos_txt(videos)
# # Read the text file to get the video list
# 	videos = read_videos_from_txt()
# # User list above and show all information of videos inside that list
# 	print("-----")
# 	print_videos(videos)
	playlist = read_playlist()
	write_playlist_txt(playlist)
	playlist = read_playlist_from_txt()
	print_playlist(playlist)
main() 