# Define a video class, a video has title and link
import webbrowser
class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.seen = False
	def open(self):
		webbrowser.open(self.link)
		self.seen = True

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos
		
# Ask an user to enter information of a video
def read_video():
		title = input("Enter in title: ") + "\n"
		link = input("Enter in link: ") + "\n"
		video = Video(title, link)
		return video


# Show information of the video
def print_video(video):
	print("Enter title: ", video.title, end="")
	print("Enter link: ", video.link, end="")


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
		print("Video " + str(i+1) + ": ")
		print_video(videos[i])     

# write a video information to text file
def write_video_txt(video, file):
	file.write(video.title)
	file.write(video.link)

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
	playlist_name = input("Enter playlist name: ") + "\n" 
	playlist_description = input("Enter playlist description: ") + "\n"
	playlist_rating = input("Enter rating (1-5): ") + "\n"
	playlist_videos = read_videos()
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

def write_playlist_txt(playlist):
	with open("data.txt", "w") as file:
		file.write(playlist.name)
		file.write(playlist.description)
		file.write(playlist.rating)
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

def print_playlist(playlist):
	print("palylist name: " + playlist.name, end="")
	print("playlist description: " + playlist.description, end="" )
	print("playlist rating: " + playlist.rating, end="" )
	print_videos(playlist.videos)

def show_menu():
	print("\n Main menu: \n")
	print("---------------------------------")
	print("|  Option 1: Create playlist	|")
	print("|  Option 2: Show playlist	|")
	print("|  Option 3: Play a video	|")
	print("|  Option 4: Add video   	|")
	print("|  Option 7: Save and Exit	|")
	print("---------------------------------")

def select_in_range(prompt, min, max):
	choice = input(prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max :
		choice = input(prompt)
	choice = int(choice)
	return choice

def play_video(playlist):
	print_videos(playlist.videos)
	total = len(playlist.videos)
	
	# if total == 0:
	# 	print("The playlist is empty.")
	# return
	
	choice = select_in_range("Select a video (1," + str(total) + "): ", 1, total)
	print("Open video: " + playlist.videos[choice-1].title + " - " + playlist.videos[choice-1].title, end="")
	playlist.videos[choice-1].open()
    # playlist.videos[choice-1].open()
	
def add_video(playlist):
	
	print("Enter new video information:")
	new_title = input("Enter new title: ") + "\n"
	new_link = input("Enter new link: "  ) + "\n"
	
	new_video = Video(new_title, new_link)
	playlist.videos.append(new_video)
	
	return playlist
	

def main():

	try:
		playlist = read_playlist_from_txt()
		print("Loaded data Successfully !!!")
	except:
		print("Welcome firt user !!!")
	while True:
		show_menu()
		choice = select_in_range("Select an option (1-7): ", 1, 7)
		if choice == 1:
			playlist = read_playlist()
			input("Press Enter to continue. ")
		elif choice == 2:
			print_playlist(playlist)
			input("Press Enter to continue. ")
		elif choice == 3:
			play_video(playlist)
			input("Press Enter to continue. ")
		elif choice == 4:
			playlist = add_video(playlist)
			input("Press Enter to continue. ")
		elif choice == 7:
			write_playlist_txt(playlist)
			input("Press Enter to continue. ")
			break
		else:
			print("wrong input, Exits.")
			break
	
main() 