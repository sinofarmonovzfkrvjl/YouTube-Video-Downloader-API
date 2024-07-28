from flask import Flask, request, jsonify, send_file
import yt_dlp
import os
import re

app = Flask(__name__)

DOWNLOAD_FOLDER = 'downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

def sanitize_filename(filename):
    # Remove any invalid characters for Windows filenames
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    video_url = data.get('url')
    if not video_url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        with yt_dlp.YoutubeDL({'format': 'best'}) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            video_title = info_dict.get('title', 'video')
            video_ext = info_dict.get('ext', 'mp4')
            sanitized_title = sanitize_filename(video_title)
            video_filename = f"{sanitized_title}.{video_ext}"
            video_path = os.path.join(DOWNLOAD_FOLDER, video_filename)

            # Move the downloaded video to the correct path
            temp_file = os.path.join(DOWNLOAD_FOLDER, 'video')
            if os.path.exists(temp_file):
                os.rename(temp_file, video_path)

        if not os.path.exists(video_path):
            return jsonify({'error': 'File not found after download.'}), 500

        return send_file(video_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/details', methods=['POST'])
def get_video_details():
    data = request.json
    video_url = data.get('url')
    if not video_url:
        return jsonify({'error': 'No URL provided'}), 400

    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)

        return jsonify(info_dict)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
