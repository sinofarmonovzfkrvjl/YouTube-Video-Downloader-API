
ENGLISH:
    this is API is downlaods video from youtube

    save app.py and download_video.py in the same folder, change video_url variable to another video url you want to download in download_video.py file and run download_video.py file

    DOCS:
        PYTHON:
    
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
    
        JAVASCRIPT:
    
            first you need to install axios by typing on terminal to npm install axios
    
            const axios = require('axios');
            const fs = require('fs');
            const path = require('path');
    
            // URL of the Flask API endpoints
            const downloadUrl = "https://127.0.0.1/download";
            const detailsUrl = "https://127.0.0.1/details";
    
            // Function to download the video and return its details
            async function downloadVideoAndGetDetails(videoUrl) {
                try {
                    // JSON payload with the video URL
                    const payload = {
                        url: videoUrl
                    };
    
                    // Make a POST request to the details endpoint
                    const detailsResponse = await axios.post(detailsUrl, payload);
    
                    if (detailsResponse.status !== 200) {
                        return `Failed to get video details: ${detailsResponse.status} - ${detailsResponse.statusText}`;
                    }
    
                    // Extract video details
                    const videoDetails = detailsResponse.data;
                    const videoTitle = videoDetails.title || 'video';
                    const videoExt = videoDetails.ext || 'mp4';
                    const videoFilename = `${videoTitle}.${videoExt}`;
    
                    // Make a POST request to the download endpoint
                    const downloadResponse = await axios.post(downloadUrl, payload, { responseType: 'arraybuffer' });
    
                    if (downloadResponse.status === 200) {
                        // Save the video file
                        const videoPath = path.join('downloads', videoFilename);
                        fs.writeFileSync(videoPath, downloadResponse.data);
                        console.log(`Video downloaded successfully and saved as ${videoFilename}`);
                    } else {
                        return `Failed to download video: ${downloadResponse.status} - ${downloadResponse.statusText}`;
                    }
    
                    // Return the video details as a list
                    return [
                        `Title: ${videoDetails.title}`,
                        `Uploader: ${videoDetails.uploader}`,
                        `Upload Date: ${videoDetails.upload_date}`,
                        `Duration: ${videoDetails.duration} seconds`,
                        `Views: ${videoDetails.view_count}`,
                        `Like Count: ${videoDetails.like_count}`,
                        `Dislike Count: ${videoDetails.dislike_count}`,
                        `Description: ${videoDetails.description}`,
                        `Saved as: ${videoFilename}`
                    ];
                } catch (error) {
                    return `Error: ${error.message}`;
                }
            }
    
            // Example usage
            const videoUrl = "https://youtu.be/RgKAFK5djSk?si=VmFnNE6p7m-3zXww";  // Replace with your video URL
            downloadVideoAndGetDetails(videoUrl).then(detailsList => console.log(detailsList));

UZBEK:
    bu API Youtubedan video yuklash uchun yasalgan

    app.py va download_video.py bitta faylga saqlang va download_video.py faylini ochib video_urlga yuklamoqchi bo'lgan video linkini bering va download_video.pyni ishga tushiring
