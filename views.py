from django.shortcuts import render, redirect 
from pytube import *

def youtube(request): 

	# checking whether request.method is post or not 
	if request.method == 'POST': 
		
		# Getting the link from page
		link = request.POST['link'] 
		video = YouTube(link) 

		# Setting the resolution for video
		stream = video.streams.get_lowest_resolution() 
		
		# Starts download the video
		stream.download() 

		# Returning to HTML page 
		return render(request, 'youtube.html') 
	return render(request, 'youtube.html')
