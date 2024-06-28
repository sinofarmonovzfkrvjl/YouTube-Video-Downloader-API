import os
import requests

# URL of the Flask API endpoints
download_url = "https://127.0.0.1/download"
details_url = "https://127.0.0.1/details"

# Function to download the video and return its details
def download_video_and_get_details(video_url):
    # JSON payload with the video URL
    payload = {
        "url": video_url
    }

    # Make a POST request to the details endpoint
    response = requests.post(details_url, json=payload)

    if response.status_code != 200:
        return f"Failed to get video details: {response.status_code} - {response.text}"

    # Extract video details
    video_details = response.json()
    video_title = video_details.get('title', 'video')
    video_ext = video_details.get('ext', 'mp4')
    video_filename = f"{video_title}.{video_ext}"

    # Make a POST request to the download endpoint
    response = requests.post(download_url, json=payload)

    if response.status_code == 200:
        # Save the video file
        video_path = os.path.join('downloads', video_filename)
        with open(video_path, 'wb') as file:
            file.write(response.content)
        print(f"Video downloaded successfully and saved as {video_filename}")
    else:
        return f"Failed to download video: {response.status_code} - {response.text}"

    # Return the video details as a list
    return [
        f"Title: {video_details.get('title')}",
        f"Uploader: {video_details.get('uploader')}",
        f"Upload Date: {video_details.get('upload_date')}",
        f"Duration: {video_details.get('duration')} seconds",
        f"Views: {video_details.get('view_count')}",
        f"Like Count: {video_details.get('like_count')}",
        f"Dislike Count: {video_details.get('dislike_count')}",
        f"Description: {video_details.get('description')}",
        f"Saved as: {video_filename}"
    ]

# Example usage
video_url = "https://youtu.be/RgKAFK5djSk?si=VmFnNE6p7m-3zXww"  # Replace with your video URL
details_list = download_video_and_get_details(video_url)

print(details_list)
