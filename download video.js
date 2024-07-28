const axios = require('axios');
const fs = require('fs');
const path = require('path');

const url = 'http://127.0.0.1:5000/download'; // replace download to details to get video details
const data = {
    url: 'https://youtu.be/FeUA-0G1p5k?si=aG696NxKKne08NXS'
};

axios.post(url, data, { responseType: 'stream' })
    .then(response => {
        if (response.status === 200) {
            const videoPath = path.join(__dirname, 'video.mp4');
            const writer = fs.createWriteStream(videoPath);

            response.data.pipe(writer);

            writer.on('finish', () => {
                console.log('Video downloaded successfully.');
            });

            writer.on('error', (err) => {
                console.error('Error writing to file:', err);
            });
        } else {
            console.error(`Error: ${response.data.error}`);
        }
    })
    .catch(error => {
        console.error('Error:', error.message);
    });
